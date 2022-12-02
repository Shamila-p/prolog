# Generated by Django 4.1.2 on 2022-11-26 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificates', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='level',
            field=models.CharField(choices=[('NA', 'NATIONAL'), ('SE', 'STATE'), ('CO', 'COLLEGE')], default=0, max_length=2),
        ),
    ]
