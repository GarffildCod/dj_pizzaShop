from django.db import models
from goods.models import Product
# Create your models here.

class Order(models.Model):

    PAY_CHOISE = [
        ('C', 'Наличные'),
        ('M', 'Карта')
    ]

    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, blank=True, null=True, verbose_name='Фамилия')
    phone = models.CharField(max_length=20, verbose_name='Номер телефона')
    address_street = models.CharField(max_length=250, verbose_name='Адрес Город/Улица')
    address_house = models.CharField(max_length=250, blank=True, null=True, verbose_name='Адрес Квартира/Подъезд')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заказа')
    update = models.DateField(auto_now=True, verbose_name='Дата обновления')
    payment = models.CharField(max_length=1, choices=PAY_CHOISE, verbose_name='Оплата')
    

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields = ['-created'])
        ]
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
    
    def __str__(self):
        return f'Order  {self.id}'
    
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE, verbose_name='Заказ')
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE, verbose_name='Продукт')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')

    def __str__(self):
        return str(self.id)
    
    def get_cost(self):
        return self.price * self.quantity
    
