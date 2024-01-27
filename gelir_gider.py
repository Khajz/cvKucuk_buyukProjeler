fatura_giderleri=0
kira_giderleri=0
market_giderleri=0
eglence_giderleri=0
diger_giderler=0
kalan=0

para = 0
para = int(input("Gelirinizi yazınız:  "))


while True:
    x = int(input("""
              Gider Girin
              1.Faturalar
              2.Kira
              3.Market Giderleri
              4.Eğlence
              5.Diğer
              1/2/3/4/5 seçim yapın:  """))

    while x!=1 and x!=2 and x!=3 and x!=4 and x!=5:
        x = int(input("Yanlış değer girdiniz, 1 ile 5 arasında bir değer giriniz:  "))
    
    if x==1:
        fatura_giderleri = int(input("Fatura giderinizi yazınız:  "))
        kalan = para - fatura_giderleri
        if kalan>0: print(f"{kalan} paranız kaldı, gider girmeye devam edebilirsiniz")
        else:
            kalan<=0
            print(f"Paranız kalmadığı için ({kalan}) gider girmeniz sonlanmıştır")
            break
    elif x==2:
        kira_giderleri= int(input("Kira Giderinizi girin:  "))
        kalan = para - kira_giderleri
        if kalan>0: print(f"{kalan} paranız kaldı, gider girmeye devam edebilirsiniz")
        else:
            kalan<=0
            print(f"Paranız kalmadığı için ({kalan}) gider girmeniz sonlanmıştır")
            break
    elif x==3:
        market_giderleri = int(input("Market Giderinizi girin:  "))
        kalan = para - market_giderleri
        if kalan>0: print(f"{kalan} paranız kaldı, gider girmeye devam edebilirsiniz")
        else:
            kalan<=0
            print(f"Paranız kalmadığı için ({kalan}) gider girmeniz sonlanmıştır")
            break
    elif x==4:
        eglence_giderleri = int(input("Eğlence masrafınızı giriniz:  "))
        kalan = para - eglence_giderleri
        if kalan>0: print(f"{kalan} paranız kaldı, gider girmeye devam edebilirsiniz")
        else:
            kalan<=0
            print(f"Paranız kalmadığı için ({kalan}) gider girmeniz sonlanmıştır")
            break
    elif x==5:
        diger_giderler = int(input("Diğer giderlerinizi giriniz:  "))
        kalan = para - diger_giderler
        if kalan>0: print(f"{kalan} paranız kaldı, gider girmeye devam edebilirsiniz")
        else:
            kalan<=0
            print(f"Paranız kalmadığı için ({kalan}) gider girmeniz sonlanmıştır")
            break
    para = kalan
    y = input("Başka bir gider girmek ister misiniz? (E/H)")
    if y =='H':
        break
