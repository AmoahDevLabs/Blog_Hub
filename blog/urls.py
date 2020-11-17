from django.urls import path
from . import views
from .feeds import LatestPostsFeed
from .views import PostCreateView, PostUpdateView, PostDeleteView, UserPostListView

app_name = 'blog'

urlpatterns = [
    # Post views
    path('', views.post_list, name='post_list'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user_posts'),
    path('<int:pk>/<slug:slug>', views.post_detail, name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('<slug:slug>/update', PostUpdateView.as_view(), name='post_update'),
    path('<slug:slug>/delete', PostDeleteView.as_view(), name='post_delete'),
    path('<int:post_id>-<slug:slug>/share', views.post_share, name='post_share'),
    path('tag/<slug:tag_slug>', views.post_list, name='post_list_by_tag'),
    path('feed/', LatestPostsFeed(), name='post_feed'),
    # path('search/', views.post_search, name='post_search')

]
