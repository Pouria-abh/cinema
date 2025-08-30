from django.urls import path
from . import views
urlpatterns=[
    path('',views.index_page.as_view(),name='home_page'),
    path('content/<slug:slug>/',views.MovieDetailview.as_view(),name='detail_page'),
    
]