kalan =0
toplam=0
para = 0
manav = ["Elma=100TL", "Armut=120TL", "Patates=150TL"]
Elma=[]
Armut=[]
Patates=[]

print (manav)
manav = input("Sebze Seçiniz:   ")
while manav != "Elma" and manav !="Patates" and manav!="Armut":
        manav = input("Sebzeyi yanlış girdiniz:     ")
kilo = int(input("Kaç Kilo Alacasın:    "))
para = int(input("Paranızı Giriniz:  "))

while True:
    if manav == "Elma":
        toplam=kilo*100
        kalan = para - toplam
        if kalan>=0:
            Elma.append(kilo)
    elif manav == "Armut":
        toplam=kilo*120
        kalan = para - toplam
        if kalan>=0:
            Armut.append(kilo)
    elif manav == "Patates":  
        toplam=kilo*150
        kalan = para - toplam
        if kalan>=0:
            Patates.append(kilo)
    else: input("Sebze ismini doğru giriniz:    ")
    para = kalan
    if kalan>100:
        print(f"{kalan} TL paranız kaldı, alışverişe devam edebilirsiniz")
    elif kalan<100:
        print(f"Kalan paranızla ({kalan}TL) başka meyve alamayacağınız için alışverişiniz sonlandı")
        print(f"{sum(Elma)} kg elma aldın")
        print(f"{sum(Armut)} kg armut aldın")
        print(f"{sum(Patates)} kg patates aldın")
        break
    else :  
        print("Paranız bittiği için alışverişiniz sonlandı")
        print(f"{sum(Elma)} kg elma aldın")
        print(f"{sum(Armut)} kg armut aldın")
        print(f"{sum(Patates)} kg patates aldın")
        break
    manav = input("Sebze Seçiniz:   ")
    kilo = int(input("Kaç Kilo Alacasın:    "))
input("Çıkmak için bir tuşa basınız")