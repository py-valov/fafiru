# Generated by Django 3.2.18 on 2023-03-13 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0002_alter_appeal_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Check',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('price', models.FloatField()),
                ('currency', models.CharField(choices=[('Долл', 'Долл'), ('Юани', 'Юани'), ('Нал.юа', 'Нал.юа'), ('Евро', 'Евро'), ('Фапьяо юа', 'Фапьяо юа')], max_length=50)),
                ('well', models.FloatField()),
                ('wellCheck', models.CharField(choices=[('$', '$'), ('¥', '¥'), ('€', '€'), ('₽', '₽')], max_length=5)),
                ('wellCommissionUSD', models.FloatField(blank=True, null=True)),
                ('commissionPercent', models.FloatField(blank=True, null=True)),
                ('commissionUSD', models.IntegerField(blank=True, null=True)),
                ('commissionRUB', models.IntegerField(blank=True, null=True)),
                ('product', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=False)),
                ('ContractNumber', models.CharField(blank=True, max_length=150, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.clients')),
            ],
        ),
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('admissionRUB', models.FloatField(blank=True, null=True)),
                ('admissionCurrency', models.FloatField(blank=True, null=True)),
                ('typeCurrency', models.CharField(blank=True, choices=[('$', '$'), ('¥', '¥'), ('€', '€')], max_length=5, null=True)),
                ('nursingRUB', models.FloatField(blank=True, null=True)),
                ('nursingCurrency', models.FloatField(blank=True, null=True)),
                ('well', models.FloatField(blank=True, null=True)),
                ('wellCommission', models.FloatField(blank=True, null=True)),
                ('priceInUSD', models.FloatField(blank=True, null=True)),
                ('ReturnPriceUSD', models.FloatField(blank=True, null=True)),
                ('typeLetter', models.CharField(blank=True, choices=[('Возврат платежа', 'Возврат платежа'), ('Корректировка платежа', 'Корректировка платежа')], max_length=100, null=True)),
                ('fileOperation', models.FileField(blank=True, null=True, upload_to='Operation Files/%Y/%m/%d')),
                ('check_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='payment.check')),
            ],
        ),
        migrations.CreateModel(
            name='CheckFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PathFile', models.FileField(blank=True, null=True, upload_to='files/%Y/%m/%d')),
                ('createFile', models.DateField(auto_now_add=True, null=True)),
                ('check_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='payment.check')),
            ],
        ),
    ]
