# Generated by Django 3.2.18 on 2023-04-12 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_users_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='group',
            field=models.CharField(blank=True, choices=[('Финансы', 'Финансы'), ('Склад', 'Склад'), ('Склад+Логистика', 'Склад+Логистика'), ('Обычный', 'Обычный'), ('Логистика', 'Логистика')], default='Обычный', max_length=100, null=True),
        ),
    ]
