from django.shortcuts import render
from django.views.generic import ListView
from .models import Restaurant

# Create your views here.
class RestaurantListView(ListView):
  model=Restaurant
  template_name = "restaurant_list.html"