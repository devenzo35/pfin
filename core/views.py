from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView  
from django.contrib.auth.models import User  
from .forms import CreateUserForm

# Create your views here.

class MyView(View):
    template_name="home.html"
    def get(self, request, *args, **kargs):
        return None
    
class HomePageView(TemplateView):
     template_name="home.html"
     
class LoginView():
    template_name = "./templates/auth/user_form.html"
   
    
def RegisterView(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            user= User.objects.create_user(username,email,password) 
            
            return redirect("home")
    else:
        form = CreateUserForm()
    
    return render(request, "registration/register.html", {'form': form})
     