# import json
from django.shortcuts import render,redirect
from course.models import Department, Semester
from fees.models import Fee
# from course.models import Department, Semester

from member.models import Student, User
# from django.http import JsonResponse

# # Create your views here.
# def display_fee(request):
#     if request.method == 'GET':
#         if request.user.role == User.PRINCIPAL:
#             fees=Fee.objects.all()
#             context={'fees':fees}
#         if request.user.role==User.TEACHER or request.user.position==User.HOD:
#             hod=User.objects.get(id=request.user.id)
#             print(hod)
#             fees=Fee.objects.filter(department_id=hod.department_id)
#             print(fees)
#             context={'fees':fees}
#             return render(request,'display_fee.html',context)
# def add_fee(request):
#     if request.method == 'GET':
#         departments=Department.objects.all()
#         semesters=Semester.objects.all()
#         context={'departments':departments,'fee_categories':Fee.FEE_CHOICES,'semesters':semesters}
#         return render(request,'add_fee.html',context)
#     if request.method == 'POST':
#         department=request.POST.get('department')
#         print(department)
#         fee_category=request.POST.get('fcategory')
#         print(fee_category)
#         amount=request.POST.get('amount')
#         fee=int(amount)
#         print(fee)
#         payment_date=request.POST.get('pdate')
#         print(payment_date)
#         semester=request.POST.get('semester')
#         Fee.objects.create(fees=fee,department_id=department,last_date=payment_date,fee_category=fee_category,semester_id=semester)
#         return redirect('display_fee')

# def edit_fee(request,fee_id):
#     if request.method=='GET':
#         fee=Fee.objects.get(id=fee_id)
#         semesters=Semester.objects.all()
#         departments=Department.objects.all()
#         context={'fee':fee,'departments':departments,'fee_categories':Fee.FEE_CHOICES,'semesters':semesters}
#         return render(request,'edit_fee.html',context)
#     if request.method == 'POST':
#         fee=Fee.objects.get(id=fee_id)
#         department=request.POST.get('department')
#         print(department)
#         fee_category=request.POST.get('fcategory')
#         print(fee_category)
#         amount=request.POST.get('amount')
#         print(amount)
#         payment_date=request.POST.get('pdate')
#         semester=request.POST.get('semester')

#         print(payment_date)
#         fee.fees=amount
#         fee.department_id=department
#         fee.semester_id=semester
#         if payment_date is not None:
#             fee.last_date=payment_date
#         fee.fee_category=fee_category
#         fee.save()
#         return redirect('display_fee')

# def remove_fee(request,fee_id):
#     fee=Fee.objects.get(id=fee_id)
#     fee.delete()
#     return redirect('display_fee')

# def student_fee(request):
#     if request.method == 'GET':
#         student=Student.objects.get(user_id=request.user.id)
#         current_semester=student.semester
#         print(current_semester)
#         fee_list=[]
#         fees=Fee.objects.filter(department_id=student.user.department_id,fee_category=student.quota)
#         print(fees)
#         for fee in fees:
#             print(fee.fees)
#             print(type(fee.fees))
#             print(fee.semester.order)
#             print(current_semester.order)
#             if fee.semester.order<=current_semester.order:
#                 print(fee.semester.order)
#                 fee_list.append(fee)
#         print(fee_list)
#         payed_fee_list=[]
#         payed_fees=FeePaid.objects.filter(semester_id=current_semester,department_id=student.user.department_id,student_id=request.user.id)
#         print(payed_fees)
#         for paid_fee in payed_fees:
#             payed_fee_list.append(paid_fee.semester.semname)

#         context={'fees':fees,'payed_fee_semester_list':payed_fee_list,'fee_list':fee_list}
#         return render(request,'student_fee.html',context)


# def payment(request,payment_id):
#     if request.method == 'GET':
#         fee=Fee.objects.get(id=payment_id)
#         context={'fee':fee}
#         return render(request,'payment.html',context)
#     if request.method == 'POST':
#         print('hgfg')
#         print(request.POST)
#         fee=request.POST['fee']
#         print(fee)
#         fees=int(float(fee))
#         print(fees)
#         print(type(fees))

#         semester_id=request.POST['semester_id']
#         print(semester_id)
#         department_id=request.POST['department_id']
#         print(department_id)

#         fee_category=request.POST['fee_category']
#         print(fee_category)

#         date=request.POST['date']
#         print(date)

#         FeePaid.objects.create(student_id=request.user.id,semester_id=semester_id,department_id=department_id,payed_date=date,fee_category=fee_category,fees_paid=fee)
#         # fee_details=json.loads(fees)
#         # print(fee_details)
#         return JsonResponse({'status': 'success'})