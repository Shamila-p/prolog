# Generated by Django 4.1.2 on 2022-11-28 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0026_remove_user_quota_student_quota'),
        ('fees', '0004_remove_feepaid_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='feepaid',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='member.student'),
        ),
    ]
