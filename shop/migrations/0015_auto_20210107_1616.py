# Generated by Django 3.1.1 on 2021-01-07 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_shop_views'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shop',
            old_name='views',
            new_name='shopviews',
        ),
    ]
