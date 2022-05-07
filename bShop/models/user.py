from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
class Users(models.Model):
    login = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    first_name = models.CharField(max_length=40,blank=True)
    second_name = models.CharField(max_length=40,blank=True)
    last_name = models.CharField(max_length=40,blank=True)
    image = models.ImageField(upload_to='media/users/%Y/%m/%d/',blank=True)
    about = models.TextField(blank=True)
    password = models.CharField(max_length=50)
    date_register = models.DateField(auto_created=True)
    date_enter = models.DateTimeField(auto_now=True)

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Users.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.Users.save()