from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login
from Paymants.models import Order

def accounts_page(request):
    if request.user.is_authenticated:
            
            orders = Order.objects.filter(user=request.user)
            print(f"User {request.user.username} has {orders.count()} orders.")
            return render(request, 'Accounts/Account_Order.html',
            {
                'user': request.user,
                'orders': orders,
            })
    return render(request, 'Accounts/Login_register.html', {
        'page': request.GET.get('page', 'login')  
    })

def user_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        print(f"Username: {username}, Password: {password}, First Name: {first_name}, Last Name: {last_name}, Email: {email}")
        if not all([username, password, first_name, last_name, email]):
            return HttpResponse("All fields are required.")
        if User.objects.filter(username=username).exists():
            return HttpResponse("Username already exists.")
        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email
        )
        user.save()
        return render(request, 'Accounts/Login_register.html')
    
    return render(request, 'Accounts/Login_register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(accounts_page)
        else:
            return HttpResponse("Invalid username or password.")
    
    return render(request, 'Accounts/Login_register.html')
