# Generated by Django 3.1.2 on 2020-10-31 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20201031_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maincontact',
            name='service1',
            field=models.TextField(null=True),
        ),
    ]