from rest_framework import serializers 
from .models import Posts 

class PostsSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = Posts # tell django which model to use
        fields = ('id', 'name', 'age',) # tell django which fields to include