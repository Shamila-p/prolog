from asyncio.windows_events import NULL
from contextlib import nullcontext
from turtle import position
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from course.models import Class, Department, Semester
from course.views import department
from member.models import EditProfile, Student, User
from django.contrib import messages


@login_required
def profile(request):
    if request.method == 'GET':
        if request.user.role == User.STUDENT:
            student = Student.objects.get(user_id=request.user.id )
            context = {'title': 'Profile', 'student': student}
        elif request.user.role == User.TEACHER:
            teacher = User.objects.get(id=request.user.id)
            context = {'title': 'Profile', 'teacher': teacher}
        elif request.user.role == User.PRINCIPAL:
            principal = User.objects.get(role=User.PRINCIPAL)
            context = {'title': 'Profile', 'principal': principal}
        # tutor=Class.objects.filter(tutor_id=request.user.id).exists()
        # context={'tutor':tutor}
        
        return render(request, 'profile.html', context)


def edit_profile(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        profile_image = request.FILES.get('profile_image')
        if request.user.role == User.STUDENT:
            p_name=request.POST.get('p_name')
            p_mobile=request.POST.get('p_mobile')
        if request.user.role == User.PRINCIPAL:
            user = User.objects.get(role=User.PRINCIPAL)
            if profile_image is not None:
                user.profile_image = profile_image
            user.first_name = name
            user.email = email
            user.phone = phone
            user.save()
        elif request.user.role == User.STUDENT:
            user = User.objects.get(id=request.user.id)
            student=Student.objects.get(user_id=request.user.id)
            if user.first_name == name:
                name=None
            if user.email == email:
                email=None
            if user.phone == phone:
               phone=None
            if user.profile_image == profile_image:
               profile_image=None
            if student.parent_name == p_name:
                p_name=None
            if student.parent_mobile == p_mobile:
                p_mobile=None
            if (name is not None or email is not None or phone is not None or profile_image is not None or p_mobile is not None or p_name is not None):
                if EditProfile.objects.filter(user_id=request.user.id).exists():
                    messages.error(request, "Pending request. You can oly send other requests once it gets approved")
                    return redirect('profile')
                else:
                    EditProfile.objects.create(name=name,phone=phone,email=email,profile_image=profile_image,parent_name=p_name,parent_mobile=p_mobile,user_id=request.user.id)
                
                     
        elif request.user.role == User.TEACHER:
            user = User.objects.get(id=request.user.id)
            if user.first_name == name:
                name=None
            if user.email == email:
                email=None
            if user.phone == phone:
               phone=None
            if user.profile_image == profile_image:
               profile_image=None
           
            if (name is not None or email is not None or phone is not None or profile_image is not None):
                EditProfile.objects.create(name=name,phone=phone,email=email,profile_image=profile_image,user_id=request.user.id)
        return redirect('profile')

def edit_profile_request(request,user_id):
    if request.method=='GET':
        user=User.objects.get(id=user_id)
        edit=EditProfile.objects.get(user_id=user_id)
        if user.role == User.STUDENT:
            student = Student.objects.get(user_id=user_id)
            context = {'student': student,'edit':edit,'user':user,}
        elif user.role == User.TEACHER:
            teacher=User.objects.get(id=user_id)
            context = {'teacher': teacher,'edit':edit,'user':user,}
        return render(request,'requests.html',context)

def accept_request(request,user_id):
    if request.method=='POST':
        edit=EditProfile.objects.get(user_id=user_id)
        user=User.objects.get(id=user_id)
        # name=edit.name
        # phone=edit.phone
        # email=edit.email
        # parent_name=edit.parent_name
        # parent_mobile=edit.parent_mobile
        # profile=edit.profile_image
        print(profile)
        if edit.user.role==User.STUDENT:
            student=Student.objects.get(user_id=user_id)
            if edit.name is not None:
                user.first_name=edit.name
                print(user.first_name)
            if edit.phone is not None:
                user.phone=edit.phone
            if edit.email is not None:
                user.email=edit.email
                user.username=edit.email
            if edit.parent_name is not None:
                student.parent_name=edit.parent_name
            if edit.parent_mobile is not None:
                student.parent_mobile=edit.parent_mobile
            if edit.profile_image != "" and edit.profile_image is not None:
                user.profile_image=edit.profile_image
            user.save()
            student.save()
            edit.delete()
            return redirect('list_students')

        if edit.user.role==User.TEACHER:
            teacher=User.objects.get(id=user_id)
            if edit.name is not None:
                teacher.first_name=edit.name
            if edit.phone is not None:
                teacher.phone=edit.phone
            if edit.email is not None:
                teacher.email=edit.email
                teacher.username=edit.email
            if edit.profile_image != "" and edit.profile_image is not None:
                teacher.profile_image=edit.profile_image
            teacher.save()
            edit.delete()
            return redirect('list_teachers')

def decline_request(request,user_id):
    if request.method=='POST':
        edit=EditProfile.objects.get(user_id=user_id)
        edit.delete()
        return redirect('list_students')



@login_required
def change_password(request):
    if request.method == 'POST':
        current_password = request.POST.get('currentpassword')
        new_password = request.POST.get('newpassword')
        confirm_password = request.POST.get('confirmpassword')
        user = User.objects.get(id=request.user.id)
        if new_password != confirm_password:
            messages.info(request, 'password not matching')
        else:
            user.set_password(new_password)
            user.save()
        return redirect('profile')


@login_required
def list_teachers(request):
    if not (request.user.role == User.PRINCIPAL or request.user.position == User.HOD):
        return HttpResponse('Unauthorized', status=401)
    else:
        if request.method == 'GET':
            teachers = User.objects.filter(role=User.TEACHER)
            hod=User.objects.get(id=request.user.id)
            print(hod)
            teacher_belongs=User.objects.filter(role=User.TEACHER,department_id=hod.department_id).exclude(position=User.HOD)
            print(teacher_belongs)
            edits=EditProfile.objects.all()
            context = {'title': 'Teachers' ,'teachers': teachers,'edits':edits,'teacher_belongs':teacher_belongs}
            return render(request, 'list_teachers.html', context)


@login_required
def add_teachers(request):
    if not (request.user.role == User.PRINCIPAL or  request.user.position ==User.HOD):
        return HttpResponse('Unauthorized', status=401)
    else:
        if request.method == 'GET':
            departments = Department.objects.all()
            context = {'departments': departments,'positions': User.POSITION_CHOICES}
            return render(request, 'add_teachers.html', context)
        if request.method == 'POST':
            name = request.POST.get('name')
            department = request.POST.get('department')
            email = request.POST.get('email')
            password = request.POST.get('password')
            mobile = request.POST.get('mobile')
            position = request.POST.get('position')
            profile_image = request.FILES['profile_image']
            hod=User.objects.get(id=request.user.id)

            if request.user.position != User.HOD:
                User.objects.create_user(first_name=name, username=email, password=password, email=email,
                                            phone=mobile, role=User.TEACHER,
                                            department_id=department, profile_image=profile_image,position=position)
            else:
                User.objects.create_user(first_name=name, username=email, password=password, email=email,
                                            phone=mobile, role=User.TEACHER,
                                            department_id=hod.department_id, profile_image=profile_image,position=position)
            return redirect('list_teachers')


@login_required
def edit_teacher(request, user_id):
    if not (request.user.role == User.PRINCIPAL or  request.user.position ==User.HOD):
        return HttpResponse('Unauthorized', status=401)
    else:
        if request.method == 'GET':
            teacher = User.objects.get(id=user_id)
            departments = Department.objects.all()
            context = {'teacher': teacher, 'departments': departments,
                       'positions': User.POSITION_CHOICES}
            return render(request, 'edit_teacher.html', context)
        if request.method == 'POST':
            name = request.POST.get('name')
            department = request.POST.get('department')
            email = request.POST.get('email')
            mobile = request.POST.get('mobile')
            position = request.POST.get('position')
            profile_image = request.FILES.get('profile_image')
            user = User.objects.get(id=user_id)
            hod=User.objects.get(id=request.user.id)
            # dep = Department.objects.get(dname=department)
            if profile_image is not None:
                user.profile_image=profile_image
            user.first_name = name
            user.email = email
            user.phone = mobile
            if request.user.position != User.HOD:
                user.department_id=department
            user.position=position
            user.save()
            return redirect('list_teachers')


@login_required
def approve_teacher(request, user_id):
    if not (request.user.role == User.PRINCIPAL or request.user.position ==User.HOD):
        return HttpResponse('Unauthorized', status=401)
    else:
        if request.method == 'POST':
            user = User.objects.get(id=user_id)
            user.is_active = not user.is_active
            user.save()
            return redirect('list_teachers')


@login_required
def remove_teacher(request, user_id):
    if not (request.user.role == User.PRINCIPAL):
        return HttpResponse('Unauthorized', status=401)
    else:
        if request.method == 'POST':
            user = User.objects.get(id=user_id)
            user.delete()
            return redirect('list_teachers')


@login_required
def list_students(request):
    if not (request.user.role == User.PRINCIPAL or request.user.role == User.TEACHER  or  request.user.position == User.HOD):
        return HttpResponse('Unauthorized', status=401)
    else:
        if request.method == 'GET':
            students = Student.objects.all()
            edits=EditProfile.objects.all()
            hod=User.objects.get(id=request.user.id)
            student_belongs=User.objects.filter(role=User.STUDENT,department_id=hod.department_id)
            # is_tutor=Class.objects.filter(tutor_id=request.user.id).exists()
            student_list=[]
            for student in student_belongs:
                student_list.append(student.id)
            studentslist=Student.objects.filter(user_id__in=student_list)
            context = {'students': students,'edits':edits,'student_belongs':student_belongs,'studentslist':studentslist}
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
            password = request.POST.get('password')

            p_name = request.POST.get('p_name')
            p_mobile = request.POST.get('p_mobile')
            print(request.FILES['profile_image'])

            profile_image = request.FILES['profile_image']
            hod=User.objects.get(id=request.user.id)

            if request.user.role==User.PRINCIPAL:
                user = User.objects.create_user(first_name=name, password=password, username=email, email=email,
                                            phone=mobile,
                                            role=User.STUDENT, department_id=department, profile_image=profile_image)
                Student.objects.create(parent_name=p_name, admsn_no=admsn_no,
                                   user_id=user.id, parent_mobile=p_mobile, batch_id=batch)
            if request.user.position == User.HOD:   
                user = User.objects.create_user(first_name=name, password=password, username=email, email=email,
                                            phone=mobile,
                                            role=User.STUDENT, department_id=hod.department_id, profile_image=profile_image)
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
            profile_image = request.FILES.get('profile_image')
            student = Student.objects.get(user_id=user_id)
            user = student.user
            if profile_image is not None:
                user.profile_image=profile_image
            user.first_name = name
            student.admsn_no = admsn_no
            if request.user.position != User.HOD and request.user.role != User.TEACHER:
                user.department_id = department
            student.batch.Semester_id = semester
            student.batch_id = batch
            user.email = email
            user.phone = mobile
            student.parent_mobile = p_mobile
            student.parent_name = p_name
            user.save()
            student.save()
            return redirect('list_students')


@login_required
def approve_student(request, user_id):
    if not (request.user.role == User.PRINCIPAL or request.user.role==User.TEACHER ):
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
            user = User.objects.get(id=user_id)
            student.delete()
            user.delete()
            return redirect('list_students')
