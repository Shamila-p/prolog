from django.shortcuts import render,redirect

from assignment.models import Assignment,module
from course.models import Class, Subject

# Create your views here.

def assignment(request):
    if request.method == 'GET':
        assignments=Assignment.objects.all()
        context={'assignments':assignments}
        return render(request,'assignment.html',context)
def add_assignment(request):
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
        class_belongs=Class.objects.get(tutor_id=request.user.id)
        subjects=Subject.objects.filter(assigned_to_id=request.user.id ,class_belongs_id=class_belongs.id)
        for subject in subjects:
            id=subject.id
        Assignment.objects.create(topic=topic,submission_date=submission,type=type,questions=upload,subject_id=id,module=modulename)
        return redirect('assignment')


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
        return redirect('assignment')

def remove_assignment(request,assignment_id):
    if request.method == 'POST':
        assignment=Assignment.objects.get(id=assignment_id)
        assignment.delete()
        return redirect('assignment')


    

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
    