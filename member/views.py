from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from course.models import Class, Department, Semester
from course.views import department
from member.models import Student, Teacher, User
from django.contrib import messages


@login_required
def profile(request):
    if request.method == 'GET':
        if request.user.role == User.STUDENT:
            student=Student.objects.get(user_id=request.user.id)
            context = {'title': 'Profile','student':student}
        elif request.user.role == User.TEACHER :
             teacher=Teacher.objects.get(user_id=request.user.id)
             context = {'title': 'Profile','teacher':teacher}

        elif request.user.role == User.PRINCIPAL:
            context = {'title': 'Profile'}
        return render(request, 'profile.html', context)

@login_required
def change_password(request):
    if request.method== 'POST':
        current_password=request.POST.get('currentpassword')
        new_password=request.POST.get('newpassword')
        confirm_password=request.POST.get('confirmpassword')
        user = User.objects.get(id=request.user.id)
        if new_password!=confirm_password:
            messages.info(request, 'password not matching')
        else:
            user.set_password(new_password)
            user.save()
        return redirect('profile')

@login_required
def list_teachers(request):
    if not (request.user.role == User.PRINCIPAL ):
        return HttpResponse('Unauthorized', status=401)
    else:
        if request.method == 'GET':
            teachers = Teacher.objects.all()
            context = {'title': 'Teachers', 'teachers': teachers}
            return render(request, 'list_teachers.html', context)


@login_required
def add_teachers(request):
    if not (request.user.role == User.PRINCIPAL ):
        return HttpResponse('Unauthorized', status=401)
    else:
        if request.method == 'GET':
            departments = Department.objects.all()
            context = {'departments': departments,
                    'positions': Teacher.POSITION_CHOICES}
            return render(request, 'add_teachers.html', context)
        if request.method == 'POST':
            name = request.POST.get('name')
            department = request.POST.get('department')
            email = request.POST.get('email')
            password=request.POST.get('password')
            mobile = request.POST.get('mobile')
            position = request.POST.get('position')
            profile_image = request.FILES['profile_image']
            user = User.objects.create_user(first_name=name, username=email, password=password,email=email, phone=mobile, role=User.TEACHER,
                                    department_id=department,profile_image=profile_image)
            Teacher.objects.create(position=position, user_id=user.id)
            return redirect('list_teachers')


@login_required
def edit_teacher(request, user_id):
    if not (request.user.role == User.PRINCIPAL ):
        return HttpResponse('Unauthorized', status=401)
    else:
        if request.method == 'GET':
            teacher = User.objects.get(id=user_id)
            departments = Department.objects.all()
            context = {'teacher': teacher, 'departments': departments,
                    'positions': Teacher.POSITION_CHOICES}
            return render(request, 'edit_teacher.html', context)
        if request.method == 'POST':
            name = request.POST.get('name')
            department = request.POST.get('department')
            email = request.POST.get('email')
            mobile = request.POST.get('mobile')
            position = request.POST.get('position')
            profile_image = request.FILES['profile_image']
            user = User.objects.get(id=user_id)
            teacher = Teacher.objects.get(user_id=user_id)
            dep = Department.objects.get(dname=department)
            user.first_name = name
            user.email = email
            user.phone = mobile
            user.department_id = dep.id
            user.profile_image=profile_image
            user.save()
            teacher.position = position
            teacher.save()
            return redirect('list_teachers')


@login_required
def approve_teacher(request, user_id):
    if not (request.user.role == User.PRINCIPAL ):
        return HttpResponse('Unauthorized', status=401)
    else:
        if request.method == 'POST':
            user = User.objects.get(id=user_id)
            user.is_active = not user.is_active
            user.save()
            return redirect('list_teachers')


@login_required
def remove_teacher(request, user_id):
    if not (request.user.role == User.PRINCIPAL ):
        return HttpResponse('Unauthorized', status=401)
    else:
        if request.method == 'POST':
            user = User.objects.get(id=user_id)
            user.delete()
            return redirect('list_teachers')


@login_required
def list_students(request):
    if not (request.user.role == User.PRINCIPAL or request.user.role == User.TEACHER):
        return HttpResponse('Unauthorized', status=401)
    else:
        if request.method == 'GET':
            students = Student.objects.all()
            context = {'students': students}
            return render(request, 'list_students.html', context)


@login_required
def add_student(request):
    if not (request.user.role == User.PRINCIPAL or request.user.role == User.TEACHER):
        return HttpResponse('Unauthorized', status=401)
    else:
        if request.method == 'GET':
            departments = Department.objects.all()
            batches = Class.objects.all()
            semesters = Semester.objects.all()
            context = {'departments': departments,
                    'batches': batches, 'semesters': semesters}
            return render(request, 'add_student.html', context)
        if request.method == 'POST':
            name = request.POST.get('name')
            admsn_no = request.POST.get('admsn_no')
            department = request.POST.get('department')
            semester = request.POST.get('semester')
            batch = request.POST.get('batch')
            email = request.POST.get('email')
            mobile = request.POST.get('mobile')
            password=request.POST.get('password')

            p_name = request.POST.get('p_name')
            p_mobile = request.POST.get('p_mobile')
            print( request.FILES['profile_image'])

            profile_image = request.FILES['profile_image']
            user = User.objects.create_user(first_name=name, password=password,username=email, email=email, phone=mobile,
                                            role=User.STUDENT, department_id=department,profile_image=profile_image)
            Student.objects.create(parent_name=p_name, admsn_no=admsn_no,
                                user_id=user.id, parent_mobile=p_mobile, batch_id=batch)
            return redirect('list_students')


@login_required
def edit_student(request, user_id):
    if not (request.user.role == User.PRINCIPAL or request.user.role == User.TEACHER):
        return HttpResponse('Unauthorized', status=401)
    else:
        if request.method == 'GET':
            student = Student.objects.get(user_id=user_id)
            departments = Department.objects.all()
            semesters = Semester.objects.all()
            batches = Class.objects.all()
            context = {'student': student, 'departments': departments,
                    'batches': batches, 'semesters': semesters}
            return render(request, 'edit_student.html', context)
        if request.method == 'POST':
            name = request.POST.get('name')
            admsn_no = request.POST.get('admsn_no')
            department = request.POST.get('department')
            semester = request.POST.get('semester')
            batch = request.POST.get('batch')
            email = request.POST.get('email')
            mobile = request.POST.get('mobile')
            p_name = request.POST.get('p_name')
            p_mobile = request.POST.get('p_mobile')
            profile_image = request.FILES['profile_image']
            student = Student.objects.get(user_id=user_id)
            user=student.user
            user.first_name = name
            student.admsn_no = admsn_no
            print(student.admsn_no)
            user.department_id = department
            student.batch.Semester_id = semester
            student.batch_id = batch
            user.email = email
            user.phone = mobile
            user.profile_image=profile_image
            print(profile_image)
            student.parent_mobile = p_mobile
            student.parent_name = p_name
            user.save()
            student.save()
            return redirect('list_students')


@login_required
def approve_student(request, user_id):
    if not (request.user.role == User.PRINCIPAL or request.user.role == User.TEACHER):
        return HttpResponse('Unauthorized', status=401)
    else:
        if request.method == 'POST':
            user = User.objects.get(id=user_id)
            user.is_active = not user.is_active
            user.save()
            return redirect('list_students')


@login_required
def remove_student(request, user_id):
    if not (request.user.role == User.PRINCIPAL or request.user.role == User.TEACHER):
        return HttpResponse('Unauthorized', status=401)
    else:
        if request.method == 'POST':
            student = Student.objects.get(user_id=user_id)
            student.delete()
            return redirect('list_students')
