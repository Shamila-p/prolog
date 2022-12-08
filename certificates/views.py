from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from certificates.models import Certificate
from course.models import Class
from member.models import Student

# Create your views here.

@login_required
def list_certificates(request):
    if request.method == 'GET':
        certificates = Certificate.objects.filter(student_id=request.user.id)
        context = {'certificates': certificates,'title': 'List Certificates'}
        return render(request, 'list_certificates.html', context)

@login_required
def add_certificate(request):
    if request.method == 'GET':
        context = {'levels': Certificate.CERTIFICATE_CHOICES,'title': 'Add Certificate'}
        return render(request, 'add_certificate.html', context)
    if request.method == 'POST':
        activity = request.POST.get("activity")
        level = request.POST.get("level")
        upload = request.FILES.get("upload")
        student = request.user.id
        print(student)
        Certificate.objects.create(
            activity_name=activity, level=level, certificate_file=upload, student_id=student)
        return redirect('list_certificates')

@login_required
def edit_certificate(request, certificate_id):
    if request.method == 'GET':
        certificate = Certificate.objects.get(id=certificate_id)
        context = {'levels': Certificate.CERTIFICATE_CHOICES,
                   'certificate': certificate,'title': 'Edit Certificate'}
        return render(request, 'edit_certificate.html', context)
    if request.method == 'POST':
        activity = request.POST.get("activity")
        level = request.POST.get("level")
        upload = request.FILES.get("upload")
        certificate = Certificate.objects.get(id=certificate_id)
        certificate.activity_name = activity
        certificate.level = level
        if upload is not None:
            certificate.upload = upload
        certificate.save()
        return redirect('list_certificates')

@login_required
def remove_certificate(request, certificate_id):
    if request.method == 'POST':
        certificate = Certificate.objects.get(id=certificate_id)
        certificate.delete()
        return redirect('list_certificates')

@login_required
def view_certificates(request):
    if request.method == 'GET':
        batch = Class.objects.get(tutor_id=request.user.id)
        students = Student.objects.filter(batch_id=batch.id)
        print(students)
        list_students = []
        # list_certificates = []
        for student in students:
            list_students.append(student.user_id)
            # print(list_students)
            # for student in list_students:
        certificates = Certificate.objects.filter(student_id__in=list_students)
        # list_certificates.append(certificates)
        context = {'certificates': certificates,'title': 'view Certificates'}
        print(context)
        return render(request, 'list_certificates.html', context)
