from django.urls import path
from .views import PostViewset,UserViewset         #,PostList, PostDetail, UserDetail, UserList,
from rest_framework.routers import SimpleRouter



router=SimpleRouter()

router.register('users',UserViewset,basename='users') # should be on top above post

router.register('',PostViewset,basename='posts')


urlpatterns=router.urls


# urlpatterns = [
#         path('users/',UserList.as_view(),name='user_list'),
#         path('users/<int:pk>',UserDetail.as_view(),name='user_detail'),
#         path("<int:pk>/", PostDetail.as_view(), name="post_detail"),
#         path("", PostList.as_view(), name="post_list"),


# ]