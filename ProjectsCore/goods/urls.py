
from django.urls import path
from goods import views

app_name = 'goods'

urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('<slug:category_slug>/', views.catalog, name='catalog_category'),
    path('<int:id>/<slug:slug>/', views.product, name='product'),
]
