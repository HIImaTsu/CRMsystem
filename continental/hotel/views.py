from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.views.generic import UpdateView
from .models import *
from .forms import *
from django.core.serializers import serialize


def index(request):
    return HttpResponse("<h1>Страница CONTINENTAL</h1>")

def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")

@login_required
def home(request):
    return render(request, 'hotel/homePage.html')

# def addbooking(request):
#     if request.method == 'POST':
#         form = AddBookingForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('booking')
#     else:
#         form = AddBookingForm()

# class UpdateGuest(UpdateView):
#     model = Booking
#     fields = ['room_id', 'checkin_date']
#     template_name = 'hotel/update.html'
#     success_url = reverse_lazy('home')

@login_required
def housekeeping(request):
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
def booking_page(request):
    return render(request, 'hotel/bookingPage.html')

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

def get_bookings(request):
    bookings = Booking.objects.all()
    bookings_json = serialize('json', bookings)
    return JsonResponse(bookings_json, safe=False)

def calendar_view(request):
    return render(request, 'hotel/calendar.html')

