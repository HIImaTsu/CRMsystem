from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('home', home, name='home'),
    # path('guest/<slug:guest_slug>/', UpdateGuest.as_view(), name='update_guest'),
]