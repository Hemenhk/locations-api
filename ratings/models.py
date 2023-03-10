from django.db import models
from django.contrib.auth.models import User
from posts.models import Post

"""
This code was borrowed from Code Institute's Django Rest Framework Project
"""


class Rating(models.Model):
    """
    Rating model, related to 'owner' and 'post'.
    'owner' is a User instance and 'post' is a Post instance.
    'unique_together' makes sure a user can't give ratings on the same post twice.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, related_name='ratings', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'post']

    def __str__(self):
        return f'{self.owner} {self.post}'
