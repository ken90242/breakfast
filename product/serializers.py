from rest_framework import serializers
from shop.serializers import ShopSerializer

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    stock_pcs = serializers.IntegerField()
    price = serializers.IntegerField()
    shop = ShopSerializer()
    # shop = serializers.ForeignKey(Shop, on_delete=models.CASCADE)
    vip = serializers.BooleanField()