from django.db import models
from django.contrib.auth.models import User
from posts.models import Post

"""
This code was borrowed from Code Institute's Django Rest Framework Project
"""


class Review(models.Model):
    """
    Review model, allowing users to leave reviews at individual posts,
    related to Post models
    """

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content
