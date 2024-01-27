def temizle(metin): #Bu metin ingizlice bağlaçları, parantezleri, yanlış yerde büyük harf kullanımlarını düzeltir.
    baglac = ["and","was","is","for","as","nor","but","yet","a","has"]
    kelimeler=metin.lower().split() 
    kelimeler=[kelime for kelime in kelimeler if kelime.lower() not in baglac]
    yeni=' '.join(kelimeler)
    
    noktali=""
    onceki=""
    bharf=True
    for harf in yeni:
        if harf==' ' and onceki==' ':
            continue
        if harf=='.' or harf=='!' or harf=='?':
            bharf=True
            noktali+=harf
        elif bharf and harf.isalpha():
            noktali+=harf.upper()
            bharf=False
        else: 
            noktali+=harf
            onceki=harf
    
    
    smetin=""
    aparantez=False
    for harf in noktali:
        if harf=='[' or harf=='(': 
            aparantez=True
        elif harf==']' or harf==')':
            aparantez=False
        elif not aparantez:
            smetin+=harf
    print(smetin)

metin="""WikiLeaks (/ˈwɪkiliːks/) is a media organisation and publisher founded in 2006. 
It operates as a non-profit and is funded by donations[13] and media partnerships. 
It has published classified documents and other media provided by anonymous sources.
[14] It was founded by Julian Assange, an Australian editor, publisher, and activist, who is currently challenging extradition to the United States over his work with WikiLeaks.
[15] Since September 2018, Kristinn Hrafnsson has served as its editor-in-chief.
[16][17] Its website states that it has released more than ten million documents and associated analyses.
[18] WikiLeaks' most recent publication was in 2021, and its most recent publication of original documents was in 2019.
[19] Beginning in November 2022, many of the documents on the organisation's website could not be accessed.[19][20][21][22] """
temizle(metin)
    