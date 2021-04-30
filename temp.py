# Add review

    if request.method == 'POST' and request.user.is_authenticated:
        content = request.POST.get('content', '')
        user = request.user

        review = Review.objects.create(product=product, user=user, content=content)

        return redirect('product_detail', product_id)


        <!--Review Section-->
    <div class="row no-gutters">
        <div class="col-12 text-center">
            <h2 class="page-title">Reviews</h2>
        </div>
         <!--Submit Review Form-->
        <div class="col-12 col-lg-6">
            <div class="card review-container-card">
                {% if request.user.is_authenticated %}
                    <form method="post" action=".">
                        {% csrf_token %}
                        <div class="field">
                            <label>Leave a review</label>
                            <div class="control">
                                <textarea class="textarea" name="content"></textarea>
                            </div>
                        </div>
                        <div class="field">
                            <div class="control">
                                <button class="button btn-success">Submit</button>
                            </div>
                        </div>
                    </form>
                    {% else %}
                        <p>Please sign in to add review!</p>
                {% endif %}
            </div>
        </div>
        <!--Reviews--> 
        <div class="col-12 col-lg-6">
            <div class="reviews-wrapper">
                {% for review in product.reviews.all %}
                    <div class="card review-container-card">
                        <p>
                            <strong>Added by: </strong>{{ review.user }} <br>
                            <strong>Date: </strong>{{ review.date_added|date:"Y-m-d" }}
                        </p>
                        {{ review.content }}
                    </div>
                {% empty %}
                    <div class="card review-container-card">
                        No reviews yet...
                    </div>
                {% endfor %}
            </div>
        </div>
    </div>