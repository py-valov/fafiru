# Generated by Django 3.2.18 on 2023-04-12 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_users_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='group',
            field=models.CharField(blank=True, choices=[('Обычный', 'Обычный'), ('Логистика', 'Логистика'), ('Финансы', 'Финансы'), ('Склад+Логистика', 'Склад+Логистика'), ('Склад', 'Склад')], default='Обычный', max_length=100, null=True),
        ),
    ]
