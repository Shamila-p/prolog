# Generated by Django 4.1.2 on 2022-10-20 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0009_alter_teacher_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='position',
            field=models.CharField(choices=[('HD', 'Hod'), ('AST', 'Assistant professor'), ('ASO', 'Associate professor')], max_length=30),
        ),
    ]