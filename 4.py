
sayac = 0
for i in range(100, 999):
    a = int(i / 100)
    b = int(i % 100/10)
    c = int(i % 10)

    if (a!=b and a!=c and b!=c):
        print(str(a) +  str(b) + str(c))
        sayac = sayac +1
print(str(sayac) + " adet sayı var.")