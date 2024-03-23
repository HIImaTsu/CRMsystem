from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import UpdateView

from .models import *
from .forms import *


booking = Booking.objects.all()


def index(request):
    return HttpResponse("Страница Continental")

def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")

def home(request):
    return render(request, 'hotel/home.html')

def addbooking(request):
    if request.method == 'POST':
        form = AddBookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking')
    else:
        form = AddBookingForm()

class UpdateGuest(UpdateView):
    model = Booking
    fields = ['room_id', 'checkin_date']
    template_name = 'hotel/update.html'
    success_url = reverse_lazy('home')