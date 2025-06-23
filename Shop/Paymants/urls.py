from django.urls import path
from .views import payment_page , remove_from_cart_paymants , create_order

app_name = 'paymants'

urlpatterns = [
    path('', payment_page, name='payment_page'),
    path('remove_from_cart/<int:your_product_id>/', remove_from_cart_paymants, name='remove_from_cart'),
    path('create_order/', create_order, name='create_order'),
    ]
