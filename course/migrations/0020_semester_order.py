# Generated by Django 4.1.2 on 2022-11-26 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0019_editsubject_semester'),
    ]

    operations = [
        migrations.AddField(
            model_name='semester',
            name='order',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
