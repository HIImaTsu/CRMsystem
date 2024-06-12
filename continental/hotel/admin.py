from django.contrib import admin
from .models import *

class GuestAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone')
    list_display_links = ('first_name', 'last_name')

class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_number', 'type', 'hotel', )
    list_display_links = ('type', 'room_number', 'hotel')

class RoomTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'hotel', 'capacity', 'price_per_night')
    list_display_links = ('name', 'hotel')

class GuestProfileAdmin(admin.ModelAdmin):
    list_display = ('guest', 'iin', 'guest_balance')
    list_display_links = ('guest',)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('guest', 'room', 'checkin_date', 'checkout_date')
    list_display_links = ('guest', 'room')

class StaffAdmin(admin.ModelAdmin):
    list_display = ('user', 'hotel', 'position')
    list_display_links = ('user',)

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('get_guest_full_name', 'get_hotel_name', 'amount', 'payment_date', 'payment_method')
    def get_guest_full_name(self, obj):
        return f"{obj.booking.guest.first_name} {obj.booking.guest.last_name}"
    get_guest_full_name.short_description = 'Guest'

    def get_hotel_name(self, obj):
        return obj.booking.room.hotel.name
    get_hotel_name.short_description = 'Hotel'

admin.site.register(Guest, GuestAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(GuestProfile, GuestProfileAdmin)
admin.site.register(Hotel)
admin.site.register(RoomType, RoomTypeAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(HouseKeeping)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Staff, StaffAdmin)



