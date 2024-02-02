from django.db import models
from accounts.models import *

# Create your models here.
class UserProfile(models.Model):
    GENDER_CHOICES = (
        ('MALE','MALE'),
        ('FEMALE','FEMALE'),
    )
    user = models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True)
    gender = models.CharField(max_length=50,choices=GENDER_CHOICES,blank=False,null=True)
    profile_picture = models.ImageField(upload_to='users/profile_pictures',blank=True,null=True)
    address = models.CharField(max_length=250,blank=False,null=True)
    zip_code = models.CharField(max_length=6,blank=False,null=False)
    latitude = models.CharField(max_length=50,blank=True,null=False)
    longitude = models.CharField(max_length=50,blank=True,null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email