# Generated by Django 3.1.6 on 2021-02-19 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_api', '0003_schools_sc_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='st_age',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='st_class',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
