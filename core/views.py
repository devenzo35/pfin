from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic.base import TemplateView
# Create your views here.

class MyView(View):
    template_name="home.html"
    def get(self, request, *args, **kargs):
        return None
    
class HomePageView(TemplateView):
     template_name="home.html"
     