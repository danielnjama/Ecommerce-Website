# Generated by Django 3.1.1 on 2020-12-21 15:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 21, 18, 48, 0, 37316)),
        ),
        migrations.AlterField(
            model_name='cviews',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 21, 18, 48, 0, 39313)),
        ),
    ]
