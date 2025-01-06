from django.shortcuts import render
from App_Shop.models import Product
#Import views
from django.views.generic import ListView, DetailView
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin

class Home(ListView):
    model = Product
    template_name = 'App_Shop/home.html'


class ProductDetail(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'App_Shop/product_detail.html'