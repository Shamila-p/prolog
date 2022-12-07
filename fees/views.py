from django.shortcuts import render,redirect
from course.models import Department, Semester
from fees.models import Fee, FeePaid
from member.models import Student, User
from django.http import JsonResponse,HttpResponse
from django.contrib import messages
import zerosms
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.http import FileResponse
# Create your views here.
def display_fee(request):
    if request.method == 'GET':
        if request.user.role == User.PRINCIPAL:
            fees=Fee.objects.all()
            context={'fees':fees}
        if request.user.role==User.TEACHER or request.user.position==User.HOD:
            hod=User.objects.get(id=request.user.id)
            print(hod)
            fees=Fee.objects.filter(department_id=hod.department_id)
            print(fees)
            context={'fees':fees}
        return render(request,'display_fee.html',context)
def add_fee(request):
    if request.method == 'GET':
        departments=Department.objects.all()
        semesters=Semester.objects.all()
        context={'departments':departments,'fee_categories':Fee.FEE_CHOICES,'semesters':semesters}
        return render(request,'add_fee.html',context)
    if request.method == 'POST':
        department=request.POST.get('department')
        print(department)
        fee_category=request.POST.get('fcategory')
        print(fee_category)
        amount=request.POST.get('amount')
        fee=int(amount)
        print(fee)
        payment_date=request.POST.get('pdate')
        print(payment_date)
        semester=request.POST.get('semester')
        if not Fee.objects.filter(department_id=department,fee_category=fee_category,semester_id=semester).exists():
            Fee.objects.create(fees=fee,department_id=department,last_date=payment_date,fee_category=fee_category,semester_id=semester)
        else:
            messages.error(request,"Fee alreday added. If you are looking for editing data please go with edit option")
        return redirect('display_fee')
            



def edit_fee(request,fee_id):
    if request.method=='GET':
        fee=Fee.objects.get(id=fee_id)
        semesters=Semester.objects.all()
        departments=Department.objects.all()
        context={'fee':fee,'departments':departments,'fee_categories':Fee.FEE_CHOICES,'semesters':semesters}
        return render(request,'edit_fee.html',context)
    if request.method == 'POST':
        fee=Fee.objects.get(id=fee_id)
        department=request.POST.get('department')
        print(department)
        fee_category=request.POST.get('fcategory')
        print(fee_category)
        amount=request.POST.get('amount')
        print(amount)
        payment_date=request.POST.get('pdate')
        semester=request.POST.get('semester')

        print(payment_date)
        fee.fees=amount
        fee.department_id=department
        fee.semester_id=semester
        if payment_date is not None:
            fee.last_date=payment_date
        fee.fee_category=fee_category
        fee.save()
        return redirect('display_fee')

def remove_fee(request,fee_id):
    fee=Fee.objects.get(id=fee_id)
    fee.delete()
    return redirect('display_fee')

def student_fee(request):
    if request.method == 'GET':
        student=Student.objects.get(user_id=request.user.id)
        current_semester=student.semester
        print(current_semester)
        fee_list=[]
        fees=Fee.objects.filter(department_id=student.user.department_id,fee_category=student.quota)
        for fee in fees:
            if fee.semester.order<=current_semester.order:
                fee_list.append(fee)
        payed_fee_list=[]
        payed_fees=FeePaid.objects.filter(department_id=student.user.department_id,student_id=request.user.id)
        print(payed_fees)
        for paid_fee in payed_fees:
            payed_fee_list.append(paid_fee.semester.semname)
           
        context={'fees':fees,'payed_fee_semester_list':payed_fee_list,'fee_list':fee_list,'payed_fees':payed_fees}
        return render(request,'student_fee.html',context)


def payment(request,payment_id):
    if request.method == 'GET':
        fee=Fee.objects.get(id=payment_id)
        context={'fee':fee}
        return render(request,'payment.html',context)
    if request.method == 'POST':
        print('hgfg')
        print(request.POST)
        fee=request.POST['fee']
        print(fee)
        fees=int(float(fee))
        print(fees)
        print(type(fees))

        semester_id=request.POST['semester_id']
        print(semester_id)
        department_id=request.POST['department_id']
        print(department_id)

        fee_category=request.POST['fee_category']
        print(fee_category)

        date=request.POST['date']
        print(date)

        FeePaid.objects.create(student_id=request.user.id,semester_id=semester_id,department_id=department_id,payed_date=date,fee_category=fee_category,fees=fees)
        # fee_details=json.loads(fees)
        # print(fee_details)
        return JsonResponse({'status': 'success'})


def sms(request):
    if request.method == 'GET':
        return render(request,'sms.html')
    if request.method == 'POST':
        msg=request.POST['msg']
        phone=request.POST['phone']
        zerosms.sms(phno=request.user.username,passwd=request.user.password,receivernum=phone,message=msg)
        return HttpResponse("send")

def invoice_generate(request,id):
        paid=FeePaid.objects.get(id=id)
        user=request.user
        template_path='invoice.html'
        
        context = {'paid': paid,'user': user}

        response = HttpResponse(content_type='application/pdf')

        response['Content-Disposition'] = 'filename="invoice.pdf"'

        template = get_template(template_path)

        html = template.render(context)

        # create a pdf
        pisa_status = pisa.CreatePDF(
        html, dest=response)
        # if error then show some funy view
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response
    