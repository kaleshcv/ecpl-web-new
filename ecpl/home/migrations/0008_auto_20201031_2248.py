# Generated by Django 3.1.2 on 2020-10-31 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20201031_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quickcontact',
            name='country',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
