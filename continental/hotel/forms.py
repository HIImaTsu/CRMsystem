from django import forms
from .models import *

class LoginUserForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    remember = forms.BooleanField(required=False)

class AddGuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ['last_name', 'first_name', 'middle_name', 'phone']

class AddGuestProfileForm(forms.ModelForm):
    class Meta:
        model = GuestProfile
        fields = ['iin', 'document_number', 'document_date', 'deadline_of_document', 'country']

class AddBookingForm(forms.ModelForm):
    room_type = forms.ModelChoiceField(queryset=RoomType.objects.all(), required=True,)
    class Meta:
        model = Booking
        fields = ['checkin_date', 'checkout_date', 'number_of_guests',
                  'number_of_nights', 'way_of_staying', 'number_of_nights']

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['amount', 'payment_method']
