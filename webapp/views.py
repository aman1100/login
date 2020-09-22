from django.shortcuts import render,redirect
from django.apps import apps

# Create your views here.
def home(request,id):
    users = apps.get_model('login','Signup') #fetching Signup class from login app
    user = users.objects.filter(user_id=id)[0]

    return render(request,'webapp/home.html',{'user':user})