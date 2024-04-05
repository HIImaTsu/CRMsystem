from django.contrib.auth import login, authenticate, logout
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.views.generic import UpdateView
from .models import *
from .forms import *
from django.core.serializers import serialize
import random
from django.contrib import messages


def index(request):
    return HttpResponse("<h1>Страница CONTINENTAL</h1>")

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

    if request.method == 'POST':
        booking_form = AddBookingForm(request.POST)
        booking_form.fields['room_type'].queryset = RoomType.objects.filter(hotel_id=hotel_id)
        guest_form = AddGuestForm(request.POST)
        profile_form = AddGuestProfileForm(request.POST)
        print(request.POST)

        if not booking_form.is_valid() or not guest_form.is_valid() or not profile_form.is_valid():
            print(booking_form.errors)
            print(guest_form.errors)
            print(profile_form.errors)

        if booking_form.is_valid() and guest_form.is_valid() and profile_form.is_valid():
            guest = guest_form.save(commit=False)
            guest.hotel = staff_member.hotel
            guest.save()

            new_booking = booking_form.save(commit=False)
            new_booking.guest = guest
            new_booking.save()

            profile = profile_form.save(commit=False)
            profile.guest = guest
            profile.save()

            return redirect('booking')
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
        'gender_choices': Guest.GENDER_CHOICES
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
    return render(request, 'hotel/bookingPage.html')

@login_required()
def night_audit(request):
    return render(request, 'hotel/nightAudit.html')

@login_required()
def cabinet(request):
    return render(request, 'hotel/homePage.html')

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



