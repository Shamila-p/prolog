# Generated by Django 4.1.2 on 2022-11-25 04:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0017_alter_subject_tutor'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='semester',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='course.semester'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='tutor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
