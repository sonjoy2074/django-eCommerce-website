from django.shortcuts import render
from App_Shop.models import Product
#Import views
from django.views.generic import ListView, DetailView
# Create your views here.

class Home(ListView):
    model = Product
    template_name = 'App_Shop/home.html'