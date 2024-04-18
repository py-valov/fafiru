from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'transport']

    def get(self, request, format=None):
        serializer = ProductSerializer(Products.objects.all(), many=True)