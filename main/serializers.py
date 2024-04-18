from rest_framework import serializers
from .models import *

class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = ["id", "kod", "name", "product", "email", "agent", "contract"]

    def get(self, request, format=None):
        serializer = ClientsSerializer(Clients.objects.all(), many=True)

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ["id", "date", "content", "category"]

    def get(self, request, format=None):
        serializer = NewsSerializer(News.objects.all(), many=True)