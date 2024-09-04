#CLASES

class Person:
    name = ""
    surname = ""
    age = 0
    def __init__(self,param_name,param_surname,param_age) -> None:
        self.name = param_name
        self.surname = param_surname
        self.age = param_age
    def __str__(self) -> str:
        return " ".join(["Name:",self.name,"Surname:",self.surname,"Age:",str(self.age)])

person = Person("jptx","aya",40)

print(str(person))

#Dificultad Extra
print("Pila")
class Pila:

    def __init__(self, p_list: list) -> None:
        self.my_list = p_list
    def add(self,p_value) -> None:
        self.my_list.append(p_value)
    def remove(self):
        self.my_list.pop()
    def count(self):
        print(f"Total Elements: {len(self.my_list)}")
    def print_all(self) -> None:
        print("Elementos en la Pila:")
        for elem in self.my_list:
            print(elem)

pila = Pila(["aa","bb","cc"])
pila.print_all()
print("Adding dd y ff")
pila.add("dd")
pila.add("ff")
pila.print_all()
print("Removing last input")
pila.remove()
pila.print_all()
pila.count()

print("************************************************")
print("Cola")
class Cola:
    def __init__(self,p_list:list) -> None:
        self.my_list = p_list
    def add(self,p_value) -> None:
        self.my_list.append(p_value)
    def remove(self):
        return self.my_list.pop(0)
    def count(self):
        print(f"Total Elements: {len(self.my_list)}")
    def print_all(self) -> None:
        print("Elementos en la Cola:")
        for elem in self.my_list:
            print(elem)

cola = Cola(["aa","bb","cc"])
cola.print_all()
print("Adding dd y ff")
cola.add("dd")
cola.add("ff")
cola.print_all()
print("Removing first input")
cola.remove()
cola.print_all()
print(f"Total Elementos: {cola.count}")
