# Generated by Django 4.1.2 on 2022-11-18 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0002_assignment_rank'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assignment',
            old_name='rank',
            new_name='type',
        ),
    ]
