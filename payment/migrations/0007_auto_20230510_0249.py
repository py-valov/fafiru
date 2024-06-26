# Generated by Django 3.2.18 on 2023-05-09 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0006_auto_20230509_1753'),
    ]

    operations = [
        migrations.AddField(
            model_name='operation',
            name='productPriceInUSDCurrency',
            field=models.CharField(choices=[('$', '$'), ('¥', '¥'), ('€', '€')], default='$', max_length=10),
        ),
        migrations.AddField(
            model_name='operation',
            name='productPriceToPakingCurrency',
            field=models.CharField(choices=[('$', '$'), ('¥', '¥'), ('€', '€')], default='$', max_length=10),
        ),
    ]
