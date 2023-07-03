from django.urls import path, include
from . import views

urlpatterns = [

    # home page url
    path('', views.home, name='home'),

]
