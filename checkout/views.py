from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "No items in cart!")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51IjcrSJsYfaQBI6AjpjM2aGUm3sgMNnBnTihsycuCDrRkNUHBGtMdnfroZxoWSYOQpZU7HrvlrV19LSfF9iqLtoc00A3qv1tdu',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
