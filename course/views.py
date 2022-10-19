from multiprocessing import context
from django.shortcuts import render,redirect
from . models import Department

# Create your views here.

def department(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        if request.method=='GET':
            departments=Department.objects.all()

            context = {'title': 'Departments','add_button_name':'ADD DEPARTMENT','departments':departments}
            return render(request,'department.html',context)

def add_department(request):
     if request.method=='GET':
            return render(request,'add_department.html')
     if request.method =='POST':
        dept_name=request.POST.get("dept_name")
        print(dept_name)
        Department.objects.create(dname=dept_name)
        return redirect('department')
def edit_department(request,id):
    if request.method=='GET':
        department=Department.objects.get(id=id)
        context={'department':department}
        return render(request,'edit_department.html',context)
    if request.method=='POST':
        dept_name=request.POST.get('dept_name')
        department=Department.objects.get(id=id)
        department.dname=dept_name
        department.save()
        return redirect('department')

def remove_department(request,id):
    if request.method=='POST':
        department=Department.objects.get(id=id)
        department.delete()
        return redirect('department')

        



