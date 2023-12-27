print(2 and 3)
print(2 or 3)
print(1 and 0)
print(1 or 0)
print(1 and "I am doing good!")
print(1 or "I am doing good!")
print(0 or {})
print(0 and {})
print([] or "Hello World!")
print([] and "Hello World!")

x = 6
y = 9
print("x, y'ye eşit mi?", x == y)
print("x, y'ye eşit değil mi?", x != y)
print("x, y'den küçük mü?", x < y)
print("x, y'den büyük mü?", x > y)
print("x, y'den küçük veya y'ye eşit mi?", x <= y)
print("x, y'den büyük veya y'ye eşit mi?", x >= y)

country = ['USA', 'Brasil', 'UK', 'Germany', 'Turkey', 'New Zealand']
print(country)

string_2 = 'I quit smoking'
new_list = list(string_2)
print(new_list)
new_list = [string_2]
print(new_list)
mixed_list = [11, 'Joseph', False, 3.14, None, [1, 2, 3]]
print(mixed_list)
empty_list = list()
print(empty_list)
empty_list = []
print(empty_list)
empty_list.append('114')
empty_list.append(12)
empty_list.append('plastic-free sea')
print(empty_list)
city = ['New York', 'London', 'İstanbul', 'Seoul', 'Sndney', 'Addis Ababa']
city.insert(2, 'Stockholm')
print(city)
city.remove('Sndney')
print(city)
city.sort()
print(city)
print(len(city))
city[1] = 'Melbourne'
print(city)

color = ['red', 'purple', 'blue', 'yellow', 'green']
colors = []
colors.append(color)
print(colors)
print(colors[0])
print(colors[0][2][2])

numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17]
print(numbers[2:5])

number_list = list(range(14))
print(number_list)

number_list = list(range(5, 75, 5))
print(number_list[0:6:2])

animals = ['elephant', 'bear', 'fox', 'wolf', 'rabbit', 'deer', 'giraffe']
print(animals[::])
print(animals[::-1])
print(animals[:-1])
print(animals[3:])
print(animals[:5])
print(animals[::2])
print(animals[-4])
print(animals[-3:])

reef = ['swordfish', 'shark', 'whale', 'jellyfish', 'lobster', 'squid', 'octopus']
print(reef[-3:])
print(reef[:-3])
print(reef[::-1])

# empty_tuple = ()
# print(type(empty_tuple))

new_tuple = ('love')
print(new_tuple)
print(type(new_tuple))

empty_tuple = tuple()
print(empty_tuple)

planets = 'mercury', 'jupiter', 'saturn'
print(planets)
print(type(planets))

my_tuple = (1, 4, 3, 4, 5, 6, 7, 4)
my_list = list(my_tuple)
print(my_list, type(my_list))
my_list = [1, 4, 3, 4, 5, 6, 7, 4]
my_tuple = tuple(my_list)
print(my_tuple, type(my_tuple))

string_3 = 'Alps'
print(string_3)
string_to_tuple = tuple(string_3)
print(string_to_tuple)
tuple_to_string = "".join(string_to_tuple)
print(tuple_to_string)

mixed_tuple = (0, 'bird', 3.14, True)
print(mixed_tuple)

even_no = (0, 2, 4, 6, 8)
print(even_no[0])
print(even_no[1])
print(even_no[2])
print(even_no[3])
print(even_no[4])

city_list = ['Tokyo', 'İstanbul', 'Moskova', 'Dublin']
city_tuple = tuple(city_list)
print(city_tuple, type(city_tuple))

# city_tuple[4] = 'New York'

empty_dict_1 = {}
empty_dict_2 = dict()
print(type(empty_dict_1))
print(type(empty_dict_2))

my_dict = {
    'key_1': 'value_1',
    'key_2': 'value_2',
    'key_3': 'value_3'
}

print(my_dict)
print(my_dict['key_3'])

state_capitals = {'Arkansas': 'Little Rock',
                  'Colorado': 'Denver',
                  'California': 'Sacramento',
                  'Georgia': 'Atlanta'
                  }

print(state_capitals['Colorado'])
state_capitals['Virginia'] = 'Richmond'
print(state_capitals)

dict_by_dict = dict(animal = 'dog', planet = 'neptun', number = 40, pi = 3.14, is_good = True)
print(dict_by_dict)
print(dict_by_dict.items())
print(dict_by_dict.keys())
print(dict_by_dict.values())

dict_by_dict.update({'is_bad' : False})
print(dict_by_dict)

del dict_by_dict['planet']
print(dict_by_dict)

print('pi' in dict_by_dict)
print('planet' not in dict_by_dict)

school_records = {
    'personal_info':
    {
        'kid': {'tom':{'class': 'intermediate', 'age': 10},
                'sue':{'class': 'elementary', 'age': 8}
                },
        'teen':{'joseph':{'class':'college', 'age': 19},
                'marry': {'class':'high school', 'age': 16}

        }
    },
    'grades_info':
    {
        'kid': {'tom': {'math': 88, 'speech': 69},
                'sue': {'math':90, 'speech':81}
                },
        'teen':{'joseph': {'coding':80, 'math':89},
                'marry': {'coding':70, 'math':96}
                }
    }
}

print(school_records['personal_info'])
print(school_records['grades_info'])
print(school_records['personal_info']['kid']['tom']['class'])

empty_set = set()
print(type(empty_set))

colorset = {'purple', 'orange', 'red', 'darkblue', 'yellow', 'red'}
print(colorset)
print(type(colorset))


flower_list = ['rose', 'violet', 'carnation', 'rose', 'orchid', 'rose', 'orchid']
flower_set = set(flower_list)
flowerlist = list(flower_set)
print(flower_list)
print(type(flower_list))
print(flower_set)
print(type(flower_set))
print(flowerlist)
print(type(flowerlist))

a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)
print(a - b)
print(a.difference(b))
print(a | b)
print(a.union(b))
print(a & b)
a.remove('c')
print(a)
a. add('c')
print(a)
print(len(a))
print('c' in a)
print('f' not in a)