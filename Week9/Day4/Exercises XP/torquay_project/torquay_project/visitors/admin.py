from django.contrib import admin
from .models import *


class HotelVacanciesAdmin(admin.ModelAdmin):
    list_display = ('name')


admin.site.register(HotelVacancies, HotelVacanciesAdmin)

admin.site.site_url = '/visitors/home'


class BookingsAdmin(admin.ModelAdmin):
    list_display = ('name')


admin.site.register(Bookings, BookingsAdmin)

admin.site.site_url = '/visitors/home'
