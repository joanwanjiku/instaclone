from django.urls import path
from . import views
from .views import PostDetailView, PostCreateView, PostDeleteView, PostUpdateView

urlpatterns = [
    path('', views.home, name='welcome'),
    path('<int:post_id>/comment/', views.add_comment, name='addcomment'),
    path('post/<int:post_id>/like', views.add_like, name='like-post'),
    path('user/', views.search_user, name='search-user'),
    path('user/<int:user_id>/', views.user_follow, name='user-profile'),
    path('user/follow/<int:user_id>/', views.follow_another, name='follow-user'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.PostCreateView.as_view(), name='new-post'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='update-post'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='delete-post'),

]