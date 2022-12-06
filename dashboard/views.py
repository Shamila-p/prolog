from django.shortcuts import render
from member.models import  User
from course.models import Department

# Create your views here.
def dashboard(request):
    if request.method == 'GET':
        students_count=User.objects.filter(role=User.STUDENT).count()
        teachers_count=User.objects.filter(role=User.TEACHER).count()
        deaprtments_count=Department.objects.count()
        departments=Department.objects.all()
        student_count_list=[]
        staff_count_list=[]
        for department in departments:
            student=User.objects.filter(role=User.STUDENT,department_id=department.id)
            student_count_list.append(student.count())
        for department in departments:
            teacher=User.objects.filter(role=User.TEACHER,department_id=department.id)
            staff_count_list.append(teacher.count())
        
        context={'students_count':students_count,'teachers_count':teachers_count,'departments_count':deaprtments_count,'departments':departments,'student_count_list':student_count_list,'staff_count_list':staff_count_list}
        return render(request,'dashboard.html',context)