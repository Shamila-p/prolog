# Generated by Django 4.1.2 on 2022-11-17 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudyMaterials', '0002_notes_uploaded_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='category',
            field=models.CharField(choices=[('NO', 'Note'), ('VI', 'Video')], max_length=2, null=True),
        ),
    ]
