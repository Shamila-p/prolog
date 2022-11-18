from turtle import position
from django.shortcuts import render, redirect,HttpResponse

from member.models import User
from .models import Class, Department, EditSubject, Semester,Subject
from django.contrib.auth.decorators import login_required


# Create your views here.

def department(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        if not (request.user.role == User.PRINCIPAL):
            return HttpResponse('Unauthorized', status=401)
        else:
            if request.method == 'GET':
                departments = Department.objects.all()
                context = {'title': 'Departments', 'departments': departments}
                return render(request, 'department.html', context)


@login_required
def add_department(request):
    if not (request.user.role == User.PRINCIPAL):
        return HttpResponse('Unauthorized', status=401)
    else:
        if request.method == 'GET':
            teachers=User.objects.filter(position=User.HOD)
            print(teachers)
            context={'teachers':teachers}
            return render(request, 'add_department.html',context)
        if request.method == 'POST':
            dept_name = request.POST.get("dept_name")
            hod=request.POST.get("hod")
            print(dept_name)
            Department.objects.create(dname=dept_name,hod_id=hod)
            return redirect('department')


@login_required
def edit_department(request, id):
    if not (request.user.role == User.PRINCIPAL):
        return HttpResponse('Unauthorized', status=401)
    else:
        if request.method == 'GET':
            department = Department.objects.get(id=id)
            teachers=User.objects.filter(position=User.HOD)
            context = {'department': department,'teachers':teachers}
            return render(request, 'edit_department.html', context)
        if request.method == 'POST':
            dept_name = request.POST.get('dept_name')
            hod=request.POST.get('hod')
            department = Department.objects.get(id=id)
            department.dname = dept_name
            department.hod_id=hod
            department.save()
            return redirect('department')


@login_required
def remove_department(request, id):
    if not (request.user.role == User.PRINCIPAL):
        return HttpResponse('Unauthorized', status=401)
    else:
        if request.method == 'POST':
            department = Department.objects.get(id=id)
            department.delete()
            return redirect('department')


@login_required
def list_semester(request):
    if not (request.user.role == User.PRINCIPAL or (request.user.role == User.TEACHER and request.user.position == User.HOD)):
        return HttpResponse('Unauthorized', status=401)
    else:
        if request.method == 'GET':
            semesters = Semester.objects.all()
            context = {'semesters': semesters}
            return render(request, 'list_semester.html', context)


@login_required
def add_semester(request):
    if not (request.user.role == User.PRINCIPAL or (request.user.role == User.TEACHER and request.user.position == User.HOD)):
        return HttpResponse('Unauthorized', status=401)
    else:
        if request.method == 'GET':
            return render(request, 'add_semester.html')
        if request.method == 'POST':
            sem_name = request.POST.get('sem_name')
            Semester.objects.create(semname=sem_name)
            return redirect('list_semester')


@login_required
def edit_semester(request, id):
    if not (request.user.role == User.PRINCIPAL or request.user.role == User.TEACHER):
        return HttpResponse('Unauthorized', status=401)
    else:
        if request.method == 'GET':
            semester = Semester.objects.get(id=id)
            context = {'semester': semester}
            return render(request, 'edit_semester.html', context)
        if request.method == 'POST':
            sem_name = request.POST.get('sem_name')
            semester = Semester.objects.get(id=id)
            semester.semname = sem_name
            semester.save()
            return redirect('list_semester')


@login_required
def remove_semester(request, id):
    if not (request.user.role == User.PRINCIPAL or request.user.role == User.TEACHER):
        return HttpResponse('Unauthorized', status=401)
    else:
        if request.method == 'POST':
            semester = Semester.objects.get(id=id)
            semester.delete()
            return redirect('list_semester')


@login_required
def list_classes(request):
    if not (request.user.role == User.PRINCIPAL or request.user.role == User.TEACHER):
        return HttpResponse('Unauthorized', status=401)
    else:
        if request.method == 'GET':
            batches = Class.objects.all()
            hod=User.objects.get(id=request.user.id)
            classes=Class.objects.filter(department_id=hod.department_id)
            context = {'batches': batches,'classes':classes,'hod':hod}
            return render(request, 'list_classes.html', context)


@login_required
def add_class(request):
    if not (request.user.role == User.PRINCIPAL or request.user.role == User.TEACHER):
        return HttpResponse('Unauthorized', status=401)
    else:
        if request.method == 'GET':
            departments = Department.objects.all()
            semesters = Semester.objects.all()
            hod=User.objects.get(id=request.user.id)

            teachers=User.objects.filter(department_id=hod.department_id,role=User.TEACHER).exclude(position=User.HOD)
            context = {'departments': departments, 'semesters': semesters,'teachers':teachers}
            return render(request, 'add_class.html', context)
        if request.method == 'POST':
            class_name = request.POST.get('name')
            semester = request.POST.get('semester')
            department = request.POST.get('department')
            tutorid=request.POST.get('tutor')
            hod=User.objects.get(id=request.user.id)
            teachers=User.objects.filter(role=User.TEACHER).exclude(position=User.HOD)
            if request.user.position == User.HOD:
                Class.objects.create(classname=class_name,
                                Semester_id=semester, department_id=hod.department_id,tutor_id=tutorid)
            if request.user.role == User.PRINCIPAL:
                Class.objects.create(classname=class_name,
                                Semester_id=semester, department_id=department)
            return redirect('list_classes')


@login_required
def edit_class(request, id):
    if not (request.user.role == User.PRINCIPAL or request.user.role == User.TEACHER):
        return HttpResponse('Unauthorized', status=401)
    else:
        hod=User.objects.get(id=request.user.id)

        if request.method == 'GET':
            batch = Class.objects.get(id=id)
            departments = Department.objects.all()
            semesters = Semester.objects.all()
            # if request.user.role == User.TEACHER and request.user.position == User.HOD:
            teachers=User.objects.filter(department_id=hod.department_id,role=User.TEACHER).exclude(position=User.HOD)
                # context={}
            context = {'batch': batch, 'departments': departments,
                    'semesters': semesters,'teachers':teachers}
            return render(request, 'edit_class.html', context)
        if request.method == 'POST':
            class_name = request.POST.get('name')
            semester = request.POST.get('semester')
            department = request.POST.get('department')
            tutor=request.POST.get('tutor')
            batch = Class.objects.get(id=id)
            batch.classname = class_name
            batch.Semester_id = semester
            if request.user.position == User.HOD:
                batch.tutor_id=tutor
                batch.department_id = hod.department_id
            else:
                batch.department_id = department
            batch.save()
            return redirect('list_classes')


@login_required
def remove_class(request, id):
    if not (request.user.role == User.PRINCIPAL or request.user.role == User.TEACHER):
        return HttpResponse('Unauthorized', status=401)
    else:
        if request.method == 'POST':
            batch = Class.objects.get(id=id)
            batch.delete()
            return redirect('list_classes')


# def list_subjects(request):
#     if request.method=='GET':
#         subjects=Subject.objects.all()
#         context={'subjects':subjects}
#         return render(request,'list_subjects.html',context)

