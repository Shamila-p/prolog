# Generated by Django 4.1.2 on 2022-11-25 03:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0016_editsubject_class_belongs'),
        ('member', '0023_remove_user_is_tutor'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='semester',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='course.semester'),
        ),
    ]
