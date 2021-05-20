from rest_framework import serializers
from .models import StockData


class StockDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockData 
        fields = ('code','name','open_price','high_price','low_price','close_price')