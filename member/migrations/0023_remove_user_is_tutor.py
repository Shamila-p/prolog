# Generated by Django 4.1.2 on 2022-11-03 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0022_user_is_tutor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_tutor',
        ),
    ]
