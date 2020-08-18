from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import registerRender
from .views import register
from .views import loginRender
from .views import loginAuthenticate 
from .views import userLogout

app_name = 'users'
urlpatterns = [
    path('register', register, name="register"),
    path('registerRender', registerRender, name="register"),
    path('login', loginRender, name = 'login'),
    path('logined', loginAuthenticate, name = 'loginAuthenticate'),
    path('userLogout', userLogout, name = 'logout')
    #path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
]
