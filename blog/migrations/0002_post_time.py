# Generated by Django 4.0.1 on 2022-01-27 07:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='time',
            field=models.DateField(default=datetime.datetime(2022, 1, 27, 7, 46, 7, 2375, tzinfo=utc), verbose_name=datetime.datetime(2022, 1, 27, 12, 44, 30, 697403)),
            preserve_default=False,
        ),
    ]
