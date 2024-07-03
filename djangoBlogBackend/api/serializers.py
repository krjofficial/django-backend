from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Blog

# Serializer for user registration and login
class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ["id", "username", "password",]
    extra_kwargs = {"password": {"write_only": True}} #Password cannot be read 



  # Method to create a new user
  def create(self, validated_data):
    user = User.objects.create_user(**validated_data)
    return user
 


class BlogSerializer(serializers.ModelSerializer):
  class Meta: 
    model = Blog
    fields = ['id', 'title', 'content', 'created_at', 'author']
    extra_kwargs = {"author": {"read_only": True}} # Author can only be read

    