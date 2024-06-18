import re
from django import forms
from orders.models import Order

class OrderCreateForm(forms.Form):
    # class Meta:
    #     model = Order
    #     fields = ['first_name', 'last_name', 'phone', 'address', 'payment']

    first_name = forms.CharField()
    last_name = forms.CharField()
    phone = forms.CharField()
    payment = forms.ChoiceField(
        choices = [
        ('C', 'Наличные'),
        ('M', 'Карта')
    ],
    )
    address_street = forms.CharField(required=False)
    address_house = forms.CharField(required=False)
   

    # def clean_phone_number(self):
    #     data = self.cleaned_data['phone_number']

    #     if not data.isdigit():
    #         raise forms.ValidationError('Номер телефона должен содержать только цифры')
        
    #     pattern = re.compile(r'^\d{10}$')
    #     if not pattern.match(data):
    #         raise forms.ValidationError('Не верный формат номера ')

