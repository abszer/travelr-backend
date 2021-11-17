from django.shortcuts import render
from rest_framework import generics
from .serializers import PostSerializer
from .models import Post

# Create your views here.
class PostList(generics.ListCreateAPIView):
     queryset = Post.objects.all().order_by('id')
     serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
     queryset = Post.objects.all().order_by('id')
     serializer_class = PostSerializer