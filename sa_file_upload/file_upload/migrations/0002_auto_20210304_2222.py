# Generated by Django 3.1.7 on 2021-03-04 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_upload', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='rollNumber',
            field=models.IntegerField(default=0),
        ),
    ]