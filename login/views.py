from django.shortcuts import render
from django.http import HttpResponse
from . models import Signup

# Create your views here.
def signup(request):

    if request.method == "POST":

        name = request.POST.get('name','false')
        phone = request.POST.get('phone','false')
        email = request.POST.get('email','false')
        users = Signup.objects.values('phone', 'email')
        for user in users:
            if(phone == user['phone']):
                return HttpResponse('phone number existed try a different number')
                break
        for user in users:
            if(email == user['email']):
                return HttpResponse('email existed try a different email')
                break
        password = request.POST.get('password','false')
        designation = request.POST.get('designation','false')
        gender = request.POST.get('gender','false')
        address = request.POST.get('address','false')
        user = Signup(password=password,name = name,phone = phone , email=email,designation = designation,gender=gender,address=address)
        user.save()
        return HttpResponse('Signup Successfull')



    return render(request,'login/signupPage.html')

def login(request):
    login_variable =False
    if request.method == "POST":

        email = request.POST.get('email','false')
        password = request.POST.get('password','false')
        print(email,password)
        users = Signup.objects.values('email','password')
        for user in users:
            if(user['email'] == email and user['password'] == password):
                login_variable=True
        if (login_variable == True):
            return HttpResponse('login successful')
        else:
            return HttpResponse('Username Password Incorrect')
    return render(request,'login/loginPage.html')

def changePassword(request):
    email_variable =False
    password_variable =False
    if request.method == "POST":
        email = request.POST.get('email', 'false')
        password = request.POST.get('password', 'false')
        newpassword = request.POST.get('newpassword', 'false')
        print(email, password,newpassword)
        users = Signup.objects.values('email', 'password')
        for user in users:
            if(user['email'] == email):
                email_variable=True
                if(password == user['password'] ):
                    password_variable=True
                    print(user['password'])
                    user['password']= newpassword
                    print(user['password'])
                    user = Signup.objects.filter(email=email).update(password=newpassword)
                    return HttpResponse("password Changed")
            print(user)
        if(email_variable != True):
            return HttpResponse('email id not exist')
        if(password_variable != True):
            return HttpResponse("incorrect old password")

    return render(request,'login/changePassword.html')


