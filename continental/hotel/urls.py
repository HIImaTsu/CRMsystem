from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('home/', home, name='home'),
    path('housekeeping/', housekeeping, name='housekeeping'),
    path('bookingPage/', booking_page, name='booking'),
    path('helpPage/', help_page, name='help'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('get-bookings/', get_bookings, name='get-bookings'),
    path('calendar/', calendar_view, name='calendar'),
    # path('guest/<slug:guest_slug>/', UpdateGuest.as_view(), name='update_guest'),
]