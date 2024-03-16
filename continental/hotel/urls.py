from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('login/', login, name='login'),
    path('booking', booking, name='booking')

]