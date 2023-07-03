from django.urls import path, include
from . import views

urlpatterns = [

    # contact us url
    path('', views.user_login, name='login'),
    path('registration', views.user_registration, name='registration'),
    path('password-reset', views.reset, name='reset'),
    path('logout', views.user_logout, name='logout')

]