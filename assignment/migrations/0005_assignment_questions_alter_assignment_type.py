# Generated by Django 4.1.2 on 2022-11-18 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0004_alter_assignment_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='questions',
            field=models.FileField(null=True, upload_to='files/'),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='type',
            field=models.CharField(choices=[('F', 'FIRST ASSIGNMENT'), ('S', 'SECOND ASSIGNMENT')], default=0, max_length=2),
        ),
    ]
