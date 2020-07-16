from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.utils import timezone
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from django.db import models

#an extended version of the posts
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

'''
# Create your models here.
# model for Post 
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
'''
# model of Loylity system
from django.db import models

class Difficulty(models.Model):
    '''System of digiculty for all other models'''
    level = models.CharField(max_length=20)
    reward = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.level

#model Skills 
class Skill(models.Model): 
    skill_name = models.TextField()
    skill_description = models.TextField()
    skill_ico = models.ImageField()#form of ico image located in forms.py
    diffictatlty = models.ForeignKey(Difficulty, on_delete=models.CASCADE, related_name="difficulty", null=True)


    def __str__(self):
        return self.skill_name


#model of userSKill
class UserSkill(models.Model): 
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name="skill", default=0)
    level = models.PositiveIntegerField(default=0)
    


#model for Profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=150)
    bio = models.TextField()

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


