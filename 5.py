ifade = input('ifadeyi girin :')

kod_tipi=""
sinyal = 0
cihaz = ['Televizyon', 'Çamaşır Makinesi', 'Buzdolabı', 'Fırın']
cihaz_durum = 0
cevap = 0
hata = 0

ifadeler = ifade.split("\\n")
ifadeler.pop(-1)
for ifade in ifadeler:
    veriler = ifade.split("-")
    if veriler[0] == "receive":
        if len(veriler) != 4:
            hata = 1
        else:
            kod_tipi = "receive - Gelen"      

    if veriler[0] == "send":
        veriler = ifade.split("-")
        if len(veriler) != 5:
            hata = 1
        else:
            kod_tipi = "send - Alma"

    sinyal_degeri = int(veriler[1])
    if sinyal_degeri>=0 and sinyal_degeri<=50:
        sinyal = 'Çok Zayıf'
    elif sinyal_degeri>=51 and sinyal_degeri<=100:
        sinyal = 'Zayıf'
    elif sinyal_degeri>=101 and sinyal_degeri<=150:
        sinyal = 'Orta'
    elif sinyal_degeri>=151 and sinyal_degeri<=200:
        sinyal = 'Güçlü'
    elif sinyal_degeri>=201 and sinyal_degeri<=255:
        sinyal = 'Çok Güçlü'
    else:
        hata = 2

    if veriler[2]=="0":
        cihaz_durum = "0 - Off"
    elif veriler[2]=="1":
        cihaz_durum = "1 - On"
    else:
        hata = 3

    if veriler[0]=="send":
        if veriler[3]=="0":
            cevap ='Cevap : 0 - İstenmiyor'
        elif veriler[3]=="1":
            cevap = 'Cevap : 1 - İsteniyor'
        else:
            hata = 4

    if hata==0:
        print("_" * 100)
        print('Kod Tipi : ', kod_tipi)
        print('Sinyal Gücü : ', sinyal)
        print('Cihaz : ', cihaz[int(veriler[2])-1])
        print('Durumu : ', cihaz_durum)
        if veriler[0]=="send":
            print(cevap)
        print("_" * 100)
    else: 
        print('Error : ', str(hata) + ".bölüm hatalı" )