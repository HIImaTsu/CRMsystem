from django.db import models
from django.utils.translation import gettext_lazy as _  # для статусов в модели Room
from django.core.exceptions import ValidationError

class Guest(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    e_mail = models.EmailField(max_length=255)
    hotel = models.ForeignKey('Hotel', on_delete=models.PROTECT, related_name='guests')

class Hotel(models.Model):
    name = models.CharField(max_length=255)

class RoomType(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.IntegerField()

class Booking(models.Model):
    guest = models.ForeignKey('Guest', on_delete=models.PROTECT, related_name='bookings')
    room = models.ForeignKey('Room', on_delete=models.PROTECT, related_name='bookings')
    checkin_date = models.DateTimeField()
    checkout_date = models.DateTimeField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def clean(self):
        # чтобы убедиться, что checkin_date раньше, чем checkout_date
        if self.checkin_date and self.checkout_date and self.checkin_date >= self.checkout_date:
            raise ValidationError(_('Дата заезда должна быть раньше даты выезда.'))

        super().clean()

class Room(models.Model):
    hotel = models.ForeignKey('Hotel', on_delete=models.PROTECT, related_name='rooms')
    type = models.ForeignKey('RoomType', on_delete=models.PROTECT, related_name='rooms')
    room_number = models.IntegerField()

    class Meta:
        unique_together = (('hotel', 'room_number'),)    # для уникальности номеров в отеле

    #  Получение статуса номера
    def get_clean_status(self):
        last_housekeeping = self.housekeepings.order_by('-date').first()
        if last_housekeeping and last_housekeeping.status:
            return "Чистый"
        return "Грязный"

class HouseKeeping(models.Model):
    room = models.ForeignKey('Room', on_delete=models.PROTECT, related_name='housekeepings')
    date = models.DateTimeField()
    is_clean = models.BooleanField(default=False)  # True - "Чистый", False - "Грязный"
    checkin_time = models.DateTimeField()
    checkout_time = models.DateTimeField()

class Payment(models.Model):
    booking = models.ForeignKey('Booking', on_delete=models.PROTECT, related_name='payment')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField()
    payment_method = models.CharField(max_length=50)


