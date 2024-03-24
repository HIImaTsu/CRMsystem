from django.conf.urls.static import static
from django.contrib import admin


from continental import settings
from hotel.views import *
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hotel.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = pageNotFound

admin.site.site_header = "Панель администрирования"