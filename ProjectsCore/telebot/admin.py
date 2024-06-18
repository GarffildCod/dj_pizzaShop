from django.contrib import admin
from telebot.models import UserBot, WorkUserBot
from core.admin import admin_site



class UserBotAdmin(admin.ModelAdmin):
    list_display = ['name', 'chat_id']
    list_filter = ['name',] 
    
    

class WorkUserBotAdmin(admin.ModelAdmin):
    list_display = ['chat_id']


admin_site.register(UserBot, UserBotAdmin)
admin_site.register(WorkUserBot, WorkUserBotAdmin)