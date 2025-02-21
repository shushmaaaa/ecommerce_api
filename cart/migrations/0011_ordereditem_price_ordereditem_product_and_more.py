# Generated by Django 5.0.6 on 2024-05-26 10:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0010_remove_cartitem_price'),
        ('products', '0008_alter_product_variant_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordereditem',
            name='price',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='ordereditem',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
        migrations.AddField(
            model_name='ordereditem',
            name='quantity',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]
