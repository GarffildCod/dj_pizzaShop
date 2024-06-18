from django.shortcuts import render
from orders.models import Order, OrderItem
from orders.forms import OrderCreateForm
from cart.cart import Cart
from django.http import HttpResponse
from telebot.management.commands.runbot import send_telegram_message_to_all


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(data=request.POST)
        if form.is_valid():
            order = Order.objects.create(
                            first_name = form.cleaned_data['first_name'],
                            last_name = form.cleaned_data['last_name'],
                            phone = form.cleaned_data['phone'],
                            address_street = form.cleaned_data['address_street'],
                            address_house = form.cleaned_data['address_house'],
                            payment = form.cleaned_data['payment'],
                        )

            for item in cart:
                OrderItem.objects.create(order=order,
                                        product=item['product'],
                                        price=item['price'],
                                        quantity=item['quantity'])
            # очистить корзину
            cart.clear()

            # Отправка сообщения в Telegram-бота
            try:
                message = f"Новый заказ 💌\nИмя:   {order.first_name}\nФамилия:   {order.last_name}\nНомер телефона:   {order.phone}\nУлица/Дом:   {order.address_street}\nКвартира/Подъезд:   {order.address_house}\nОплата:   {order.payment}"
                send_telegram_message_to_all(message)
            except Exception as e:
                print(f"Произошла ошибка при отправке сообщения в Telegram: {e}")


            return render(request,
                            'orders/created.html',
                            {'order': order})
        else:
            return HttpResponse('Форма не валид ')
    else:
        form = OrderCreateForm()
    return render(request,
                    'orders/create.html',
                    {'cart': cart, 'form': form})