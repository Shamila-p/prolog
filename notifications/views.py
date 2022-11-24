from django.shortcuts import render

# Create your views here.
def send_complaint(request):
    if request.method == 'GET':
        return render(request,'complaint.html')