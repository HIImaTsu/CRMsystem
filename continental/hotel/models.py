from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _  # для статусов в модели Room
from django.core.exceptions import ValidationError

class Guest(models.Model):
    MALE = 'М'
    FEMALE = 'Ж'
    GENDER_CHOICES = (
        (MALE, 'Мужской'),
        (FEMALE, 'Женский'),
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=MALE)
    phone = models.CharField(max_length=20)
    hotel = models.ForeignKey('Hotel', on_delete=models.PROTECT, related_name='guests')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class GuestProfile(models.Model):
    guest = models.OneToOneField(Guest, on_delete=models.CASCADE, related_name='profile')
    country = models.CharField(max_length=255, default='Казахстан')
    iin = models.CharField(max_length=12, blank=True, null=True, unique=True)
    document_number = models.CharField(max_length=50, unique=True)
    document_date = models.DateField()
    deadline_of_document = models.DateField()
    guest_balance = models.IntegerField(default=1000)


class Hotel(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class RoomType(models.Model):
    hotel = models.ForeignKey('Hotel', on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=50)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name

class Booking(models.Model):
    class Status(models.TextChoices):
        CHECKING_IN = 'I', _('Заезжающий')
        STAYING = 'S', _('Проживающий')
        CHECKED_OUT = 'O', _('Выехавший')
    class ArrivalMethod(models.TextChoices):
        BY_AIR = 'AIR', _('Аэропорт')
        BY_TRAIN = 'TRAIN', _('ЖД-пути')
        BY_OWN = 'OWN', _('Своим ходом')
    guest = models.ForeignKey('Guest', on_delete=models.PROTECT, related_name='bookings')
    room = models.ForeignKey('Room', on_delete=models.PROTECT, related_name='bookings')
    number_of_guests = models.IntegerField()
    number_of_nights = models.IntegerField()
    status_of_guest = models.CharField(max_length=1, choices=Status.choices, default=Status.CHECKING_IN)
    way_of_staying = models.CharField(max_length=30, choices=ArrivalMethod.choices, default=ArrivalMethod.BY_OWN)
    checkin_date = models.DateTimeField(null=False, blank=False)
    checkout_date = models.DateTimeField(null=False, blank=False)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=1000)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")

    def __str__(self):
        return f"{self.guest.first_name} {self.guest.last_name} - Booking ID: {self.id}"

# Чтобы убедиться, что checkin_date раньше, чем checkout_date
    def clean(self):
        super().clean()
        if self.checkin_date > self.checkout_date:
            raise ValidationError(_('Дата заезда должна быть раньше даты выезда.'))

    def save(self, *args, **kwargs):
        if not self.room_id:  # Проверяем, что поле room не заполнено
            default_room = Room.objects.get(id=2)  # Получаем объект комнаты по умолчанию
            self.room = default_room
        super().save(*args, **kwargs)


class Room(models.Model):
    hotel = models.ForeignKey('Hotel', on_delete=models.PROTECT, related_name='rooms')
    type = models.ForeignKey('RoomType', on_delete=models.PROTECT, related_name='rooms')
    room_number = models.IntegerField()

    def __str__(self):
        return f"{self.room_number} ({self.hotel.name})"

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
    class PaymentMethod(models.TextChoices):
        CASH = 'CASH', _('Наличные')
        KASPI = 'KASPI', _('KASPI')
        HALYK = 'HALYK', _('HALYK')
        NON_CASH = 'NON_CASH', _('Безналичные')
    booking = models.ForeignKey('Booking', on_delete=models.PROTECT, related_name='payment')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=30, choices=PaymentMethod.choices)


class Staff(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    hotel = models.ForeignKey('Hotel', on_delete=models.CASCADE)
    position = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username
