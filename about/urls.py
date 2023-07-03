from django.urls import path, include
from . import views

urlpatterns = [

    # contact us url
    path('', views.about, name='about'),

]


