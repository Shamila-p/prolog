from multiprocessing import context
from turtle import position
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from course.models import Department
from course.views import department

from member.models import Teacher, User


@login_required
def profile(request):
        if request.method == 'GET':
            context={'title':'Profile'}
            return render(request, 'profile.html',context)

def list_teachers(request):
    if request.method=='GET':
        teachers=Teacher.objects.all()
        context={'title':'Teachers','teachers':teachers}
        return render(request, 'list_teachers.html',context)
        
def add_teachers(request):
    if request.method=='GET':
        departments=Department.objects.all()
        context={'departments':departments,'positions':Teacher.POSITION_CHOICES}
        return render(request,'add_teachers.html',context)
    if request.method=='POST':
        name=request.POST.get('name')
        department=request.POST.get('department')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        position=request.POST.get('position')
        user=User.objects.create(first_name=name,username=email,email=email,phone=mobile, role=User.TEACHER,department_id=department)
        Teacher.objects.create(position=position,user_id=user.id)
        return redirect('list_teachers')

def edit_teacher(request,user_id):
    if request.method=='GET':
        teacher=User.objects.get(id=user_id)
        departments=Department.objects.all()
        context={'teacher':teacher,'departments':departments,'positions':Teacher.POSITION_CHOICES}
        return render(request,'edit_teacher.html',context)
    if request.method=='POST':
        name=request.POST.get('name')
        department=request.POST.get('department')
        print(department)
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        position=request.POST.get('position')
        user=User.objects.get(id=user_id)
        teacher=Teacher.objects.get(user_id=user_id)
        dep=Department.objects.get(dname=department)
        user.first_name=name
        user.email=email
        user.phone=mobile
        user.department_id=dep.id
        user.save()
        teacher.position=position
        teacher.save()
        return redirect('list_teachers')
    

def approve_teacher(request,user_id):
    if request.method=='POST':
        user=User.objects.get(id=user_id)
        user.is_active=not user.is_active
        user.save()
        return redirect('list_teachers')

def remove_teacher(request,user_id):
    if request.method=='POST':
        user=User.objects.get(id=user_id)
        user.delete()
        return redirect('list_teachers')


def list_students(request):
    if request.method=='GET':
        return render(request,'list_students.html')

def add_student(request):
    if request.method=='GET':
        departments=Department.objects.all()
        context={'departments':departments}
        return render(request,'add_student.html',context)
    if request.method=='POST':
        name=request.POST.get('name')
        admsn_no=request.POST.get('admsn_no')
        department=request.POST.get('department')
        semester=request.POST.get('semester')
        batch=request.POST.get('batch')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        p_name=request.POST.get('p_name')
        p_mobile=request.POST.get('p_mobile')
        User.objects.create_user
       
