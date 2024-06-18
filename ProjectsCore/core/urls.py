
from django.contrib import admin
from django.urls import path,include
from core.admin import admin_site

# Для медеа файлов
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin_site.urls),
    path('cart/', include('cart.urls', namespace='cart')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('product', include('goods.urls', namespace='goods')),
    path('', include('main.urls', namespace='main')),
]


# Для медеа файлов
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)


