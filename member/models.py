from asyncio.windows_events import NULL
from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
from common.models import auditModel
from course.models import Class, Department, Semester
# from fees.models import Fee


class User(AbstractUser, auditModel):
    STUDENT = "ST"
    TEACHER = "TR"
    PRINCIPAL = "PR"

    ROLES_CHOICES = [
        (STUDENT, "Student"),
        (TEACHER, "Teacher"),
        (PRINCIPAL, "Principal"),
    ]

    




    HOD = "HD"
    ASSISTANT_PROFESSOR = "AST"
    ASSOCIATE_PROFESSOR = "ASO"

    POSITION_CHOICES = [
        (HOD, "Hod"),
        (ASSISTANT_PROFESSOR, "Assistant professor"),
        (ASSOCIATE_PROFESSOR, "Associate professor"),
    ]

    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=60)
    profile_image = models.ImageField(upload_to='profile_image',default='profile_image/default-avatar.jpg',null=True)
    role = models.CharField(
        max_length=2, choices=ROLES_CHOICES, null=False)
    department = models.ForeignKey(Department, null=True, on_delete=models.CASCADE)
    position = models.CharField(
        max_length=3, choices=POSITION_CHOICES, null=False,default=NULL)
    
    
    @property
    def profile_image_url(self):
        try:
            url = self.profile_image.url
        except ValueError:
            url = ""
        return url

    @property
    def position_value(self):
        current_position = self.position
        for position in User.POSITION_CHOICES:
            if position[0] == current_position:
                value = position[1]
        return value

   
  

class Student(auditModel):


    MANAGEMENT="MA"
    NRI="NR"
    GOVRNMENT="GO"

    QUOTA_CHOICES = [
        (MANAGEMENT, "MANAGEMENT"),
        (NRI, "NRI"),
        (GOVRNMENT, "GOVRNMENT"),
    ]

    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    batch = models.ForeignKey(Class, null=True, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, null=True, on_delete=models.CASCADE)
    admsn_no=models.CharField(max_length=6,null=True)
    parent_name = models.CharField(max_length=30)
    parent_mobile = models.CharField(max_length=15)
    quota=models.CharField(max_length=2,choices=QUOTA_CHOICES,null=False,default=NULL)
   
    @property
    def quota_value(self):
        fee_quota_value= self.quota
        for fee_quota in Student.QUOTA_CHOICES:
            if fee_quota[0] == fee_quota_value:
                return fee_quota[1]

class EditProfile(auditModel):
    user = models.ForeignKey(User,null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=15,null=True)
    phone = models.CharField(max_length=15,null=True)
    email = models.CharField(max_length=30,null=True)
    parent_name = models.CharField(max_length=30,null=True)
    parent_mobile = models.CharField(max_length=15,null=True)
    profile_image = models.ImageField(upload_to='profile_image',default='profile_image/default-avatar.jpg',null=True)
    
    @property
    def profile_image_url(self):
        try:
            url = self.profile_image.url
        except ValueError:
            url = ""
        return url


class TimeTable(auditModel):
    time_table=models.FileField(upload_to='files/', null=True)
    batch = models.ForeignKey(Class, null=True, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, null=True, on_delete=models.CASCADE)