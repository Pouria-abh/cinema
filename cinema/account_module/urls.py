from django.urls import path
from . import views
urlpatterns=[
    path('login',views.Login_page.as_view(),name='login_page'),
    path('logout',views.Logout_page.as_view(),name='logout_page'),
    path('register',views.Register_page.as_view(),name='register_page')
]