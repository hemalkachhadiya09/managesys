# Generated by Django 3.2.5 on 2021-07-13 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manageapp', '0003_auto_20210713_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complain',
            name='ctitle',
            field=models.CharField(max_length=30),
        ),
    ]
