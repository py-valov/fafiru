from django.db import models
from main.models import Clients, Appeal
from product.models import ProductToTransport

class Check(models.Model):
    CURRENCY = [
        ('Долл', 'Долл'),
        ('Юа', 'Юа'),
        ('Нал.юа', 'Нал.юа'),
        ('Евро', 'Евро'),
        ('Фапьяо юа', 'Фапьяо юа'),
    ]

    WELLCHECK = [
        ('$', '$'),
        ('¥', '¥'),
        ('€', '€'),
        ('₽', '₽'),
    ]

    date = models.DateField()
    client = models.ForeignKey(Clients, on_delete=models.PROTECT)
    price = models.FloatField()
    currency = models.CharField(max_length=50, choices=CURRENCY)
    well = models.FloatField()
    wellCheck = models.CharField(max_length=5, choices=WELLCHECK)
    wellCommissionUSD = models.FloatField(null=True, blank=True)
    commissionPercent = models.FloatField(null=True, blank=True)
    commissionUSD = models.IntegerField(null=True, blank=True)
    commissionRUB = models.IntegerField(null=True, blank=True)
    product = models.CharField(max_length=255)
    status = models.BooleanField(default=False)
    ContractNumber = models.CharField(max_length=150, null=True, blank=True, default='YY2018-30')
    appeal = models.ForeignKey(Appeal, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return '{0}'.format(self.client.name)

class CheckFiles(models.Model):
    check_id = models.ForeignKey(Check, on_delete=models.PROTECT)
    PathFile = models.FileField(upload_to="files/%Y/%m/%d", null=True, blank=True)
    createFile = models.DateField(auto_now_add=True, null=True, blank=True)

class Operation(models.Model):
    TYPE_LETTER = [
        ('Возврат платежа', 'Возврат платежа'),
        ('Корректировка платежа', 'Корректировка платежа'),
    ]

    TYPE_CURRENCY = [
        ('$', '$'),
        ('¥', '¥'),
        ('€', '€'),
    ]
    name = models.CharField(max_length=50)
    check_id = models.ForeignKey(Check, related_name='opers', on_delete=models.PROTECT)
    date = models.DateField()
    admissionRUB = models.FloatField(null=True, blank=True)
    admissionCurrency = models.FloatField(null=True, blank=True)
    typeCurrency = models.CharField(max_length=5, choices=TYPE_CURRENCY, null=True, blank=True)
    nursingRUB = models.FloatField(null=True, blank=True)
    nursingCurrency = models.FloatField(null=True, blank=True)
    well = models.FloatField(null=True, blank=True)
    wellCommission = models.FloatField(null=True, blank=True)
    priceInUSD = models.FloatField(null=True, blank=True)
    ReturnPriceUSD = models.FloatField(null=True, blank=True)
    typeLetter = models.CharField(max_length=100, choices=TYPE_LETTER, null=True, blank=True)
    fileOperation = models.FileField(upload_to="Operation Files/%Y/%m/%d", null=True, blank=True)
    productToTransport_id = models.ForeignKey(ProductToTransport, on_delete=models.PROTECT, null=True, blank=True)
    productPriceToPaking = models.FloatField(null=True, blank=True)
    productPriceToPakingCurrency = models.CharField(max_length=10, choices=TYPE_CURRENCY, default='$', null=True, blank=True)
    productPriceInUSD = models.FloatField(null=True, blank=True)
    productPriceInUSDCurrency = models.CharField(max_length=10, choices=TYPE_CURRENCY, default='$', null=True, blank=True)


    def __str__(self):
        return self.name