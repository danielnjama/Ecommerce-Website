# Generated by Django 3.1.1 on 2021-01-06 14:13

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_auto_20201221_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='tags',
            field=models.CharField(choices=[('technology', 'technology'), ('social', 'social'), ('political', 'political')], max_length=120),
        ),
        migrations.AlterField(
            model_name='comments',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 6, 17, 13, 52, 605109)),
        ),
        migrations.AlterField(
            model_name='cviews',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 6, 17, 13, 52, 606109)),
        ),
    ]