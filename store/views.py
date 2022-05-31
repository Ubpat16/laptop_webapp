from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView

from .models import Laptop, Order, OrderItem


# Create your views here.


class HomeView(ListView):
  context_object_name = 'list_of_laptops'
  template_name = 'store/index.html'
  
  def get_queryset(self):
    return Laptop.objects.all()
    
class ProductView(DetailView):
  model = Laptop
  template_name = 'store/product.html'
  
class NewProductView(CreateView):
  model = Laptop
  template_name = 'store/new_product.html'
  fields = '__all__'
  