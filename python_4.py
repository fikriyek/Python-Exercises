a = 5
if(a == 5):
    print('a, 5\'e eşittir')

empty_seat = 14
if empty_seat > 3:
    print('There is still seat to sit.')

course = 'Bilge Adam'

if course == 'Cosmios':
    print('İşi garanti ettin, tebrikler...')
else:
    print('Tekrar düşünmelisin...')

number = 1
if number <= 3:
    print('Number is smaller than or equal to 3.')
else:
    print('Number is bigger than 3.')

weight = 72

if(weight > 100):
    print('That\'s too heavy')
elif(weight > 75):
    print('I can lift that!')
else:
    print('That\'s too light!')

# audience = 'baby'
# if audience == 'kid':
#     print('it\'s free to go to cinema...')
# elif audience == 'teen':
#     print('discounted price!')
# elif audience == 'adult':
#     print('normal price.')
# else:
#     print('No such audience, stay at your home!')

audience_group = 'kid', 'teen', 'adult'
audience = 'baby'

if audience in audience_group:
    if audience == 'kid':
        print('it/s free to go to cinema.')
    elif audience == 'teen':
        print('discounted price!')
    else:
        print('normal price.')
else:
    print('No such audience, stay at your home!')


# score = int(input("Enter your score:"))

# if score >= 90:
#     if score >= 95:
#         score_letter = 'A+'
#     else:
#         score_letter = 'A'
# elif score >= 80:
#     if score >= 85:
#         score_letter = 'B+'
#     else:
#         score_letter = 'B'
# else:
#     score_letter = 'below B'

# print("Your degree: %s" %score_letter)

number = 0

while number < 6:
    print(number)
    number += 1
print('now, number is bigger or equal to 6.')
print(number)

my_list = ['a', 'b', 'c', 'd', 'e']

a = 0
while a < len(my_list):
    print("square of {} is {}".format(a, a**2))
    a += 1

# answer = 44

# question = 'What number am I thinking of? '
# print('Let\'s play the guessing game!')

# while True:
#     guess = int(input(question))

#     if guess < answer:
#         print('Little higher...')
#     elif guess > answer:
#         print('Little lower...')
#     else:
#         print('Are you MINDREADER!!!')
#         break

for i in [1, 2, 3, 4, 5]:
    print(i)

for i in range (0, 15):
    print(i)

seasons = ['spring', 'summer', 'autumn', 'winter']

for season in seasons:
    print(season)

for i in {'n1': 'one', 'n2':'two'}:
    print(i)

course = 'clarusway'

for i in course:
    print(i)

# times = int(input('How many times should I say \'I love you: '))

# for i in range(times):
#     print('I love you')

# n = int(input('Enter a number between 1-10: '))

# for i in range (11):
#     print('{}x{} = {}'.format(n, i, n * i))

# for i in range (11):
#     print('%d x %d = %d' % (n, i, n*i))

list_b = list(range(10))
print(list_b)
print(type(list_b))

set_b = set(range(10))
print(set_b)
print(type(set_b))

print(*range(0, 5))

print(*range(5, 25, 2))

print(*'separate')

print(*range(10, 0, -2))

who = ['I am ', 'You are ']
mood = ['happy', 'confident']

for i in who:
    for ii in mood:
        print(i + ii)

sum_num = 0
for i in range(1, 75):
    sum_num += i
print(sum_num)

# sayi = int(input('Lutfen bir sayi giriniz: '))

# flag = False
# for i in range(2, sayi):
#     if sayi % i == 0:
#         flag = True
#         break

# if flag == False:
#     print('{}, asal bir sayıdır.'.format(sayi))
# else:
#     print('{}, asal bir sayı değildir.'.format(sayi))


prime = []

for num in range(2, 100):
    status = True
    for i in range(2, num):
        if num % i == 0:
            status = False
    if status:
        prime.append(num)

print(prime)
