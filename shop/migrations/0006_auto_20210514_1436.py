# Generated by Django 3.2 on 2021-05-14 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_rename_orders_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(default='', max_length=111),
        ),
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.CharField(default='', max_length=111),
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.CharField(default='', max_length=111),
        ),
        migrations.AlterField(
            model_name='order',
            name='items_json',
            field=models.CharField(default='', max_length=5000),
        ),
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.CharField(default='', max_length=90),
        ),
        migrations.AlterField(
            model_name='order',
            name='state',
            field=models.CharField(default='', max_length=111),
        ),
    ]