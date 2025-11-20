from django.shortcuts import render
from app_lab3 import views
from django.http import HttpResponse
from django.shortcuts import render
from django import template

def home(request):
    return render(request, 'templates/index.html')
    
def hello(request):
    return HttpResponse(u'Привет, Мир!', content_type="text/plain; charset=utf-8")

def static_handler(request):
    return render(request, 'static_handler.html')
# Create your views here.
