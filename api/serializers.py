from rest_framework import serializers
from common.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'wholesale_price', 'retail_price')
