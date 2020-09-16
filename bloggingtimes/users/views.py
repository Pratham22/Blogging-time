from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile
from django.contrib.auth.models import User, auth
from django.contrib.auth import login, authenticate, logout
from django.core.files.storage import FileSystemStorage

# Create your views here.
def updateProfilePic(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            newProfileImage = request.FILES.get('profileImage')
            user = Profile.objects.get(user = request.user)
            user.profileImage = newProfileImage if newProfileImage is not '' else request.user.profile.profileImage
            fs=FileSystemStorage()
            filename=fs.save(newProfileImage.name,newProfileImage)
            try:
                user.save()                
            except:
                return render(request, 'errorPage.html')
            return render(request, 'userprofileedit.html')
        else:
            return render(request, 'errorPage.html')
    else:
        return render(request, 'login.html')

def updateInfo(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            newMotive = request.POST['motive']
            newDOB = request.POST['dob']
            newAge = request.POST['age']
            newWebsite = request.POST['website']
            newFreelance = 'False'
            newAbout = request.POST['about']
            newDegree = request.POST['degree']
            print(newMotive, newAbout, newAge, newDegree, newDegree, newFreelance, newWebsite)
            user = Profile.objects.get(user = request.user)
            user.motive = newMotive if newMotive is not '' else request.user.profile.motive
            user.dob = newDOB if newDOB is not '' else request.user.profile.dob
            user.age = newAge if newAge is not '' else request.user.profile.age
            user.website = newWebsite if newWebsite is not '' else request.user.profile.website
            user.freelance = newFreelance if newFreelance is not '' else request.user.profile.freelance
            user.about = newAbout if newAbout is not '' else request.user.profile.about
            user.degree = newDegree if newDegree is not '' else request.user.profile.degree
            try:
                user.save()                
            except:
                print('Done')
                return render(request, 'errorPage.html')
            return HttpResponse('<h2>Update Done Succesfully</h2>')
        else:
            return render(request, 'errorPage.html')
    else:
        return render(request, 'login.html')

def updatePhone(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            newPhone = request.POST['phone']
            user = Profile.objects.get(user = request.user)
            user.phone = newPhone if newPhone is not None else request.user.profile.phone
            try:
                user.save()
            except:
                return render(request, 'errorPage.html')
            return HttpResponse('<h2>Update Done Succesfully</h2>')
        else:
            return render(request, 'errorPage.html')
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
                return render(request, 'errorPage.html')
            return HttpResponse('<h2>Update Done Succesfully</h2>')
        else:
            return render(request, 'errorPage.html')
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
                return render(request, 'errorPage.html')
            return HttpResponse('<h2>Update Done Succesfully</h2>')
        else:
            return render(request, 'errorPage.html')
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
            user.phone = newPhone if newPhone is not '' else request.user.profile.phone
            user.email = newEmail if newEmail is not '' else request.user.profile.email
            user.address = newAddress if newAddress is not '' else request.user.profile.address
            user.twitter = newTwitter if newTwitter is not '' else request.user.profile.twitter
            user.facebook = newFacebook if newFacebook is not '' else request.user.profile.facebook
            user.instagram = newInstagram if newInstagram is not '' else request.user.profile.instagram
            user.skype = newSkype if newSkype is not '' else request.user.profile.skype
            user.linkedin = newLinkedin if newLinkedin is not '' else request.user.profile.linkedin
            try:
                user.save()
            except:
                return render(request, 'errorPage.html')
            return HttpResponse('<h2>Update Done Succesfully</h2>')
        else:
            return render(request, 'errorPage.html')
    else:
        return render(request, 'login.html')    

def userLogout(request):
    logout(request)
    print(User.username)
    return render(request, 'login.html')

def loginRender(request):
    return render(request, 'login.html')

def loginAuthenticate(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print('Logined')
            login(request, user)
            return render(request, 'userprofile.html', {'userData':'Logged In'})
        else:
            return render(request, 'test.html', {'userData':'Not logged In'})
    else:
        return render(request, 'errorPage.html')

def register(request):
    return render(request, 'register.html')

def registerRender(request):
    if request.method == 'POST':
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
                
                try:
                    profile = Profile.objects.create(
                        profileImage = 'blankProfile.jpg',
                        motive = 'Your Motive',
                        dob = '1998-10-22',
                        age = 0,
                        website = 'YourWebsite@company.com',
                        degree = 'Your Degree',
                        freelance = False,
                        about = 'About Yourself',
                        user = user,
                        phone = phone,
                        designation = 'Your Designation',
                        city = 'Your City',
                        address = 'Your Address',
                        email = 'YourEmail.com',
                        twitter = 'YourTwitter.com',
                        facebook = 'YourFacebook.com',
                        instagram = 'YourInstagram.com',
                        skype = 'YourSkype.com',
                        linkedin = 'YourLinkedIn.com' 
                    )
                except:
                    return HttpResponse("Something went wrong!")
                user.save()
                profile.save()
                login(request, user)
                return render(request, 'userprofile.html')
        else:
            print('Enter Data Properly')
    else:
        return render(request, 'errorPage.html')