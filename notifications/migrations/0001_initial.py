# Generated by Django 4.1.2 on 2022-11-25 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0019_editsubject_semester'),
        ('member', '0024_student_semester'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=500)),
                ('send_to', models.CharField(max_length=10)),
                ('batch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='course.class')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='course.department')),
                ('semester', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='course.semester')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='member.student')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
