# Generated by Django 4.1.2 on 2022-10-20 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_class'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='semester',
            name='department',
        ),
    ]
