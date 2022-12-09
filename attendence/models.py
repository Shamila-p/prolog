import os
from django.db import models
from common.models import auditModel
from member.models import Student,User
from course.models import Subject,Class,Semester
from twilio.rest import Client
# Create your models here.

class Attendence(auditModel):
    date=models.DateField()
    subject=models.ForeignKey(Subject, null=True, on_delete=models.CASCADE)
    student=models.ForeignKey(Student, null=True, on_delete=models.CASCADE)
    teacher=models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    semester=models.ForeignKey(Semester, null=True, on_delete=models.CASCADE)
    class_belongs=models.ForeignKey(Class, null=True, on_delete=models.CASCADE)
    is_present=models.BooleanField(default=False)

    # def save(self,*args,**kwargs):
    #     print('ytr')
    #     if self.is_present is False:

    #         account_sid = 'AC58bbdc3cc418d9b6ff26b59f21453d82'
    #         auth_token = '42ec5dc088caed6bc5b74773c054a1bf'
    #         client = Client(account_sid, auth_token)

    #         message = client.messages.create(
    #                                     body=f'student is absent',
    #                                     from_='+18055904816',
    #                                     to='+918590426660'
    #                                 )

    #         print(message.sid)
    #         return super().save(*args,**kwargs)