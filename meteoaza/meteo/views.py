from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'meteo/homePage.html')

def sens(request):
    with open(r'Z:\TEK\DAT_MD\MD_RW1.TEK', 'r', encoding='ANSI')as f:
        l = f.read().split(';')
    context = {'md1': l[12][2:], 'md2': l[47][2:]}
    return render(request, 'meteo/sens.html', context)

def news(request):
    return render(request, 'meteo/news.html')

def docs(request):
    return render(request, 'meteo/docs.html')

def about(request):
    return render (request, 'meteo/about.html')
