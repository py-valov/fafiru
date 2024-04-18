from django.db import models

class Transports(models.Model):
    CATEGORY = [
        ('Сборная', 'Сборная'),
        ('Авиа', 'Авиа'),
        ('Машина', 'Машина'),
        ('ЖД', 'ЖД'),
        ('Море', 'Море'),
    ]

    STATUS = [
        ('Сбор на складе', 'Сбор на складе'),
        ('СВХ', 'СВХ'),
        ('Таможня', 'Таможня'),
        ('Выпуск/разгрузка', 'Выпуск/разгрузка'),
        ('Отчетность на товар', 'Отчетность на товар'),
        ('Закрыта', 'Закрыта'),
    ]

    date_create = models.DateField()
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=100, choices=CATEGORY, default='Сборная')
    region = models.CharField(max_length=250, null=True, blank=True)
    status = models.CharField(max_length=100, choices=STATUS, default='Сбор на складе')
