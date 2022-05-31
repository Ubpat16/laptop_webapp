from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, TemplateView

from .models import Laptop, Order, OrderItem


# Create your views here.


class HomeView(ListView):
    context_object_name = 'list_of_laptops'
    template_name = 'shop.html'

    def get_queryset(self):
        return Laptop.objects.all()


class ProductView(TemplateView):
    model = Laptop
    template_name = 'product.html'


class NewProductView(CreateView):
    model = Laptop
    template_name = 'new_product.html'
    fields = '__all__'


class CartPageView(TemplateView):
    template_name = 'cart.html'


class CheckoutPageView(TemplateView):
    template_name = 'checkout.html'
