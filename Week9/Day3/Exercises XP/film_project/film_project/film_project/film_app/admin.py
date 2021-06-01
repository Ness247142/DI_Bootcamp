from django.contrib import admin
from .models import *

admin.site.register(Country)
admin.site.register(Category)
admin.site.register(Director)


class FilmAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'created_in_country')


admin.site.register(Film, FilmAdmin)

admin.site.site_url = '/film_app/homepage'
