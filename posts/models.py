from django.db import models
from django.contrib.auth.models import User

"""
This code was borrowed from Code Institute's Django Rest Framework Project
"""

class Post(models.Model):
    """
    Post model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    price = models.CharField(max_length=300, default='')
    contact = models.CharField(max_length=300, default='')
    content = models.TextField()
    image = models.ImageField(
        upload_to='images/', default='../default_post_kh6p7i', blank=True
    )
    image_filter = models.CharField(
        max_length=32, default='normal'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
