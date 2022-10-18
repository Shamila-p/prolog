from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import auth
from member.models import User
# Create your views here.
def login(request):
    if request.user.is_authenticated :
        return redirect('profile')
    else:
        if request.method=='GET':
            return render(request,'login.html')
        if request.method=='POST':
            email=request.POST['email']
            password=request.POST['password']
            user=auth.authenticate(username=email,password=password)
            
            if user is not None:
                auth.login(request,user)
                return redirect('profile')
            else:
                messages.error(request,"wrong credentials")
            return redirect('login')
def logout(request):
    if request.method=='GET':
        auth.logout(request)
        return redirect('login')