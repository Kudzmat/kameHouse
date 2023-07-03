from django.shortcuts import render
from .models import *
from index.models import *


# about page
def about(request):
    about_data = About.objects.all()  # getting about objects
    team_data = Team.objects.all()  # getting team information

    context = {
        'about': about_data,
        'team': team_data
    }

    return render(request, 'about.html', context)
