# Generated by Django 4.1.2 on 2022-12-12 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fees', '0006_alter_feepaid_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fee',
            name='fees',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='feepaid',
            name='fees',
            field=models.IntegerField(default=None),
        ),
    ]