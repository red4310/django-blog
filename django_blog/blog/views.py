from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return HttpResponse('Blog Home')

def about(request):
    return HttpResponse('About Page')
