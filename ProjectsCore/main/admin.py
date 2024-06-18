from django.contrib import admin

from main.models import Content, ContentCategory
from core.admin import admin_site

# Register your models here.


# @admin_site.register(Category)
class ContentAdmin(admin.ModelAdmin):
    list_display = ['id', 'nameSite']
    

# @admin_site.register(Category)
class ContentCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category']
    


admin_site.register(Content, ContentAdmin)
admin_site.register(ContentCategory, ContentCategoryAdmin)
