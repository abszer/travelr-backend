from django.urls import path
from . import views

urlpatterns = [
     path('api/posts', views.PostsList.as_view(), name='posts_list'),
     path('api/posts/<int:pk>', views.PostsDetail.as_view(), name='posts_detail'),
]