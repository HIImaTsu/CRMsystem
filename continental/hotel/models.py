from django.db import models

class Guest(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    e_mail = models.CharField(max_length=255)
    hotel_id = models.ForeignKey('Hotel', on_delete=models.PROTECT)

class Hotel(models.Model):
    name = models.CharField(max_length=255)

class RoomType(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.IntegerField()

class Booking(models.Model):
    guest_id = models.ForeignKey('Guest', on_delete=models.PROTECT)
    # рассмотреть тип связывания этой таблицы с другими
    room_id = models.ForeignKey('Room', on_delete=models.PROTECT)
    checkin_date = models.DateTimeField()
    checkout_date = models.DateTimeField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

class Room(models.Model):
    hotel_id = models.ForeignKey('Hotel', on_delete=models.PROTECT)
    type_id = models.ForeignKey('RoomType', on_delete=models.PROTECT)
    status = models.CharField(max_length=20)
    room_number = models.IntegerField()

class HouseKeeping(models.Model):
    room_id = models.ForeignKey('Room', on_delete=models.PROTECT)
    date = models.DateTimeField()
    status = models.CharField(max_length=20)
    checkin_time = models.DateTimeField()
    checkout_time = models.DateTimeField()

class Payment(models.Model):
    booking_id = models.ForeignKey('Booking', on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField()
    payment_method = models.CharField(max_length=50)
