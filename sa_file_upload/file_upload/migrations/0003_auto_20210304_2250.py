# Generated by Django 3.1.7 on 2021-03-04 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_upload', '0002_auto_20210304_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='rollNumber',
            field=models.IntegerField(default=0, unique=True),
        ),
    ]
