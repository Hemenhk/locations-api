from rest_framework import serializers
from .models import Post
from ratings.models import Rating


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    rating_id = serializers.SerializerMethodField()
    ratings_count = serializers.ReadOnlyField()
    reviews_count = serializers.ReadOnlyField()

    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

        def get_rating_id(self, obj):
            user = self.context['request'].user
            if user.is_authenticated:
                rating = Rating.objects.filter(
                    owner=user, post=obj
                ).first()
                return rating.id if rating else None
            return None

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'created_at', 'updated_at',
            'content', 'image', 'is_owner', 'profile_id', 'profile_image',
            'image_filter', 'title', 'rating_id', 'ratings_count', 
            'reviews_count'
        ]
