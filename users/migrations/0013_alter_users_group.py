# Generated by Django 3.2.18 on 2023-05-09 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_alter_users_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='group',
            field=models.CharField(blank=True, choices=[('Склад', 'Склад'), ('Логистика', 'Логистика'), ('Финансы', 'Финансы'), ('Обычный', 'Обычный'), ('Склад+Логистика', 'Склад+Логистика')], default='Обычный', max_length=100, null=True),
        ),
    ]
