from django.shortcuts import render
from rest_framework import generics
from .serializers import PostsSerializer
from .models import Posts

# Create your views here.
class PostsList(generics.ListCreateAPIView):
    queryset = Posts.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = PostsSerializer # tell django what serializer to use

class PostsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Posts.objects.all().order_by('id')
    serializer_class = PostsSerializer