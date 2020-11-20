from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Person)
admin.site.register(Message)
admin.site.register(Cottage)
admin.site.register(Reservation)
