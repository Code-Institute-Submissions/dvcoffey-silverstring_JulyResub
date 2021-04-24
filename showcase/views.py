from django.shortcuts import render
from .models import Showcase

# Create your views here.


def showcase(request):

    return render(request, 'showcase/showcase.html')