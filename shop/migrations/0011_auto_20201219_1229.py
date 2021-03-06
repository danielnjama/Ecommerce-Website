# Generated by Django 3.1.1 on 2020-12-19 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_auto_20201203_1903'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop',
            name='shortdescription',
        ),
        migrations.AlterField(
            model_name='shop',
            name='category',
            field=models.CharField(choices=[('laptops', 'laptops'), ('desktops', 'desktops'), ('accessories', 'accessories'), ('others', 'others')], max_length=120),
        ),
        migrations.AlterField(
            model_name='shop',
            name='image1',
            field=models.ImageField(help_text='width >=255px,heigth >=291px', upload_to='image51862926581'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='image2',
            field=models.ImageField(blank=True, help_text='width >=255px,heigth >=291px: this field can be blank', null=True, upload_to='image51862926581'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='pricebefore',
            field=models.IntegerField(default=0),
        ),
    ]
