# serializers.py
from rest_framework import serializers
from .models import *

class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ['first_name', 'last_name', 'phone']  # Включите необходимые поля

class BookingSerializer(serializers.ModelSerializer):
    guest_info = GuestSerializer(source='guest')  # Добавляем информацию о госте

    class Meta:
        model = Booking
        fields = ['guest_info', 'checkin_date', 'checkout_date', 'number_of_guests']



