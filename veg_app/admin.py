from django.contrib import admin

# Register your models here.
from .models import VegPriceTrend, VegPrice, WeatherData, VegetablePriceByPref, ProduceAmount

admin.site.register(VegPriceTrend)
admin.site.register(VegPrice)
admin.site.register(WeatherData)
admin.site.register(VegetablePriceByPref)
admin.site.register(ProduceAmount)