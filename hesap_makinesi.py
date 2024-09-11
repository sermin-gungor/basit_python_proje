from tkinter import *

tk = Tk()
tk.title("Hesap Makinesi") #açılacak olan pencerenin ismi
tk.geometry("500x500") #açılacak olan pencerenin büyüklüğü

#label tanımlamaları
sayi1_label = Label(text="1. sayi",font="verdana 17 bold") 
sayi1_label.place(x=50, y=10)

sayi2_label = Label(text="2. sayi",font="verdana 17 bold")
sayi2_label.place(x=50, y=50)

sonuc_label = Label(tk, text="", font="verdana 17 bold")
sonuc_label.place(x=50, y=400)

#kullanıcıdan bilgi almamı sağlayacak olan entry tanımlamaları
input1 = Entry(bg="white", fg="black", font="verdana 17 bold")
input1.place(x=150, y=11, width=60, height=30)

input2 = Entry(bg="white", fg="black", font="verdana 17 bold")
input2.place(x=150, y=51, width=60, height=30)


#yapılacak olan işlemlerin fonksiyon halinde tanımlanmaları

def toplama():
    try:
        sayi1 = int(input1.get())
        sayi2 = int(input2.get())
        sonuc = sayi1+sayi2
        sonuc_label.config(text="Toplam: " + str(sonuc)) # sonuç bilgisini label e yazdırma
        islem = f"{sayi1} + {sayi2} = {sonuc}"
        gecmis.append(islem) #yapılan işlemi geçmişe ekleme
    except ValueError:#sayı dışında veri girildiği zaman hata veriyor
        sonuc_label.config(text="Geçerli sayılar giriniz!")

def cikarma():
    try:
        sayi1 = int(input1.get())
        sayi2 = int(input2.get())
        sonuc = sayi1-sayi2
        sonuc_label.config(text="Fark: " + str(sonuc))
        islem = f"{sayi1} - {sayi2} = {sonuc}"
        gecmis.append(islem)
    except ValueError:
        sonuc_label.config(text="Geçerli sayılar giriniz!")    
    

def carpma():
    try:
        sayi1 = int(input1.get())
        sayi2 = int(input2.get())
        sonuc = sayi1*sayi2
        sonuc_label.config(text="Çarpım: " + str(sonuc))    
        islem = f"{sayi1} * {sayi2} = {sonuc}"
        gecmis.append(islem)
    except ValueError:
        sonuc_label.config(text="Geçerli sayılar giriniz!")
    

def bolme():
    try:
        sayi1 = int(input1.get())
        sayi2 = int(input2.get())
        sonuc = sayi1/sayi2
        sonuc_label.config(text="Bölüm: " + str(sonuc)) 
        islem = f"{sayi1} / {sayi2} = {sonuc}"
        gecmis.append(islem)
    except ValueError:
        sonuc_label.config(text="Geçerli sayılar giriniz!")

def us_alma():
    try:
        sayi1 = int(input1.get())
        sayi2 = int(input2.get())
        sonuc = sayi1**sayi2
        sonuc_label.config(text="Üs: " + str(sonuc))  
        islem = f"{sayi1} ** {sayi2} = {sonuc}"
        gecmis.append(islem)
    except ValueError:
        sonuc_label.config(text="Geçerli sayılar giriniz!")

def kalan_bulma():
    try:
        sayi1 = int(input1.get())
        sayi2 = int(input2.get())
        sonuc = sayi1%sayi2
        sonuc_label.config(text="Kalan: " + str(sonuc))
        islem = f"{sayi1} % {sayi2} = {sonuc}"
        gecmis.append(islem)
    except ValueError:
        sonuc_label.config(text="Geçerli sayılar giriniz!")

gecmis =[]

def gecmis_goster():
    gecmis_penceresi = Toplevel(tk) #pencere üstünde pencere açmaya yarıyor
    gecmis_penceresi.title("İşlem Geçmişi")
    gecmis_penceresi.geometry("300x200")
    
    # Geçmişi gösteren bir metin alanı
    text_area = Text(gecmis_penceresi, width=30, height=10, font="verdana 12")
    text_area.pack(pady=10)
    
    #bu for döngüsü gecmis listesinde bulunan verilerin text e alt alta eklenmesine yarıyor
    for islem in gecmis:
        text_area.insert(END, islem + "\n")


    
#fonksiyonlara erişebimemiz için gerekli olan butonlar
Button(text="Toplama", command=toplama, font="verdana 12 bold").place(x=50, y=160, width=150, height=50)
Button(text="Çıkarma", command=cikarma, font="verdana 12 bold").place(x=200, y=160, width=150, height=50)
Button(text="Çarpma", command=carpma, font="verdana 12 bold").place(x=50, y=220, width=150, height=50)
Button(text="Bölme", command=bolme, font="verdana 12 bold").place(x=200, y=220, width=150, height=50)
Button(text="Üs Alma", command=us_alma, font="verdana 12 bold").place(x=50, y=280, width=150, height=50)
Button(text="Kalan Bulma", command=kalan_bulma, font="verdana 12 bold").place(x=200, y=280, width=150, height=50)
Button(text="Geçmiş", command=gecmis_goster,font="verdana 12 bold").place(x=100,y=340,width=150, height=50)




tk.mainloop() #arayüzün çalıştırılmasını sağlıyor