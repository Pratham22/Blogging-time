from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import home,PostDetailView,all_blogs,create_blog,create_post
app_name = 'blog'
urlpatterns = [
    path('',home.as_view(),name="home"),
    path('blogs',all_blogs.as_view(),name="all-blog"),
    path('post/<int:pk>/', PostDetailView, name='post-detail'),
    path('createblog/',create_post,name="create-blog"),
]
