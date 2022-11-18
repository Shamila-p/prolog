from django.shortcuts import render,redirect

from StudyMaterials.models import Notes




def study_materials(request):
    if request.method == 'GET':
        return render(request, 'study_materials.html')


def module(request, module_name):
    if request.method == 'GET':
        materials=Notes.objects.all()
        context = {'module_name': module_name,'materials':materials,'categories':Notes.MATERIAL_CHOICES}
        return render(request, 'module.html', context)

def add_materials(request,module_name):
    if request.method == 'GET':
        context={'materials':Notes.MATERIAL_CHOICES,'module_name': module_name}
        return render(request, 'add_materials.html',context)
    if request.method== 'POST':
        filename=request.POST.get('filename')
        category=request.POST.get('category')
        uploaded= request.FILES.get('upload')
        Notes.objects.create(filename=filename,module=module_name,category=category,filepath=uploaded)
        return redirect('module',module_name=module_name)

def edit_materials(request,material_id):
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
        return redirect('module',module_name=material.module)


def remove_materials(request,material_id):
    if request.method== 'POST':   
        material=Notes.objects.get(id=material_id)
        material.delete()
        return redirect('module',module_name=material.module)

