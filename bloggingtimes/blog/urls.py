from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import home
app_name = 'blog'
urlpatterns = [
    path('',home.as_view(),name="home"),
    #path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
]
