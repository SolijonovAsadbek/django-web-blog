# Generated by Django 4.0.1 on 2022-01-27 07:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='time',
            field=models.DateField(verbose_name=datetime.datetime(2022, 1, 27, 12, 46, 19, 155735)),
        ),
    ]
