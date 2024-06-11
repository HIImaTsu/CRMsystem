from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('home/', home, name='home'),
    path('house-keeping/', house_keeping, name='housekeeping'),
    path('booking/', booking, name='booking'),
    path('help-page/', help_page, name='help'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('add-booking/', add_booking, name='add-booking'),
    path('night-audit/', night_audit, name='night-audit'),
    path('cabinet/', cabinet, name='cabinet'),
    path('api/bookings/', booking_data, name='api_bookings'),
]