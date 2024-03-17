from django.shortcuts import render
from rest_framework import generics,permissions,viewsets
from django.contrib.auth import get_user_model
from .serilalizers import PostSerializer, UserSerializer
from posts.models import Post
from posts.permissions import IsAuthorOrReadOnly



# Create your views here.

# class PostList(generics.ListAPIView):
#     permission_classes = (IsAuthorOrReadOnly,) # new
#     queryset=Post.objects.all()
#     serializer_class=PostSerializer

# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     # permission_classes = (permissions.IsAdminUser,) # new
#     permission_classes = (IsAuthorOrReadOnly,) # new
#     queryset=Post.objects.all()
#     serializer_class=PostSerializer



# class UserList(generics.ListAPIView):
#     queryset=get_user_model().objects.all()
#     serializer_class=UserSerializer

# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset=get_user_model().objects.all()
#     serializer_class=UserSerializer

############ Viewset replaces above views

class UserViewset(viewsets.ModelViewSet):
    permission_classes=(permissions.IsAdminUser,)
    queryset=get_user_model().objects.all()
    serializer_class=UserSerializer


class PostViewset(viewsets.ModelViewSet):
    permission_classes=(IsAuthorOrReadOnly,)
    queryset=Post.objects.all()
    serializer_class=PostSerializer