from django.contrib import admin
from .models import Profile
from django import forms
from phonenumber_field.widgets import PhoneNumberPrefixWidget


class ContactForm(forms.ModelForm):
    class Meta:
        widgets = {
            'phone' : PhoneNumberPrefixWidget(initial='NGN')
        }


admin.site.register(Profile)

# Register your models here.
