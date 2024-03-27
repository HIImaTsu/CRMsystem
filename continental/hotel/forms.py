from django import forms
from .models import *

class LoginUserForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)




# class AddGuestForm(forms.ModelForm):
#
#     class Meta:
#         model = Guest
#         fields = ['first_name', 'last_name', 'phone', 'e_mail']
#         widgets = {
#         }
# class AddBookingForm(forms.ModelForm):
#     class Meta:
#         model = Booking
#         fields = ['checkin_date', 'checkout_date']
#         widgets = {
#
#         }