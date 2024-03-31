from django.contrib import admin
from .models import *

class GuestAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'country', 'phone')
    list_display_links = ('first_name', 'last_name')

class RoomAdmin(admin.ModelAdmin):
    list_display = ('type', 'hotel', 'room_number')
    list_display_links = ('type', 'room_number', 'hotel')

class GuestProfileAdmin(admin.ModelAdmin):
    list_display = ('guest', 'iin', 'guest_balance')
    list_display_links = ('guest',)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('guest', 'room', 'checkin_date', 'checkout_date')
    list_display_links = ('guest', 'room')

class StaffAdmin(admin.ModelAdmin):
    list_display = ('user', 'hotel', 'position')
    list_display_links = ('user',)

admin.site.register(Guest, GuestAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(GuestProfile, GuestProfileAdmin)
admin.site.register(Hotel)
admin.site.register(RoomType)
admin.site.register(Room, RoomAdmin)
admin.site.register(HouseKeeping)
admin.site.register(Payment)
admin.site.register(Staff, StaffAdmin)



