# Generated by Django 4.1.2 on 2022-10-25 04:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0017_alter_user_profile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='EditProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=30)),
                ('parent_name', models.CharField(max_length=30)),
                ('parent_mobile', models.CharField(max_length=15)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]