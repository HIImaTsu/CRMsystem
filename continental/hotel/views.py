import json
from itertools import groupby

from django.contrib.auth import login, authenticate, logout
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models.functions import TruncDate
from django.forms import model_to_dict
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.views.generic import UpdateView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from .forms import *
from django.core.serializers import serialize
import random
import logging
from django.contrib import messages
from django.core.serializers import serialize

from .serializers import BookingSerializer


def index(request):
    return render(request, 'hotel/example4.html')

def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")

@login_required
def home(request):
    return render(request, 'hotel/homePage.html')

@login_required()
def add_booking(request):

    staff_member = Staff.objects.get(user=request.user)
    hotel_id = staff_member.hotel.id
    room_types = RoomType.objects.filter(hotel__id=hotel_id)
    way_of_staying_choices = Booking.ArrivalMethod.choices
    payment_method = Payment.PaymentMethod.choices

    if request.method == 'POST':
        booking_form = AddBookingForm(request.POST)
        booking_form.fields['room_type'].queryset = RoomType.objects.filter(hotel_id=hotel_id)
        guest_form = AddGuestForm(request.POST)
        profile_form = AddGuestProfileForm(request.POST)

        if booking_form.is_valid() and guest_form.is_valid() and profile_form.is_valid():

            messages.success(request, 'Бронь и гость успешно зарегистрированы!')

            guest = guest_form.save(commit=False)
            guest.hotel = staff_member.hotel
            guest.save()

            new_booking = booking_form.save(commit=False)
            new_booking.guest = guest
            new_booking.save()

            profile = profile_form.save(commit=False)
            profile.guest = guest
            profile.save()

            # ДЛЯ ВВЕДЕНИЯ О БАЛАНСЕ ГОСТЯ
            payment_method = request.POST.get('paymentMethod')
            amount = request.POST.get('amount')
            if payment_method and amount:
                try:
                    amount = float(amount)  # Убедитесь, что сумма преобразуется в число
                except ValueError:
                    # Необходима обработка ошибки, если сумма не является числом
                    pass

                # Создаем новую запись оплаты
                Payment.objects.create(
                    booking=new_booking,
                    method=payment_method,
                    amount=amount
                )

            redirect_url = reverse('booking')  # Используем reverse, чтобы получить URL по имени пути
            return JsonResponse({'redirect_url': request.build_absolute_uri(redirect_url)})

        else:
            messages.error(request, 'Введены некорректные данные.')
    else:
        booking_form = AddBookingForm()
        guest_form = AddGuestForm()
        profile_form = AddGuestProfileForm()

    return render(request, 'hotel/reservationPage.html', {
        'booking_form': booking_form,
        'guest_form': guest_form,
        'profile_form': profile_form,
        'room_types': room_types,
        'way_of_staying_choices': way_of_staying_choices,
        'gender_choices': Guest.GENDER_CHOICES,
        'payment_method': payment_method,
    })

# class UpdateGuest(UpdateView):
#     model = Booking
#     fields = ['room_id', 'checkin_date']
#     template_name = 'hotel/update.html'
#     success_url = reverse_lazy('home')

@login_required
def house_keeping(request):
    # Рассмотреть оптимизацию подсчета данных этих

    # today = timezone.now().date()
    # now = timezone.now()
    #
    # checkouts = Booking.objects.filter(checkout_date__gte=today, checkout_date__lte=now).count()
    # checkins = Booking.objects.filter(checkin_date__gte=today, checkin_date__lte=now).count()
    # wet_cleanings = HouseKeeping.objects.filter(date__gte=today, date__lte=now, is_clean=False).count()
    #
    # data = {
    #     'checkouts': checkouts,
    #     'checkins': checkins,
    #     'wet_cleanings': wet_cleanings,
    # }
    return render(request, 'hotel/housekeeping.html')

@login_required()
def booking(request):
    bookings_list = Booking.objects.annotate(date=TruncDate('checkin_date')).order_by('date')
    bookings_grouped = {k: list(v) for k, v in groupby(bookings_list, lambda x: x.date)}

    return render(request, 'hotel/bookingPage.html', {'bookings_grouped': bookings_grouped})

@login_required()
def night_audit(request):
    return render(request, 'hotel/nightAudit.html')

@login_required()
def cabinet(request):
    return render(request, 'hotel/accountPage.html')

def help_page(request):
    return render(request, 'hotel/helpPage.html')


def login_user(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'],
                                password=cd['password'])
            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
    else:
        form = LoginUserForm()
    return render(request, 'hotel/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

@api_view(['GET'])
def booking_data(request):
    bookings = Booking.objects.all().select_related('guest')
    serializer = BookingSerializer(bookings, many=True)
    return Response(serializer.data)  # Rest Framework позаботится о форматировании ответа




