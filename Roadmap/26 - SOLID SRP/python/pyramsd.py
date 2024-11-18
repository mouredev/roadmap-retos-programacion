# USO CORRECTO
class Order:
    def __init__(self, order_id, items):
        self.order_id = order_id
        self.items = items

    def calculate_total(self):
        total = sum(item.price for item in self.items)
        return total

class OrderRepository:
    def save(self, order):
        # Código para guardar la orden en la base de datos
        pass

class OrderEmailer:
    def send_confirmation_email(self, order):
        # Código para enviar un email de confirmación al cliente
        pass


class Items:
    def __init__(self, name: str, price: int) -> None:
        self.name: str = name
        self.price: str = price

item1 = Items("Agenda", 20)
item2 = Items("Libro", 10)
item3 = Items("Cuaderno", 30)

order = Order(order_id=1, items=[item1, item2, item3])

total = order.calculate_total()
print(total)

order_repo = OrderRepository()
order_repo.save(order)

emalier = OrderEmailer()
emalier.send_confirmation_email(order)

# USO INCORRECTO
class Order:
    def __init__(self, order_id, items):
        self.order_id = order_id
        self.items = items

    def calculate_total(self):
        total = sum(item.price for item in self.items)
        return total

    def save_to_database(self):
        # Código para guardar la orden en la base de datos
        pass

    def send_confirmation_email(self):
        # Código para enviar un email de confirmación al cliente
        pass


"""
EXTRA
"""
# USO INCORRECTO
class Library:
    def __init__(self) -> None:
        self.libros: list[dict] = []
        self.usuarios: list[dict] = []
        self.prestamos: dict = {}


    def registrar_libros(self, titulo: str, autor: str, copias: int) -> None:
        libro = {"Titulo":titulo, "Autor":autor, "Copias":copias}
        self.libros.append(libro)

    def registrar_usuario(self, nombre: str, user_id: int, email: str) -> None:
        usuario = {"Nombre":nombre, "ID":user_id, "Email":email}
        self.usuarios.append(usuario)

    def prestar_libro(self, user_id: int, titulo_libro: str) -> bool:
        for libro in self.libros:
            if libro["Titulo"] == titulo_libro and libro["Copias"] > 0:
                self.prestamos[user_id] = titulo_libro
                libro["Copias"] -= 1
                return True
        return False
    
    def devolver_libro(self, user_id: int) -> bool:
        if user_id in self.prestamos:
            titulo_libro = self.prestamos.pop(user_id)
            for libro in self.libros:
                if libro["Titulo"] == titulo_libro:
                    libro["Copias"] += 1
                    return True
        return False
    

libreria = Library()
libreria.registrar_libros("La pata del pato", "Sergio Ruiz", 10)
libreria.registrar_usuario("Maicol", 5, "maicol@gmail.com")
print(libreria.libros)
libreria.prestar_libro(5, "La pata del pato")
print(libreria.libros)
print(libreria.usuarios)
print(libreria.prestamos)
libreria.devolver_libro(5)
print(libreria.libros)


# USO CORRECTO
class Libro:
    def __init__(self) -> None:
        self.libros: dict = {}

    def registrar_libro(self, titulo: str, autor: str, copias: int):
        if titulo in self.libros:
            print(f"Titulo {titulo} ya existe")
            return
        self.libros[titulo] = {"Autor": autor,
                                 "Copias": copias}
        print(f"Titulo {titulo} fue agregado correctamente")

    def buscar_libro(self, titulo: str):
        for titulos, libro in self.libros.items():
            if titulos == titulo:
                return titulos, libro
        print(f"Titulo {titulo} no fue encontrado")


class User:
    def __init__(self) -> None:
        self.usuarios = {}

    def registrar_usuario(self, nombre: str, id: int, email: str):
        if nombre in self.usuarios:
            print(f"Usuario {nombre} ya se encuentra registrado")
            return
        
        self.usuarios[id] = {"nombre": nombre, "Correo": email}
        print(f"Usuario {nombre} fue agregado correctamente")

    def buscar_usuario(self , id: int):
        for ids, user in self.usuarios.items():
            if ids == id:
                return ids, user
        print(f"Identificador {id} no fue encontrado")

class LibraryManager:
    def __init__(self, book_manager, user_manager) -> None:
        self.list_loans = {}
        self.book_manager = book_manager
        self.user_manager = user_manager

    def prestamo(self, id, titulos):
        libro = self.book_manager.buscar_libro(titulos)
        usuario = self.user_manager.buscar_usuario(id)
        if usuario and libro and libro[1]['Copias'] > 0:
            self.list_loans[id] =  titulos
            libro[1]['Copias'] -= 1
            print(f"Libro {titulos} fue prestado al dni {id} y quedan {libro[1]['Copias']} disponibles")
            return
        print(f"Ha ocurrido un error")
    
    def retornar(self, id, titulo):
        for ids, titles in self.list_loans.items():
            if ids == id and titles == titulo:
                del self.list_loans[id]
                book = self.book_manager.buscar_libro(titulo)
                if book:
                    book[1]['Copias']+=1
                    print(f"Libro {titulo} fue devuelto por el id {id}, quedan {book[1]['Copias']} disponibles")
                    return
        print(f"Ha ocurrido un error al retornar el libro")
book_manager = Libro()
book_manager.registrar_libro("La culpa es de la vaca", "Jaime Lopera", 15)
book_manager.registrar_libro("El programador pragmatico", "Andrew Hunt", 20)

user_manager = User()
user_manager.registrar_usuario("alan", 123456, "alan2085@gmail.com")
user_manager.registrar_usuario("matheo", 852963, "matheo0301@gmail.com")

library_manager = LibraryManager(book_manager, user_manager)
library_manager.prestamo(123456, "El programador pragmatico")
library_manager.prestamo(852963, "El programador pragmatico")
library_manager.retornar(123456, "El programador pragmatico")
library_manager.retornar(852963, "El programador pragmatico")