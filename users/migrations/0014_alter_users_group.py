# Generated by Django 3.2.18 on 2023-05-09 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_alter_users_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='group',
            field=models.CharField(blank=True, choices=[('Склад+Логистика', 'Склад+Логистика'), ('Склад', 'Склад'), ('Обычный', 'Обычный'), ('Логистика', 'Логистика'), ('Финансы', 'Финансы')], default='Обычный', max_length=100, null=True),
        ),
    ]
