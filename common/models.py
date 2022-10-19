from django.db import models




# Create your models here.
class auditModel(models.Model):
    created_date= models.DateTimeField(auto_now=True)
    creator=models.ForeignKey("member.User",null=True,on_delete=models.CASCADE)
    class Meta:
        abstract=True