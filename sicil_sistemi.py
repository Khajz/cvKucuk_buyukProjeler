def kkontrol(kadi):
    skadi=kadi.strip(" ")        
    if skadi.lower()=='mustafa':
        return True
    else:
        return False
def skontrol(pswrd):
    if pswrd.lower()=='aca13':
        return True
    else:
        return False
def sicilvebastir(girishak):
    print("Giriş başarılı!")
    print(f"{girishak}. Hakkınızda girdiniz!")
    sicil=[]
    adlar=[]
    maaslar=[]
    for i in range(3):
        sira=i+1
        sicilno=input(f"{sira}. Kişinin sicilnosunu girin!: ")
        sicil.append(sicilno.upper())
        ad=input(f"{sira}. Kişinin ismini ve soyismini girin!: ")
        adlar.append(ad.capitalize())
        maas=input(f"{sira}. Kişinin maaşını giriniz!: ")
        maaslar.append(maas)
    print(sicil)
    secim=input("Kimin Sicilini görmek istiyorsun?: ")
    ysecim=secim.upper()
    while True:
        if ysecim not in sicil:
            ysecim=input("Yanlış girdiniz, tekrar deneyin!: ")
        else: break
    x=sicil.index(ysecim)
    print(f"Sicil no: {sicil[int(x)]}")
    print(f"İsim: {adlar[int(x)]}")
    print(f"Maaşı: {maaslar[int(x)]}")
    input()
kadi=input("Kullanıcı adını gir!: ")
while kkontrol(kadi)==False:
    kadi=input("Kullanıcı adını yanlış girdin tekrar gir!: ")
pswrd=input("Şifreni gir!: ")
girishak=0
for i in range(1,5):
    if skontrol(pswrd)==False:
        print("Giriş başarısız!")
        pswrd=input(f"Şifreni yanlış girdin tekrar gir! Kalan hak {4-i}: ")
        girishak=girishak+i
    if i==3 and skontrol(pswrd)==False:
        print("Giriş başarısız, hakkınız bitti sistem kapanıyor!")
        input()
girishak=girishak+1
if skontrol(pswrd)==True:
    sicilvebastir(girishak)