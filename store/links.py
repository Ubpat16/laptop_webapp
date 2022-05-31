from django.urls import path
from .views import HomeView, ProductView, NewProductView, CartPageView, CheckoutPageView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('product/', ProductView.as_view(), name="product"),
    path('new', NewProductView.as_view(), name='new_product'),
    path('cart', CartPageView.as_view(), name='cart'),
    path('checkout', CheckoutPageView.as_view(), name='checkout'),
  ]