from django.db import models
from common.models import auditModel
from course.models import Department, Semester
from member.models import Student, User

# Create your models here.
class Fee(auditModel):
    MANAGEMENT="MA"
    NRI="NR"
    GOVRNMENT="GO"

    FEE_CHOICES = [
        (MANAGEMENT, "MANAGEMENT"),
        (NRI, "NRI"),
        (GOVRNMENT, "GOVRNMENT"),
    ]


    department=models.ForeignKey(Department, null=True, on_delete=models.CASCADE)
    fee_category=models.CharField(max_length=12,choices=FEE_CHOICES,null=False)
    fees=models.IntegerField(null=False,default=None)
    created_date=models.DateTimeField(auto_now=True)
    last_date=models.DateField()
    semester=models.ForeignKey(Semester, null=True, on_delete=models.CASCADE)



    @property
    def fee_value(self):
        fee_category_value= self.fee_category
        for fee_category in Fee.FEE_CHOICES:
            if fee_category[0] == fee_category_value:
                value = fee_category[1]
        return value


class FeePaid(auditModel):
    department=models.ForeignKey(Department, null=True, on_delete=models.CASCADE)
    fee_category=models.CharField(max_length=12,null=False)
    fees=models.IntegerField(null=False,default=None)
    payed_date=models.DateTimeField(auto_now=True)
    semester=models.ForeignKey(Semester, null=True, on_delete=models.CASCADE)
    student=models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    