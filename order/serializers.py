from rest_framework import serializers
from shop.serializers import ShopSerializer
from shop.models import Shop
from product.models import Product
from .models import Order
from django.shortcuts import get_object_or_404
from product.serializers import ProductSerializer

class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = Order
        fields = "__all__"

    def create(self, validated_data):
        return Order(**validated_data)

class OrderCreateSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    customer_id = serializers.CharField()
    qty = serializers.IntegerField()

    def create(self, validated_data):
        Order.objects.create(
            product=get_object_or_404(Product, pk=validated_data["product_id"]),
            qty=validated_data["qty"],
            customer_id=validated_data["customer_id"],
        )
        # TODO: decreace product stock pieces

        return Order(**validated_data)
