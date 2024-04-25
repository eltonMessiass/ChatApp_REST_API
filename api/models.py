from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=50, blank=True)
    first_name = models.CharField(max_length=50,blank=True)
    last_name = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.user.username}"


    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        try:
            if created:
                profile = Profile.objects.create(user=instance)  
                profile.username = instance.username
                profile.first_name = instance.first_name
                profile.last_name = instance.last_name
                profile.save()
        except:
            pass
    
 