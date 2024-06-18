from django.contrib import admin
from orders.models import Order, OrderItem
from core.admin import admin_site


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'phone',
                    'address_street','address_house', 'payment',
                    'created', 'update']
    list_filter = ['payment', 'created', 'update']
    inlines = [OrderItemInline]
    

admin_site.register(Order, OrderAdmin)
