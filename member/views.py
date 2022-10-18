from django.shortcuts import render,redirect
from member.models import User

# Create your views here.
def profile(request):
        if request.method=='GET':
            if request.user.is_authenticated:
                return render(request,'profile.html')
            else:
                return redirect('login')
