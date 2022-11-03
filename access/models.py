from django.db import models
from common.models import auditModel
from member.models import User
# Create your models here.
class ForgotPassword(auditModel):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    uuid=models.CharField(max_length=50)