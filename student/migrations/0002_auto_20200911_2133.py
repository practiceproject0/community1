# Generated by Django 3.1.1 on 2020-09-11 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentregistration',
            name='roll_no',
            field=models.IntegerField(auto_created=True),
        ),
    ]
