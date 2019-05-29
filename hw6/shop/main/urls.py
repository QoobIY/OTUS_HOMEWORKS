from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('products', views.ProductsView.as_view(), name='products'),
    path('product/<int:pk>', views.ProductView.as_view(), name='product'),
    path('generate', views.generate),
]
