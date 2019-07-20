from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # with open(r'z:\tek\dat_md\MD_RW1.TEK', 'r', encoding="windows-1252")as f:
    with open('/home/meteoaza/github/django/MD_RW1.TEK', 'r', encoding="windows-1252")as f:
        l = f.read().split(';')
    context = {'temp': l[27][2:], 'pres': l[24][2:], 'hum': l[28][2:], 'wind1': l[38][2:-2], 'wind2': l[39][2:],}
    return render(request, 'meteo/homePage.html', context)

def sens(request):
    try:
        with open(r'c:\Users\Meteoaza\github\django\MD_RW1.TEK', 'r', encoding="windows-1252")as f:
            l = f.read().split(';')
        context = {'temp': l[27][2:], 'pres': l[24][2:], 'hum': l[28][2:]}
    except:
        context = {'temp': '----', 'pres': '----', 'hum': '----'}
    return render(request, 'meteo/sens.html', context)

def news(request):
    return render(request, 'meteo/news.html')

def docs(request):
    return render(request, 'meteo/docs.html')

def sin(request):
    return render(request, 'meteo/sin.html')

def about(request):
    return render(request, 'meteo/about.html')
