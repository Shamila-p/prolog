# Generated by Django 4.1.2 on 2022-11-17 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0014_editsubject_subjectcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='class_belongs',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='course.class'),
        ),
    ]
