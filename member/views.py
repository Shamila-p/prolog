import os
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from course.models import Class, Department, EditSubject, Semester, Subject
from course.views import department
from member.models import EditProfile, Student, TimeTable, User
from django.contrib import messages
from django.db.models import Q
import mimetypes


@login_required
def profile(request):
    if request.method == 'GET':
        if request.user.role == User.STUDENT:
            student = Student.objects.get(user_id=request.user.id)
            context = {'student': student, 'title': 'Profile'}
        elif request.user.role == User.TEACHER:
            teacher = User.objects.get(id=request.user.id)
            context = {'teacher': teacher, 'title': 'Profile'}
        elif request.user.role == User.PRINCIPAL:
            principal = User.objects.get(role=User.PRINCIPAL)
            context = {'principal': principal, 'title': 'Profile'}
        # is_tutor=Class.objects.filter(tutor_id=request.user.id).exists()
        # teacher = User.objects.get(id=request.user.id)
        # context={'teacher':teacher,}
        return render(request, 'profile.html', context)


def edit_profile(request):
    if request.method=='GET':
        if request.method == 'GET':
            if request.user.role == User.STUDENT:
                student = Student.objects.get(user_id=request.user.id)
                context = {'student': student, 'title': 'Edit Profile'}
            elif request.user.role == User.TEACHER:
                teacher = User.objects.get(id=request.user.id)
                context = {'teacher': teacher, 'title': 'Edit Profile'}
            elif request.user.role == User.PRINCIPAL:
                principal = User.objects.get(role=User.PRINCIPAL)
                context = {'principal': principal, 'title': 'Edit Profile'}
       
        return render(request, 'edit_profile.html', context)
        # print(request.user.id)
        # student = Student.objects.get(user_id=request.user.id)
        # teacher = User.objects.get(id=request.user.id)
        # principal = User.objects.get(role=User.PRINCIPAL)

        # context={'title':'Edit Profile','student':student,'teacher':teacher,'principal':principal}
        # return render(request,'edit_profile.html',context)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        profile_image = request.FILES.get('profile_image')
        if request.user.role == User.STUDENT:
            p_name = request.POST.get('p_name')
            p_mobile = request.POST.get('p_mobile')
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
            student = Student.objects.get(user_id=request.user.id)
            if user.first_name == name:
                name = None
            if user.email == email:
                email = None
            if user.phone == phone:
                phone = None
            if user.profile_image == profile_image:
                profile_image = None
            if student.parent_name == p_name:
                p_name = None
            if student.parent_mobile == p_mobile:
                p_mobile = None
            if (name is not None or email is not None or phone is not None or profile_image is not None or p_mobile is not None or p_name is not None):
                if EditProfile.objects.filter(user_id=request.user.id).exists():
                    messages.error(
                        request, "Pending request. You can oly send other requests once it gets approved")
                    return redirect('profile')
                else:
                    EditProfile.objects.create(name=name, phone=phone, email=email, profile_image=profile_image,
                                               parent_name=p_name, parent_mobile=p_mobile, user_id=request.user.id)

        elif request.user.role == User.TEACHER:
            user = User.objects.get(id=request.user.id)
            if user.first_name == name:
                name = None
            if user.email == email:
                email = None
            if user.phone == phone:
                phone = None
            if user.profile_image == profile_image:
                profile_image = None

            if (name is not None or email is not None or phone is not None or profile_image is not None):
                EditProfile.objects.create(
                    name=name, phone=phone, email=email, profile_image=profile_image, user_id=request.user.id)
        return redirect('profile')


def edit_profile_request(request, user_id):
    if request.method == 'GET':
        user = User.objects.get(id=user_id)
        edit = EditProfile.objects.get(user_id=user_id)
        if user.role == User.STUDENT:
            student = Student.objects.get(user_id=user_id)
            context = {'student': student, 'edit': edit, 'user': user, 'title': 'Edit Requests'}
        elif user.role == User.TEACHER:
            teacher = User.objects.get(id=user_id)
            context = {'teacher': teacher, 'edit': edit, 'user': user,'title': 'Edit Requests' }
        return render(request, 'requests.html', context)


def accept_request(request, user_id):
    if request.method == 'POST':
        edit = EditProfile.objects.get(user_id=user_id)
        user = User.objects.get(id=user_id)
        # name=edit.name
        # phone=edit.phone
        # email=edit.email
        # parent_name=edit.parent_name
        # parent_mobile=edit.parent_mobile
        # profile=edit.profile_image
        print(profile)
        if edit.user.role == User.STUDENT:
            student = Student.objects.get(user_id=user_id)
            if edit.name is not None:
                user.first_name = edit.name
                print(user.first_name)
            if edit.phone is not None:
                user.phone = edit.phone
            if edit.email is not None:
                user.email = edit.email
                user.username = edit.email
            if edit.parent_name is not None:
                student.parent_name = edit.parent_name
            if edit.parent_mobile is not None:
                student.parent_mobile = edit.parent_mobile
            if edit.profile_image != "" and edit.profile_image is not None:
                user.profile_image = edit.profile_image
            user.save()
            student.save()
            edit.delete()
            return redirect('list_students')

        if edit.user.role == User.TEACHER:
            teacher = User.objects.get(id=user_id)
            if edit.name is not None:
                teacher.first_name = edit.name
            if edit.phone is not None:
                teacher.phone = edit.phone
            if edit.email is not None:
                teacher.email = edit.email
                teacher.username = edit.email
            if edit.profile_image != "" and edit.profile_image is not None:
                teacher.profile_image = edit.profile_image
            teacher.save()
            edit.delete()
            return redirect('list_teachers')


def decline_request(request, user_id):
    if request.method == 'POST':
        edit = EditProfile.objects.get(user_id=user_id)
        edit.delete()
        return redirect('list_students')


@login_required
def change_password(request):
    if request.method == 'GET':
        context={'title':'Change/Reset Password',}
        return render(request,'change_password.html',context)
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
            hod = User.objects.get(id=request.user.id)
            print(hod)
            teacher_belongs = User.objects.filter(
                role=User.TEACHER, department_id=hod.department_id).exclude(position=User.HOD)
            print(teacher_belongs)
            edits = EditProfile.objects.all()
            context = {'title': 'Teachers', 'teachers': teachers,
                       'edits': edits, 'teacher_belongs': teacher_belongs,'title': 'List Teachers'}
            return render(request, 'list_teachers.html', context)


@login_required
def add_teachers(request):
    if not (request.user.role == User.PRINCIPAL or request.user.position == User.HOD):
        return HttpResponse('Unauthorized', status=401)
    else:
        if request.method == 'GET':
            departments = Department.objects.all()
            context = {'departments': departments,
                       'positions': User.POSITION_CHOICES,'title': 'Add Teacher'}
            return render(request, 'add_teachers.html', context)
        if request.method == 'POST':
            name = request.POST.get('name')
            department = request.POST.get('department')
            email = request.POST.get('email')
            password = request.POST.get('password')
            mobile = request.POST.get('mobile')
            position = request.POST.get('position')
            profile_image = request.FILES['profile_image']
            hod = User.objects.get(id=request.user.id)

            if request.user.position != User.HOD:
                User.objects.create_user(first_name=name, username=email, password=password, email=email,
                                         phone=mobile, role=User.TEACHER,
                                         department_id=department, profile_image=profile_image, position=position)
            else:
                User.objects.create_user(first_name=name, username=email, password=password, email=email,
                                         phone=mobile, role=User.TEACHER,
                                         department_id=hod.department_id, profile_image=profile_image, position=position)
            return redirect('list_teachers')


@login_required
def edit_teacher(request, user_id):
    if not (request.user.role == User.PRINCIPAL or request.user.position == User.HOD):
        return HttpResponse('Unauthorized', status=401)
    else:
        if request.method == 'GET':
            teacher = User.objects.get(id=user_id)
            departments = Department.objects.all()
            context = {'teacher': teacher, 'departments': departments,
                       'positions': User.POSITION_CHOICES,'title': 'Edit Teacher'}
            return render(request, 'edit_teacher.html', context)
        if request.method == 'POST':
            name = request.POST.get('name')
            department = request.POST.get('department')
            email = request.POST.get('email')
            mobile = request.POST.get('mobile')
            position = request.POST.get('position')
            profile_image = request.FILES.get('profile_image')
            user = User.objects.get(id=user_id)
            hod = User.objects.get(id=request.user.id)
            # dep = Department.objects.get(dname=department)
            if profile_image is not None:
                user.profile_image = profile_image
            user.first_name = name
            user.email = email
            user.phone = mobile
            if request.user.position != User.HOD:
                user.department_id = department
            user.position = position
            user.save()
            return redirect('list_teachers')


@login_required
def approve_teacher(request, user_id):
    if not (request.user.role == User.PRINCIPAL or request.user.position == User.HOD):
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
    if not (request.user.role == User.PRINCIPAL or request.user.role == User.TEACHER or request.user.position == User.HOD):
        return HttpResponse('Unauthorized', status=401)
    else:
        if request.method == 'GET':
            if request.user.role == User.PRINCIPAL or request.user.position == User.HOD:
                students = Student.objects.all()
                edits = EditProfile.objects.all()
                hod = User.objects.get(id=request.user.id)
                student_belongs = User.objects.filter(
                    role=User.STUDENT, department_id=hod.department_id)
                student_list = []
                for student in student_belongs:
                    student_list.append(student.id)
                studentslist = Student.objects.filter(user_id__in=student_list)
                context = {'students': students, 'edits': edits,
                           'student_belongs': student_belongs, 'studentslist': studentslist,'title': 'List Student'}
            is_tutor = Class.objects.filter(tutor_id=request.user.id).exists()

            if request.user.role == User.TEACHER and is_tutor:
                # tutor = User.objects.get(id=request.user.id)
                class_students = Class.objects.get(tutor_id=request.user.id)
                tutor_students = Student.objects.filter(
                    batch_id=class_students.id, semester_id=class_students.Semester_id)
                context = {'is_tutor': is_tutor,
                           'tutor_students': tutor_students,'title': 'List Student'}

            # tutor_student_list=[]
            # for student in tutor_students:
            #     tutor_student_list.append(student.id)
            return render(request, 'list_students.html', context)


@login_required
def add_student(request):
    if not (request.user.role == User.PRINCIPAL or request.user.role == User.TEACHER):
        return HttpResponse('Unauthorized', status=401)
    else:
        if request.method == 'GET':
            departments = Department.objects.all()
            semesters = Semester.objects.all()
            is_tutor = Class.objects.filter(tutor_id=request.user.id).exists()

            if request.user.role == User.TEACHER and request.user.position == User.HOD:
                print(request.user.id)
                logined_department = Department.objects.get(
                    hod_id=request.user.id)
                batches = Class.objects.filter(
                    department_id=logined_department.id)
                print(batches)
                context = {'batches': batches, 'departments': departments,
                           'semesters': semesters, 'quota_list': Student.QUOTA_CHOICES,'title': 'Add Student'}
            elif request.user.role == User.PRINCIPAL:
                print('ggg')
                batches = Class.objects.all()
                context = {'batches': batches, 'departments': departments,
                           'semesters': semesters, 'quota_list': Student.QUOTA_CHOICES,'title': 'Add Student'}
            elif request.user.role == User.TEACHER and is_tutor:
                print('g')
                student = Class.objects.get(tutor_id=request.user.id)
                print(student)
                context = {'student': student, 'departments': departments,
                           'quota_list': Student.QUOTA_CHOICES,'title': 'Add Student'}
            return render(request, 'add_student.html', context)
        if request.method == 'POST':
            name = request.POST.get('name')
            admsn_no = request.POST.get('admsn_no')
            department = request.POST.get('department')
            # semester = request.POST.get('semester')
            batch = request.POST.get('class')
            quota = request.POST.get('quota')
            print(batch)
            email = request.POST.get('email')
            mobile = request.POST.get('mobile')
            password = request.POST.get('password')

            p_name = request.POST.get('p_name')
            p_mobile = request.POST.get('p_mobile')
            print(request.FILES['profile_image'])

            profile_image = request.FILES['profile_image']
            hod = User.objects.get(id=request.user.id)
            is_tutor = Class.objects.filter(tutor_id=request.user.id).exists()
            if request.user.role == User.PRINCIPAL:
                batch_id = Class.objects.get(id=batch)

                user = User.objects.create_user(first_name=name, password=password, username=email, email=email,
                                                phone=mobile,
                                                role=User.STUDENT, department_id=department, profile_image=profile_image, position=0)
                Student.objects.create(parent_name=p_name, admsn_no=admsn_no,
                                       user_id=user.id, parent_mobile=p_mobile, batch_id=batch_id.id, semester_id=batch_id.Semester_id, quota=quota)
            if request.user.position == User.HOD:
                batch_id = Class.objects.get(id=batch)

                user = User.objects.create_user(first_name=name, password=password, username=email, email=email,
                                                phone=mobile,
                                                role=User.STUDENT, department_id=hod.department_id, profile_image=profile_image, position=0)
                Student.objects.create(parent_name=p_name, admsn_no=admsn_no,
                                       user_id=user.id, parent_mobile=p_mobile, batch_id=batch_id.id, semester_id=batch_id.Semester_id, quota=quota)
            if request.user.role == User.TEACHER and is_tutor:
                tutor = Class.objects.get(tutor_id=request.user.id)
                user = User.objects.create_user(first_name=name, password=password, username=email, email=email,
                                                phone=mobile,
                                                role=User.STUDENT, department_id=hod.department_id, profile_image=profile_image, position=0)
                Student.objects.create(parent_name=p_name, admsn_no=admsn_no,
                                       user_id=user.id, parent_mobile=p_mobile, batch_id=tutor.id, semester_id=tutor.Semester_id, quota=quota)
            return redirect('list_students')


@login_required
def edit_student(request, user_id):
    if not (request.user.role == User.PRINCIPAL or request.user.role == User.TEACHER):
        return HttpResponse('Unauthorized', status=401)
    else:
        if request.method == 'GET':
            student = Student.objects.get(user_id=user_id)
            departments = Department.objects.all()
            is_tutor = Class.objects.filter(tutor_id=request.user.id).exists()
            semesters = Semester.objects.all()
            batches = 0
            batch = 0
            if request.user.role == User.TEACHER and request.user.position == User.HOD:
                logined_department = Department.objects.get(
                    hod_id=request.user.id)
                batches = Class.objects.filter(
                    department_id=logined_department.id)
            elif request.user.role == User.PRINCIPAL:
                batches = Class.objects.all()
            elif request.user.role == User.TEACHER and is_tutor:
                batch = Class.objects.get(tutor_id=request.user.id)
            context = {'student': student, 'departments': departments,
                       'batches': batches, 'semesters': semesters, 'quota_list': Student.QUOTA_CHOICES, 'batch': batch,'title': 'Edit Student'}
            return render(request, 'edit_student.html', context)
        if request.method == 'POST':
            is_tutor = Class.objects.filter(tutor_id=request.user.id).exists()

            name = request.POST.get('name')
            admsn_no = request.POST.get('admsn_no')
            department = request.POST.get('department')
            # semester = request.POST.get('semester')
            quota = request.POST.get('quota')
            print(quota)
            batch = request.POST.get('batch')
            print(batch)
            email = request.POST.get('email')
            mobile = request.POST.get('mobile')
            p_name = request.POST.get('p_name')
            p_mobile = request.POST.get('p_mobile')
            profile_image = request.FILES.get('profile_image')
            student = Student.objects.get(user_id=user_id)
            print(student)
            user = student.user
            if profile_image is not None:
                user.profile_image = profile_image
            user.first_name = name
            student.admsn_no = admsn_no
            if request.user.position != User.HOD and request.user.role != User.TEACHER:
                user.department_id = department
            if not is_tutor:
                batche = Class.objects.get(id=batch)
                print(batche)
                print(batche.Semester_id)
                student.batch_id = batch

                student.semester_id = batche.Semester_id
            user.email = email
            user.phone = mobile
            student.parent_mobile = p_mobile
            student.parent_name = p_name
            # student.semester_id = semester
            if quota is not None:
                student.quota = quota
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
            user = User.objects.get(id=user_id)
            student.delete()
            user.delete()
            return redirect('list_students')


@login_required
def my_class(request):
    if request.method == 'GET':
        teacher = Class.objects.get(tutor_id=request.user.id)
        print(teacher.id)
        print(teacher.Semester_id)
        print(request.user.id)
        subject_details = Subject.objects.filter(tutor_id=request.user.id,semester_id=teacher.Semester_id)
        print(subject_details)
        timetable = TimeTable.objects.filter(
            batch_id=teacher.id, semester_id=teacher.Semester_id)
        is_uploaded = TimeTable.objects.filter(
            batch_id=teacher.id, semester_id=teacher.Semester_id).exists()
        print(is_uploaded)
        context = {'teacher': teacher,
                   'subject_details': subject_details, 'timetable': timetable, 'is_uploaded': is_uploaded,'title': 'My Class'}
        return render(request, 'my_class.html', context)


@login_required
def add_subject(request):
    if request.method == 'GET':
        teacher = User.objects.get(id=request.user.id)
        class_belongs_to = Class.objects.get(tutor_id=request.user.id)
        # |Q(id=teacher.id)
        teachers = User.objects.filter(
            department_id=teacher.department_id, role=User.TEACHER).exclude(position=User.HOD)
        context = {'teachers': teachers, 'class_belongs_to': class_belongs_to,'title': 'Add Subject'}
        return render(request, 'add_subject.html', context)
    if request.method == 'POST':
        subject_name = request.POST.get('subject_name')
        subject_code = request.POST.get('subject_code')
        print(subject_code)

        assigned = request.POST.get('assigned')
        teacher = Class.objects.get(tutor_id=request.user.id)
        print(teacher)
        print(teacher.Semester_id)
        class_belongs = Class.objects.get(tutor_id=request.user.id)
        print(class_belongs)
        batches = Class.objects.filter(
            classname=class_belongs.classname, Semester_id=class_belongs.Semester_id)
        for batch in batches:
            id = batch.id
        EditSubject.objects.create(subjectname=subject_name, subjectcode=subject_code, tutor_id=request.user.id,
                                   assigned_to_id=assigned, class_belongs_id=id, semester_id=teacher.Semester_id)
        return redirect('my_class')


@login_required
def edit_subject(request, subject_id):
    if request.method == 'GET':
        subject = Subject.objects.get(id=subject_id)
        teacher = User.objects.get(id=request.user.id)
        teachers = User.objects.filter(department_id=teacher.department_id, role=User.TEACHER).exclude(
            Q(position=User.HOD) | Q(id=teacher.id))
        context = {'subject': subject, 'teachers': teachers,'title': 'Edit Subject'}
        return render(request, 'edit_subject.html', context)
    if request.method == 'POST':
        subject_name = request.POST.get('subject_name')
        subject_code = request.POST.get('subject_code')
        assigned = request.POST.get('assigned')
        edit = Subject.objects.get(id=subject_id)
        edit.subjectname = subject_name
        edit.subjectcode = subject_code
        edit.assigned_to_id = assigned
        edit.save()
        return redirect('my_class')


@login_required
def remove_subject(request, subject_id):
    if request.method == 'POST':
        edit = Subject.objects.get(id=subject_id)
        edit.delete()
        return redirect('my_class')


@login_required
def subject_request(request):
    if request.method == 'GET':
        subjects = EditSubject.objects.all()
        if len(subjects) == 0:

            # hod=User.objects.get(id=request.user.id)
            # is_tutor=Class.objects.filter(department_id=hod.department_id)
            # for tutor in is_tutor:
            #     tutors=EditSubject.objects.all()
            #     print(tutors)
            #     if tutor.tutor_id in tutors.tutor_id:
            #         t=tutor
            #         print(t)
            # tutor=User.objects.filter(department_id=hod.department_id,role=User.TEACHER)
            messages.info(request, "No new subject requests")

        context = {'subjects': subjects,'title': 'Subject Requests'}
        return render(request, 'subject_request.html', context)


@login_required
def approve_request(request, subject_id):
    if request.method == 'POST':
        print(subject_id)

        edit = EditSubject.objects.get(id=subject_id)
        Subject.objects.create(subjectname=edit.subjectname, subjectcode=edit.subjectcode, tutor_id=edit.tutor_id,
                               assigned_to_id=edit.assigned_to_id, class_belongs_id=edit.class_belongs_id, semester_id=edit.semester_id)
        edit.delete()
        return redirect('subject_request')


@login_required
def deny_request(request, subject_id):
    if request.method == 'POST':
        edit = EditSubject.objects.get(id=subject_id)
        print(edit)
        edit.delete()
        return redirect('subject_request')


@login_required
def my_subjects(request):
    if request.method == 'GET':
        classes = Subject.objects.filter(assigned_to_id=request.user.id)
        print(classes)
        if len(classes) == 0:
            messages.info(request, "No subjects assigned yet")
        context = {'classes': classes,'title': 'Subjects'}
        return render(request, 'my_subjects.html', context)


@login_required
def student_details(request, class_id, subject_id, semester_id):
    print(class_id)
    print(semester_id)
    if request.method == 'GET':
        print('g')
        subject = Subject.objects.get(id=subject_id)
        students = Student.objects.filter(
            batch_id=class_id, semester_id=semester_id)
        print(students)
        context = {'students': students, 'subject': subject,'title': 'Student Details'}
        return render(request, 'student_details.html', context)


@login_required
def add_timetable(request, class_id, semester_id):
    if request.method == 'POST':
        timetable = request.FILES.get('timetable')
        print(class_id)
        print(semester_id)
        is_uploaded = TimeTable.objects.filter(
            batch_id=class_id, semester_id=semester_id).exists()
        print(is_uploaded)
        if is_uploaded is not True:
            TimeTable.objects.create(time_table=timetable,
                                     batch_id=class_id, semester_id=semester_id)
            messages.info(request, "File uploaded Succesfully")
        else:
            messages.info(
                request, "Timetable already uploaded. If you are looking for editing please choose the edit option")
        return redirect('my_class')


@login_required
def view_timetable(request):
    if request.method == 'GET':
        student = Student.objects.get(user_id=request.user.id)
        timetable = TimeTable.objects.filter(
            batch_id=student.batch_id, semester_id=student.semester_id)
        context = {'timetable': timetable}
        return render(request, 'view_table.html', context)


@login_required
def download_file(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = 'test.txt'
    filepath = BASE_DIR + '/downloadapp/Files/' + filename
    path = open(filepath, 'r')
    mime_type, _ = mimetypes.guess_type(filepath)
    response = HttpResponse(path, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response


@login_required
def change_semester(request):
    if request.method == 'POST':
        # teacher=User.objects.get(user_id=request.user.id)
        batch=Class.objects.get(tutor_id=request.user.id)
        students=Student.objects.filter(semester_id=batch.Semester_id,batch_id=batch.id)
        semesters=Semester.objects.all()
        order_list=[]
        for semester in semesters:
            order_list.append(semester.order)
        print(order_list)
        max_order=max(order_list)
        print(max_order)
        for student in students:
             if student.semester.order != (max_order):
                print(student.semester)
                order=int(student.semester.order )
                print(type(order))
                order_new=order+1
                print(order_new)
                newsemester=Semester.objects.get(order=order_new)
                student.semester_id=newsemester.id
                batch.Semester_id=newsemester.id
                batch.tutor_id=request.user.id
                subjects=Subject.objects.filter(tutor_id=request.user.id)
                print(subjects)
               
                student.save()
                batch.save()
        return redirect('list_students')
