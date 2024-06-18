from django.shortcuts import render, get_object_or_404
from goods.models import Product, Category
from cart.forms import CartAddProductForm
from django.core.paginator import Paginator
from main.models import Content
# Create your views here.


def catalog(request, category_slug=None):

    page = request.GET.get('page', 1)
    query = request.GET.get('q', None)
    content = Content.objects.first()

    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category= category)


    # Пагинация
    paginator = Paginator(products, 8)

    current_page = paginator.page(int(page))

    context = {
        'title': 'Каталог',
        'category': category,
        'categories': categories,
        'content': content,
        'products': current_page
    }
    return render(request, 'goods/catalog.html', context)



def product(request, id, slug):

    content = Content.objects.first()

    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    category = product.category
    products_similar = Product.objects.filter(category=category, available=True)
    products_similar_num = products_similar[0:3]
    context = {
        'title': 'Продукт',
        'product': product,
        'products_similar': products_similar_num,
        'category': category,
        'content': content,
        'cart_product_form': cart_product_form,
    }
    return render(request, 'goods/product.html', context)