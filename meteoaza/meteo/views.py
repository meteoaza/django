from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {'title': 'Meteo-Manas'}
    return render(request, 'meteo/index.html', context)

def docs(request):
    context = {'title': 'Meteo-Docs'}
    return render(request, 'meteo/docs.html', context)

def sin(request):
    context = {'title': 'Meteo-Sinoptic'}
    return render(request, 'meteo/sin.html', context)

def about(request):
    context = {'title': 'Meteo-About'}
    return render(request, 'meteo/about.html', context)
