from django.shortcuts import render
from django.views.generic.base import View
from .models import Order
from .serializers import OrderSerializer, OrderCreateSerializer
from product.models import Product

from rest_framework.views import APIView
from rest_framework.response import Response

from django.http import Http404
from rest_framework import status
from django.shortcuts import get_object_or_404
import json

# Create your views here.
def checkings(handler):
    def warp(instance, request, *args, **kwargs):
        product = get_object_or_404(Product, pk=request.data["product_id"])
        if request.data['qty'] > product.stock_pcs:
            return Response({ "error_reason": "Out of stock" }, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        if product.vip == True and not request.data['is_vip']:
            return Response({ "error_reason": "Unqualified identity" }, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        return handler(instance, request, *args, **kwargs)
    return warp

class OrderListView(APIView):
    queryset = Order.objects

    def get(self, request, format=None):
        snippets = Order.objects.all()
        serializer = OrderSerializer(snippets, many=True)
        return Response(serializer.data)
    
    @checkings
    def post(self, request, format=None):
        serializer = OrderCreateSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            order = Order.objects.last()
            newly_serializer = OrderSerializer(order)

            product = Product.objects.get(pk=order.product.id)
            product.stock_pcs -= order.qty
            product.save()

            return Response(newly_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_204_NO_CONTENT)

class OrderDetailView(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = OrderSerializer(snippet)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()

        product = Product.objects.get(pk=snippet.product.id)
        start_available = bool(product.stock_pcs == 0)
        product.stock_pcs += snippet.qty
        product.save()

        payload = {
            "start_available": start_available,
            "product_id": product.id,
        }

        return Response(json.dumps(payload), status=status.HTTP_201_CREATED)

