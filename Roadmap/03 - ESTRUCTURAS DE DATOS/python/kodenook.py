
import time

""" List """

cars = ['bmw', 'ferrari', 'toyota']

''' Insert '''
cars.append('lamborghini') # insert to the end
cars.insert(2, 'bugatti') # Insert at a index

print(cars)

''' Edit '''
cars[0] = 'maserati'

print(cars)

''' Delete '''
cars.pop(1) # delete index or default(last)
cars.remove('toyota') # delete by value

print(cars)

''' Order '''
cars.reverse() # reverse
print(cars)

cars.sort() # ascending
print(cars)

cars.sort(reverse = True) # descending
print(cars)

""" Tuples """

fruits = ('apple', 'banana', 'orange')

print(fruits)

''' tuples are inmutable '''

""" Sets """

countries = {'chile', 'germany', 'japan'}

''' Set items are unchangeable '''

''' insert '''

countries.add('spain')
print(countries)

''' delete '''

countries.remove('germany') # if not exist will raise an error
countries.discard('sweden') # if not exist will not raise an error
countries.pop() # remove an random item
print(countries)

""" Dictionaries """

person = {
    'name': 'kodenook',
    'country': 'chile'
}

''' insert '''

person['continent'] = 'america'
person.update({'car': 'lamborghini'}) # edit, if key not exist add
print(person)

''' edit '''

person['car'] = 'ferrari'
print(person)

''' delete '''

person.pop('country')
del person['name']
person.popitem() # remove the last inserted
print(person)

""" Exercise """

option = 0
data = {}

while (option != 5):

    print('\033c')

    print('1. search')
    print('2. add')
    print('3. edit')
    print('4. delete')
    print('5. exit')

    option = int(input('choose a option: '))

    if option == 1:
        name = input('name: ')

        if name in data:
            print(data[name])

            time.sleep(5)

    elif option == 2:
        name = input('name: ')
        number = input('number: ')

        if name in data:
            data[name] = number

    elif option == 3:
        name = input('name: ')
        number = input('number: ')

        if name in data:
            data[name] = number

    elif option == 4:
        name = input('name: ')

        if name in data:
            del data[name]
