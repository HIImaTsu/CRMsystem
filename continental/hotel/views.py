import random

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .forms import *
from django.core.serializers import serialize
from django.contrib import messages
from .serializers import BookingSerializer
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm


def index(request):
    return HttpResponse("<h1>Страница CONTINENTAL</h1>")

def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")

@login_required
def home(request):
    return render(request, 'hotel/homePage.html', {'username': request.user.username})

@login_required()
def add_booking(request):
    staff_member = Staff.objects.get(user=request.user)
    hotel_id = staff_member.hotel.id
    hotel = staff_member.hotel
    room_types = RoomType.objects.filter(hotel__id=hotel_id)
    way_of_staying_choices = Booking.ArrivalMethod.choices
    payment_method = Payment.PaymentMethod.choices

    # СНАЧАЛА ПРОВЕРЯЕМ ГОСТЯ И ЗАПОЛНЯЕМ ДАННЫЕ ГОСТЯ - ПОТОМ УЖЕ СОЗДАЕМ БРОНЬ
    if request.method == 'POST':
        booking_form = AddBookingForm(request.POST)
        guest_form = AddGuestForm(request.POST)
        iin = request.POST.get('iin')
        document_number = request.POST.get('document_number')
        try:
            existing_profile = GuestProfile.objects.get(iin=iin, document_number=document_number)
            guest = existing_profile.guest
            messages.success(request, 'Гость найден в системе. Создаем бронирование для существующего гостя.')
        except GuestProfile.DoesNotExist:
            if guest_form.is_valid():
                guest = guest_form.save(commit=False)
                guest.hotel = hotel
                guest.save()

                profile_form = AddGuestProfileForm(request.POST)
                if profile_form.is_valid():
                    profile = profile_form.save(commit=False)
                    profile.guest = guest
                    profile.save()
                    messages.success(request, 'Новый гость и профиль успешно созданы. Бронь зарезервирована')
                else:
                    messages.error(request, 'Ошибка в данных профиля.')
                    return JsonResponse({'redirect_url_error': request.build_absolute_uri(reverse('add-booking'))})
            else:
                messages.error(request, 'Ошибка в данных гостя.')
                return JsonResponse({'redirect_url_error': request.build_absolute_uri(reverse('add-booking'))})

            # Создаем новую бронь
        if booking_form.is_valid():
            checkin_date = booking_form.cleaned_data['checkin_date']
            checkout_date = booking_form.cleaned_data['checkout_date']

            room_type_id = request.POST.get('room_type')  # Получаем ID из формы
            try:
                room_type = RoomType.objects.get(pk=room_type_id)  # Ищем объект RoomType по ID
            except RoomType.DoesNotExist:
                messages.error(request, "Категория номера не найдена.")
                return JsonResponse({'redirect_url_error': request.build_absolute_uri(reverse('add-booking'))})

            available_rooms = [room for room in Room.objects.filter(type=room_type)
                               if is_room_available(room, checkin_date, checkout_date)]
            if available_rooms:
                new_booking = booking_form.save(commit=False)
                new_booking.room = random.choice(available_rooms)
                new_booking.guest = guest
                new_booking.save()
                return JsonResponse({'redirect_url': request.build_absolute_uri(reverse('booking'))})
            else:
                messages.error(request, 'Свободных номеров на выбранные даты нету')
                return JsonResponse({'redirect_url_error': request.build_absolute_uri(reverse('add-booking'))})
        else:
            # print("Booking Form Errors:", booking_form.errors)
            # print("Guest Form Errors:", guest_form.errors)
            messages.error(request, 'Ошибка в данных бронирования.')
            return JsonResponse({'redirect_url_error': request.build_absolute_uri(reverse('add-booking'))})

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
        'username': request.user.username,
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
    return render(request, 'hotel/housekeeping.html', {'username': request.user.username})

@login_required()
def booking(request):
    return render(request, 'hotel/bookingPage.html', {'username': request.user.username})

@login_required()
def night_audit(request):
    return render(request, 'hotel/nightAudit.html', {'username': request.user.username})

@login_required()
def cabinet(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) # Обновить сессию пользователя, чтобы не выходить из системы
            messages.success(request, 'Ваш пароль был успешно изменен.')
            return redirect('cabinet')  # перенаправить на страницу профиля
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'hotel/accountPage.html', {
        'username': request.user.username,
        'form': form,
    })

def help_page(request):
    return render(request, 'hotel/helpPage.html', {'username': request.user.username})


def login_user(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'],
                                password=cd['password'])
            if user and user.is_active:
                login(request, user)
                if cd.get('remember'):
                    request.session.set_expiry(604800)  # 1 неделя жизни, указывается в секундах
                else:
                    request.session.set_expiry(0)  # Сессия закроется при закрытии браузера
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
    return Response(serializer.data)


def is_room_available(room, checkin_date, checkout_date):
    # Получаем все бронирования для номера
    bookings = Booking.objects.filter(room=room)
    for booking in bookings:
        if booking.checkin_date < checkout_date and booking.checkout_date > checkin_date:
            return False  # Даты перекрываются, номер недоступен
    return True  # Номер доступен для бронирования



