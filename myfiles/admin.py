from django.contrib import admin
from myfiles.models import Service
# Register your models here.
class AdminService(admin.ModelAdmin):
    list_display = ['id','nomi','old_price','new_price','manzil','rooms','rasm','vaqt']

admin.site.register(Service,AdminService)