from django.urls import path
from .views import *

urlpatterns = [
  path('posts/', PostList.as_view(), name='posts_list_url'),
  path('post/create', PostCreate.as_view(), name='post_create_url'),
  path('post/<str:slug>/', PostDetails.as_view(), name='post_details_url'),
  path('post/<str:slug>/update/', PostUpdate.as_view(), name='post_update_url'),
  path('post/<str:slug>/delete/', PostDelete.as_view(), name='post_delete_url'),
  path('tags/', TagList.as_view(), name='tags_list_url'),
  path('tag/create/', TagCreate.as_view(), name='tag_create_url'),
  path('tag/<str:slug>/', TagDetails.as_view(), name='tag_details_url'),
  path('tag/<str:slug>/update/', TagUpdate.as_view(), name='tag_update_url'),
  path('tag/<str:slug>/delete/', TagDelete.as_view(), name='tag_delete_url'),
]
