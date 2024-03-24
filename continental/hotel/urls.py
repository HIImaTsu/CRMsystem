from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('home/', home, name='home'),
    path('housekeeping/', housekeeping, name='housekeeping'),
    path('bookingPage/', bookingPage, name='booking'),
    path('helpPage/', helpPage, name='help'),
    path('login/', login, name='login')
    # path('guest/<slug:guest_slug>/', UpdateGuest.as_view(), name='update_guest'),
]