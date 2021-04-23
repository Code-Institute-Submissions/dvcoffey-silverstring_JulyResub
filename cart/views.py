from django.shortcuts import render, redirect

# Create your views here.


def view_cart(request):
    """ A view that renders the shopping cart """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add to the shopping cart """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    gauge = None
    if 'string_gauge' in request.POST:
        gauge = request.POST['string_gauge']
    cart = request.session.get('cart', {})

    if gauge:
        if item_id in list(cart.keys()):
            if gauge in cart[item_id]['items_by_cart'].keys():
                cart[item_id]['items_by_gauge'][gauge] += quantity
            else:
                cart[item_id]['items_by_gauge'][gauge] = quantity
        else:
            cart[item_id] = {'items_by_gauge': {gauge: quantity}}
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
        else:
            cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)
