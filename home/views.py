from django.shortcuts import render, redirect, reverse

# Create your views here.


def index(request):
    """ A view to return the home page """

    return render(request, 'home/index.html')


def admin(request):
    if not request.user.is_superuser:
        return redirect(reverse('home'))

    return render(request, 'home/admin.html')
