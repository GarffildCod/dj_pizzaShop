from django.shortcuts import render
from main.models import Content, ContentCategory
from goods.models import Product
from django.core.paginator import Paginator
# Create your views here.


def index(request):

    content = Content.objects.first()
    contentCategory = ContentCategory.objects.all()[:4]

    # Выбираем 4 случайных товара
    random_products = Product.objects.order_by('?')[:4]
    # Инициализируем пагинатор с этими товарами
    paginator = Paginator(random_products, 4)
    # Получаем номер текущей страницы из GET-параметров
    page = request.GET.get('page', 1)
    # Получаем текущую страницу объектов
    current_page = paginator.page(page)

    context = {
        'title': 'Главная',
        'content': content,
        'contentCategory': contentCategory,
        'paginator': current_page,
    }

    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'О нас'
    }
    return render(request, 'main/about.html', context)

def contact(request):

    context = {
        'title': 'Контакты'
    }

    return render(request, 'main/contact.html', context)