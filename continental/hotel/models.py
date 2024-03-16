from django.db import models

class Guest(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    e_mail = models.CharField(max_length=255)
    hotel_id = models.ForeignKey('Hotel', on_delete=models.PROTECT)

class Hotel(models.Model):
    name = models.CharField(max_length=255)

# class Staff(models.Model):
#     full_name = models.CharField(max_length=255)
#     position = models.CharField(max_length=100)
#     phone = models.CharField(max_length=20)

class RoomType:
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.IntegerField()

class Booking:
    guest_id = models.ForeignKey('Guest', on_delete=models.PROTECT)
    room_id = models.ForeignKey('Room', on_delete=models.PROTECT)
    checkin_date = models.DateTimeField()
    checkout_date = models.DateTimeField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

class Room:
    hotel_id = models.ForeignKey('Hotel', on_delete=models.PROTECT)
    type_id = models.ForeignKey('RoomType', on_delete=models.PROTECT)
    status = models.CharField(max_length=20)
    room_number = models.IntegerField()

class HouseKeeping:
    room_id = models.ForeignKey('Room', on_delete=models.PROTECT)
    date = models.DateTimeField()
    status = models.CharField(max_length=20)
    checkin_time = models.DateTimeField()
    checkout_time = models.DateTimeField()

class Payment:
    booking_id = models.ForeignKey('Booking', on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField()
    payment_method = models.CharField(max_length=50)
