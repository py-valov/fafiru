# Generated by Django 3.2.18 on 2023-04-12 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_appealcomments_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appeal',
            name='category',
            field=models.CharField(choices=[('Склад', 'Склад'), ('Счета', 'Счета'), ('Расчет товара', 'Расчет товара'), ('Доставка', 'Доставка')], max_length=50),
        ),
    ]