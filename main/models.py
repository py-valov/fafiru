from django.db import models

from users.models import Users


# Create your models here.
class Clients(models.Model):
    CONTRACT = [
        ('Агентский', 'Агентский'),
        ('Поставка', 'Поставка'),
    ]

    AGENT = [
        ('Фаст Импорт', 'Фаст Импорт'),
        ('Шеян', 'Шеян'),
        ('ТОНГАРД', 'ТОНГАРД'),
        ('ПБ', 'ПБ'),
    ]

    kod = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    product = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=False, blank=True, default="")
    contract = models.CharField(max_length=50, choices=CONTRACT)
    agent = models.CharField(max_length=50, choices=AGENT)
    positiveBalance = models.FloatField(null=True, blank=True, default=0)
    negativeBalance = models.FloatField(null=True, blank=True, default=0)

    def __str__(self):
        return self.name
    

class News(models.Model):
    CATEGORY_NEWS = [
        ('Важное', 'Важное'),
        ('Оповещение', 'Оповещение'),
        ('Таможня', 'Таможня'),
    ]

    date = models.DateField()
    content = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=CATEGORY_NEWS)

    def __str__(self):
        return self.content
    

class Appeal(models.Model):
    CATEGORY_APPEALS = [
        ('Склад', 'Склад'),
        ('Счета', 'Счета'),
        ('Расчет товара', 'Расчет товара'),
        ('Доставка', 'Доставка'),
    ]

    date = models.DateField()
    content = models.CharField(max_length=2550)
    category = models.CharField(max_length=50, choices=CATEGORY_APPEALS)
    doneAppeal = models.BooleanField(default=False)
    client = models.ForeignKey(Clients, on_delete=models.PROTECT)
    user_create = models.ForeignKey(Users, on_delete=models.PROTECT, null=True, blank=True)
    file = models.FileField(upload_to="appeal-files/%Y/%m/%d", null=True, blank=True)

    def __str__(self):
        return self.content
    
class AppealComments(models.Model):
  date_create = models.DateTimeField(auto_now_add=True)
  user = models.ForeignKey(Users, on_delete=models.PROTECT)
  content = models.CharField(max_length=1255)
  file_comment = models.FileField(upload_to="appeal-comments/%Y/%m/%d", null=True, blank=True)
  appeal = models.ForeignKey(Appeal, on_delete=models.PROTECT)