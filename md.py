with open(r'z:\tek\DAT_MD\MD_RW1.TEK', 'r', encoding='ANSI')as f:
    r = f.read().split(';')
i = len(r)
with open(r'c:\Users\Meteoaza\github\md.txt', 'a', encoding='ANSI')as f:
    for i in r:
        print(i[3:])
        f.write(i + '\n')
