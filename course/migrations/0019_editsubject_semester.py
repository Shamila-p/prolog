# Generated by Django 4.1.2 on 2022-11-25 04:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0018_subject_semester_alter_subject_tutor'),
    ]

    operations = [
        migrations.AddField(
            model_name='editsubject',
            name='semester',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='course.semester'),
        ),
    ]
