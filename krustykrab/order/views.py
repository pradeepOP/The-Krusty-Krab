from django.shortcuts import render, redirect
from .models import Order, OrderItem
from cart.cart import Cart

def start_order(request):
    cart = Cart(request)

    if request.method == 'POST':
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        address = request.POST.get("address")
        zipcode = request.POST.get("zipcode")
        city = request.POST.get("city")
        phone = request.POST.get("phone")

        order = Order.objects.create(
            user=request.user,
            first_name=first_name,
            last_name=last_name,
            email=email,
            address=address,
            zipcode=zipcode,
            city=city,
            phone=phone,
        )

        for item in cart:
            menuItem = item['menuItem']
            quantity = int(item["quantity"])
            price = menuItem.price * quantity
            item = OrderItem.objects.create(order=order, menuItem=menuItem, price=price, quantity=quantity) 

        return redirect('account')      
    return redirect('cart')     