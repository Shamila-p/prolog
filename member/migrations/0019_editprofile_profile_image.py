# Generated by Django 4.1.2 on 2022-10-25 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0018_editprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='editprofile',
            name='profile_image',
            field=models.ImageField(default='profile_image/default-avatar.jpg', null=True, upload_to='profile_image'),
        ),
    ]
