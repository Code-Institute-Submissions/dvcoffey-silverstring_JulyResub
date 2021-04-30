# Add review

    if request.method == 'POST' and request.user.is_authenticated:
        stars = request.POST.get('stars', 3)
        content = request.POST.get('content', '')
        user = request.user

        review = Review.objects.create(product=product, user=user, stars=stars, content=content)

        return redirect('product_detail', product_id)