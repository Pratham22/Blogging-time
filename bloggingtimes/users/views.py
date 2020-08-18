from django.shortcuts import render

from django.contrib.auth.models import User, auth
from django.contrib.auth import login, authenticate, logout

# Create your views here.
def userLogout(request):
    logout(request)
    print(User.username)
    return render(request, 'test.html')

def loginRender(request):
    return render(request, 'login.html')

def loginAuthenticate(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        print('Logined')
        login(request, user)
        return render(request, 'test.html', {'userData':'Logged In'})
    else:
        return render(request, 'test.html', {'userData':'Not logged In'})
def register(request):
    return render(request, 'register.html')

def registerRender(request):
    username = request.POST['username']
    firstName = request.POST['firstName']
    lastName = request.POST['lastName']
    email = request.POST['email']
    password = request.POST['password']
    phone = request.POST['phone']

    if firstName is not None and lastName is not None and email is not None and password is not None:
        if User.objects.filter(username = username).exists():
            return render(request, 'test.html', {'userData':'Username Already Taken'})
        elif User.objects.filter(email = email).exists():
            return render(request, 'test.html', {'userData':'Email Already Taken'})
        else:
            user = User.objects.create_user(
                username = username, 
                password = password,
                email = email,
                first_name = firstName,
                last_name = lastName)
            
            user.save()
            
            userInfo = {
                'firstName': firstName,
                'lastName': lastName,
                'email': email,
                'password': password,
                'phone': phone
            }
            return render(request, 'test.html', {'userData':userInfo})
    else:
        print('Enter Data Properly')