from django.shortcuts import render, redirect
from django.contrib import messages
from course.models import Class, Subject
from member.models import User, Student
from notifications.models import Complaint, Notification
# from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def complaint(request):
    if request.method == 'GET':
        if request.user.role == 'ST':
            student = Student.objects.get(user_id=request.user.id)
            print(student)
            print(student.batch_id)
            print(student.semester_id)
            subjects = Subject.objects.filter(
                class_belongs_id=student.batch_id, semester_id=student.semester_id)
            teachers = []
            for subject in subjects:
                teachers.append(subject.assigned_to.first_name)
            print(teachers)
        context = {'teachers': teachers, 'sends': User.ROLES_CHOICES,
                   'send_to': User.POSITION_CHOICES,'title': 'Complaints'}
        return render(request, 'complaint.html', context)
    if request.method == 'POST':
        print('hgjmj')
        send_to = request.POST.get('send_to')
        print(send_to)
        complaint = request.POST.get('complaint')
        print(complaint)
        student = Student.objects.get(user_id=request.user.id)
        print(student)
        Complaint.objects.create(send_to=send_to, message=complaint, student_id=student.id, batch_id=student.batch_id,
                                 semester_id=student.semester_id, department_id=student.batch.department_id)
        return redirect('complaint')

@login_required
def display_complaint(request):
    if request.method == 'GET':
        context = {}

        if request.user.role == 'PR':
            if Complaint.objects.filter(send_to=User.PRINCIPAL).exists():
                complaints = Complaint.objects.filter(send_to=User.PRINCIPAL)
                context = {'complaints': complaints,'title': 'List Complaints'}

            else:
                    messages.info(request, "No complaints yet")
                    return redirect('no_complaint')
        if request.user.role == 'TR' and request.user.position == User.HOD:
            hod = User.objects.get(id=request.user.id)
            if Complaint.objects.filter(send_to=User.HOD, department_id=hod.department_id).exists():
                complaints = Complaint.objects.filter(
                    send_to=User.HOD, department_id=hod.department_id)
                print(complaints)
                context = {'complaints': complaints}
            else:
                messages.info(request, "No complaints yet")
                return redirect('no_complaint')
        is_tutor = Class.objects.filter(tutor_id=request.user.id).exists()

        if request.user.role == 'TR' and not request.user.position == User.HOD:
            complaints = Complaint.objects.filter(
                send_to=request.user.first_name, department_id=request.user.department_id)
            if len(complaints) == 0:
                messages.info(request, "No complaints yet")

            print(complaints)
            context = {'complaints': complaints,'title': 'Complaints '}
        # if request.user.role == 'TR' and not is_tutor:
        #     complaints=Complaint.objects.filter(send_to=request.user.first_name,department_id=request.user.department_id)
        #     context={'complaints':complaints}
        return render(request, 'display_complaint.html', context)

@login_required
def no_complaint(request):
    if request.method == 'GET':
        return render(request, 'no_complaint.html',{'title':'Complaints'})

@login_required
def notification(request):
    if request.method == 'GET':
        context = {'sends': User.ROLES_CHOICES,
                   'send_to': User.POSITION_CHOICES,'title': 'Notificatons'}
        # context={'student':User.STUDENT,'hod':User.HOD,'teacher':User.TEACHER}
        return render(request, 'notification.html', context)
    if request.method == 'POST':
        print('hgjmj')
        send_to = request.POST.get('send_to')
        print(send_to)
        notification = request.POST.get('notification')
        print(notification)
        Notification.objects.create(send_to=send_to, message=notification)
        return redirect('notification')


@login_required
def view_notification(request):
     if request.method == 'GET':
        notifications=Notification.objects.all()
        context={'notifications':notifications}
        return render(request, 'view_notification.html', context)
@login_required
def display_notification(request):
    if request.method == 'GET':
        notification_list=[]
        if request.user.position == User.HOD:
            # notifications = Notification.objects.filter(
            #     Q(send_to=User.HOD) | Q(send_to=User.TEACHER))
            notifications = Notification.objects.filter(send_to=User.HOD)
            notification_list.append(notifications)
        if request.user.role == User.TEACHER:
            notifications = Notification.objects.filter(send_to=User.TEACHER)
            notification_list.append(notifications)

        if request.user.role == User.STUDENT:
            notifications = Notification.objects.filter(send_to=User.STUDENT)
            notification_list.append(notifications)
        print(notification_list)
        context = {'notification_list': notification_list,'title': 'Display Notifications'}
        return render(request, 'display_notification.html', context)
