from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Signup,adminPortal

# Create your views here.
def signup(request):

    if request.method == "POST":

        name = request.POST.get('name','false')
        phone = request.POST.get('phone','false')
        email = request.POST.get('email','false')
        users = Signup.objects.values('phone', 'email')
        for user in users:
            if(phone == user['phone']):
                params = {'msg': 'phone number already existed try a different number'}
                return render(request, 'login/signupPage.html', params)
                break
        for user in users:
            if(email == user['email']):
                params = {'msg': 'email already existed try a different email'}
                return render(request, 'login/signupPage.html', params)
                break
        password = request.POST.get('password','false')
        designation = request.POST.get('designation','false')
        gender = request.POST.get('gender','false')
        address = request.POST.get('address','false')
        user = Signup(password=password,name = name,phone = phone , email=email,designation = designation,gender=gender,address=address)
        user.save()
        user= Signup.objects.filter(phone=phone)[0]
        url = '/login/userProfile/'
        id = user.user_id
        page =(f'{url}{id}')
        return redirect(page)
    return render(request,'login/signupPage.html')

def userProfile(request,id):
    user = Signup.objects.filter(user_id=id)[0]
    return render(request,'login/userProfile.html',{'user':user})

def login(request):
    login_variable =False
    if request.method == "POST":

        email = request.POST.get('email','false')
        password = request.POST.get('password','false')
        print(email,password)
        users = Signup.objects.values('email','password')
        for user in users:
            if(user['email'] == email and user['password'] == password):
                user= Signup.objects.filter(email=email)[0]
                login_variable = True
                print(user.user_id)
                url = '/home/home/'
                id = user.user_id
                page = (f'{url}{id}')
        if (login_variable == True):
            return redirect(page)
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
                    params = {'msg': 'Password change successfully'}
                    return render(request,'login/changePassword.html',params)
                    break
        if(email_variable != True):
            return HttpResponse('email id not exist')
        if(password_variable != True):
            return HttpResponse("incorrect old password")

    return render(request,'login/changePassword.html')

def selectadmin(request):
    admins = adminPortal.objects.all()
    return render(request, 'login/adminProfile.html', {'admins': admins})

def admin(request,id):
    if request.method == "POST":
        email = request.POST.get('email', 'false')
        password = request.POST.get('password', 'false')
        admin=adminPortal.objects.filter(admin_id=id)[0]
        if(admin.email == email and admin.password == password):
            users=Signup.objects.all()
            return render(request,'login/adminAccount.html',{'admin':admin ,'users':users})
        else:
            return HttpResponse('invalid username password')

    return render(request,'login/adminPortal.html')

def adminActions(request):
    if request.method == "POST":
        del_user_id= request.POST.get('delete_button_name','false')
        del_user_id =del_user_id[20:-1]
        print(del_user_id)
        users =Signup.objects.values('user_id')
        print(users)
        for user in users:
            if(del_user_id == str(user['user_id'])):
                user=Signup.objects.filter(user_id=del_user_id)
                user.delete()

        return HttpResponse('user deleted succesfully')