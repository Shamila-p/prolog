# Generated by Django 4.1.2 on 2022-12-12 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0027_timetable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='quota',
            field=models.CharField(choices=[('MA', 'MANAGEMENT'), ('NR', 'NRI'), ('GO', 'GOVRNMENT')], default=None, max_length=2),
        ),
        migrations.AlterField(
            model_name='user',
            name='position',
            field=models.CharField(choices=[('HD', 'Hod'), ('AST', 'Assistant professor'), ('ASO', 'Associate professor')], max_length=3),
        ),
    ]