from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def register(request):
    if  request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created successfully')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})

def UserLogin(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        form = authenticate(username=username, password=password)
        messages.success(request, f'Login Successfully ')
        if form is not None:
            login(request, form)
            return redirect('blog-home')
        else:
            messages.success(request, f'Username Or Password is incorrect')
            return redirect('login')
    return render(request, 'user/login.html')


def LogoutUser(request):
    logout(request)
    return redirect('login')
    

@login_required
def Profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }
    return render(request, 'user/profile.html', context)


# Create your views here.
