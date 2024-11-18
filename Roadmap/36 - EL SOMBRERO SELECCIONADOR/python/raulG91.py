import random
house = {
    'frontend': 0,
    'backend': 0,
    'mobile': 0,
    'data':0
}

name = input('Enter your name ')

print("1 - WHat's your favourite framework ?")
print(" a React")
print(" b Node.js")
print(" c Flutter")
print(" d Keras")
choice = input("> ")
choice = choice.lower()

match choice:
    case 'a': house['frontend'] += 1
    case 'b': house['backend'] += 1
    case 'c': house['mobile'] += 1
    case 'd': house['data'] += 1
    case _: print("Incorrect option ")

print("2 - which language do you prefer?")
print(" a Python")
print(" b HTML/CSS")
print(" c Java")
print(" d Kotlin")
choice = input("> ")
choice = choice.lower()
match choice:
    case 'a': house['data'] += 1
    case 'b': house['frontend'] += 1
    case 'c': house['backend'] += 1
    case 'd': house['mobile'] += 1
    case _: print("Incorrect option ")

print("3 - Which activity do you prefer")
print(" a Build UI interfaces")
print(" b Develop APIs")
print(" c Apps for mobile")
print(" d Analyse data from a source")
choice = input("> ")
choice = choice.lower()
match choice:
    case 'a': house['frontend'] += 1
    case 'b': house['backend'] += 1
    case 'c': house['mobile'] += 1
    case 'd': house['data'] += 1
    case _: print("Incorrect option ")

print("4 - Where do you want to view your apps")
print(" a Browser")
print(" b SAAS")
print(" c App store/Play store")
print(" d Other")
choice = input("> ")
choice = choice.lower()
match choice:
    case 'a': house['frontend'] += 1
    case 'b': house['backend'] += 1
    case 'c': house['mobile'] += 1
    case 'd': house['data'] += 1
    case _: print("Incorrect option ")

print("5 - What is more valuable for you?")
print(" a Create a nice UI")
print(" b Analyse data and create reports")
print(" c Use your app everywhere with your phone")
print(" d Create a solution for a problem")
choice = input("> ")
choice = choice.lower()
match choice:
    case 'a': house['frontend'] += 1
    case 'b': house['data'] += 1
    case 'c': house['mobile'] += 1
    case 'd': house['backend'] += 1
    case _: print("Incorrect option ")


print("6 - Which tool do you prefer to learn?")
print(" a Android studio")
print(" b Figma")
print(" c Power BI")
print(" d Mongo DB")
choice = input("> ")
choice = choice.lower()
match choice:
    case 'a': house['mobile'] += 1
    case 'b': house['frontend'] += 1
    case 'c': house['data'] += 1
    case 'd': house['backend'] += 1
    case _: print("Incorrect option ")

print("7 - if you need to optimze something what do you prefer?")
print(" a Optimize database access")
print(" b Optimize response time")
print(" c Optimize UI")
print(" d Other")
choice = input("> ")
choice = choice.lower()
match choice:
    case 'a': house['backend'] += 1
    case 'b': house['mobile'] += 1
    case 'c': house['frontend'] += 1
    case 'd': house['data'] += 1
    case _: print("Incorrect option ")

print("8 - Do you know any of the following technologies?")
print(" a Docker")
print(" b Vue")
print(" c Swift")
print(" d Bigquery")
choice = input("> ")
choice = choice.lower()
match choice:
    case 'a': house['backend'] += 1
    case 'b': house['frontend'] += 1
    case 'c': house['mobile'] += 1
    case 'd': house['data'] += 1
    case _: print("Incorrect option ")

print("9 - How do you see your carreer in 5 years?")
print(" a UI Master")
print(" b Backend master")
print(" c Mobile master")
print(" d Data master")
choice = input("> ")
choice = choice.lower()
match choice:
    case 'a': house['frontend'] += 1
    case 'b': house['backend'] += 1
    case 'c': house['mobile'] += 1
    case 'd': house['data'] += 1
    case _: print("Incorrect option ")

bigger = 0
houses_selected = []
print(house)
for element in house:
    if house[element]> bigger:
        bigger = house[element]
        houses_selected = []
        houses_selected.append(element)
    elif house[element] == bigger:
        houses_selected.append(element)   

print(f'Name {name} house: {random.choices(houses_selected)}')        