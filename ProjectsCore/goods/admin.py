from django.contrib import admin
from goods.models import Category, Product
from core.admin import admin_site

# Register your models here.


# @admin_site.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent_id']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['parent_id'] 

# @admin_site.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'available', 'price', 'created', 'updated']
    list_filter = ['available', 'created', 'category', 'updated'] 
    list_editable = ['price', 'available'] 
    prepopulated_fields = {'slug': ('name',)}
    



admin_site.register(Category, CategoryAdmin)
admin_site.register(Product, ProductAdmin)