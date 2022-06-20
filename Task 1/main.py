# Turimas "users" masyvas. 
import collections
# Parašykite funkcijas, kurios atlikas nurodytas užduotis:
# 1. funkcija "filter_dog_owners" - kaip argumentą priims masyvą ir duoto masyvo
# atveju grąžins "users", kurie turi augintinį.
# 2. funkcija "filter_adults" - kaip argumentą priims masyvą ir duoto masyvo
# atveju grąžins masyvą su "users", kurie yra pilnamečiai.

users = [
  { "id": '1', "name": 'John Smith', "age": 20, "hasDog": True },
  { "id": '2', "name": 'Ann Smith', "age": 24, "hasDog": False },
  { "id": '3', "name": 'Tom Jones', "age": 31, "hasDog": True },
  { "id": '4', "name": 'Rose Peterson', "age": 17, "hasDog": False },
  { "id": '5', "name": 'Alex John', "age": 25, "hasDog": True },
  { "id": '6', "name": 'Ronald Jones', "age": 63, "hasDog": True },
  { "id": '7', "name": 'Elton Smith', "age": 16, "hasDog": True },
  { "id": '8', "name": 'Simon Peterson', "age": 30, "hasDog": False },
  { "id": '9', "name": 'Daniel Cane', "age": 51, "hasDog": True },
]


def filter_dog_owners(dog):
    a = [x for x in dog if x['hasDog'] == True]
    x = [y['name'] for y in a if 'name' in y]
    print('Dog owners:', x)


filter_dog_owners(users)


def filter_adults(age):
    a = [x for x in age if x['age'] >= 18]
    x = [y['name'] for y in a if 'name' in y]
    print('Adults:', x)


filter_adults(users)

# name = [y['name'] for y in users if 'name' in y]
# boole = [x['hasDog'] for x in users if 'hasDog' in x]
#
# dictionary = dict(zip(name, boole))
#
# print(dictionary)
# print(name)
# print(boole)
#
# a = [li['name'] for li in users]
# b = [li['hasDog'] for li in users]
#
# print(a)
# print(b)