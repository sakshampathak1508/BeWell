# Generated by Django 3.2.4 on 2021-06-16 12:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 6, 16, 17, 45, 14, 148236)),
        ),
    ]