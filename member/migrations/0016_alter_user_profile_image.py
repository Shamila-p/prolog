# Generated by Django 4.1.2 on 2022-10-21 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0015_alter_user_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(default='default-avatar.jpg', null=True, upload_to='profile_image'),
        ),
    ]
