# Tanimlanan bir string'in belli indekslerine erisme
a = "Sinem Şeker"
print(a[0])
print(a[6])
print(a[10])

# olmayan bir index numarasi girdigimizde hata aliriz.
# print(a[14])

# Python derleyicisi burada hata vermiyor, normalde vermesi lazim. Olmayan bir index numarasi verirseniz o string'in son elemanina kadar tarar.
print(a[2:34])
# İlgili string'i tam tersine cevirir.
print(a[::-1])
# Negatif indeksleme
print(a[-7:-2])
# İlgili string'in -7. indeksi ile baslar, sonunu vermedigimiz icin sonuna kadar yani -1'e kadar gider.
print(a[-7:])
# İlgili string'in -7. indeksini bulur, Sonuncu -7. olacak sekilde cikti verir.
print(a[:-7])
# İlgili string'in kac karakterden olustugunu bulur.
print(len(a))

print(len("Sinem Şeker"))

lena = len(a)
print(lena)

# Ornek
name = "Sinem"
surname = "Şeker"
age = 25

message = "Benim adım " + name + " " + " ve soyadım " + surname + ". Ben " + str(age) + " yaşındayım."
print(message)

# stringleri integer bir degerle carparak coklayabiliriz.
message_2 = name * 2
print(message_2)

# % operatoru ile string bicimlendirme
# %s alfabetik karakterler
# %d integer/numerik degerler
# %f float degerler

ifade = "%d %s ve %.2f kardesim var" % (4, "kızım", 5)
print(ifade)

# sentence ilk 8 karakteri ekrana basar.
sentence = "apologizing is a virtue"
print("%.8s" % sentence)

message_3 = "Python %d yılında %s tarafından geliştirildi." % (1991, "Guido Van Rossum")
print(message_3)
# message_3 ilk 20 karakteri ekrana basar.
print("%.20s" % message_3)

message_4 = "%(miktar)d kilo %(meyve)s fiyat %(tutar).3f" % {"miktar" : 5, "meyve" : "elma", "tutar" : 50}
print(message_4)

# String formatlama
product = "elma"
fiyat = 15
kg = 2 

message_5 = "{} kilo {} {} TL".format(kg, product, (fiyat * kg))
print(message_5)

# Eger fazla parametre verirsek python derleyicisi hata vermez.
message_6 = "{k} kg {p} {kf} TL".format(kf = (kg*fiyat), k = kg, p = product)
print(message_6)

# Konumsal argumanlar ile de islem yapabiliyoruz.
message_7 = "{k} kg {p} {} TL".format((kg*fiyat), k = kg, p = product)
print(message_7)
message_8 = "{k} kg {p} {0} TL".format((kg*fiyat), k = kg, p = product)
print(message_8)
message_9 = "{1} kg {2} {0} TL".format((kg*fiyat), kg, product)
print(message_9)

# f-string ile bicimlendirme
fruit = "Orange"
vegetable = "Tomato"
amount = 6
output_1 = f"The amount of {fruit} and {vegetable} we bought totally {amount} pounds"
print(output_1)

result = f"{4 * 5}"
print(result)

# .capitalize() ilk harf buyuk
myName = "FİKRİYE"
output_2 = f"My name is {myName.capitalize()}"
print(output_2)

message_10 = f"{kg} kg {product} {fiyat * kg} TL"
print(message_10)
messaage_11 = f"Bana {{9 + 3}} hesapla dedi"
print(messaage_11)

message_12 = f"{kg} kg {product} {'Çok pahalı' if fiyat * kg > 20 else fiyat * kg} TL" 
print(message_12)

# text = "www.clarusway.com"
# print(text.startswith("https://"))
# print(text.endswith(".com"))

# startswitch
note_1 = "Python mükemmel bir dildir."
sonuc = note_1.startswith("Python")
print(sonuc)
sonuc = note_1.startswith("python")
print(sonuc)
sonuc = note_1.startswith("Python mükemmel bir dildir")
print(sonuc)
sonuc = note_1.startswith("mükemmel bir dildir.")
print(sonuc)
sonuc = note_1.startswith("Python mükemmel bir1 dildir.")
print(sonuc)

# endswitch
sonuc = note_1.endswith("Python mükemmel bir dildir")
print(sonuc)
sonuc = note_1.endswith("python mükemmel bir dildir")
print(sonuc)
sonuc = note_1.endswith("dildir.")
print(sonuc)
sonuc = note_1.endswith("dildir. ")
print(sonuc)

print(len(note_1))
sonuc = note_1.startswith("Python", 0, 22)
print(sonuc) # note_1 Python ile basliyor
sonuc = note_1.startswith("mükemmel", 0, 22) # note_1 mükemmel ile baslamiyor
print(sonuc)
sonuc = note_1.endswith("dildir.", 20, 27)
print(sonuc)
sonuc = note_1.endswith("bir", 15, 19)
print(sonuc)

note_2 = "Python güzel bir dildir."
sonuc = note_2.replace("Python", "Java")
print(sonuc) # kopyasi degistirilir, original dizi degistirilmez.
print(note_2)
# original degistirilmek isteniyorsa 
note_2 = note_2.replace("Python", "Java")
print(note_2)
# Buyuk-kucuk harf duyarliligi var
sonuc = note_2.replace("java", "Python")
print(sonuc)
note_3 = "Python öğrenilmesi kolay bir dildir. Python'ın gün geçtikçe kullanımı yaygınlaşmaktadır. Python Backend programlamada tercih edilmektedir."
sonuc = note_3.replace("Python", "Java", 2) # Count 1 ise text'teki ilk karsilasilan Python ifadesi degistirilir. Eger 2 ise karsilasilan ilk 2 Python ifadesi degistirilir.
print(sonuc)

sonuc = note_2.swapcase() # Buyuk harfler kucuk, kucuk harfler buyuk yapilir.
print(sonuc)
sonuc = note_2.upper() # Tum harfler buyuk
print(sonuc)
sonuc = note_2.lower() # Tum harfler kucuk
print(sonuc)
print(note_2) # Original dizi bozulmaz.
sonuc = note_2.title()
print(sonuc)
sonuc = note_2.capitalize() # Sadece ilk kelimenin ilk harfi buyuk
print(sonuc)

note_4 = "    Python   güzel   bir     dildir.    "
print(note_4)
sonuc = note_4.strip()
print(sonuc)
sonuc = note_4.lstrip() # soldaki bosluklar kaldirilir
print(sonuc)
sonuc = note_4.lstrip("    Python") # soldaki bosluklar kaldirilir
print(sonuc)
sonuc = note_4.rstrip() # sagdaki bosluklar kaldirilir
print(sonuc)
sonuc = note_4.rstrip("dir.    ") # sagdaki bosluklar kaldirilir
print(f"sonuc: {sonuc}")
print(note_4)


text_3 = "Python mükemmel bir dildir." # bosluk karakterleri harf olmadigi icin False dondurur
print(text_3.isalpha())
text_4 = "Python" # bosluk yok, True dondurur
print(text_4.isalpha())

text_5 = "12345ab"
print(text_5.isdigit())
text_5 = "12345"
print(text_5.isdigit()) # string rakam iceriyorsa True, icermiyorsa False dondurur.

# dikkate aldigi kisim ilk karsilastigi harfin indexi
print(text_3.index("b"))
print(text_3.index("bir"))

# bir string'in elemanlarini bir listenin elemanlari haline getirmek icin split metodu
sonuc = text_3.split() # default'u bosluk
print(sonuc)
text_6 = "Python, güzel, bir, dildir."
sonuc = text_6.split(",") # parametre de verebiliriz
print(sonuc)
sonuc = text_6.isupper() # butun harfler buyuk mu kontrol ediyor
print(sonuc)
text_7 = "PYTHON GÜZEL BİR DİLDİR."
sonuc = text_7.isupper()
print(sonuc)