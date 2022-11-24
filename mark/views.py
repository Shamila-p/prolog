from django.shortcuts import render,redirect
from mark.models import Mark
from member.models import Student
from course.models import Class, Subject

# Create your views here.
def mark(request,class_id,subject_id):
    if request.method == 'GET':
        # class_belongs=Class.objects.get(tutor_id=request.user.id)
        # subjects=Subject.objects.filter(assigned_to_id=request.user.id ,class_belongs_id=class_belongs.id)
        # subject=None
        # for i in subjects:
        #     subject=i
        # subject=Subject.objects.get(id=subject.id)
        # students=Student.objects.filter(batch_id=subject.class_belongs_id)
        students=Student.objects.filter(batch_id=class_id)

        context={'students':students,'class_id':class_id,'subject_id':subject_id}
        return render(request,'mark.html',context)

def view_marks(request,class_id,subject_id):
    if request.method=='GET':
        marks=Mark.objects.filter(class_belongs_id=class_id,subject_id=subject_id,teacher_id=request.user.id)
        context={'marks':marks,'class_id':class_id,'subject_id':subject_id}
        return render(request,'view_marks.html',context)

def add_mark(request,class_id,subject_id,student_id):
    if request.method == 'GET':
        print(student_id)
        context={'exams':Mark.EXAM_CHOICES,'class_id':class_id,'subject_id':subject_id,'student_id':student_id}
        return render(request,'add_mark.html',context)
    if request.method == 'POST':
        total_score=request.POST.get('tmark')
        scored_mark=request.POST.get('smark')
        exam_type=request.POST.get('type')
        # class_belongs=Class.objects.get(tutor_id=request.user.id)
        # subjects=Subject.objects.filter(assigned_to_id=request.user.id ,class_belongs_id=class_belongs.id)
        # for i in subjects:
        #     id=i
        # subject=Subject.objects.get(id=id.id)
        student=Student.objects.get(user_id=student_id)
        Mark.objects.create(exam_type=exam_type,total_score=total_score,marked_score=scored_mark,subject_id=subject_id,teacher_id=request.user.id,student_id=student.id,class_belongs_id=class_id)
        return redirect('view_marks',class_id=class_id,subject_id=subject_id)



def edit_mark(request,class_id,subject_id,student_id):
    mark=Mark.objects.filter(student_id=student_id,class_belongs_id=class_id,subject_id=subject_id,teacher_id=request.user.id).exists()
    if mark is not None:
        if request.method == 'GET':
            mark=Mark.objects.filter(student_id=student_id,class_belongs_id=class_id,subject_id=subject_id,teacher_id=request.user.id)
            print(mark)
            context={'exams':Mark.EXAM_CHOICES,'mark':mark}
            return render(request,'edit_mark.html',context)        
        if request.method == 'POST':
            total_score=request.POST.get('tmark')
            scored_mark=request.POST.get('smark')
            exam_type=request.POST.get('type')
            marks=Mark.objects.filter(student_id=student_id,class_belongs_id=class_id,subject_id=subject_id,teacher_id=request.user.id)
            for mark in marks:
                mark.total_score=total_score
                mark.marked_score=scored_mark
                mark.exam_type=exam_type
                mark.save()
            return redirect('view_marks',class_id=class_id,subject_id=subject_id)
