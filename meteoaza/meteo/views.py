from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    with open('/home/meteoaza/github/django/MD_RW1.TEK', 'r', encoding="windows-1252")as f:
        l = f.read().split(';')
    context = {'temp': l[27][2:], 'pres': l[24][2:], 'hum': l[28][2:]}
    return render(request, 'meteo/homePage.html', context)

def sens(request):
    with open('/home/meteoaza/github/django/MD_RW1.TEK', 'r', encoding="windows-1252")as f:
        l = f.read().split(';')
    context = {'md1': l[12][2:], 'md2': l[47][2:]}
    return render(request, 'meteo/sens.html', context)

def news(request):
    return render(request, 'meteo/news.html')

def docs(request):
    return render(request, 'meteo/docs.html')

def sin(request):
    return render(request, 'meteo/sin.html')

def about(request):
    return render(request, 'meteo/about.html')
