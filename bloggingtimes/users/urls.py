from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import registerRender
from .views import register
from .views import loginRender
from .views import loginAuthenticate 
from .views import userLogout
from .views import editProfile
from .views import profile
from .views import userProfileEdit
from .views import updateAddress
from .views import updateEmail
from .views import updatePhone

app_name = 'users'
urlpatterns = [
    path('register', register, name="register"),
    path('registerRender', registerRender, name="register"),
    path('login', loginRender, name = 'login'),
    path('logined', loginAuthenticate, name = 'loginAuthenticate'),
    path('userLogout', userLogout, name = 'logout'),
    path('profile', profile, name = 'profile'),
    path('editprofile', editProfile, name = 'editProfile'),
    path('userProfileEdit', userProfileEdit, name = 'userProfileEdit'),
    path('updateAddress', updateAddress, name = 'updateAddress'),
    path('updateEmail', updateEmail, name = 'updateEmail'),
    path('updatePhone', updatePhone, name = 'updatePhone')
    #path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
]
