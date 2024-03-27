from django.db import models
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
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    country = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    hotel = models.ForeignKey('Hotel', on_delete=models.PROTECT, related_name='guests')

class GuestProfile(models.Model):
    guest = models.OneToOneField(Guest, on_delete=models.CASCADE, related_name='profile')
    iin = models.CharField(max_length=12, blank=True, null=True, unique=True)
    document_number = models.CharField(max_length=50, unique=True)
    document_date = models.DateField()
    deadline_of_document = models.DateField()
    guest_balance = models.IntegerField()

class Hotel(models.Model):
    name = models.CharField(max_length=255)

class RoomType(models.Model):
    name = models.CharField(max_length=50)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.IntegerField()

class Booking(models.Model):
    class Status(models.TextChoices):
        CHECKING_IN = 'I', _('Заезжающий')
        STAYING = 'S', _('Проживающий')
        CHECKED_OUT = 'O', _('Выехавший')
    guest = models.ForeignKey('Guest', on_delete=models.PROTECT, related_name='bookings')
    room = models.ForeignKey('Room', on_delete=models.PROTECT, related_name='bookings')
    number_of_guests = models.IntegerField()
    number_of_nights = models.IntegerField()
    status_of_guest = models.CharField(max_length=1, choices=Status.choices, default=Status.CHECKING_IN)
    way_of_staying = models.CharField(max_length=255, )
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
    class PaymentMethod(models.TextChoices):
        CASH = 'CASH', _('Наличные')
        KASPI = 'KASPI', _('KASPI')
        HALYK = 'HALYK', _('HALYK')
        NON_CASH = 'NON_CASH', _('Безналичные')
    booking = models.ForeignKey('Booking', on_delete=models.PROTECT, related_name='payment')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField()
    payment_method = models.CharField(max_length=30, choices=PaymentMethod.choices)

