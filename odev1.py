# 1- Verilen bir listeyi sondan basa dogru yazdirma
number_list = ["1, 3, 5, 7, 2, 4, 6, 8, 9"]
print("Sondan basa liste: ", number_list[::-1])
string_1 = "Fikriye"
print("Sondan basa string: ", string_1[::-1])

# 2- Bir metnin icinde belirli bir kelimeyi arayarak o kelimenin kac kez gectigini bulan program
text_1 = "Bu bir örnek metindir. Bu metin içinde kaç tane 'bir' kelimesi geçiyor acaba?"
counter = text_1.count("bir")
print("'bir' kelimesinin tekrar sayisi: " + str(counter)) 

# 3- Verilen bir liste icindeki en buyuk iki sayinin toplamini hesaplayan program
list = [4, 2, 8, 1, 9, 5, 6, 3, 7]
list.sort(reverse=True)
print("Buyukten kucuge sirali list: ", list)
sum = list[0] + list[1]
print("En buyuk iki sayinin toplami: " + str(sum))

# 4- Verilen bir metindeki harflerin sayisini hesaplayan program
text_2 = "Bu bir örnek metindir."
text_length = len(text_2)
print("Verilen bir metindeki karakter sayisi: " + str(text_length))

# 5- Verilen bir sayinin karesini hesaplayan program
number = 5
square = number ** 2
print("{} sayisinin karesi: {}.".format(number, square))

# 6- Verilen bir sayi dizisindeki elemanlarin ortalamasini hesaplayan bir program
# Birinci yol
numbers = [2, 4, 6, 8, 10]
numbers_length = len(numbers)
sum = 0
for i in range (numbers_length):
    sum += numbers[i]
average = sum / (numbers_length)
print("Ortalama: " + str(average))

# Ikinci yol
numbers = [2, 4, 6, 8, 10]
numbers_length = len(numbers)
sum = 0
sum = sum + numbers[0]
sum = sum + numbers[1]
sum = sum + numbers[2]
sum = sum + numbers[3]
sum = sum + numbers[4]
average = sum / (numbers_length)
print("Ortalama: " + str(average))

# 7- Verilen iki sayinin toplamini, farkini, carpimini, bolumunu bulan program
number_1 = 18
number_2 = 21

sum_numbers = number_1 + number_2
print("Iki sayinin toplami: " + str(sum_numbers))

sub_numbers_1 = number_1 - number_2
print("Birinci sayiyi ikinci sayidan cikar: " + str(sub_numbers_1))

sub_numbers_2 = number_2 - number_1
print("Ikinci sayiyi birinci sayidan cikar: " + str(sub_numbers_2))

mul_numbers = number_1 * number_2
print("Iki sayinin carpimi: " + str(mul_numbers))

div_numbers_1 = number_1 / number_2 # Bolme islemi
print("Birinci sayinin ikinci sayiya bolumu: " + str(div_numbers_1))

div_numbers_2 = number_2 / number_1 # Bolme islemi
print("Ikinci sayinin birinci sayiya bolumu: " + str(div_numbers_2))

div_numbers_3 = number_1 // number_2 # Tam bolen
print("Birinci sayinin ikinci sayiya bolumu: " + str(div_numbers_3))

div_numbers_4 = number_2 // number_1 # Tam bolen
print("Ikinci sayinin birinci sayiya bolumu: " + str(div_numbers_4))

mod_numbers_1 = number_1 % number_2 # Mod alma
print("{} % {} = {} ".format(number_1, number_2, mod_numbers_1))

mod_numbers_2 = number_2 % number_1 # Mod alma
print("{} % {} = {} ".format(number_2, number_1, mod_numbers_2))

# 8- Verilen bir string'deki tum bosluklari kaldiran program
string_2 = "Merhaba dünya, nasılsınız?"
string_2 = string_2.replace(" ", "")
print("Bosluksuz yeni string: " + string_2)

# 9-
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# İlk alt listenin ikinci elemanına erişmek için
print("Ilk alt listenin ikinci elemani: ", matrix[0] [1])

# İkinci alt listenin üçüncü elemanına erişmek için
print("Ikinci alt listenin ucuncu elemani: ", matrix[1] [2])

# Son alt listenin ilk elemanına erişmek için
print("Son alt listenin ilk elemani: ", matrix[2] [0])

# ilk alt listenin ilk elemanını 0 ile değiştirmek
print("Ilk alt listenin ilk elemani: ", matrix[0] [0])
matrix[0][0] = 0
print("Ilk alt listenin ilk elemani: ", matrix[0] [0])

# ikinci alt listenin ikinci elemanını 10 ile değiştirmek
print("Ikinci alt listenin ikinci elemani: ", matrix[1] [1])
matrix[1][1] = 10
print("Ikinci alt listenin ikinci elemani: ", matrix[1] [1])

# 10- Verilen koddaki hatayı düzeltin
string_fixed = "Bugün hayatımın en güzel günü. Hayalini kurduğum meslek olan "'.... Developer'" olmaya her geçen gün dahada yaklaşıyorum, elimden gelenin fazlasını yapıyorum. Başarımın meyvesini alacağıma çok eminim Cosmios Yazılım Akademi en büyük yardımcım."
print("Duzeltilmis string: \n" + string_fixed)


# 11- Aşağıda verilen kodun çıktısı ne olur ? Lütfen çalıştırmadan önce tahmin ediniz ve cevabınızı tahmin ettiğiniz çıktıyı yazınız.
x = 12
y = 21

y = x
x += y
y *= y
x /= y
# Tahminim:
# y = x, y = 12 olur.
# x += y, x'e y eklenir ve toplama sonucu x'e atanir. x = 12, y = 12, x = 12 + 12 = 24 olur.
# y *= y, y kendisi ile carpilir ve sonuc tekrar y'ye atanir. y = 12 * 12 = 144 olur.
# x/= y, x y'ye bolunur ve sonuc x'e atanir. x = 24 ve y = 144. x'in yeni degeri 0.1666666667.
# Ozetle x = 0.1666666667 ve y = 144 olacaktir.
print(x)
print(y)

# 12- Adınızı ve soydınızı giriniz. 
# Adınızın ilk 3 karakteri parçalayıp soyadınızın son 3 karakterini parçalayıp elde ettiğiniz verileri tek bir kelime haline getirip bir değişkene atayınız.
name = "Fikriye"
surname = "Küçükömeroğlu"
sentence = name[0:3] + surname[-4:-1]
print(sentence)

# 13- Aşağıda verilen kodun çıktısı ne olur ? Lütfen çalıştırmadan önce tahmin ediniz ve cevabınızı tahmin ettiğiniz çıktıyı yazınız.
example = "Ben başarılı bir insanım."
# Tahminim: "baş" kelimesi ekrana yazdirilacaktir.
print("{}".format(example[4:7]))

# 14- Aşağıda verilen kodun çıktısı ne olur ? Lütfen çalıştırmadan önce tahmin ediniz ve cevabınızı tahmin ettiğiniz çıktıyı yazınız.
L1 = []
L1.append([1, [2, 3], 4])
L1.extend([7, 8, 9])

# Tahminim:
L1 = [[1, [2, 3], 4]]  # append islemi sonrasi
L1 = [[1, [2, 3], 4], [7, 8, 9]] # extend islemi sonrasi
# compiler error vermesini beklerim, cunku L1[2] elemani mevcut degil.
# print(L1[0][1][1] + L1[2]) 

# 16-
tuple_1 = ("1", 2, [1, "2"], {"set": "Setler sırasız bir yapıya sahiptir"})
t_1 = (1, 3, 5, 7, 9)
# Verilen tuple veri türünün kaç elemanlı olduğunu
len_tuple = len(tuple_1)
print("Eleman sayisi: " + str(len_tuple))

# 5 numaralı indeks numaralı elemanın ne olduğunu bulunuz
# print("5. indeksteki eleman: " + tuple_1[4])

# [1, "2"] elemanını silip onun yerine "her geçen gün python'u daha iyi öğreniyorum" ifadesini ekleyiniz.
list_tuple = [*tuple_1,]
print(list_tuple)
print(type(tuple_1))
print(type(list_tuple))
list_tuple.pop(2)
list_tuple.insert(2, "her geçen gün python'u daha iyi öğreniyorum")
print(list_tuple)
print(type(list_tuple))
list_tuple = tuple(list_tuple)
print(type(list_tuple))