from django.http import HttpRequest
from django.shortcuts import render , redirect
from django.urls import reverse
from django.views.generic import CreateView , View
from .forms import loginForm , RegisterModelForm
from .models import User
from django.contrib.auth import login ,logout

# Create your views here.


class Login_page(View):
    def get(self,request:HttpRequest):
        login_form=loginForm()
        context={'login_form':login_form}
        return render(request,'account_module/login_page.html',context)
    
    def post(self,request:HttpRequest):
        login_form=loginForm(request.POST)
        if login_form.is_valid():
           user_name=login_form.cleaned_data.get('user_name')
           user_pass=login_form.cleaned_data.get('password')
           user :User=User.objects.filter(username__iexact=user_name).first()
           if user is not  None:
               if user.check_password(user_pass):
                   print('true')
                   login(request,user)
                   return redirect(reverse('home_page'))
               else:
                   login_form.add_error('password','نام کاربری یا رمز عبور اشتباه است')
           else:
              login_form.add_error('password','نام کاربری یا رمز عبور اشتباه است')
                       
                   
            
        context={'login_form':login_form}
        return render(request,'account_module/login_page.html',context)
    

class Register_page(View):
    def get(self,request):
        register_form=RegisterModelForm()
        context={'register_form':register_form}
        return render(request,'account_module/register_page.html',context)
    
    def post(self,request):
        register_form=RegisterModelForm(request.POST)
        if register_form.is_valid():
            user_name=register_form.cleaned_data.get('user_name')
            user_pass=register_form.cleaned_data.get('password')
            user :bool=User.objects.filter(username__iexact=user_name).exists()
            if user:
                register_form.add_error('user_name','نام کاربری وجود دارد')
            else :
                new_user=User(username=user_name)
                new_user.set_password(user_pass)
                new_user.save()
                return redirect(reverse('login_page'))
            
               
                    
        context={'register_form':register_form}
        return render(request,'account_module/register_page.html',context)
        
class Logout_page(View):
    def get(self,requset:HttpRequest):
        logout(requset)
        return redirect(reverse('login_page'))
                