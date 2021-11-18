from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
     class Meta:
          model = Post
          fields = ('id', 'title', 'image_url', 'likes', 'public', 'description', 'location', 'user',)