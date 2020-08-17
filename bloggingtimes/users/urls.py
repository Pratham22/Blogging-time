from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import registerRender
from .views import register

app_name = 'users'
urlpatterns = [
    path('register', register, name="register"),
    path('registerRender', registerRender, name="register")
    #path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
]
