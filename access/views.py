from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import auth
from member.models import User
from django.conf import settings
from django.core.mail import send_mail



def login(request):
    if request.user.is_authenticated:
        return redirect('profile')
    else:
        if request.method == 'GET':
            return render(request, 'login.html')
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = auth.authenticate(username=email, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('profile')
            else:
                messages.error(request, "wrong credentials")
            return redirect('login')

def forgot_password(request):
    if request.method == 'GET':
        return render(request,'forgot_password.html')
    if request.method == 'POST':
        email=request.POST.get('email')
        print(email)
        subject = 'welcome to GFG world'
        message = 'Hi '
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail( subject, message, email_from, recipient_list )
        return redirect('login')

def logout(request):
    if request.method == 'GET':
        auth.logout(request)
        return redirect('login')
