from django.db import models
from goods.models import Category
# Create your models here.

class Content(models.Model):
    nameSite = models.CharField(max_length=50, blank=True, null=True ,verbose_name='Названия магазина')
    phoneWork = models.CharField(max_length=20, blank=True, null=True ,verbose_name='Рабочий номер телефона')
    emailWork = models.EmailField(blank=True, null=True, verbose_name='Рабочий Email')
    textBanerMain = models.TextField(blank=True, null=True , verbose_name='Текст на главный банер')
    photoBanerMainOne =  models.ImageField(upload_to='content', blank=True, null=True, verbose_name='Главный банер 1 ()')
    photoBanerMainTwo =  models.ImageField(upload_to='content', blank=True, null=True, verbose_name='Главный банер 2 ()')
    urlDeliveryClub = models.URLField(verbose_name='Ссылка на Delivery Club', blank=True, null=True)
    adressShop = models.CharField(max_length=200, verbose_name='Адрес магазина', blank=True, null=True)
    ulrWhatsApp = models.URLField(verbose_name='Ссылка на WhatsApp', blank=True, null=True)
    banerLinkShop = models.ImageField(upload_to='content', blank=True, null=True, verbose_name='Банер магазин')
    banerLinkAbout = models.ImageField(upload_to='content', blank=True, null=True, verbose_name='Банер О нас')
    banerLinkContactUs = models.ImageField(upload_to='content', blank=True, null=True, verbose_name='Банер контакты')
    banerDeliveryClubIndex = models.ImageField(upload_to='content', blank=True, null=True, verbose_name='Банер контакты Delivery Club на главной')
    banerAboutContent = models.ImageField(upload_to='content', blank=True, null=True, verbose_name='Банер на страницу \"О нас для\" описания ')
    
    class Meta:
        verbose_name='Контент на странице'
        verbose_name_plural='Контент на страницах'
    
    def __str__(self):
        return self.nameSite
    
class ContentCategory(models.Model):
    category = models.ForeignKey(Category, verbose_name='Выберите категорию', on_delete=models.CASCADE)
    photoCategory = models.ImageField(upload_to='contentCategory', blank=True, null=True, verbose_name='Фото категории')

    class Meta:
        verbose_name='Категории на главное меню'
        verbose_name_plural='Категории на главное меню'
        
 