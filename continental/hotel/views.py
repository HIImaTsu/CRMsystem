from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import *
from .forms import *

booking = Booking.objects.all()

def index(request):
    return HttpResponse("Страница Continental")

def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")

def login(request):
    return render(request, 'hotel/index.html')

def booking(request):
    return render(request, 'hotel/booking.html')

# def addguest(request):
#     if request.method == 'POST':
#         form = AddGuestForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = AddGuestForm()
#
# def addbooking(request):
#     if request.method == 'POST':
#         form = AddBookingForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('booking')
#     else:
#         form = AddBookingForm()
