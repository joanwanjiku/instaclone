from django.urls import path
from . import views
from .views import PostDetailView, PostCreateView

urlpatterns = [
    path('', views.home, name='welcome'),
    path('<int:post_id>/comment/', views.add_comment, name='addcomment'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.PostCreateView.as_view(), name='new-post')
]