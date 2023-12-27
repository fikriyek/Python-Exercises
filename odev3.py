# Bir kelime almak ve olumsuz anlam dondurmek icin bir islev tanimlayin.
# Bir kelime verildiginde, one 'degil' eklenmis yeni bir kelime dondurun. 
# Ancak kelime zaten 'degil' ile basliyorsa diziyi degistirmeden dondurun.

# word = input("Lutfen bir kelime giriniz: ")
# print(type(word))

# def changeString(var):
#     if(var.startswith("not") == True):
#         return var
#     else:
#         return "not " + var

# new_word = changeString(word)
# print(new_word)

# Bos olmayan bir dizi ve bir int n verildiğinde, n indeksindeki karakretin kaldırıldığı
# yeni bir dize döndürür.
# n'in değeri, orijinal dizideki bir karakterin geçerli bir indeksi olacaktır (yani n, 0, ...len(str-1) dahil)
# aralığında olacaktır.
# string = input("Lutfen bir dizi giriniz: ")

# len_string = len(string)

# n = int(input("Indeks numarasi giriniz: "))
# while(n >= len_string):
#     n = int(input("Indeks numarasi giriniz: "))

# def updateString(string, n):
#     string = list(string)
#     string.pop(n)
#     return string

# updated_string = ''.join(updateString(string, n))
# print(updated_string)

# bir dizi verildiğinde, ilk ve son karakterlerin yer değiştirdiği yeni bir dizi döndürür.
# string = input("Lutfen ters cevirmek istediginiz diziyi giriniz: ")

# def reverseString(string):
#     return string[::-1]

# reversed_string = reverseString(string)
# print(reversed_string) 

# Girilen sayilarin min'ini bulmak için my_min adlı bir fonksiyon tanımlayın.
# size_of_list = int(input("Eleman sayisi: "))
# empty_list = []

    
# def findMinVal(empty_list):
#     for i in range(size_of_list):
#         empty_list.append(input(f"{i}. eleman: "))
    
#     min_value = min(empty_list)
#     return min_value
    
# min_val__in_list = findMinVal(empty_list)
# print(min_val__in_list)

# Girilen tum int tipi sayilarin toplamini dondurmak icin my_sum adli bir fonksiyon tanimlayin.
# size_of_list = int(input("Eleman sayisi: "))
# my_list = []

# def sum_list(my_list):
#     sum_items = 0
#     for i in range(size_of_list):
#         my_list.append(input(f"{i}. eleman: "))
#         sum_items += int(my_list[i])

#     return sum_items

# sum_list_items = sum_list(my_list)
# print(sum_list_items)


# number = int(input("Faktörüyeli hesaplanacak olan sayi: "))

# def faktoriyel_hesapla(number):
#     carp = 1
#     for i in range(1, number + 1):
#         carp *= i

#     return carp

# result = faktoriyel_hesapla(number)
# print(result)
