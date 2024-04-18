from rest_framework import serializers
from .models import *

class OperationsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Operation
        fields = ['name','admissionCurrency', 'nursingCurrency', 'typeCurrency']

    def get(self, request, format=None):
        serializer = ChecksSerializer(Check.objects.all(), many=True)

class ChecksSerializer(serializers.ModelSerializer):
    opers = OperationsSerializer(many=True)
    client = serializers.CharField(source="client.name", read_only=True)
    client_kod = serializers.CharField(source="client.kod", read_only=True)
    client_contract = serializers.CharField(source="client.contract", read_only=True)

    class Meta:
        model = Check
        fields = ["id", "date", "client", "client_kod", "client_contract", "price", "currency" ,"well", "wellCheck", "wellCommissionUSD", "commissionPercent", "commissionUSD", "commissionRUB", "product", "status", "ContractNumber", "opers"]

    def get(self, request, format=None):
        serializer = ChecksSerializer(Check.objects.all(), many=True)