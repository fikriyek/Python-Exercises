logic = True and False or not False or True
print(logic)

# Karsilastirma Operatorleri
info_email = "test@test.com"
info_password = "12345"

enter_email = "test@test2.com" == info_email
print(enter_email) # False degeri dondurur
enter_email = "test@test.com" == info_email
print(enter_email) # True degeri dondurur

enter_password = "12345" == info_password
print(enter_password) # True degeri dondurur

info_phone = 123456789

enter_phone = info_phone != 123479
print(enter_phone) # True degeri dondurur
enter_phone = info_phone != 123456789
print(enter_phone) # False degeri dondurur

a = 89
b = 34
print(a > b) # True degeri dondurur
print(a < b) # False degeri dondurur
print(a >= b) # True degeri dondurur
print(a <= b) # False degeri dondurur
print(a != b) # True degeri dondurur
print(a == b) # False degeri dondurur

# AND
# True and True = True
# True and False = False
# False and True = False
# False and False = False

# OR
# True or True = True
# True or False = True
# False or True = True
# False and False = False

# NOT
# Not True = False
# Not False = True

question = True and False or True and not False or True
print(question)

a = True and True or not False and True or False and True or not False
print(a)

b = (bool({}))
print(b)

c = (bool(()))
print(c)

d = (bool([]))
print(d)

e = bool(0)
print(e)

f = bool(0.0)
print(f)

g = bool(0 + 0)
print(g)

h = bool("")
print(h)

j = ([] and "Hello World")
print(j)

t = 5 and "s" and [1, 2, 3] and [] and True
print(t) # ekranda [] gosterir

v = ['a'] and "False" and 2 and "True" and {"a" : 1} # en son degerlendirmeye aldigi True ifadeyi yani {"a" : 1} degerini dondurur.
print(v)

y = 0 or "" or 1 or ["s"] or "ders" or (1, 2, 3, 4) or {1, 2, 3}
print(y) # en son degerlendirmeye aldigi  true degeri yani 1'i dondurur.

name = "Ayşe Doğan"
list_1 = [name] # ['Ayşe Doğan']
print(name)
print(list_1)
list_2 = list(name) # ['A', 'y', 'ş', 'e', ' ', 'D', 'o', 'ğ', 'a', 'n']
print(list_2)

# Bos bir liste nasil olusturulur?
list_3 = []
list_4 = list()
print(list_3)
print(type(list_3))
print(list_4)
print(type(list_4))

# Liste birden farkli veri tipi barindirabilir.
list_5 = [11, 11.2, "onbir", True, False, [1, 2, 3, 4, 5], (1, 2, 3), {"a": 1}, {1, 2, 3}]
print(list_5)
print(type(list_5))

new_list = [1, 2, 3, 4, 5]
new_list.append("string")
print(new_list)

city = ["Ankara", "İzmir", "Antalya", "Kayseri"]
city.insert(2, "İstanbul")
print(city)
inserted_list = ["a", "b", "c", "d"]
inserted_list.insert(4, "new")
print(inserted_list)

list_6 = [1, 2, 3, "d", "false", True]
list_6.remove("false")
print(list_6)

list_7 = [1, 2, "false", 3, "d", "false", True, "false"]
list_7.remove("false")
print(list_7)
# list_7.remove(x) # listede olmayan elemani silmek istersek derleme hatasi verir.
list_8 = [32, 4, 564, 78, 98, -424, 546.232, 0.0]
list_8.sort() # Kucukten buyuge siralama
print(list_8)
list_8.sort(reverse = True) # Buyukten Kucuge siralama
print(list_8)

list_9 = ["ali", "veli", "ayşe", "fatma", "kaan", "kerim", "ayşin", "kerem"]
list_9.sort()
print(list_9)
print(len(list_9)) # liste uzunlugunu verir

n = "Pakize"
print(n[2])
# n[2] = "ğ" # stringler'de eleman degisikligi yapilamaz. Derleme hatasi verir.
print(n[2])

list_10 = ["opel", "dacia", "mazda", "toyota"]
list_10[0] = "honda"
print(list_10[0])
print(list_10)

list_10[0:2] = ["Bmw", "Mercedes"]
print(list_10) # 0.indeksten baslar, 2.indekse kadar (2 dahil degil) degisiklik yapar

list_10[0:2] = ["Audi"]
print(list_10) # 2.indekslik yere tek eleman yerlestirir.
list_10[0:2] = ["Audi", "Telas", "Ferrari"]
print(list_10)
list_10[0:2] = "Audi"
print(list_10) # ['A', 'u', 'd', 'i', 'toyota'] bu sekilde listeye yedirmeye calisir.
print(list_10[4][2]) # 4 = toyota, 2 = y