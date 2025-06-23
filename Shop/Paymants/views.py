from django.shortcuts import render, redirect
from .models import Order, OrderItem ,Payment
from Products.models import Product
from django.http import HttpResponse
from collections import Counter
from Accounts.views import accounts_page

def payment_page(request):
    if request.user.is_authenticated:
        cart = request.session.get('cart', [])
        if not cart:
            return redirect('products:product_list')
        cart_counter = Counter(cart)
        cart_items = []
        for product_id, quantity in cart_counter.items():
            product = Product.objects.get(id=product_id)
            cart_items.append({
                'product': product,
                'quantity': quantity 
            })
        print(f"Cart items: {cart_items}")
        total_amount = sum(item['product'].price * item['quantity'] for item in cart_items)
        return render(request,"Paymants/paymants.html", {'cart': cart_items,'total_amount': total_amount})
    else:
        return redirect(accounts_page)

def remove_from_cart_paymants(request, your_product_id):
    cart = request.session.get('cart', [])
    if your_product_id in cart:
        cart.remove(your_product_id)
        request.session['cart'] = cart
    return redirect('paymants:payment_page')

def create_order(request):
    if request.method == 'POST':
        shipping_address = request.POST.get('shipping_address')
        zip_code = request.POST.get('zipcode')
        payment_method = request.POST.get('paymant_method')
        cart = request.session.get('cart', [])
        cart_counter = Counter(cart)
        if not shipping_address or not zip_code or not payment_method:
            return redirect('paymants:payment_page')
        
        total_amount = sum(Product.objects.get(id=product_id).price * quantity for product_id, quantity in cart_counter.items())
        if total_amount <= 0:
            return HttpResponse("Your cart is empty or the total amount is zero. Please add items to your cart before proceeding to payment.")
        order = Order.objects.create(
            user=request.user,
            shipping_address=shipping_address,
            zip_code=zip_code,
            total_amount=total_amount,
            payment_method=payment_method,
            status='Pending',
        )
        Payment.objects.create(
            order=order,
            amount=order.total_amount,
            payment_method=payment_method,
            status='Pending',)
        
        for product_id, quantity in cart_counter.items():
            product = Product.objects.get(id=product_id)
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=quantity,
                price=product.price
            )
        
        
        request.session['cart'] = []
        del request.session['cart']
        return render(request, "Paymants/success.html", {'order': order , 'payment_method': payment_method})
    else:
        return redirect('paymants:payment_page')