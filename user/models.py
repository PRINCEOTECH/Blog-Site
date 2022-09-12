from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from PIL import Image





class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.CharField(max_length=300)
    phone = PhoneNumberField(null=True, blank=True, unique=True)

    def __str__(self):
        return f'{self.user.username} Profile'


    def save(self, *args, **kawrgs):
        super().save(*args, **kawrgs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)    

# Create your models here.
