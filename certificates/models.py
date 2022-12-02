from django.db import models
from common.models import auditModel
from asyncio.windows_events import NULL



# Create your models here.
class Certificate(auditModel):
    NATIONAL_EVENT="NA"
    STATE_EVENT="SE"
    COLLEGE_EVENT="CO"
    MOOC_COURSE="MC"

    CERTIFICATE_CHOICES=[
        (NATIONAL_EVENT, "NATIONAL EVENT E"),
        (STATE_EVENT, "STATE EVENT"),
        (COLLEGE_EVENT, "COLLEGE EVENT"),
        (MOOC_COURSE, "MOOC COURSE"),
    ]


    activity_name=models.CharField(max_length=500)
    created_date=models.DateTimeField(auto_now=True)
    level=models.CharField(
        max_length=2, choices=CERTIFICATE_CHOICES, null=False,default=NULL)
    certificate_file=models.FileField(upload_to='files/', null=True)
    student=models.ForeignKey("member.User", null=True, on_delete=models.CASCADE)

    @property
    def level_value(self):
        current_level = self.level
        for level in Certificate.CERTIFICATE_CHOICES:
            if level[0] == current_level:
                value = level[1]
        return value