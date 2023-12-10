from.cart import Cart
# create context processor so that our cart can work on all pages of site

def cart(request):
    # return the default data from the cart
    return {'cart':Cart(request)}