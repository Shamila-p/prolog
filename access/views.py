import uuid
from django.contrib import messages
from django.shortcuts import render, redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth.models import auth
from member.models import User
from django.conf import settings
from django.core.mail import send_mail
from access.models import ForgotPassword



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
        reset_id=str(uuid.uuid1())
        email=request.POST.get('email')
        if not User.objects.filter(email=email).exists():
            messages.info(request, 'This email not registered yet')
        else:
            user=User.objects.get(email=email)
            ForgotPassword.objects.create(uuid=reset_id,user_id=user.id)
            reset_url=settings.DOMAIN_URL+'reset-password/'+reset_id
            subject = 'Reset Password - Prolog'
            message = ' You are receiving this email because you requested a password reset. Please Click below link to reset password. Thanks for using our site! ' + reset_url
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail( subject, message, email_from, recipient_list )
            return redirect('login')

def reset_password(request,reset_id):
    if request.method == 'GET':
        if not ForgotPassword.objects.filter(id=reset_id).exists():
            return HttpResponse('Unauthorized', status=401)
        return render(request,'reset_password.html')
    else:
        new=request.POST.get('password')
        confirm=request.POST.get('confirm_password')
        if new == confirm:
            forgot=ForgotPassword.objects.get(uuid=reset_id)
            print(forgot)
            user=User.objects.get(id=forgot.user_id)
            user.set_password(new)
            user.save()
            return redirect('login')
        else:
            messages.error(request,"Two passwords doesnt match")
            return redirect('reset_password')

def logout(request):
    if request.method == 'GET':
        auth.logout(request)
        return redirect('login')
