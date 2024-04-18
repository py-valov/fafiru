from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    GROUP = {
        ('Обычный', 'Обычный'),
        ('Финансы', 'Финансы'),
        ('Логистика', 'Логистика'),
        ('Склад', 'Склад'),
        ('Склад+Логистика', 'Склад+Логистика'),
    }

    image = models.ImageField(upload_to='users_images', null=True, blank=True)
    group = models.CharField(max_length=100, choices=GROUP, null=True, blank=True, default='Обычный')