sayilar=[]
for i in range(1,6):
    sayi=int(input("Sayı giriniz: "))
    sayilar.append(sayi)
for i in range(len(sayilar)):
    for a in range(i+1,len(sayilar)):
        if sayilar[i]>= sayilar[a]:
            sayilar[i],sayilar[a]=sayilar[a],sayilar[i]
print(sayilar)
    