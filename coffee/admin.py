from django.contrib import admin

from .models import Coffee, contactt_us, Reservation
# Register your models here.

# @admin.register(Coffee)
class CoffeeAdmin(admin.ModelAdmin):
    
    list_display = ['name','price','quantity']
    
    

admin.site.register(Coffee,CoffeeAdmin)
admin.site.register(contactt_us)
admin.site.register(Reservation)