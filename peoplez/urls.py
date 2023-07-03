from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.time_machine, name='time'),  # community

    path('inside', views.inside, name='inside'),  # inside

    path('user-profile', views.user_profile, name='profile'),  # profile page

    path('save-timeline', views.save_timeline, name='save_timeline')
]
