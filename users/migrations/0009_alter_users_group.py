# Generated by Django 3.2.18 on 2023-04-12 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_users_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='group',
            field=models.CharField(blank=True, choices=[('Логистика', 'Логистика'), ('Склад+Логистика', 'Склад+Логистика'), ('Финансы', 'Финансы'), ('Склад', 'Склад'), ('Обычный', 'Обычный')], default='Обычный', max_length=100, null=True),
        ),
    ]
