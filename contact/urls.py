from django.urls import path, include
from . import views

urlpatterns = [

    # contact us url
    path('', views.contact, name='contact'),

]