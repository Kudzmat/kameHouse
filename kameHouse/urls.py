from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

                  # admin url path
                  path("admin/", admin.site.urls),

                  # index/ homepage urls
                  path('', include('index.urls')),

                  # peoplez / time machine urls
                  path('Trunks-time-machine/', include('peoplez.urls')),

                  # contact us url
                  path('contact-kame-house/', include('contact.urls')),

                  # contact us url
                  path('about-kame-house/', include('about.urls')),

                  # my account url
                  path('authentication/', include('authentication.urls'))

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
