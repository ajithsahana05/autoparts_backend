# Generated by Django 4.0.2 on 2022-04-18 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_customerinfo_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiryinfo',
            name='status',
            field=models.CharField(default='pending', max_length=30),
        ),
    ]
