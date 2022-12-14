from datetime import datetime
from django.contrib.auth.decorators import login_required
import json
from django.http import JsonResponse
from django.shortcuts import render, redirect
from course.models import Class, Subject
from .models import Attendence
from member.models import Student, User
from django.contrib import messages
from twilio.rest import Client
from decouple import config


# Create your views here.

@login_required
def attendence(request, class_id, subject_id, semester_id):
    if request.method == 'GET':
        # class_belongs=Class.objects.get(tutor_id=request.user.id)
        # subjects=Subject.objects.filter(assigned_to_id=request.user.id ,class_belongs_id=class_belongs.id)
        # for i in subjects:
        #     id=i
        # subject=Subject.objects.get(id=id.id)
        students = Student.objects.filter(
            batch_id=class_id, semester_id=semester_id)
        print(students)
        context = {'students': students, 'class_id': class_id,
                   'subject_id': subject_id, 'semester_id': semester_id,'title': ' Add Attendence','hours':Attendence.HOUR_CHOICES}
        return render(request, 'attendence.html', context)

@login_required
def add_attendence(request, class_id, subject_id, semester_id):
    if request.method == 'POST':
        date = request.POST['date']
        hour=request.POST['hour']
        print(hour)
        bb = request.POST['attendences']
        attendences = json.loads(bb)
        print(attendences)
        for attendence in attendences:
            name = attendence["name"]
            is_present = attendence["is_present"]
            if is_present is False:
                account_sid = config('account_sid')
                auth_token = config('auth_token')
                client = Client(account_sid, auth_token)

                message = client.messages.create(
                                            body=f'student is absent',
                                            from_='+18055904816',
                                            to='+918590426660'
                                        )

                # print(message.sid)
            # class_belongs=Class.objects.get(tutor_id=request.user.id)
            # subjects=Subject.objects.filter(assigned_to_id=request.user.id ,class_belongs_id=class_id,semester_id=semester_id,subject_id=subject_id)
            # for i in subjects:
            #     id=i
            # subject=Subject.objects.get(id=id.id)
            user = User.objects.get(first_name=name)
            student = Student.objects.get(user_id=user.id)
            if Attendence.objects.filter(date=date,hour=hour, subject_id=subject_id, teacher_id=request.user.id, student_id=student.id, semester_id=semester_id, class_belongs_id=class_id).exists():
                is_exist = True
            else:
                is_exist = False
                Attendence.objects.create(date=date,hour=hour,subject_id=subject_id, is_present=is_present, teacher_id=request.user.id,
                                          student_id=student.id, semester_id=semester_id, class_belongs_id=class_id)
                
        if is_exist:
            messages.info(
                request, "Attendence alreday added. If you want to edit please choose edit option")
        else:
            messages.info(request, "attendence added")
        return JsonResponse({'status': 'success'})

@login_required
def edit_attendence(request, class_id, subject_id, semester_id):
    if request.method == 'GET':
        selected_date = request.GET.get('date')
        selected_hour = request.GET.get('hour')
        print(selected_date)
        if selected_date is None:
            selected_date = datetime.today().strftime('%Y-%m-%d')
            print(selected_date)
        attendences = Attendence.objects.filter(
            date=selected_date, hour=selected_hour,class_belongs_id=class_id, subject_id=subject_id, semester_id=semester_id, teacher_id=request.user.id)
        context = {'class_id': class_id, 'subject_id': subject_id, 'semester_id': semester_id,
                   'attendences': attendences, 'selected_date': selected_date,'title': 'Edit Attendence','hours':Attendence.HOUR_CHOICES}
        return render(request, 'edit_attendence.html', context)
        # if selected_date is not None:
        #     attendence=Attendence.objects.filter(date=selected_date,class_belongs_id=class_id,subject_id=subject_id,semester_id=semester_id,teacher_id=request.user.id)
        # else:
        #     attendence=Attendence.objects.filter(date=date.today(),class_belongs_id=class_id,subject_id=subject_id,semester_id=semester_id,teacher_id=request.user.id)
        # context={'class_id':class_id,'subject_id':subject_id,'semester_id':semester_id,'attendences':attendence,'selected_date':selected_date}
        # return render(request,'edit_attendence.html',context)
    if request.method == 'POST':
        print('jhkh,gh')
        selected_date = request.POST['selected_date']
        selected_hour = request.POST['selected_hour']
        print(selected_date)
        bb = request.POST['attendences']
        print(bb)
        attendences = json.loads(bb)
        print(attendences)
        for attendence in attendences:
            print(attendence)
            name = attendence["name"]
            print(name)
            studentname = User.objects.filter(
                first_name=name, department_id=request.user.department_id)
            for student in studentname:
                stu = Student.objects.get(user_id=student.id)
                print(stu)
            print(studentname)
            is_present = attendence["is_present"]
            current = Attendence.objects.filter(date=selected_date,hour=selected_hour, class_belongs_id=class_id,
                                                subject_id=subject_id, semester_id=semester_id, teacher_id=request.user.id, student_id=stu)
            print(current)
            for student in current:
                print(student.is_present)
                student.is_present = is_present
                student.save()
        return JsonResponse({'status': 'success'})
# def edit_attendence(request,class_id,subject_id,semester_id):
#     if request.method == 'GET':
#         selected_date=request.GET.get('date')
#         print(selected_date)
#         if selected_date is None:
#             selected_date=datetime.today().strftime('%Y-%m-%d')
#             print(selected_date)
#         attendences=Attendence.objects.filter(date=selected_date,class_belongs_id=class_id,subject_id=subject_id,semester_id=semester_id,teacher_id=request.user.id)
#         context={'class_id':class_id,'subject_id':subject_id,'semester_id':semester_id,'attendences':attendences,'selected_date':selected_date}
#         return render(request,'edit_attendence.html',context)
#         # if selected_date is not None:
#         #     attendence=Attendence.objects.filter(date=selected_date,class_belongs_id=class_id,subject_id=subject_id,semester_id=semester_id,teacher_id=request.user.id)
#         # else:
#         #     attendence=Attendence.objects.filter(date=date.today(),class_belongs_id=class_id,subject_id=subject_id,semester_id=semester_id,teacher_id=request.user.id)
#         # context={'class_id':class_id,'subject_id':subject_id,'semester_id':semester_id,'attendences':attendence,'selected_date':selected_date}
#         # return render(request,'edit_attendence.html',context)
#     if request.method == 'POST':
#         print('jhkh,gh')
#         selected_date=request.POST['selected_date']
#         print(selected_date)
#         bb=request.POST['attendences']
#         print(bb)
#         attendences=json.loads(bb)
#         print(attendences)
#         for attendence in attendences:
#             name=attendence["name"]
#             is_present=attendence["is_present"]
#             current=Attendence.objects.filter(date=selected_date,class_belongs_id=class_id,subject_id=subject_id,semester_id=semester_id,teacher_id=request.user.id)
#             for student in current:
#                  student.is_present=is_present
#                  student.save()
#         return JsonResponse({'status': 'success'})

@login_required
def view_attendence(request, class_id, subject_id, semester_id):
    if request.method == 'GET':
        selected_date = request.GET.get('date')
        selected_hour = request.GET.get('hour')
        print(selected_date)
        if selected_date is None:
            selected_date = datetime.today().strftime('%Y-%m-%d')
            print(selected_date)
        attendences = Attendence.objects.filter(
            date=selected_date,hour=selected_hour, class_belongs_id=class_id, subject_id=subject_id, semester_id=semester_id, teacher_id=request.user.id)
        print(attendences)
        context = {'class_id': class_id, 'subject_id': subject_id, 'semester_id': semester_id,
                   'attendences': attendences, 'selected_date': selected_date,'hours':Attendence.HOUR_CHOICES}
        return render(request, 'view_attendence.html', context)

        # if selected_date is not None:
        #     attendences=Attendence.objects.filter(date=selected_date,class_belongs_id=class_id,subject_id=subject_id,semester_id=semester_id,teacher_id=request.user.id)
        #     if attendences is None:
        #         messages.info(request,"no record")
        # else:
        #     attendences=Attendence.objects.filter(date=date.today(),class_belongs_id=class_id,subject_id=subject_id,semester_id=semester_id,teacher_id=request.user.id)
        #     if attendences is None:
        #          messages.info(request,"no record")

        # print(attendences)
# def student_attendence(request):
#     student=Student.objects.get(user_id=request.user.id)
#     subjects=Subject.objects.filter(class_belongs_id=student.batch_id,semester_id=student.semester)
#     context={'subjects':subjects}
#     return render(request,'student_attendence.html',context)

# def view_student_attendence(request,subject_id):
#     # if request.method == 'GET':
#     #     print(subject_id)
#     #     return render(request,'view_student_attendence.html')
#         if request.method == 'GET':
#             student=Student.objects.get(user_id=request.user.id)
#             selected_date=request.GET.get('date')
#             print(selected_date)
#             if selected_date is None:
#                 selected_date=datetime.today().strftime('%Y-%m-%d')
#                 print(selected_date)
#             attendences=Attendence.objects.filter(date=selected_date,class_belongs_id=student.batch_id,subject_id=subject_id,semester_id=student.semester_id,student_id=student.id)
#             print(attendences)
#             context={'class_id':student.batch_id,'subject_id':subject_id,'semester_id':student.semester_id,'attendences':attendences,'selected_date':selected_date}
#             return render(request,'view_student_attendence.html',context)

#         selected_date=request.GET.get('date')
#         print(selected_date)
#         if selected_date is None:
#             selected_date=datetime.today().strftime('%Y-%m-%d')
#             print(selected_date)
#         attendences=Attendence.objects.filter(date=selected_date,class_belongs_id=class_id,subject_id=subject_id,semester_id=semester_id,teacher_id=request.user.id)
#         context={'class_id':class_id,'subject_id':subject_id,'semester_id':semester_id,'attendences':attendences,'selected_date':selected_date}
#         return render(request,'view_attendence.html',context)
    # student=Student.objects.get(user_id=request.user.id)
