from django.contrib import admin

from phone.models import Phone

# Register your models here.

@admin.register(Phone) 
class PhoneAdmin(admin.ModelAdmin):
    list_display =['phone_name','phone_type','phone_ID','owner']