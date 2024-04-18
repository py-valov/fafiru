# Generated by Django 3.2.18 on 2023-03-25 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_products_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='productfiles',
            name='date_create',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
    ]