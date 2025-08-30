from django.shortcuts import render
from django.views.generic.base import TemplateView
from booking_module.models import Movie , ShowTimes
from django.views.generic import ListView , DetailView
from django.http import HttpResponse
# Create your views here.

class index_page(ListView):
    model = Movie
    template_name = 'home_module/index_page.html'
    queryset=Movie.objects.filter(is_active=True)
    
    
    
class MovieDetailview(DetailView):
    template_name='home_module/detail_page.html'
    model = Movie
    queryset=Movie.objects.filter(is_active=True)
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['showtimes']=ShowTimes.objects.filter(movie=self.object).order_by('time')
        
        return context
    
    
    
    
    
def header_partial(request):
    return render(request,'shared/header_partial.html')    


def footer_partial(request):
    return render(request,'shared/footer_partial.html')    


