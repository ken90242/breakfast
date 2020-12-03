from rest_framework import serializers

class ShopSerializer(serializers.Serializer):
    shop_id = serializers.CharField()
    name = serializers.CharField()
