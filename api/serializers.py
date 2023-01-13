from rest_framework import serializers
from .models import Room, Article

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'code', 'host', 'guest_can_pause', 'votes_to_skip', 'created_at')

class ArticleSerialize(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ("title", "description")
