# Generated by Django 4.1.2 on 2022-11-25 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0019_editsubject_semester'),
        ('mark', '0002_mark_class_belongs'),
    ]

    operations = [
        migrations.AddField(
            model_name='mark',
            name='semester',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='course.semester'),
        ),
    ]
