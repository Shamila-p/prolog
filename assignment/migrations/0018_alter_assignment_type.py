# Generated by Django 4.1.2 on 2022-12-12 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0017_alter_assignmentmark_assignment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='type',
            field=models.CharField(choices=[('F', 'FIRST ASSIGNMENT'), ('S', 'SECOND ASSIGNMENT')], default=None, max_length=2),
        ),
    ]