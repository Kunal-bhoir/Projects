from django.shortcuts import render
from django.http import HttpResponse


def home(requests):
    return render(requests, 'basic/index.html')

def report(requests):
    return render(requests, 'basic/report.html')
# Create your views here.
