# Generated by Django 2.2.3 on 2019-08-16 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_product_express'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='videofile',
            field=models.FileField(null=True, upload_to='videos/', verbose_name=''),
        ),
    ]
