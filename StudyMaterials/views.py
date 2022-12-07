from django.shortcuts import render,redirect
from django.contrib import messages
from StudyMaterials.models import Notes
from course.models import Class, Semester
from member.models import Student




def study_materials(request,class_id,semester_id,subject_id):
    if request.method == 'GET':
        context={'class_id':class_id,'subject_id':subject_id,'semester_id':semester_id}
        return render(request, 'study_materials.html',context)


def module(request,class_id,subject_id, semester_id,module_name):
    print(semester_id)
    if request.method == 'GET':
        materials=Notes.objects.filter(class_belongs_id=class_id,subject_id=subject_id,semester_id=semester_id)
        context = {'module_name': module_name,'materials':materials,'categories':Notes.MATERIAL_CHOICES,'class_id':class_id,'subject_id':subject_id,'semester_id':semester_id}
        return render(request, 'module.html', context)

def add_materials(request,class_id,subject_id,semester_id,module_name):
    if request.method == 'GET':
        context={'materials':Notes.MATERIAL_CHOICES,'class':class_id,'subject':subject_id,'module_name': module_name,'semester_id':semester_id}
        return render(request, 'add_materials.html',context)
    if request.method== 'POST':
        filename=request.POST.get('filename')
        category=request.POST.get('category')
        uploaded= request.FILES.get('upload')
        Notes.objects.create(filename=filename,module=module_name,category=category,filepath=uploaded,subject_id=subject_id,class_belongs_id=class_id,semester_id=semester_id)
        return redirect('module',module_name=module_name,class_id=class_id,subject_id=subject_id,semester_id=semester_id)

def edit_materials(request,class_id,subject_id,module_name,material_id,semester_id):
    if request.method=='GET':
        material=Notes.objects.get(id=material_id)
        context = {'material':material,'categories':Notes.MATERIAL_CHOICES,'class_id':class_id,'subject_id':subject_id,'module_name':module_name,'semester_id':semester_id}
        return render(request,'edit_material.html',context)
    if request.method== 'POST':
        filename=request.POST.get('filename')
        category=request.POST.get('category')
        uploaded= request.FILES.get('upload')
        material=Notes.objects.get(id=material_id)
        material.filename=filename
        material.category=category
        if uploaded is not None:
            material.filepath=uploaded
        material.save()
        return redirect('module',module_name=material.module,class_id=class_id,subject_id=subject_id,semester_id=semester_id)


def remove_materials(request,material_id,class_id,subject_id,semester_id,module_name):
    if request.method== 'POST':   
        material=Notes.objects.get(id=material_id)
        material.delete()
        return redirect('module',module_name=module_name,class_id=class_id,subject_id=subject_id,semester_id=semester_id)

def view_materials(request):
    if request.method == 'GET':
        semesters=Semester.objects.all()
        context={'semesters':semesters}
        # student=Student.objects.get(user_id=request.user.id)
        # materials=Notes.objects.filter(class_belongs_id=student.batch_id,semester_id=student.semester_id)
        # context={'materials':materials}
        return render(request,'view_materials.html',context)
    if request.method == 'POST':
        semester=request.POST.get('semester')
        print(semester)
        # student=Student
        return redirect(material_semester,semester_id=semester)

def material_semester(request,semester_id):
    student=Student.objects.get(user_id=request.user.id)
    batches=Class.objects.filter(Semester_id=semester_id,classname=student.batch.classname)
    batch_id_list=[]
    for batch in batches:
        batch_id_list.append(batch.id)
    materials=Notes.objects.filter(class_belongs_id__in=batch_id_list,semester_id=semester_id)
    if len(materials) == 0:
        messages.info(request,"materials not available")
    context={'material_list':materials}
    return render(request,'semester_materials.html',context)


def list_materials(request,semester_id,subject_id):
    if request.method == 'GET':
        student=Student.objects.get(user_id=request.user.id)
        batches=Class.objects.filter(Semester_id=semester_id,classname=student.batch.classname)
        for batch in batches:
            if not Notes.objects.filter(class_belongs_id=batch.id,semester_id=semester_id,subject_id=subject_id).exists:
                messages.info("No materials available")
            materials=Notes.objects.filter(class_belongs_id=batch.id,semester_id=semester_id,subject_id=subject_id)
            print(materials)
            context={'materials':materials}
            return render(request,'list_materials.html',context)


