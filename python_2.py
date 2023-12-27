# DERS 2
print(4 + 11)
print(39 + 1.0)
number_1 = 46
print(number_1 / 23)
print((3 * 4) / 2)
print(2 ** 3)
print(64 ** 0.5)
print(7 // 2)
print(7 / 2)
print(9 % 2)

a = 5
b = 2
# a = a + b
# print(a)
# a += b
# print(a)
# a = a - b
# print(a)
# a -= b
# print(a)
# a = a * b
# print(a)
# a *= b
# print(a)
# a = a / b
# print(a)
# a /= b
# print(a)
# a = a // b
# print(a)
# a //= b
# print(a)
# a = a % b
# print(a)
# a %= b
# print(a)
# a = a ** b
# print(a)
# a **= b
# print(a)
meyve = 'Turuncu'
sebze = '''Domates'''
print(meyve, """ ve """, sebze)

fruit = "Orange"
print('Word: ', fruit)
print("First Letter: ", fruit[0])
print("Second Letter: ", fruit[1])
print('3rd to 5th letters: ', fruit[2:5])
print('Letter all after 3rd: ', fruit[2:])
print(fruit[:])
print(fruit[:5])
print(fruit[2:])
print(fruit[::2])
city = 'Amsterdam'
print(city[1:])
print(city[:6])
print(city[::2])
print(city[1::2])
print(city[-3:])
print(city[::-1])

name = "Fikriye"
print(name*3)
surname = "Kucukomeroglu"
print(name + surname)

sentence_1 = '%d %s ve %d kız kardeşim var' % (1, 'oğlum', 3)
print(sentence_1)
sentence_2 = "apologizing is a virtue"
print("%.15s" % sentence_2)
print("%(miktar)d kilo %(meyve)s kaldı." % {"miktar": 33, "meyve": "muz"})
print("{state} is the most {adjective} state of the {country}.".format(state = "California", adjective = "crowded", country = "USA"))

print("{1} {0} {6} {2} {5} {3}".format('ay', 6, 'iş', 'olacağım', 'buldum', 'bulmuş', 'sonra'))

fruit = "Orange"
vegetable = "Tomato"
amount = 6
output = f"The amount of {fruit} and {vegetable} we bought are totally {amount} pounds"
print(output)

result = f"{4 * 5}"
print(result)

my_name = "JOSEPH"
output = f"My name is {my_name.capitalize()}"
print(output)

name = "Joseph"
job = "teachers"
domain = "Data Science"

message = (
    f"Hi {name}!"
    f" You are one of the {job}"
    f" in the {domain} section."
)

print(message)

text = "www.clarusway.com"
print(text.startswith("w"))
print(text.endswith(".c"))

email = "clarusway@clarusway.com is my e-mail address"
print(email.startswith("@", 9, 15))
print(email.endswith("-", 10, 32))

string = "i live and work in Virginia."
print(string.capitalize())
print(string.swapcase())
print(string.upper())
print(string.lower())
print(string.title())
print(string.replace('i', '+'))
print(string)
print([] and "Hello World!")
print(2 or 3)
print(None or 1)

space_string = "    listen first    "
print(space_string)
print(space_string.strip())
source_string = "interoperability"
print(source_string.strip("in"))
