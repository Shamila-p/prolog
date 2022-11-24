from django.shortcuts import render,redirect

from StudyMaterials.models import Notes




def study_materials(request,class_id,subject_id):
    if request.method == 'GET':
        context={'class_id':class_id,'subject_id':subject_id}
        return render(request, 'study_materials.html',context)


def module(request,class_id,subject_id, module_name):
    if request.method == 'GET':
        materials=Notes.objects.filter(class_belongs_id=class_id,subject_id=subject_id)
        context = {'module_name': module_name,'materials':materials,'categories':Notes.MATERIAL_CHOICES,'class_id':class_id,'subject_id':subject_id}
        return render(request, 'module.html', context)

def add_materials(request,class_id,subject_id,module_name):
    if request.method == 'GET':
        context={'materials':Notes.MATERIAL_CHOICES,'class':class_id,'subject':subject_id,'module_name': module_name}
        return render(request, 'add_materials.html',context)
    if request.method== 'POST':
        filename=request.POST.get('filename')
        category=request.POST.get('category')
        uploaded= request.FILES.get('upload')
        Notes.objects.create(filename=filename,module=module_name,category=category,filepath=uploaded,subject_id=subject_id,class_belongs_id=class_id)
        return redirect('module',module_name=module_name,class_id=class_id,subject_id=subject_id)

def edit_materials(request,class_id,subject_id,module_name,material_id):
    if request.method=='GET':
        material=Notes.objects.get(id=material_id)
        context = {'material':material,'categories':Notes.MATERIAL_CHOICES,'class_id':class_id,'subject_id':subject_id,'module_name':module_name}
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
        return redirect('module',module_name=material.module,class_id=class_id,subject_id=subject_id)


def remove_materials(request,material_id,class_id,subject_id,module_name):
    if request.method== 'POST':   
        material=Notes.objects.get(id=material_id)
        material.delete()
        return redirect('module',module_name=module_name,class_id=class_id,subject_id=subject_id)
