from django.shortcuts import render
from django.views.generic import CreateView , View
from .forms import loginModelForm , RegisterModelForm

# Create your views here.


class Login_page(View):
    def get(self,request):
        login_form=loginModelForm()
        context={'login_form':login_form}
        return render(request,'account_module/login_page.html',context)
    
    def post(self,request):
        return render(request,'')
    

class Register_page(View):
    def get(self,request):
        register_form=RegisterModelForm()
        context={'register_form':register_form}
        return render(request,'account_module/register_page.html',context)
    
    def post(self,request):
        return render(request,'')
        