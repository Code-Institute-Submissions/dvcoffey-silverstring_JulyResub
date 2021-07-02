from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Review
from products.models import Product
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django import forms
from django.core.paginator import Paginator


@login_required
def add_review(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':

        print("POST requested")
        form = ReviewForm(request.POST, request.FILES)
        form.instance.user = request.user
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added review!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request, 'Review not added. Please check your form.')
    else:
        initial = {'product': product}
        form = ReviewForm(initial=initial)
        form.fields['product'].widget = forms.HiddenInput()

    template = 'review/add_review.html'
    context = {
        'form': form,
        'product': product,
    }
    return render(request, template, context)
