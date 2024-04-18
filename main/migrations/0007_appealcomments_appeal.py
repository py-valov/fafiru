# Generated by Django 3.2.18 on 2023-04-12 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_appealcomments'),
    ]

    operations = [
        migrations.AddField(
            model_name='appealcomments',
            name='appeal',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='main.appeal'),
            preserve_default=False,
        ),
    ]