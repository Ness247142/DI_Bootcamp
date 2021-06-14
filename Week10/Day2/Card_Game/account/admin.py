from django.contrib import admin
from .models import *
from forum.models import *

admin.site.register(Profile)
admin.site.register(Thread)
admin.site.register(Comment)