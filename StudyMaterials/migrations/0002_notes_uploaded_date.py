# Generated by Django 4.1.2 on 2022-11-17 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudyMaterials', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='uploaded_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]