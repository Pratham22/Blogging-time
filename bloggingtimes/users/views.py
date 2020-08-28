from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile
from django.contrib.auth.models import User, auth
from django.contrib.auth import login, authenticate, logout

# Create your views here.
def updatePhone(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            newPhone = request.POST['phone']
            user = Profile.objects.get(user = request.user)
            user.phone = newPhone if newPhone is not None else request.user.profile.phone
            try:
                user.save()
            except:
                return HttpResponse('<h2>Something went wrong</h2>')
            return HttpResponse('<h2>Update Done Succesfully</h2>')
        else:
            return HttpResponse('<h2>Something went wrong</h2>')
    else:
        return render(request, 'login.html')

def updateEmail(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            newEmail = request.POST['email']
            user = Profile.objects.get(user = request.user)
            user.email = newEmail if newEmail is not None else request.user.profile.email
            try:
                user.save()
            except:
                return HttpResponse('<h2>Something went wrong</h2>')
            return HttpResponse('<h2>Update Done Succesfully</h2>')
        else:
            return HttpResponse('<h2>Something went wrong</h2>')
    else:
        return render(request, 'login.html') 

def updateAddress(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            newAddress = request.POST['address']
            user = Profile.objects.get(user = request.user)
            user.address = newAddress if newAddress is not None else request.user.profile.address
            try:
                user.save()
            except:
                return HttpResponse('<h2>Something went wrong</h2>')
            return HttpResponse('<h2>Update Done Succesfully</h2>')
        else:
            return HttpResponse('<h2>Something went wrong</h2>')
    else:
        return render(request, 'login.html')   

def userProfileEdit(request):
    if request.user.is_authenticated:
        return render(request, 'userprofileedit.html')
    else:
        return render(request, 'login.html') 

def profile(request):
    if request.user.is_authenticated:
        return render(request, 'userprofile.html')
    else:
        return render(request, 'login.html')    

def editProfile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            newTwitter = request.POST['twitter']
            newFacebook = request.POST['facebook']
            newInstagram = request.POST['instagram']
            newSkype = request.POST['skype']
            newLinkedin = request.POST['linkedin']
            newAddress = request.POST['address']
            newEmail = request.POST['email']
            newPhone = request.POST['phone']
            user = Profile.objects.get(user = request.user)
            user.phone = newPhone if newPhone is not None else request.user.profile.phone
            user.email = newEmail if newEmail is not None else request.user.profile.email
            user.address = newAddress if newAddress is not None else request.user.profile.address
            user.twitter = newTwitter if newTwitter is not None else request.user.profile.twitter
            user.facebook = newFacebook if newFacebook is not None else request.user.profile.facebook
            user.instagram = newInstagram if newInstagram is not None else request.user.profile.instagram
            user.skype = newSkype if newSkype is not None else request.user.profile.skype
            user.linkedin = newLinkedin if newLinkedin is not None else request.user.profile.linkedin
            try:
                user.save()
            except:
                return HttpResponse('<h2>Something went wrong</h2>')
            return HttpResponse('<h2>Update Done Succesfully</h2>')
        else:
            return HttpResponse('<h2>Something went wrong</h2>')
    else:
        return render(request, 'login.html')    

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
        return render(request, 'userprofile.html', {'userData':'Logged In'})
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
            return render(request, 'userprofile.html')
    else:
        print('Enter Data Properly')
