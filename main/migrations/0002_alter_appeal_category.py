# Generated by Django 3.2.18 on 2023-03-09 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appeal',
            name='category',
            field=models.CharField(choices=[('Важное', 'Важное'), ('Информирование', 'Информирование'), ('Оповещение', 'Оповещение'), ('Товар', 'Товар'), ('Доставка', 'Доставка')], max_length=50),
        ),
    ]
