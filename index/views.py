from django.shortcuts import render
from . models import *


# Create your views here.

# home / landing page
def home(request):
    about_data = About.objects.all()  # getting about objects
    slider_data = Slider.objects.all()  # getting slider objects
    context = {
        'about': about_data,
        'slider': slider_data
    }

    return render(request, 'index.html', context)



