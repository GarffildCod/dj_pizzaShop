from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from goods.models import Product
from django.urls import reverse
from cart.cart import Cart
from cart.forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):
    
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                quantity=cd['quantity'],
                override_quantity=cd['override'])
        # После успешной обработки формы перенаправляем пользователя обратно на ту же страницу
        return redirect(product.get_absolute_url())
   

@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')



def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={
                            'quantity': item['quantity'],
                            'override': True})
    context = {
        'cart': cart,
        'title': 'Корзина'
    }
    return render(request, 'cart/detail.html', context)