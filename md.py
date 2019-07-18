with open('/home/meteoaza/github/django/MD_RW1.TEK', 'r', encoding='windows-1252')as f:
    r = f.read().split(';')
i = len(r)
i = int(i)
with open('/home/meteoaza/github/django/md.txt', 'w', encoding='windows-1252')as f:
    for n in range(i):
        print(r[n])
        f.write(r[n] + '\n')
