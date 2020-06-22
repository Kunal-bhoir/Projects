from django.shortcuts import render 
from django.http import HttpResponse
from .models import post

def home(requests):
    context = {
        'posts' : post.objects.all()
            }
    return render(requests,'blog/home.html', context)

def about(requests):
    return render(requests,'blog/about.html', {'title': 'About'})    

# Create your views here.