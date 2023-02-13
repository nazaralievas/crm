from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('products/', products, name='products'),
    path('customer/<int:pk>/', customer, name='customer'),
    path('create_order/', createOrder, name='create_order'),
]
