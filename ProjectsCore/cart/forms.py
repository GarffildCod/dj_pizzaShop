from django import forms 

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 15)]

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(label='Количество',
        choices=PRODUCT_QUANTITY_CHOICES,
        coerce=int,
        widget=forms.Select(attrs={
            'class': 'custom-select-me',  # Класс 
        })
    )
    override = forms.BooleanField(required=False,
        initial=False,
        widget=forms.HiddenInput)