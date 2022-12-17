from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

"""
This code was borrow from Code Institute and customized to fit this project
"""
class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    # As this is a business app, the email field is required for user safety
    email = models.EmailField(max_length=300)
    # As this is a business app, the name field is required for user safety
    name = models.CharField(max_length=300)
    # As this is a business app, the content field is required for user safety
    content = models.TextField()
    image = models.ImageField(
        upload_to='images/', default='../default_profile_xxpwvt'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)