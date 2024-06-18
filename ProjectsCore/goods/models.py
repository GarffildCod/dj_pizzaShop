from django.db import models
from django.urls import reverse


class Category(models.Model):

    name = models.CharField(max_length=200, verbose_name='Категория')
    slug = models.SlugField(max_length=250, unique=True)
    
    parent_id = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE,
                                related_name='children', verbose_name='Родительская категория')
    

    class Meta:
        ordering = ['name'] 
        indexes = [
            models.Index(fields=['name']), 
        ]
        db_table = 'category'
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse("goods:catalog_category", args=[self.slug])


    def __str__(self):
        return f"{self.name}"
    
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products',
                                on_delete=models.CASCADE, verbose_name='Категория') 
    name = models.CharField(max_length=200, verbose_name="Название продукта")
    slug = models.SlugField(max_length=200)
    image = models.ImageField(upload_to='products', blank=True, null=True, verbose_name='Картинка')
    description = models.TextField(blank=True, null=True, verbose_name='Описание') 
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена') 
    available = models.BooleanField(default=True, verbose_name='Наличие')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания') 
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')



    
    class Meta:
        ordering = ['name'] 
        indexes = [
            models.Index(fields=['id', 'slug']), 
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]
        verbose_name = "Продукт"
        verbose_name_plural = 'Продукты'

    def get_absolute_url(self):
        return reverse('goods:product',args=[self.id, self.slug])
    

    
    def __str__(self): 
        return self.name
    