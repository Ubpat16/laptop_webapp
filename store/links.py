from django.urls import path
from .views import HomeView, ProductView, NewProductView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('product/<int:pk>/', ProductView.as_view(), name="product"),
    path('add', NewProductView.as_view(), name='add'),
  ]