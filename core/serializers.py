from rest_framework import serializers
from .models import User, Discussion, Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'mobile_no', 'email', 'followers', 'following']


class DiscussionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discussion
        fields = ['id', 'user', 'text', 'image', 'hashtags', 'created_on', 'view_count']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'discussion', 'user', 'text', 'created_on', 'likes', 'replies']
