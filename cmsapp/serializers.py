from rest_framework import serializers
from cmsapp.models import User, Post, Like

##### Created serializers for the User, Post, and Like models. Serializers help in converting complex data types, such as models, into JSON format.

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
