from django.db import models

from main.models import Clients, Appeal
from transports.models import Transports


class Products(models.Model):
    TRANSPORT = [
        ('Сборная', 'Сборная'),
        ('Авиа', 'Авиа'),
        ('Машина', 'Машина'),
        ('ЖД', 'ЖД'),
        ('Море', 'Море'),
    ]

    CATEGORY = [
        ('Одежда', 'Одежда'),
        ('Оборудование', 'Оборудование'),
        ('Инструменты', 'Инструменты'),
        ('Станки', 'Станки'),
    ]

    CURRENCY = [
        ('$', '$'),
        ('¥', '¥'),
        ('€', '€'),
    ]

    STATUS = [
        ('На складе', 'На складе'),
        ('Частично отгружен', 'Частично отгружен'),
        ('Отгружен', 'Отгружен'),
    ]

    date = models.DateField()
    client_id = models.ForeignKey(Clients, on_delete=models.PROTECT)
    namePaking = models.CharField(max_length=100)
    weight = models.FloatField()
    volume = models.FloatField()
    price = models.FloatField(default=0.00, blank=True, null=True)
    nameProduct = models.CharField(max_length=255)
    transport = models.CharField(max_length=255, choices=TRANSPORT, default='Сборная')
    category = models.CharField(max_length=255, choices=CATEGORY, default='Одежда')
    currency = models.CharField(max_length=10, choices=CURRENCY, default='$')
    status = models.CharField(max_length=50, choices=STATUS, default='На складе')
    ContractNumber = models.CharField(max_length=150, null=True, blank=True, default='YY2018-30')
    weightBalance = models.FloatField(blank=True, null=True)
    volumeBalance = models.FloatField(blank=True, null=True)
    priceBalance = models.FloatField(blank=True, null=True)
    appeal = models.ForeignKey(Appeal, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.namePaking

class ProductFiles(models.Model):
    product_id = models.ForeignKey(Products, on_delete=models.PROTECT)
    date_create = models.DateField(auto_now_add=True, blank=True, null=True)
    file = models.FileField(upload_to="productFiles/%Y/%m/%d", null=True, blank=True)

class Comments(models.Model):
    product_id = models.ForeignKey(Products, on_delete=models.PROTECT)
    comment = models.CharField(max_length=255)

    def __str__(self):
        return self.comment
    
class ProductToTransport(models.Model):
    transport_id = models.ForeignKey(Transports, on_delete=models.PROTECT)
    product_id = models.ForeignKey(Products, on_delete=models.PROTECT, null=True, blank=True)
    weight = models.FloatField()
    volume = models.FloatField()
    comments = models.CharField(max_length=250)