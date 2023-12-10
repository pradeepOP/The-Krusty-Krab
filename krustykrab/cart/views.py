from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .cart import Cart
from core.models import MenuItem
# Create your views here.

def add_to_cart(request, menuItem_id):
    cart = Cart(request)
    cart.add(menuItem_id)

    return render(request, 'cart/menu_cart.html')


def cart(request):
    return render(request, 'cart/cart.html')


@login_required(login_url="login")
def checkout(request):
    return render(request, 'cart/checkout.html')

def update_cart(request, menuItem_id, action):
    cart = Cart(request)

    if action == 'increment':
        cart.add(menuItem_id, 1, True)
    else:
        cart.add(menuItem_id, -1, True)
    
    menuItem = MenuItem.objects.get(pk=menuItem_id)
    quantity = cart.get_item(menuItem_id)

    if quantity:
        quantity=quantity['quantity']

        item = {
            'menuItem':{
                'id':menuItem.id,
                'name':menuItem.name,
                'featured_image':menuItem.featured_image,
                'price':menuItem.price,

            },
            'total_price': (quantity * menuItem.price),
            'quantity':quantity,
        }
    else:
        item = None

    response = render(request, 'cart/partials/cart_item.html', {'item':item})
    response['HX-Trigger'] = 'update-menu-cart'
    return response
    

def hx_menu_cart(request):
    return render(request, 'cart/menu_cart.html')

def hx_cart_total(request):
    return render(request, 'cart/partials/cart_total.html')