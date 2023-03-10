from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Review

"""
This code was borrowed from Code Institute's Django Rest Framework Project
"""


class ReviewSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
    
    # natural time for reviews created
    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    # natural time for reviews updated
    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    class Meta:
        model = Review
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'profile_id',
            'profile_image', 'is_owner', 'post', 'content', 'created_at',
            'updated_at'
        ]


class ReviewDetailSerializer(ReviewSerializer):
    """
    Serializer for the comment model used in Detail view
    Post is a read only field so that we don't have to set it on each update
    """
    post = serializers.ReadOnlyField(source='post.id')
