from django.urls import path

from blog.models import Post
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView



urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/', PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/', PostDeleteView.as_view(), name="post_delete"),
]