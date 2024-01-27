def temizleme(metin): #Bu fonksiyon tekrar eden özel simgeleri, boşlukları, yanlış yerde olan büyük harfleri temizler
    # tekrarsiz=""
    # onceki_karakter=""
    # for karakter in metin:
    #     if karakter!=onceki_karakter:
    #         tekrarsiz+=karakter
    #         onceki_karakter=karakter
    tekrarsiz=""
    onceki_karakter=""
    
    for karakter in metin:
        if karakter=='.' and onceki_karakter=='.':
            continue
        elif karakter==',' and onceki_karakter==',':
            continue
        elif karakter=='?' and onceki_karakter=='?':
            continue
        elif karakter=='!' and onceki_karakter=='!':
            continue
        elif karakter=="'" and onceki_karakter=="'":
            continue
        elif karakter==":" and onceki_karakter==":":
            continue
        elif karakter==";" and onceki_karakter==";":
            continue
        elif karakter==' ' and onceki_karakter==' ':
            continue
        elif karakter=='$' and onceki_karakter=='$':
            continue
        elif karakter=='#' and onceki_karakter=='#':
            continue
        else:
           tekrarsiz+=karakter
        
        onceki_karakter=karakter    
    
    
    duzenli=tekrarsiz.lower() and tekrarsiz.capitalize()
    
    sonuc=""
    bharf=True
    
    for karakter in duzenli:
        if karakter=='.' or karakter=='?' or karakter=='!':
            bharf=True
            sonuc+=karakter
        elif bharf and karakter.isalpha():
            sonuc+=karakter.upper()
            bharf=False
        else: sonuc+=karakter
    return sonuc
            
metinler="beren saatmiş.            ben de,,,,,,,,,,,,,,,, allık:....... #####kafeketifi "
yeni=temizleme(metinler)
print(yeni)