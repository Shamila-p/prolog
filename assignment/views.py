import mimetypes
import os
from django.shortcuts import render,redirect,HttpResponse
from member.models import Student
from assignment.models import Assignment,module
from course.models import Class, Subject

# Create your views here.

def assignment(request,class_id,subject_id):
    if request.method == 'GET':
        assignments=Assignment.objects.filter(teacher_id=request.user.id,subject_id=subject_id,class_belongs_id=class_id)
        context={'assignments':assignments,'subject_id':subject_id,'class_id':class_id}
        return render(request,'assignment.html',context)
def add_assignment(request,class_id,subject_id):
    if request.method == 'GET':
        module_list=module.objects.all()
        context={'types':Assignment.ASSIGNMENT_CHOICES,'modules':module_list}
        return render(request,'add-assignment.html',context)
    if request.method == 'POST':
        topic = request.POST.get('topic')
        type = request.POST.get('type')
        modulename = request.POST.get('modulename')
        submission = request.POST.get('submission')
        upload = request.FILES.get('upload')
        # class_belongs=Class.objects.get(tutor_id=request.user.id)
        # subjects=Subject.objects.filter(assigned_to_id=request.user.id ,class_belongs_id=class_belongs.id)
        # for subject in subjects:
        #     print(subject)
        #     id=subject.id
        #     print(id)
        subject=subject_id
        Assignment.objects.create(topic=topic,submission_date=submission,type=type,questions=upload,module=modulename,teacher_id=request.user.id,subject_id=subject,class_belongs_id=class_id)
        return redirect('assignment',subject_id=subject_id,class_id=class_id)


def edit_assignment(request,assignment_id):
    if request.method == 'GET':
        assignment=Assignment.objects.get(id=assignment_id)
        modules=module.objects.all()
        context={'assignment':assignment,'types':Assignment.ASSIGNMENT_CHOICES,'modules':modules}
        return render(request,'edit_assignment.html',context)
    if request.method == 'POST':
        topic = request.POST.get('topic')
        type = request.POST.get('type')
        modulename = request.POST.get('modulename')
        submission = request.POST.get('submission')
        upload = request.FILES.get('upload')
        assignment=Assignment.objects.get(id=assignment_id)
        assignment.topic=topic
        assignment.type=type
        assignment.module=modulename
        assignment.submission_date=submission
        if upload is not None:
            assignment.questions=upload
        assignment.save()
        return redirect('assignment',subject_id=assignment.subject_id,class_id=assignment.class_belongs_id)

def remove_assignment(request,assignment_id):
    print(assignment_id)
    if request.method == 'POST':
        assignment=Assignment.objects.get(id=assignment_id)
        assignment.delete()
        return redirect('assignment',subject_id=assignment.subject_id,class_id=assignment.class_belongs_id)


    

def list_module(request):
    if request.method == 'GET':
        # context={'types':Assignment.ASSIGNMENT_CHOICES}
        modules=module.objects.all()
        context={'modules':modules}
        return render(request,'list_module.html',context)


def add_module(request):
    if request.method == 'GET':
        return render(request,'add_module.html')
    if request.method == 'POST':
        modulename=request.POST.get('modulename')
        module.objects.create(modulename=modulename)
        return redirect(list_module)

def remove_module(request,module_id):
    modulename=module.objects.get(id=module_id)
    modulename.delete()
    return redirect('list_module')
    

def view_assignments(request):
    if request.method == 'GET':
        student=Student.objects.get(user_id=request.user.id)
        assignments=Assignment.objects.filter(class_belongs_id=student.batch_id)
        context={'assignments':assignments}
        return render(request,'view_assignments.html',context)

def download_file(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = 'test.txt'
    filepath = BASE_DIR + '/downloadapp/Files/' + filename
    path = open(filepath, 'r')
    mime_type, _ = mimetypes.guess_type(filepath)
    response = HttpResponse(path, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response