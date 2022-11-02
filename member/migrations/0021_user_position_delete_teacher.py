# Generated by Django 4.1.2 on 2022-11-02 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0020_alter_editprofile_email_alter_editprofile_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='position',
            field=models.CharField(choices=[('HD', 'Hod'), ('AST', 'Assistant professor'), ('ASO', 'Associate professor')], default=0, max_length=3),
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
    ]
