from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'mainPage/homePage.html')

def report(request):
    l = [line.strip('\n') for line in open(r'd:\IRAM\MAINT\LOGs\maintReport.txt', 'r', encoding='utf-8')]
    context = {'report': l}
    return render(request, 'report/report.html', context)

def log(request):
    l = [line.strip('\n') for line in open(r'd:\IRAM\MAINT\LOGs\maintLog.txt', 'r', encoding='utf-8')]
    context = {'log': l}
    return render(request, 'report/log.html', context)
