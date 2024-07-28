#Forma incorrecta
class Specie:

    def define_specie(self, specie):
        match specie:
            case "Humano":
                print("Soy un humano")
            case "Perro":
                print("Soy un perro")
            case "Gato":
                print("Soy un gato")

subject1 = Specie()
subject1.define_specie("Humano")
subject2 = Specie()
subject2.define_specie("Perro")

'''
    Esta forma es incorrecta para el OCP porque si hay que añadir especies hay que ir retocando la clase,
    lo que es lo contrario al principio Open/Closed
'''

#Forma correcta

class Speciee:
    def identify_specie(self):
        pass

class Human(Speciee):
    def identify_specie(self):
        return "Soy un humano con OCP"

class Dog(Speciee):
    def identify_specie(self):
        return "Soy un perro con OCP"

class Cat(Speciee):
    def identify_specie(self):
        return "Soy un gato con OCP"

human = Human()
print(human.identify_specie())
dog = Dog()
print(dog.identify_specie())
cat = Cat()
print(cat.identify_specie())

'''
    Esta sí es buena forma de aplicar el OCP, pues enemos la clase base, con las funciones y ya
    a cada especie le crearíamos su clase con sus atributos y sobreescribiendo los métodos comunes que
    queramos.
    Estamos añadiendo funcionalidades sin tener que modificar la clase
'''

print("\n", "*"*7, "EJERCICIO EXTRA", "*"*7)
class Calculator:
    def operation(self):
        pass

class Sum(Calculator):
    def operation(self, num):
        num2 = int(input("Elige un 2º número: "))
        return num + num2

class Subst(Calculator):
    def operation(self, num):
        num2 = int(input("Elige un 2º número: "))
        return num - num2

class Mult(Calculator):
    def operation(self, num):
        num2 = int(input("Elige un 2º número: "))
        return num * num2

class Div(Calculator):
    def operation(self, num):
        num2 = int(input("Elige un 2º número: "))
        return num / num2

class Pow(Calculator):
    def operation(self, num):
        num2 = int(input("¿A qué potencia quieres elevar? "))
        return pow(num, num2)

def calculator():
    num1 = int(input("Elige un número: "))

    op = input("¿Qué operación quieres realizar?\n"+
            "Suma(+)\n"+
            "Resta(-)\n"+
            "Multiplicar(*)\n"+
            "División(/)\n"+
            "Potencia(**)\n")

    match op:
        case "+":
            opt = Sum()
            print(opt.operation(num1))
        case "-":
            opt = Subst()
            print(opt.operation(num1))
        case "*":
            opt = Mult()
            print(opt.operation(num1))
        case "/":
            opt = Div()
            print(opt.operation(num1))
        case "**":
            opt = Pow()
            print(opt.operation(num1))

calculator()
