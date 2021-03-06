"""breakfast URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from rest_framework.documentation import include_docs_urls

from product.views import ProductListView
from order.views import OrderListView, OrderDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'products/$', ProductListView.as_view(), name='product'),
    url(r'orders/$', OrderListView.as_view(), name='order'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='orderDetail'),
    path('api-auth/', include('rest_framework.urls')),
    url(r'docs/$', include_docs_urls(title='API')),
]
