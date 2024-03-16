from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import *
from .forms import *

def index(request):
    return HttpResponse("Страница входа Continental")

def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")

def addguest(request):
    if request.method == 'POST':
        form = AddGuestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddGuestForm()

def login(request):
    return render(request, 'index.html')

def booking(request):
    return render(request, 'booking.html')

def addbooking(request):
    if request.method == 'POST':
        form = AddBookingForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            return redirect('booking')
    else:
        form = AddBookingForm()
