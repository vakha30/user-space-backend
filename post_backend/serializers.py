from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User


class PostSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source="creator.id")

    class Meta:
        model = Post
        fields = ("id", "title", "text", "created_at", "creator")
