from django.shortcuts import render

# Create your views here.

##### 5. The following CRUD APIs should be implemented for all three tables:



from rest_framework import generics, permissions
from .models import User, Post, Like
from .serializers import UserSerializer, PostSerializer, LikeSerializer
from .permissions import IsOwnerOrReadOnly

### Create API: To add new user to the corresponding table.

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

## Read API: To retrieve a specific user from the corresponding table.

class GetUserView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

#Update API: To update the details of a specific user in the corresponding table.
class UpdateUserView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

#Delete API: To delete a specific user from the corresponding table.
class DeleteUserView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
### Create API: To add new Post to the corresponding table.
class CreatePostView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

## Read API: To retrieve a specific Post from the corresponding table.

class GetPostView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    
#Update API: To update the details of a specific Post in the corresponding table.

class UpdatePostView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    
#Delete API: To delete a specific Post from the corresponding table.
class DeletePostView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    
## Read API: To retrieve a specific Like from the corresponding table.
class CreateLikeView(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    
## Read API: To retrieve a specific Like from the corresponding table.
class GetLikeView(generics.RetrieveAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    
#Update API: To update the details of a specific Like in the corresponding table.
class UpdateLikeView(generics.UpdateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]
    
#Delete API: To delete a specific Like from the corresponding table.
class DeleteLikeView(generics.DestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    
##### 6.The GET all post/blog API should also return the number of likes for each post/blog.

from rest_framework.response import Response
class PostListWithLikeCountView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        posts_with_like_count = []
        for post in serializer.data:
            like_count = Like.objects.filter(post_id=post['id']).count()
            post['like_count'] = like_count
            posts_with_like_count.append(post)
        return Response(posts_with_like_count)
    
    

