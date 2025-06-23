from django.urls import path 
from .views import product_list, add_to_cart, remove_from_cart

app_name = 'products'

urlpatterns = [
    path('', product_list, name='product_list'),
    path('porducts/<int:your_product_id>/add_to_cart/', add_to_cart, name='add_to_cart'),
    path('porducts/<int:your_product_id>/remove_from_cart/', remove_from_cart, name='remove_from_cart'),
]
