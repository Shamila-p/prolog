# Generated by Django 4.1.2 on 2022-12-01 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0011_submittedassignment_class_belongs_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='submittedassignment',
            name='submitted_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
