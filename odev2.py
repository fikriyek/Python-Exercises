# Soru-1
# Eğer meyve sepette değilse, "Biraz alabilirim" deyin.
# Aksi takdirde, "Zaten var" deyin.

basket = ['apple', 'peach', 'blackberry']
fruit = 'apple'

if(fruit in basket) : 
    print(f"{fruit} is already in the basket.")
else:
    print(f"I can have some {fruit}")

# Soru-2
total = 149
country = "FR"

if country == "FR":
    if total <= 50:
        print("Shipping Cost is  €30")
    elif total <= 100:
        print("Shipping Cost is €15")
    elif total <= 150:
        print("Shipping Costs €10")
    else:
        print("Free Shipping")
if country == "DE": 
    if total <= 50:
        print("Shipping Cost is  €25")
    else:
        print("Free Shipping")
# Yukarıdaki programa göre kargo ücreti ne kadar?
# country = "FR" oldugu icin ilk if dongusune girecegiz.
# total = 149; 
# total <= 50 mi, hayır.
# total <= 100 mü, hayır.
# total <= 150 mi, evet. Console'a "Shipping Costs €10" yazacak.
# ikinci elif'e girdigi icin else'e girmeyecek.
# ikinci if uygulamasına geliyor sira.
# country = "FR" oldugu icin if = FALSE olacak, bu donguye girmeyecek.
# Console'da sedece "Shipping Costs €10" yazacak.

# Soru-3
# Aşağıda verilen koşulları sağlayan bir program yazınız. 
# Değişkenin adını olarak tanımlayın number.
# 10'a eşit number veya 10'dan büyükse, şunu yazdırın: 'Sayı 10'a eşit veya 10'dan büyük',
# 10'dan küçükse number, şunu yazdırın: 'Sayı 10'dan küçük'.

number = int(input("Bir sayi giriniz: "))
if(number >= 10):
    print(f"{number} is bigger than or equal to 10")
else:
    print(f"{number} is smaller than 10.")

# Soru-4
# Tom adında 13 yaşında bir çocuk, PlayStation-4 oynamak istiyor. 
# Ancak ona maddi gücü yetmediği için PS4'ün fiyatına ulaşmak için para biriktirmeye başladı (ps4_price değişkeni). 
# Tom'a ne kadar zaman kaldığını söyleyen bir program yazalım. Kaydedilen tutara (saved_amount değişkeni) göre aşağıdaki üç seçenekten birini yazdıran basit bir kod yazın:

# Eğer kaydedilen tutar ps4_price'in yarısından az veya eşitse, "Daha fazla biriktirmelisin, biriktirmeye devam et!" yazdırın.
# Eğer kaydedilen tutar ps4_price'in yarısından büyükse, "Yarısından fazlasını biriktirdin, biriktirmeye devam et!" yazdırın.
# Eğer kaydedilen tutar ps4_price'tan büyükse, "Yippee! PS4'ünü satın alabilirsin." yazdırın.

ps4_price = 3000 # PlayStation-4'ün fiyatı 3000 lira olsun

saved_amount = float(input("Tom, kaç lira biriktirdin? "))

if(saved_amount <= (ps4_price / 2)):
    print("You should save more, keep saving.")
elif (saved_amount > (ps4_price / 2)):
    if(saved_amount < ps4_price):
        print("you saved more than half, keep saving.")
    else:
        print("Yippie! You can buy your PS4.")
# there is no need else loop.

# Soru-5
# Aşağıdaki listenin tüm öğelerini aşağıdaki gibi ayrı satırlara yazdıran programı yazdırın:
# Not: whileDöngü kullanın.
# Örnek çıktı:
# Rose
# Orchid
# Tulip
flowers = ['Rose', 'Orchid', 'Tulip']

index = 0
length = len(flowers)
while(index < length):
    print(f"{flowers[index]}")
    index = index + 1

# Soru-6
# Aşağıdaki listedeki her bir sayının karesini ayrı satırlara yazdıran bir program yazınız .
iterable = [1, 2, 3, 4]
for i in iterable:
    print(f"{i} * {i} = {i **2 }")

# Soru-7
# Aşağıdaki tuple'ın tüm öğelerini örnek çıktıdaki gibi ayrı satırlara yazdıran programı yazdırın:
# Not: for Döngü kullanın.
# Örnek çıktı:
# Elma 
# Muz 
# Portakal
meyveler = ('Elma' ,'Muz' ,'Portakal' )
for meyve in meyveler:
    print(f"{meyve}")

# Soru-8
# Bayan Brown bir Matematik öğretmenidir. 
# Öğrencilerinin sayısal notlarını alan, bunları math_mark değişkenine atayan ve aşağıda tanımlanan harf tabanlı notlar olarak yazdıran bir program yazmak istiyor:
# 85-100 ➔ A (Mükemmel)
# 70-84 ➔ B (İyi)
# 60-69 ➔ C (Orta)
# 45-59 ➔ D (Fena Değil)
# 0-44 ➔ F (Başarısız)
# if, elif ve else deyimlerini kullanarak programınızı yazınız.
exam_1 = int(input("1. vize notu: "))
while(exam_1 < 0 or exam_1 > 100):
    print("Gecersiz not girdiniz. Lutfen gecerli bir not giriniz: ")
    exam_1 = int(input("1. vize notu: "))

exam_2 = int(input("2. vize notu: "))
while(exam_2 < 0 or exam_2 > 100):
    print("Gecersiz not girdiniz. Lutfen gecerli bir not giriniz: ")
    exam_2 = int(input("2. vize notu: "))

exam_3 = int(input("Final notu: "))
while(exam_3 < 0 or exam_3 > 100):
    print("Gecersiz not girdiniz. Lutfen gecerli bir not giriniz: ")
    exam_3 = int(input("Final notu: "))


average = ((exam_1 + exam_2) * 0.2) + (exam_3 * 0.6)

if(average >= 85 and average <= 100):
    math_work = 'A'
elif(average >= 70 and average <= 84):
    math_work = 'B'
elif(average >= 60 and average <= 69):
    math_work = 'C'
elif(average >= 45 and average <= 59):
    math_work = 'D'
else:
    math_work = "F"

print(f"Ogrencinin not ortalamasi: {average} harf notu: {math_work}")

# Soru-9
# Aşağıdaki listeden her öğeyi ve karşılık gelen türünü yazdıran bir program yazın.
sample_list = [{"bölüm":5, "konu":2}, [1, 4], 2020, 3.14, 1+618j, "Yanlış", True, (10, 20)]
# Örnek olarak çıktı satırından biri: Yanlış'ın türü <class 'str'> şeklindedir.
# Not: Programı for deyimi ile yazınız.
for item in sample_list:
    print(f"{item} ogesinin turu {type(item)} seklindedir.")

# Soru-10
# Kullanıcıdan bir sayı alan ve bunun asal olup olmadığını kontrol etmek için sonucu ekrana yazdıran bir program yazınız .
number = int(input("Lutfen bir sayi giriniz: "))
# 1.durum, negatif sayi giriyorsak pozitif sayi girene kadar kullanicidan sayi girmesini istesin.
# while(number < 0):
#     print("Negatif bir sayi girdiniz!")
#     number = int(input("Lutfen pozitif bir sayi giriniz: "))

# durum = 1
# for i in range(2, number):
#     if(number % i == 0):
#         durum = 0
#         break
#     else:
#         durum = 1

# if(durum == 1):
#     print(f"{number} bir asal sayidir.")
# else:
#     print(f"{number} bir asal sayi degildir.")

# 2.cozum negatif sayi girmissek console'a "girilen sayi asal sayi degildir" seklinde bir yazi yazdirsin.
if(number < 0):
    print(f"{number} bir asal sayi degildir.")
else:
    durum = 1
    for i in range(2, number):
        if(number % i == 0):
            durum = 0
            break
        else:
            durum = 1

    if(durum == 1):
        print(f"{number} bir asal sayidir.")
    else:
        print(f"{number} bir asal sayi degildir.")