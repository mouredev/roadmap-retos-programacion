"""EJERCICIO"""

# --------- lista ------------
l = [] # lista vacía

# Operación de inserción de datos en la lista
for i in range(5):
    l.append(i)
print(l)

# Operación de actualización de un elemento
l[2] = 7
print(l)

# Operación de borrado de un elemento
l.remove(4)
print(l)

# Operación de ordenación de elementos
l_ordenada = sorted(l)
print(l_ordenada)

# --------- Tupla ------------
t = (1, 2, 3, 4) # tupla

dicc = {} # diccionario vacío

# Operación de inserción de datos en el diccionario
dicc["Inserción 1"] = "Este es el valor para la primera inserción"
dicc["Inserción 2"] = "Este se corresponde con la segunda inserción"
print(dicc)

# Operación de actualización de datos en el diccionario
dicc["Inserción 2"] = "Segunda inserción modificada"
print(dicc)

# Operación de borrado de un elemento
del dicc["Inserción 1"]
print(dicc)

# ------- Conjunto -----------
cj = {"Pedro"} # Conjunto
print(cj)

# Operación de inserción de datos en el conjunto
cj.add("Jose")
print(cj)

# Operación de actualización de datos en el conjunto
cj.update(["Luis", "Ana", "Isabel"])
print(cj)

# Operación de borrado de datos en el conjunto
cj.remove("Pedro")
print(cj)

# DIFICULTAD EXTRA

class Diary():
    """
    Clase para crear agendas con los atributos y métodos
    correspondientes
    """
    def __init__(self):
        self.contacts = []
        self.elec = str()
        self.n = 0
        self.register = int()

    diccInst = {"A": "añadir registro", "F": "búscar registro",
                "U": "modificar registro", "E": "eliminar registro",
                "S": "ver todos los registros", "Q": "salir del programa"}

    @classmethod
    def methods(cls):
        """
        Método que informa de las operaciones disponibles en cada
        instancia del Diary
        """
        print("Después de crear el objeto de la clase Diary llama",
              "al método 'election' para realizar alguna de las",
              "siguientes operaciones:\n"+
              "(Debes indicar la letra mayúscula que tiene asociada)\n")
        for key, value in Diary.diccInst.items():
            print(f"{key}: {value}")

    def election(self):
        """
        Método para tomar la elección del usuario
        """
        self.elec = input("Elige una operación: ").upper()

        if self.elec == "A":
            return self.insert()

        if self.elec == "F":
            print("\nIndica qué tipo de registro quieres buscar: N (nombre)",
              ", P (teléfono) o R (número de registro)")
            type_search = str(input("Tipo de registro: ")).upper()
            return self.search(type_search)

        if self.elec == "U":
            print()
            return self.update()

        if self.elec == "E":
            print()
            return self.delete()

        if self.elec == "S":
            print("\n------ AGENDA ------")
            for item in self.contacts:
                print(f"{item[0]} --> Nombre: {item[1]}, teléfono: {item[2]}")

        if self.elec == "Q":
            return self.__del__

    def insert(self):
        """
        Método para añadir un registro al diario
        """
        print()
        name = str(input("Nombre: "))
        phone = input("Teléfono: ")

        if len(phone) > 11 or len(phone) < 9:
            print("\nEl número de teléfono no puede tener más de"+
                  " 11 caracteres ni menos de 9")
        elif phone != int:
            print("\nNo se puede introducir un número no numérico en"+
                  " el campo teléfono")
        else:
            self.n += 1
            self.contacts.append([self.n, name, phone])
            print("\nEl contacto ha sido añadido a la agenda")

    def search(self, s):
        """
        Método para buscar un registro en la agenda
        """
        if s == "P":
            phone_number = str(input("Indica el número de teléfono: "))
            for item in self.contacts:
                if item[2] == phone_number:
                    print(f"\nRegistro: {item[0]} --> Nombre: {item[1]}, teléfono: {item[2]}")

        if s == "N":
            contact_name = str(input("Indica el nombre del contacto: "))
            for item in self.contacts:
                if item[1] == contact_name:
                    print(f"\nRegistro: {item[0]} --> Nombre: {item[1]}, teléfono: {item[2]}")

        if s == "R":
            self.register = int(input("Indica el número de registro: "))
            for item in self.contacts:
                if item[0] == self.register:
                    print(f"\nRegistro: {item[0]} --> Nombre: {item[1]}, teléfono: {item[2]}")

    def update(self):
        """
        Método para modificar el registro indicado
        """
        self.search("R")
        change = str(input("\n¿Qué quieres cambiar? (P: teléfono, N: nombre, A: todo): ")).upper()

        if change == "N":
            new_name = str(input("Indica el nuevo nombre: "))
            self.contacts[self.register - 1][1] = new_name
            print("\nRegistro actualizado")
            print(f"\nRegistro: {self.contacts[self.register - 1][0]} --> \
                  Nombre: {self.contacts[self.register - 1][1]}, \
                    teléfono: {self.contacts[self.register - 1][2]}")

        if change == "P":
            new_phone = str(input("Indica el nuevo teléfono: "))
            self.contacts[self.register - 1][2] = new_phone
            print("\nRegistro actualizado")
            print(f"\nRegistro: {self.contacts[self.register - 1][0]} --> \
                  Nombre: {self.contacts[self.register - 1][1]}, \
                    teléfono: {self.contacts[self.register - 1][2]}")

        if change == "A":
            new_name = str(input("Indica el nuevo nombre: "))
            new_phone = str(input("Indica el nuevo teléfono: "))
            self.contacts[self.register - 1][1] = new_name
            self.contacts[self.register - 1][2] = new_phone
            print("\nRegistro actualizado")
            print(f"\nRegistro: {self.contacts[self.register - 1][0]} --> \
                  Nombre: {self.contacts[self.register - 1][1]}, \
                    teléfono: {self.contacts[self.register - 1][2]}")

    def delete(self):
        """
        Método para eliminar un registro
        """
        self.search("R")
        desition = str(input("\nSeguro que quieres borrar el registro? (Y: sí, N: no): ")).upper()
        if desition == "Y":
            self.contacts.remove(self.contacts[self.register - 1])
            print("\nRegistro eliminado de la agenda")
        else:
            print("\nVeo que lo has pensado mejor")

    def __del__(self):
        """
        Método para borrar la instancia y salir de la aplicación
        """
        print("\nAcabas de destruir el objeto creado para esta agenda")
