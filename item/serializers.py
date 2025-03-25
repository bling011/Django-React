from rest_framework import serializers
from .models import Comment, Item

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['email', 'password']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Item
        fields = '__all__'
