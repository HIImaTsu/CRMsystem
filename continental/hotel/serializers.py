# serializers.py
from rest_framework import serializers
from .models import *

class GuestProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuestProfile
        fields = ['guest_balance']

class GuestSerializer(serializers.ModelSerializer):
    profile = GuestProfileSerializer()

    class Meta:
        model = Guest
        fields = ['first_name', 'last_name', 'phone', 'profile']

class BookingSerializer(serializers.ModelSerializer):
    guest_info = GuestSerializer(source='guest')

    class Meta:
        model = Booking
        fields = ['guest_info', 'checkin_date', 'checkout_date', 'room', 'total_price']



