# Generated by Django 3.2.18 on 2023-03-25 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0002_alter_appeal_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('namePaking', models.CharField(max_length=100)),
                ('weight', models.FloatField()),
                ('volume', models.FloatField()),
                ('price', models.FloatField()),
                ('nameProduct', models.CharField(max_length=255)),
                ('transport', models.CharField(choices=[('Сборная', 'Сборная'), ('Авиа', 'Авиа'), ('Машина', 'Машина'), ('ЖД', 'ЖД'), ('Море', 'Море')], default='Сборная', max_length=255)),
                ('category', models.CharField(choices=[('Одежда', 'Одежда'), ('Оборудование', 'Оборудование'), ('Инструменты', 'Инструменты'), ('Станки', 'Станки')], default='Одежда', max_length=255)),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.clients')),
            ],
        ),
        migrations.CreateModel(
            name='ProductFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to='productFiles/%Y/%m/%d')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.products')),
            ],
        ),
    ]
