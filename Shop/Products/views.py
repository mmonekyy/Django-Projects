from django.shortcuts import render , redirect
from .models import Product
from collections import Counter

def product_list(request):
    products = Product.objects.all()
    cart = request.session.get('cart', [])
    cart_counter = Counter(cart)
    cart_products = []
    
    for product_id, quantity in cart_counter.items():
        product_id = Product.objects.get(id=product_id) 
        cart_products.append({
            'product': product_id,
            'quantity': quantity
        })
    print(f"Cart contents: {cart_products}")
    
    return render(request, 'products/products.html', 
                 {'products': products, 
                  'cart_products': cart_products})

def add_to_cart(request, your_product_id):
    cart = request.session.get('cart', [])
    added_product = Product.objects.get(id=your_product_id)
    cart.append(added_product.id)
    print(f"Product details: {added_product.name}, Price: {added_product.price}, Stock: {added_product.stock}")
    if cart.count(added_product.id) > added_product.stock:
        cart.remove(added_product.id)
        print(f"Removed {added_product.name} from cart due to insufficient stock.")
    request.session['cart'] = cart
    return redirect('products:product_list')

def remove_from_cart(request, your_product_id):
    cart = request.session.get('cart', [])
    if your_product_id in cart:
        cart.remove(your_product_id)
        request.session['cart'] = cart
    return redirect('products:product_list')
