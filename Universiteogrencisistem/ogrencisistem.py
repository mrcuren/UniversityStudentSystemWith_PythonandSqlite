import sqlite3 as sql


def t_add():
    baglan=sql.connect("meric.db")
    cursor=baglan.cursor()
    uogrno =input("Notuna artı puan eklemek istediğiniz ogrencinin numara: ")
    dersad=input("Notuna artı puan eklemek istediğiniz degerlendirmeyi yazınız (Vize,Final,Odev1,Odev2,Kısasınav1,kısasınav2,proje) :").lower()
    unot=input(f" Eklemek istediğiniz  {dersad} puanını giriniz: ")

    if(dersad=="vize"):
        ubaglantı="""UPDATE SCHOLLSYSTEM SET vize = ?+vize  WHERE ogrencino = ?"""
        cursor.execute(ubaglantı,(unot,uogrno))
        print("Ek puan eklendi! ")
        baglan.commit()
        baglan.close()
    
    if(dersad=="final"):
        ubaglantı="""UPDATE SCHOLLSYSTEM SET final = ?+final  WHERE ogrencino = ?"""
        cursor.execute(ubaglantı,(unot,uogrno))
        print("Ek puan eklendi! ")
        baglan.commit()
        baglan.close()
    if(dersad=="odev1"):
        ubaglantı="""UPDATE SCHOLLSYSTEM SET odev1 = ?+odev1  WHERE ogrencino = ?"""
        cursor.execute(ubaglantı,(unot,uogrno))
        print("Ek puan eklendi! ")
        baglan.commit()
        baglan.close()

    if(dersad=="odev2"):
        ubaglantı="""UPDATE SCHOLLSYSTEM SET odev2 = ?+odev2  WHERE ogrencino = ?"""
        cursor.execute(ubaglantı,(unot,uogrno))
        print("Ek puan eklendi! ")
        baglan.commit()
        baglan.close()
    if(dersad=="kısasınav1"):
        ubaglantı="""UPDATE SCHOLLSYSTEM SET kısas1 = ?+kısas1  WHERE ogrencino = ?"""
        cursor.execute(ubaglantı,(unot,uogrno))
        print("Ek puan eklendi! ")
        baglan.commit()
        baglan.close()
    if(dersad=="kısasınav2"):
        ubaglantı="""UPDATE SCHOLLSYSTEM SET kısas2 = ?+kısas2  WHERE ogrencino = ?"""
        cursor.execute(ubaglantı,(unot,uogrno))
        print("Ek puan eklendi! ")
        baglan.commit()
        baglan.close()
    if(dersad=="proje"):
        ubaglantı="""UPDATE SCHOLLSYSTEM SET proje = ?+proje  WHERE ogrencino = ?"""
        cursor.execute(ubaglantı,(unot,uogrno))
        print("Ek puan eklendi! ")
        baglan.commit()
        baglan.close()
def t_delete():
    baglan=sql.connect("meric.db")
    cursor=baglan.cursor()
    uogrno =input("Notunu sileceğiniz  ogrencinin numara: ")
    dersad=input("Hangi degerlendirme notunu sileceksiniz (Vize,Final,Odev1,Odev2,Kısasınav1,kısasınav2,proje) :").lower()
    unot=0
    if(dersad=="vize"):
        ubaglantı="""UPDATE SCHOLLSYSTEM SET vize = ?  WHERE ogrencino = ?"""
        cursor.execute(ubaglantı,(unot,uogrno))
        print("Not silindi! ")
        baglan.commit()
        baglan.close()
    
    if(dersad=="final"):
        ubaglantı="""UPDATE SCHOLLSYSTEM SET final = ?  WHERE ogrencino = ?"""
        cursor.execute(ubaglantı,(unot,uogrno))
        print("Not silindi! ")
        baglan.commit()
        baglan.close()
    if(dersad=="odev1"):
        ubaglantı="""UPDATE SCHOLLSYSTEM SET odev1 = ?  WHERE ogrencino = ?"""
        cursor.execute(ubaglantı,(unot,uogrno))
        print("Not silindi! ")
        baglan.commit()
        baglan.close()

    if(dersad=="odev2"):
        ubaglantı="""UPDATE SCHOLLSYSTEM SET odev2 = ?  WHERE ogrencino = ?"""
        cursor.execute(ubaglantı,(unot,uogrno))
        print("Not silindi! ")
        baglan.commit()
        baglan.close()
    if(dersad=="kısasınav1"):
        ubaglantı="""UPDATE SCHOLLSYSTEM SET kısas1 = ?  WHERE ogrencino = ?"""
        cursor.execute(ubaglantı,(unot,uogrno))
        print("Not silindi! ")
        baglan.commit()
        baglan.close()
    if(dersad=="kısasınav2"):
        ubaglantı="""UPDATE SCHOLLSYSTEM SET kısas2 = ?  WHERE ogrencino = ?"""
        cursor.execute(ubaglantı,(unot,uogrno))
        print("Not silindi! ")
        baglan.commit()
        baglan.close()
    if(dersad=="proje"):
        ubaglantı="""UPDATE SCHOLLSYSTEM SET proje = ?  WHERE ogrencino = ?"""
        cursor.execute(ubaglantı,(unot,uogrno))
        print("Not silindi! ")
        baglan.commit()
        baglan.close()
def t_view_no():
    baglan=sql.connect("meric.db")
    cursor=baglan.cursor()
    ogrnoa=input("Listelemek istediğiniz ogrenci no : ")
    ubaglantı="""SELECT * from SCHOLLSYSTEM WHERE ogrencino = ?"""
    cursor.execute(ubaglantı,(ogrnoa,))
    liste_ekle=cursor.fetchall()
    for i in liste_ekle:
        print(i)

def t_view_ders():
    baglan=sql.connect("meric.db")
    cursor=baglan.cursor()
    dersa=input("Listelemek istediğiniz ders adı : ")
    ubaglantı="""SELECT * from SCHOLLSYSTEM WHERE dersad = ?"""
    cursor.execute(ubaglantı,(dersa,))
    liste_ekle=cursor.fetchall()
    for i in liste_ekle:
        print(i)

def t_view_bolum():
    baglan=sql.connect("meric.db")
    cursor=baglan.cursor()
    boluma=input("Listelemek istediğiniz bölüm adı : ")
    ubaglantı="""SELECT * from SCHOLLSYSTEM WHERE bolumad = ?"""
    cursor.execute(ubaglantı,(boluma,))
    liste_ekle=cursor.fetchall()
    for i in liste_ekle:
        print(i)

def t_view():
    baglan=sql.connect("meric.db")
    cursor=baglan.cursor()
    print("""
    1-Bölüme göre listeleme
    2-Derse göre listeleme
    3-Numaraya göre listeleme
    """)
    tsecim =int(input("Neyi listelemek istiyorsunuz?"))
    if(tsecim==1):
        t_view_bolum()
    if(tsecim==2):
        t_view_ders()
    if(tsecim==3):
        t_view_no()
    

def transactions():
    print("""
     DİĞER İŞLEMLER
     ----------

    1-Derse ek puan ekleme
    2-Not silme 
    3-Öğrenci bilgilerini görüntüleme 
     
    """)
    secim=int(input("Lütfen belirlenen rakamlara göre seçim yapınız."))
    if(secim==1):
        t_add()
    if secim==2:
        t_delete()
    if secim==3:
        t_view()





def add():
    print("""
    KAYIT EKLEME MENÜSÜ
    -----------------

    """)
    baglanti=sql.connect("meric.db")
    cursor=baglanti.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS SCHOLLSYSTEM(bolumad TEXT,dersad TEXT,ogrenci TEXT,ogrencino INT,vize INT,final INT,kısas1 TEXT,kısas2 TEXT,odev1 INT,odev2 INT,proje INT,ortalama INT,harfnot TEXT)")

    bolümad=input("Bölüm adi giriniz: ")
    liste=[]    
    adetders=int(input("Kaç adet öğrenci gireceksiniz: "))
    if(adetders>=5 and adetders <= 20):
        ders=input("Ders adını giriniz:")

        for i in range(adetders):   
    
            ograd=input("Öğrenci adını girin: ")
            ogrno=int(input("Öğrencinin numarasını giriniz: "))
            dersvize=int(input(f"{ders} dersinin ara sınav(Vize) notunu giriniz: "))
            dersk1=int(input(f"{ders} dersinin 1. kısa sınav notunu giriniz: "))
            dersk2=int(input(f"{ders} dersinin 2. kısa sınav notunu giriniz: "))
            derso1=int(input(f"{ders} dersinin 1.odev notunu giriniz: "))
            derso2=int(input(f"{ders} dersinin 2. odev notunu giriniz: "))
            dersf=int(input(f"{ders} dersinin final notunu giriniz: "))
            dersp=int(input(f"{ders} dersinin proje notunu giriniz: "))
            ortalama=(((dersvize*22.5)/100)+((derso1*3.375)/100)+((derso2*3.375)/100)+((dersk1*3.375)/100)+((dersk2*3.375)/100)+((dersp*9)/100)+((dersf*55)/100))
            
            if ortalama>=90 and ortalama<=100:
                harf = "AA"
            elif ortalama>=85 and ortalama<=89:
                harf = "BA"
            elif ortalama>=80 and ortalama<=84:
                harf = "BB"
            elif ortalama>=75 and ortalama<=79:
                harf = "CB"
            elif ortalama>=70 and ortalama<=74:
                harf = "CC"
            elif ortalama>=65 and ortalama<=69:
                harf = "DC"
            elif ortalama>=60 and ortalama<=64:
                harf = "DD"
            elif ortalama>=50 and ortalama<=59:
                harf = "FD"
            elif ortalama<50:
                harf = "FF"

            ekle=[bolümad,ders,ograd,ogrno,dersvize,dersf,dersk1,dersk2,derso1,derso2,dersp,ortalama,harf]
            liste.append(ekle)

        print(liste)
        asd=tuple(liste)

        add_command= """INSERT INTO SCHOLLSYSTEM VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)"""
        cursor.executemany(add_command,asd)
        print("Eklendi")
        baglanti.commit()
        baglanti.close()
    else:
        print("Belirlediğiniz aralıkta öğrenci seçemezsiniz! ")


    
def ogrnot_update():
    baglan=sql.connect("meric.db")
    cursor=baglan.cursor()
    uogrno =input("Notunu güncellemek istediğiniz ogrencinin numara: ")
    dersad=input("Güncellemek istediğiniz degerlendirmeyi yazınız (Vize,Final,Odev1,Odev2,Kısasınav1,kısasınav2,proje) :").lower()
    unot=input(f" Yeni {dersad} notunu giriniz: ")

    if(dersad=="vize"):
        ubaglantı="""UPDATE SCHOLLSYSTEM SET vize = ?  WHERE ogrencino = ?"""
        cursor.execute(ubaglantı,(unot,uogrno))
        print("Güncellendi! ")
        baglan.commit()
        baglan.close()
    
    if(dersad=="final"):
        ubaglantı="""UPDATE SCHOLLSYSTEM SET final = ?  WHERE ogrencino = ?"""
        cursor.execute(ubaglantı,(unot,uogrno))
        print("Güncellendi! ")
        baglan.commit()
        baglan.close()
    if(dersad=="odev1"):
        ubaglantı="""UPDATE SCHOLLSYSTEM SET odev1 = ?  WHERE ogrencino = ?"""
        cursor.execute(ubaglantı,(unot,uogrno))
        print("Güncellendi! ")
        baglan.commit()
        baglan.close()

    if(dersad=="odev2"):
        ubaglantı="""UPDATE SCHOLLSYSTEM SET odev2 = ?  WHERE ogrencino = ?"""
        cursor.execute(ubaglantı,(unot,uogrno))
        print("Güncellendi! ")
        baglan.commit()
        baglan.close()
    if(dersad=="kısasınav1"):
        ubaglantı="""UPDATE SCHOLLSYSTEM SET kısas1 = ?  WHERE ogrencino = ?"""
        cursor.execute(ubaglantı,(unot,uogrno))
        print("Güncellendi! ")
        baglan.commit()
        baglan.close()
    if(dersad=="kısasınav2"):
        ubaglantı="""UPDATE SCHOLLSYSTEM SET kısas2 = ?  WHERE ogrencino = ?"""
        cursor.execute(ubaglantı,(unot,uogrno))
        print("Güncellendi! ")
        baglan.commit()
        baglan.close()
    if(dersad=="proje"):
        ubaglantı="""UPDATE SCHOLLSYSTEM SET proje = ?  WHERE ogrencino = ?"""
        cursor.execute(ubaglantı,(unot,uogrno))
        print("Güncellendi! ")
        baglan.commit()
        baglan.close()

    
def ograd_update():
    baglan=sql.connect("meric.db")
    cursor=baglan.cursor()
    uad =input("Güncellemek istediğiniz ogrenci ad: ")
    unew_ad=input("Yeni ogrenci adı : ")
    ubaglantı="""UPDATE SCHOLLSYSTEM SET ogrenci = ?  WHERE ogrenci = ?"""
    cursor.execute(ubaglantı,(unew_ad,uad))
    print("Güncellendi! ")
    baglan.commit()
    baglan.close()
    
def ogrno_update():
    baglan=sql.connect("meric.db")
    cursor=baglan.cursor()
    unumber =input("Güncellemek istediğiniz ogrenci numarası: ")
    unew_number=input("Yeni ogrenci numarası : ")
    ubaglantı="""UPDATE SCHOLLSYSTEM SET ogrencino = ?  WHERE ogrencino = ?"""
    cursor.execute(ubaglantı,(unew_number,unumber))
    print("Güncellendi! ")
    baglan.commit()
    baglan.close()

def ders_update():
    baglan=sql.connect("meric.db")
    cursor=baglan.cursor()
    uders=input("Güncellemek istediğiniz ders ad: ")
    unew_ders=input("Yeni ders adı : ")
    ubaglantı="""UPDATE SCHOLLSYSTEM SET dersad = ?  WHERE dersad = ?"""
    cursor.execute(ubaglantı,(unew_ders,uders))
    print("Güncellendi! ")
    baglan.commit()
    baglan.close()
    
    
def update():
    
    print("""
    GÜNCELLEME MENÜSÜ
    -----------------
    1-Ders adı güncelleme
    2-Öğrenci adı güncelleme
    3-Öğrenci no güncelleme
    4-Öğrenci notlarını güncelleme
    """)
    sec= int(input("Lütfen belirtilen şekilde seçim yapınız:"))
    if sec==1:
        ders_update()
    if sec==2:
        ograd_update()
    if sec==3:
        ogrno_update()
    if sec==4:
        ogrnot_update()
    else:
        print("Lütfen geçerli bir rakamla belirtin!")

def delete():
    print("""

    KAYIT SİLME MENÜSÜ
    -----------------

    1-Öğrenci numarasına göre 
    2-Öğrenci adına göre 
    3-Ders adına göre
    4-Bölüm adına göre

    """)
    secenek=int(input("Hangi kritere göre silme işlemi yapmak istersiniz: "))

    if secenek==1:
        baglan=sql.connect("meric.db")
        cursor=baglan.cursor()
        dnumber =input("Kaydını silmek istediğiniz ogrenci no: ")
    
        dbaglantı="""DELETE from SCHOLLSYSTEM WHERE ogrencino = {}"""
        cursor.execute(dbaglantı.format(dnumber))
        print(f"{dnumber} numaralı öğrencinin kayıtları silinmiştir. ")
        baglan.commit()
        baglan.close()
    
    if secenek ==2:
        baglan=sql.connect("meric.db")
        cursor=baglan.cursor()
        dogrname =input("Kaydını silmek istediğiniz ogrenci adı: ")
    
        dabaglantı="""DELETE from SCHOLLSYSTEM WHERE ogrenci = ? """
        cursor.execute(dabaglantı,(dogrname,))
        print(f"{dogrname} adlı öğrencinin kayıtları silinmiştir. ")
        baglan.commit()
        baglan.close()
    
    if secenek == 3:
        baglan=sql.connect("meric.db")
        cursor=baglan.cursor()
        ddersad =input("Kaydını silmek istediğiniz ders adı: ")
    
        dbaglantıcommand="""DELETE from SCHOLLSYSTEM WHERE dersad = ? """
        cursor.execute(dbaglantıcommand,(ddersad,))
        print(f"{ddersad} dersinin kayıtları silinmiştir. ")
        baglan.commit()
        baglan.close()
    
    if secenek==4:
        baglan=sql.connect("meric.db")
        cursor=baglan.cursor()
        dboad =input("Kaydını silmek istediğiniz bolum: ")
    
        dbbaglantı="""DELETE from SCHOLLSYSTEM WHERE bolumad = ?"""
        cursor.execute(dbbaglantı,(dboad,))
        print(f"{dboad} dersinin kayıtları silinmiştir. ")
        baglan.commit()
        baglan.close()
    





print("""
[]===========SUBU-PY==============[]
|                                  
|     Programa Hoşgeldiniz!       |
|                                 |
[]===========SUBU-PY==============[]
""")
print("""

 ANA MENÜ 
----------

1-Ekleme İşlemleri
2-Güncelleme İşlemleri
3-Kayıt Silme İşlemleri
4- Diğer işlemler 

çıkış için ----->  0

""")
secim=int(input("Lütfen belirlenen rakamlara göre seçim yapınız."))

if(secim==1):
    add()

elif secim==2:
    update()

elif secim==3:
    delete()

elif secim==4:
    transactions()
elif secim==0:
    print("TEKRAR BEKLERİZ\n iYİ GÜNLER")
else:
    print("Lütfen doğru tercih yapınız!")


    














    
