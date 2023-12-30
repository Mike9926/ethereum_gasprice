from django.contrib import admin
from .models import GasPrice

@admin.register(GasPrice)
class GasPriceAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'gas_price', 'transaction_speed')
    search_fields = ('timestamp', 'gas_price', 'transaction_speed')
