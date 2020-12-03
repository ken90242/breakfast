from django.shortcuts import render
from django.views.generic.base import View
from .models import Product
from order.models import Order
from .serializers import ProductSerializer

# from django.forms.models import model_to_dict
from django.core import serializers
from django.http import JsonResponse
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count, Sum

from django.http import Http404
from rest_framework import status


# Create your views here.
class ProductListView(APIView):
    queryset = Product.objects

    def get(self, request, format=None):
        top = request.query_params.get('top', None)

        if top:
            ordered_results = Order.objects.values("product_id").annotate(total_qty=Sum('qty')).values('product_id', 'total_qty').order_by('-total_qty')

            ordered_products = []
            for result in ordered_results:
                ordered_products.extend(Product.objects.filter(id=result['product_id']))

            snippets = ordered_products[:int(top)]
        else:
            snippets = Product.objects.all()

        serializer = ProductSerializer(snippets, many=True)
        return Response(serializer.data)

