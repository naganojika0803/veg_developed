from django.contrib import admin

# Register your models here.
from .models import VegPriceTrend, VegPrice

admin.site.register(VegPriceTrend)
admin.site.register(VegPrice)