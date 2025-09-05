from django.urls import path
from . import views


urlpatterns=[
    path('',views.MovieListPage.as_view(),name='movie_list_page'),
    path('gener/<gener>',views.MovieListPage.as_view(),name='movie_list_by_gener')
]