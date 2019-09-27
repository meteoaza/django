from datetime import datetime


def time_now(request):
    time = datetime.now().strftime('%H:%M %d-%b-%Y')
    return {'time_now': time}

def sens(request):
    try:
        # with open(r'z:\tek\dat_md\MD_RW1.TEK', 'r', encoding="windows-1252")as f:
        with open('/home/meteoaza/github/django/MD_RW1.TEK', 'r', encoding="windows-1252")as f:
            l = f.read().split(';')
            context = {'temp': l[27][2:], 'pres': l[24][2:], 'hum': l[28][2:], 'wind1': l[38][2:-2], 'wind2': l[39][2:],}
    except:
        context = {'temp': '----', 'pres': '----', 'hum': '----'}
    return (context)
