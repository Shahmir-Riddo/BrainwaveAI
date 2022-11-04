from django.db import models
from django.contrib.auth.models import User


# Extending User Model Using a One-To-One Link
class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email =  models.CharField(max_length=50)
    message = models.CharField(max_length=400)


