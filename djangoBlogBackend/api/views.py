from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, BlogSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Blog

# Create your views here.
class CreateUserView(generics.CreateAPIView):
  queryset = User.objects.all() # to avoid duplication 
  serializer_class = UserSerializer # tells what data needs to be accepted to make a new user (username and password)
  permission_classes = [AllowAny]
  # specifies who can allowed to call this view
  # AllowAny means anyone can access this view (not just authenticated users)


class BlogListCreate(generics.ListCreateAPIView): 
  # listCreateAPIView - lists all the blogs that have been created or it will create a new blog
  serializer_class = BlogSerializer
  permission_classes = [IsAuthenticated]

  # for additional Functionalities we are overriding the default methods in listCreateAPIView
  # refer to documentation for getting the methods of listCreateAPIView
  def get_queryset(self):
    user = self.request.user # get the user who is logged in
    return Blog.objects.filter(author=user) # only display the blog written by the user
  
  def perform_create(self, serializer):
    if serializer.is_valid():
      serializer.save(author=self.request.user) # save the blog with the author as the logged in user
    else:
      print(serializer.errors)


class BlogDelete(generics.DestroyAPIView):
  # DestroyAPIView is used to delete a blog

  # setting the stage
  serializer_class = BlogSerializer
  permission_classes = [IsAuthenticated] # User must be authenticated to perform this action

  # for additional functionalities we are overriding the default methods in DestroyAPIView
  # refer to documentation for getting the methods of DestroyAPIView
  # specify the valid blogs that the user can delete
  def get_queryset(self):
    user = self.request.user # get the user who is logged in
    return Blog.objects.filter(author=user) # only capable of deleting the blog written by the user
  
  
