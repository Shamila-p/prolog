from multiprocessing import context
from django.shortcuts import render,redirect
from . models import Class, Department, Semester

# Create your views here.

def department(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        if request.method=='GET':
            departments=Department.objects.all()

            context = {'title': 'Departments','departments':departments}
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

def list_semester(request):
    if request.method=='GET':
        semesters=Semester.objects.all()
        context={'semesters':semesters}
        return render(request,'list_semester.html',context)

def add_semester(request):
    if request.method=='GET':
        return render(request,'add_semester.html')
    if request.method=='POST':
        sem_name=request.POST.get('sem_name')
        Semester.objects.create(semname=sem_name)
        return redirect('list_semester')

def edit_semester(request,id):
    if request.method=='GET':
        semester=Semester.objects.get(id=id)
        context={'semester':semester}
        return render(request,'edit_semester.html',context)
    if request.method=='POST':
        sem_name=request.POST.get('sem_name')
        semester=Semester.objects.get(id=id)
        semester.semname=sem_name
        semester.save()
        return redirect('list_semester')
def remove_semester(request,id):
    if request.method=='POST':
        semester=Semester.objects.get(id=id)
        semester.delete()
        return redirect('list_semester')

def list_classes(request):
     if request.method=='GET':
        batches=Class.objects.all()
        context={'batches':batches}
        return render(request,'list_classes.html',context)

def add_class(request):
    if request.method=='GET':
        departments=Department.objects.all()
        semesters=Semester.objects.all()
        context={'departments':departments,'semesters':semesters}
        return render(request,'add_class.html',context)
    if request.method=='POST':
        class_name=request.POST.get('name')
        semester=request.POST.get('semester')
        department=request.POST.get('department')
        Class.objects.create(classname=class_name,Semester_id=semester,department_id=department)
        return redirect('list_classes')
def edit_class(request,id):
    if request.method=='GET':
        batch=Class.objects.get(id=id)
        departments=Department.objects.all()
        semesters=Semester.objects.all()
        context={'batch':batch,'departments':departments,'semesters':semesters}
        return render(request,'edit_class.html',context)
    if request.method=='POST':
        class_name=request.POST.get('name')
        semester=request.POST.get('semester')
        department=request.POST.get('department')
        batch=Class.objects.get(id=id)
        batch.classname=class_name
        batch.Semester_id=semester
        batch.department_id=department
        batch.save()
        return redirect('list_classes')
def remove_class(request,id):
    if request.method=='POST':
        batch=Class.objects.get(id=id)
        batch.delete()
        return redirect('list_classes')





   



