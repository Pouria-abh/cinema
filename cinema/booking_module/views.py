from django.shortcuts import render
from booking_module.models import Movie , Gener
from django.views.generic import ListView 
# Create your views here.



class MovieListPage(ListView):
    model = Movie
    template_name = 'booking_module/movie_list_page.html'
    queryset=Movie.objects.filter(is_active=True)
    
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['geners']=Gener.objects.filter(movie__isnull=False).distinct()
        
        return context
    
    def get_queryset(self):
        query =super().get_queryset()
        gener_name=self.kwargs.get('gener')
        if gener_name is not None:
            query=query.filter(gener__url_title=gener_name)
            
        
        
        return query
    