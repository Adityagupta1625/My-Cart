# Generated by Django 3.2 on 2021-06-12 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='https://ecomms3.s3.amazonaws.com/static/shop/images/'),
        ),
    ]
