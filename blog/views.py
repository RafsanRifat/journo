from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def home_view(request):
    return render(request, 'blog/home.html')
