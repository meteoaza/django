from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def index(request):
    return render(request, 'mainPage/homePage.html')

def sens(request):
    t = datetime.now()
    with open(r'C:\Users\Meteoaza\github\maint\Sens\Sens.dat', 'r', encoding='utf-8')as f:
        l = f.read().split(',')
    context = {'time': t, 'lt1': l[0][2:-1], 'lt2': l[1][2:-1], 'lt3': l[2][2:-1],
               'lt4': l[3][2:-1], 'lt5': l[4][2:-1], 'lt6': l[5][2:-1], 'cl1': l[6][2:-1],
               'cl2': l[7][2:-1], 'cl3': l[8][2:-1], 'cl4': l[9][2:-1], 'wt1': l[10][2:-1],
               'wt2': l[11][2:-1], 'wt3': l[12][2:-1], 'wt4': l[13][2:-1], 'wt5': l[14][2:-1],
               'wt6': l[14][2:-1]}
    return render(request, 'mainPage/sens.html', context)

def report(request):
    l = [line.strip('\n') for line in open(r'd:\IRAM\MAINT\LOGs\maintReport.txt', 'r', encoding='utf-8')]
    context = {'report': l}
    return render(request, 'report/report.html', context)

def log(request):
    l = [line.strip('\n') for line in open(r'd:\IRAM\MAINT\LOGs\maintLog.txt', 'r', encoding='utf-8')]
    context = {'log': l}
    return render(request, 'report/log.html', context)
def clear_log(request):
    with open(r'd:\IRAM\MAINT\LOGs\\maintLog.txt', 'w')as f:
        f.write('')
    return render(request, 'report/log.html')
def clear_rep(request):
    with open(r'd:\IRAM\MAINT\LOGs\\maintReport.txt', 'w')as f:
        f.write('')
    return render(request, 'report/report.html')
