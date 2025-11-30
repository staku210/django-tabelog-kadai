from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Restaurant

# Create your views here.
class RestaurantListView(ListView):
  model=Restaurant
  template_name = "restaurant_list.html"

class RestaurantDetailView(DetailView):
  model=Restaurant
  template_name="restaurant_detail.html"