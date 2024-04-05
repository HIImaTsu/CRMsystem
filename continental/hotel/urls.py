from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('home/', home, name='home'),
    path('house-keeping/', house_keeping, name='housekeeping'),
    path('booking/', booking, name='booking'),
    path('help-page/', help_page, name='help'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('add-booking/', add_booking, name='add-booking'),
    path('night-audit/', night_audit, name='night-audit'),
    path('cabinet/', cabinet, name='cabinet'),
    # path('guest/<slug:guest_slug>/', UpdateGuest.as_view(), name='update_guest'),
]