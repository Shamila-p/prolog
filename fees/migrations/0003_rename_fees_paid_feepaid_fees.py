# Generated by Django 4.1.2 on 2022-11-28 06:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fees', '0002_feepaid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feepaid',
            old_name='fees_paid',
            new_name='fees',
        ),
    ]
