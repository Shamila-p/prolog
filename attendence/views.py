import json
from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import render,redirect
from course.models import Class, Subject
from .models import Attendence
from member.models import Student,User
from django.contrib import messages

# Create your views here.
def attendence(request,class_id,subject_id):
    if request.method == 'GET':
        # class_belongs=Class.objects.get(tutor_id=request.user.id)
        # subjects=Subject.objects.filter(assigned_to_id=request.user.id ,class_belongs_id=class_belongs.id)
        # for i in subjects:
        #     id=i
        # subject=Subject.objects.get(id=id.id)
        students=Student.objects.filter(batch_id=class_id)
        context={'students':students,'class_id':class_id,'subject_id':subject_id}
        return render(request,'attendence.html',context)
    
def add_attendence(request,class_id,subject_id):
    if request.method == 'POST':
        date=request.POST['date']
        bb=request.POST['attendences']
        attendences=json.loads(bb)
        for attendence in attendences:
            name=attendence["name"]
            is_present=attendence["is_present"]
            class_belongs=Class.objects.get(tutor_id=request.user.id)
            subjects=Subject.objects.filter(assigned_to_id=request.user.id ,class_belongs_id=class_belongs.id)
            for i in subjects:
                id=i
            subject=Subject.objects.get(id=id.id)
            user=User.objects.get(first_name=name)
            student=Student.objects.get(user_id=user.id)
            Attendence.objects.create(date=date,subject_id=subject.id,is_present=is_present,teacher_id=request.user.id,student_id=student.id)
            messages.info(request,"attendence added")
            return JsonResponse({'status': 'success'})




