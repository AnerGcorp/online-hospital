from django.contrib import admin

# Register your models here.
from .models import Medicine, Pharmacist, PharmacyShop, Order, Cart

admin.site.register(Pharmacist)
admin.site.register(Medicine)
admin.site.register(PharmacyShop)
admin.site.register(Cart)
admin.site.register(Order)
