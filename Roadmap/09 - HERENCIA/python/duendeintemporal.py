#9 { Retos para Programadores } HERENCIA Y POLIMORFISMO
"""  
 * EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.

"""

# Bibliography
# Professional JavaScript for web developers by Matt Frisbie
# GPT

# In Python, inheritance is a mechanism that allows one class to acquire the properties and methods of another class.
# This is typically achieved through class inheritance, enabling code reuse and the creation of hierarchical relationships between classes.

# All classes in Python can inherit from other classes, allowing for a prototype chain where a class can access properties and methods from its parent class.

log = print

# Define the base class Animal
class Animal:
    def __init__(self, name=None, sound=None, animal_type=None):
        self._name = name if name else 'set no name'
        self._sound = sound if sound else 'set no sound'
        self._type = animal_type if animal_type else 'set no type'

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def speak(self):
        log(f"{self.name} the {self._type} says: {self._sound}!")

# Define the Dog class that inherits from Animal
class Dog(Animal):
    def __init__(self, name, sound, animal_type):
        super().__init__(name, sound, animal_type)

    def eat(self, meal):
        log(f"{self._name} the {self._type} eats some: {meal}")

    def move(self):
        log(f"The {self._type} moves its tail.")

# Create an instance of Dog
cap_dog = Dog('Capitan', 'I guau some pizza', 'Dog')
cap_dog.speak()  # Capitan the Dog says: I guau some pizza!
cap_dog.eat('pizza')  # Capitan the Dog eats some: pizza
cap_dog.move()  # The Dog moves its tail.

# Define the Cat class that inherits from Animal
class Cat(Animal):
    def __init__(self, name, sound, animal_type):
        super().__init__(name, sound, animal_type)

    def eat(self, meal):
        log(f"{self._name} the {self._type} eats some: {meal}")

    def move(self):
        log(f"The {self._type} hunts the rat.")

# Create an instance of Cat
black_jack = Cat('BlackJack', 'Miuauuuu', 'Cat')
black_jack.speak()  # BlackJack the Cat says: Miuauuuu!
black_jack.eat('rat snack')  # BlackJack the Cat eats some: rat snack
black_jack.move()  # The Cat hunts the rat.

# Note: It's interesting to know that we can use variables like key-value pairs assigned to object properties.
# This also works with functions.

def make_person(name, age, email):
    return {'name': name, 'age': age, 'email': email}

person = make_person('Angy', 28, 'badgirl@greenhouse.net')
log(person)  # {'name': 'Angy', 'age': 28, 'email': 'badgirl@greenhouse.net'}

# Using destructuring (unpacking)
person_name = person.get('name')
person_age = person.get('age')
person_email = person.get('email')
person_job = person.get('job', 'Web Developer')  # Default value if 'job' is not found

log(person_age)  # 28
log(person_job)  # Web Developer

import re

import re  # Make sure to import the re module

# Define the User class
class User:
    def __init__(self, id, name, email, country):
        try:
            self._id = self.set_id(id)
            self._name = self.set_name(name)
            self._email = self.set_email(email)
            self._country = self.set_country(country)
            self.validate_properties()  # Validate properties before freezing or sealing
        except Exception as error:
            log('Error creating User:', error)

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email

    @property
    def country(self):
        return self._country

    @id.setter
    def id(self, id):
        self._id = self.set_id(id)

    @name.setter
    def name(self, name):
        self._name = self.set_name(name)

    @email.setter
    def email(self, email):
        self._email = self.set_email(email)

    @country.setter
    def country(self, country):
        self._country = self.set_country(country)

    def set_id(self, id):  # Corrected to a regular method
        id_string = str(id)
        max_length = 15

        if len(id_string) > max_length:
            raise ValueError(f"ID must be at most {max_length} characters long.")

        return id_string

    def set_name(self, name):
        name_string = str(name)
        max_length = 35

        if len(name_string) > max_length:
            raise ValueError(f"Name must be at most {max_length} characters long.")

        return name_string

    def set_email(self, email):
        email_regex = r'^[^\s@]+@[^\s@]+\.[a-zA-Z]{2,}(\.[a-zA-Z]{2,})?$'

        if not re.match(email_regex, email):
            raise ValueError('Invalid email address format.')

        return email

    def set_country(self, country):
        country_string = str(country)
        max_length = 35

        if len(country_string) > max_length:
            raise ValueError(f"Country must be at most {max_length} characters long.")

        return country_string

    def validate_properties(self):
        if not self._id or not self._name or not self._email or not self._country:
            raise ValueError('All properties must be set before freezing the object.')

    def user_data(self):
        return {'id': self._id, 'name': self._name, 'email': self._email, 'country': self._country}

# Example usage of User class
try:
    sussy = User('0067', 'Sussan', 'sussy45@something.dt', 'Canada')
    log(sussy.user_data())  # {'id': '0067', 'name': 'Sussan', 'email': 'sussy45@something.dt', 'country': 'Canada'}
except Exception as error:
    log('Failed to create user:', error)

# Note: If we use a number to set the value for id, '0067' becomes '67' because it is turned to a decimal value.

# Define the SuperUser class that inherits from User
class SuperUser(User):
    def __init__(self, id, name, email, country):
        super().__init__(id, name, email, country)
        self.permission = True

    def has_permission(self):
        return self.permission

    def display_user_info(self):
        user_info = self.user_data()
        return f"{user_info['name']} has permission: {self.has_permission()}"

class SuperUser:
    def __init__(self, user_id, name, email, country):
        self._id = user_id
        self.name = name
        self.email = email
        self.country = country
        self.permission = True  # Assuming permission is always true for this example

    def user_data(self):
        # Returns user data as a dictionary
        return {
            "id": self._id,
            "name": self.name,
            "email": self.email,
            "country": self.country
        }

# Creating an instance of SuperUser
niko = SuperUser('001', 'Niko', 'duendeintemporal@hotmail.com', 'Venezuela')
niko.country = 'undefined'  # Setting country to 'undefined'

# Logging the outputs
log(niko._id)  # 001
log(niko.country)  # undefined
log(niko.permission)  # True
log(niko.user_data())  # {'id': '001', 'name': 'Niko', 'email': 'duendeintemporal@hotmail.com', 'country': 'undefined'}

class Employed:
    def __init__(self, user_id, name, occupation):
        try:
            self._id = self.set_id(user_id)
            self._name = self.set_name(name)
            self._occupation = self.set_occupation(occupation)
            self.validate_properties()
        except Exception as error:
            log('Error creating Employed:', error)

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def occupation(self):
        return self._occupation

    @id.setter
    def id(self, user_id):
        self._id = self.set_id(user_id)

    @name.setter
    def name(self, name):
        self._name = self.set_name(name)

    @occupation.setter
    def occupation(self, occupation):
        self._occupation = self.set_occupation(occupation)

    def set_id(self, user_id):
        id_string = str(user_id)
        max_length = 15

        if len(id_string) > max_length:
            raise ValueError(f'ID must be at most {max_length} characters long.')

        return id_string

    def set_name(self, name):
        name_string = str(name)
        max_length = 35

        if len(name_string) > max_length:
            raise ValueError(f'Name must be at most {max_length} characters long.')

        return name_string

    def set_occupation(self, occupation):
        occupation_str = str(occupation)
        max_length = 50

        if len(occupation_str) > max_length:
            raise ValueError(f'Occupation must be at most {max_length} characters long.')

        return occupation_str

    def validate_properties(self):
        if not self._id or not self._name or not self._occupation:
            raise ValueError('All properties must be set before freezing the object.')

    def employed_data(self):
        return {'id': self._id, 'name': self._name, 'occupation': self._occupation}


class Developer(Employed):
    def __init__(self, user_id, name, occupation, languages, area=None):
        super().__init__(user_id, name, occupation)
        self._languages = languages
        self._area = area

    def functions(self):
        log(f'Developer ID: {self._id} | Name: {self._name} | Occupation: {self._occupation} | Area: {self._area} | Languages: {", ".join(self._languages)}')


class Secretary(Employed):
    def functions(self):
        log(f'Secretary ID: {self._id} | Name: {self._name} | Occupation: {self._occupation} | Responsibilities: Administrative operations and user attention.')


class Manager(Employed):
    def __init__(self, user_id, name, occupation, employeds):
        super().__init__(user_id, name, occupation)
        self._employeds = employeds  # Expecting a list of employee names

    def functions(self):
        log(f'Manager ID: {self._id} | Name: {self._name} | Occupation: {self._occupation} | Supervising Employees: {", ".join(self._employeds)}')


class GeneralManager(Manager):
    def functions(self):
        log(f'General Manager ID: {self._id} | Name: {self._name} | Occupation: {self._occupation} | Supervising Employees: {", ".join(self._employeds)}')


# Creating instances
s1 = Secretary('0023', 'Gabriela Mistral', 'Secretary')
d12 = Developer('0041', 'Niko Zen', 'Web Developer', ['Python', 'JavaScript', 'Rust', 'Ruby', 'Bash'])
m3 = Manager('0098', 'Patty Smith', 'Manager', [s1.name, d12.name])
mg2 = GeneralManager('003', 'Lenny Kravitz', 'General Manager', [m3.name])


# Logging the outputs
log(s1.employed_data())  
# Output: {'id': '0023', 'name': 'Gabriela Mistral', 'occupation': 'Secretary'}

d12.functions()  
# Output: Developer ID: 0041 | Name: Niko Zen | Occupation: Web Developer | Area: None | Languages: Python, JavaScript, Rust, Ruby, Bash

m3.functions()  
# Output: Manager ID: 0098 | Name: Patty Smith | Occupation: Manager | Supervising Employees: Gabriela Mistral, Niko Zen

mg2.functions()  
# Output: General Manager ID: 003 | Name: Lenny Kravitz | Occupation: General Manager | Supervising Employees: Patty Smith
    
