from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.

class index_page(TemplateView):
    template_name='home_module/index_page.html'
    