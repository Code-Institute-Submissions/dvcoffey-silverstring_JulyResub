from django.shortcuts import render
from .models import Showcase

# Create your views here.


def showcase(request):

    showcases = Showcase.objects.all
    context = {
        'showcases': showcases,
    }

    return render(request, 'showcase/showcase.html', context)
