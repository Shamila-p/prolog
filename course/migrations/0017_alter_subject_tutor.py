# Generated by Django 4.1.2 on 2022-11-25 04:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0016_editsubject_class_belongs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='tutor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='course.semester'),
        ),
    ]
