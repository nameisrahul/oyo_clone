from django.contrib import admin

# Register your models here.
from accounts.models import *
admin.site.register(HotelUser)
admin.site.register(HotelVendor)
admin.site.register(Ameneties)
admin.site.register(Hotel)