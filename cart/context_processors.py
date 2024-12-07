from .cart import Cart

# create context processor for cart page to work in all pages
def cart(request):
    # return the default data from our cart
    return {'cart': Cart(request)}