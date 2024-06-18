from django.db import models

# Create your models here.

class UserBot(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    chat_id = models.CharField(max_length=20, verbose_name='Id пользователя (В боте написать /start)')

    class Meta:
        verbose_name = 'Пользователи в бот заказов'
        verbose_name_plural = 'Пользователи в бот заказов' 

    def __str__(self):
        return f'{self.name}'
    

class WorkUserBot(models.Model):
    chat_id = models.CharField(max_length=20, verbose_name='')

    class Meta:
        verbose_name = 'Для бота разработчиков'
        verbose_name_plural = 'Для бота разработчиков' 
    
    def __str__(self):
        return self.chat_id