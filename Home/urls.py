from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('shop', views.shop, name='shop'),
    path('productdetails', views.productdetails, name='product_details'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('shop', views.shop, name='shop'),
    path('checkout', views.checkout, name='checkout'),
    path('cart', views.cart, name='cart'),
]
