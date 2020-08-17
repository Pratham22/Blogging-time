from django.shortcuts import render
from users.models import userData
# Create your views here.
def register(request):
    return render(request, 'register.html')

def registerRender(request):
    firstName = request.POST['firstName']
    lastName = request.POST['lastName']
    email = request.POST['email']
    password = request.POST['password']
    phone = request.POST['phone']

    if firstName is not None and lastName is not None and email is not None and password is not None:
        user = userData(
            firstName = firstName, 
            lastName = lastName, 
            email = email, 
            password = password, 
            phone = phone)
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