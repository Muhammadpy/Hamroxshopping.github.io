
from re import template
from django.shortcuts import render
from django.views import View 
from .models import *
from django.views.generic import  DetailView, CreateView
# Create your views here.


class HomeView(View):
    def get(self, request):
        big_banner = Banner.objects.filter(banner_type='Big').order_by('-id')[:3]
        small_banners = Banner.objects.filter(banner_type='Small').order_by('-id')[:3]
        products = Product.objects.all().order_by('views')
        
        contest = {"big_banner":big_banner,"small_banners":small_banners}
        contest['products'] = products
        return render(request, "index.html",contest)

class ProductDetail(DetailView):
    model = Product
    template_name = "detail.html"
