from django.conf import settings

from core.models import MenuItem

class Cart(object):
    def __init__(self, request):
        self.session = request.session

        # get the current session key if exists
        cart = self.session.get(settings.CART_SESSION_ID)

        #if session doesnot exists 
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        
        # making cart available for all pages of site
        self.cart = cart

    # method to iterate through products in cart
    def __iter__(self):
        for p in self.cart.keys():
            self.cart[str(p)]['menuItem'] = MenuItem.objects.get(pk=p)

        for item in self.cart.values():
            item['total_price'] = item['menuItem'].price * item['quantity']

            yield item

    # method to check the length
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
    
    # saving session
    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True
        
    # adding to the cart
    def add(self, menuItem_id, quantity=1, update_quantity=False):
        menuItem_id = str(menuItem_id)
        
        # checking if item added to the cart or not

        if menuItem_id not in self.cart:
            self.cart[menuItem_id] = {'quantity':1, 'id': menuItem_id}

        # for updating
        if update_quantity:
            self.cart[menuItem_id]['quantity'] += int(quantity)

            if self.cart[menuItem_id]['quantity'] == 0:
                self.remove(menuItem_id)

        self.save()

    # method for removing item from cart
    def remove(self, menuItem_id):
        if menuItem_id in self.cart:
            del self.cart[menuItem_id]
            self.save()

    # method to get total cost
    def get_total_cost(self):
        for p in self.cart.keys():
            self.cart[str(p)]['menuItem'] = MenuItem.objects.get(pk=p)

        return sum(item['menuItem'].price * item['quantity'] for item in self.cart.values())

    def get_item(self, menuItem_id):
        if str(menuItem_id) in self.cart:
            return self.cart[str(menuItem_id)]
        else:
            return None