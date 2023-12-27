# print bir fonksiyondur, eger ekranda cikti almak istiyorsaniz kullanabilirsiniz.
print("Hello World!!!")

a = 3 + 2
if a == 5:
    print(a)  # kosul saglandiginda a degeri ekranda yazar.

# Yorum satiri eklemek icin # kullanilir.
# Satir sonu yorumlarda # isaretinden once 2 bosluk, sonra 1 bosluk birakilmali

"""
Yorum satirlarini 3 cift tirnak arasinda da yazabiliriz.
3 adet cift tirnak da kullanabiliriz, 3 adet tek tirnak da kullanabiliriz.
Github'a python ile ilgili kodlari atmak istersek ve uzun uzadiya kodu/implementasyonu
aciklamak istersem kullaniriz.
"""

'''
Yorum satirlarini 3 cift tirnak arasinda da yazabiliriz.
3 adet cift tirnak da kullanabiliriz, 3 adet tek tirnak da kullanabiliriz.
Github'a python ile ilgili kodlari atmak istersek ve uzun uzadiya kodu/implementasyonu
aciklamak istersek kullaniriz.
Eger tek tirnak actiysam tek tirnak kapatmam lazim
Eger cift tirnak actiysam cift tirnak kapatmam lazim
'''

# python'da bir string'in uzunlugunu, yani kac karakterden olustugunu ogrenmek icin 
# len fonksiyonunu kullaniriz.
# len maksimum 72 olmali. Yani tek bir satirda 72 karakter olmali.
# comment yazinca soldan saga scroll aktif olmamali. Oluyorsa fazla karakter sayisina sahip yorum yazdik demektir.

print(len("Yorum satirlarini 3 cift tirnak arasinda da yazabiliriz."))  # len = 56
print(len("3 adet cift tirnak da kullanabiliriz, 3 adet tek tirnak da kullanabiliriz."))  #len = 74
print(len("Github'a python ile ilgili kodlari atmak istersek ve uzun uzadiya kodu/implementasyonu aciklamak istersek kullaniriz."))  #len = 117

number = 1
# yanlis degisken tanimlaması, sayi ile baslayamayiz ----> 1number
# yanlis degisken tanimlamasi, sayi degisken ismi olamaz ----> 1
# Turkce karakter kullanilmamasi tavsiye edilir. İstanbul = 5 dersek hata vermez, ama kullanılmasa daha iyi.
# number two seklinde degisken tanimlamasi yapamayiz. number_two, yani arada _ olmali.
# python anahtar kelimeleri degisken ismi olamaz. if = 5 diyemeyiz.

# python keyword'lerini gormek istersem: 
print(help('keywords'))

# C ve C++'ın aksine degisken turunu python'da belirtmeye gerek yok.
# sayi = 5 dedigimizde bu degiskenin turunun integer oldugunu anlar ve bellekte 4 byte'lik alan ayirir.
sayi = 5

# string'leri tek tirnak icinde de cift tirnak icinde de kullanabilirim. Uc tek tirnak, uc cift tirnak
# icinde de kullanabilirim. Burda onemli olan aynı baslayip ayni bitirmem lazım. Yani tek tirnak actiysam
# tek tirnak ile kapatmam lazim.
print("Merhaba")
print('Merhaba')
print('''Merhaba''')
print("""Merhaba""")

# int tamsayı, pozitif ve negatif
x = 1
y = 39849272794793
z = -7643764376276247

# degiskenlerin type'larini kontrol etmek icin type() fonksiyonunu kullaniriz.
print(type(x))
print(type(y))
print(type(z))

a = 0.0
b = 32432442.923849284924
c = -324.8272
d = 12e4  # type'ı float

print(type(a))
print(type(b))
print(type(c))
print(type(d))

# kompleks sayilar
q = 8 + 5j
v = 5j
w = -3j

print(type(q))
print(type(v))
print(type(w))

# boolean (true = 1, false = 0)
k = True
m = False

print(type(k))
print(type(m))

age = 35
weight = 98.8
name = "Ali"
isStudent = True

print(type(age))
print(type(weight))
print(type(name))
print(type(isStudent))

sonuc = float(age)
print(sonuc)
print(type(sonuc))

sonuc = int(weight)
print(sonuc)
print(type(sonuc))

sonuc = str(isStudent)
print(sonuc)
print(type(sonuc))

sonuc = int(isStudent)
print(sonuc)
print(type(sonuc))

sonuc = float(isStudent)
print(sonuc)
print(type(sonuc))

sonuc = str(age)
print(sonuc)
print(type(sonuc))

sonuc = str(weight)
print(sonuc)
print(type(sonuc))

a = "10"
sonuc = int(a)
print(sonuc)
print(type(sonuc))

# Compiler hata verir, t degeri int degere donusturulemez
# a = "t"
# sonuc = int(a)
# print(sonuc)
# print(type(sonuc))

# Compiler hata verir, kompleks deger int'e donusturulemez
# p = 7 + 7j
# sonuc = int(p)
# print(sonuc)
# print(type(sonuc))

# Int veri türü complex'e donusturulebilir
h = 9
sonuc = complex(h)
print(sonuc)
print(type(sonuc))

x = 4
print(x)

x = "SAlary"
print(x)

x = str(3)
print(x)

# python'da tek satirda birden fazla degiskene atama yapabiliriz
a, b, c = 10, 20, 30
print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c))

x = "Python"
y = " is"
z = " awesome"
print(x, y, z)
print(x + y + z)  # bu durumda cikti bitisik

# integer ile string ifadeyi + operatorunu kullanarak ekrana yazdiramayiz, derleme hatasi verir.
# x = 5
# y = "John"
# print(x + y)

# bu sekildeki komut satirinda degisiklik yapmak icin tek tek tum satirlari degistirmem lazim, hata yapmaya acik bir islem
print(500 + (500 * 0.18))
print(500 + (500 * 0.18))
print(500 + (500 * 0.18))
print(500 + (500 * 0.18))
print(500 + (500 * 0.18))
print(500 + (500 * 0.18))
print(500 + (500 * 0.18))
print(500 + (500 * 0.18))
print(500 + (500 * 0.18))

# degiskenleri kullanirsak hata yapmayi indirgemis oluruz, sadece product'ın guncellenmesi
# ile aslinda tum komut satirlari guncellenmis olur
product = 550
kdv = 0.18

print(product + (product * kdv))
print(product + (product * kdv))
print(product + (product * kdv))
print(product + (product * kdv))
print(product + (product * kdv))
print(product + (product * kdv))
print(product + (product * kdv))
print(product + (product * kdv))
print(product + (product * kdv))

# Odev
# Bu komut satirinda ne yapmaliyiz ki, uc degiskene dort deger atayabilelim? 
# Onerim c'yi list olarak tanimlariz, *c
# Boylelikle c = [30, 80] degerlerini tutar ve hata vermez
a, b, *c = 10, 20, 30, 80
print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c))