###############################################################################
### EJERCICIO
###############################################################################
# Una clase que gestiona 3 responsabilidades, sin aplicar SRP.
class shop:
    """
    Una clase que gestiona las diferentes responsabilidades de una tienda.
    """
    def __init__(self):
        self.products = {}
    
    def add_product(self, product:str, price:str, amount:int):
        """
        Agrega un producto a la tienda
        """
        self.products[product] = (price, amount)
    
    def del_product(self, product:str):
        """
        Elimina un producto de la tienda
        """
        if product in self.products:
            del self.products[product]
        else:
            print(f"El producto {product} no existe en la tienda.")
    
    def search_product(self, product:str):
        """
        Busca si un producto en la tienda
        """
        if product in self.products:
            return self.products[product]
        else:
            print(f"El producto {product} no existe en la tienda.")



# Refactorizamos aplicando SRP, separando las tres responsabilidades en diferentes clases.
class Shop:
    """
    Responsabilidad de los productos de la tienda
    """
    def __init__(self):
        self.products = {}

        
class AddProduct:
    """
    Responsabilidad de agregar un producto a la tienda
    """ 
    @staticmethod
    def add_product(shop: Shop, product:str, price:str, amount:int):
        Shop.products[product] = (price, amount)


class DelProduct:
    """
    Responsabilidad de borrar un producto de la tienda
    """
    @staticmethod
    def del_product(shop: Shop, product:str):
        if product in Shop.products:
            del Shop.products[product]
        else:
            print(f"El producto {product} no existe en la tienda.")


class SearchProduct: 
    """
    Responsabilidad de buscar si un producto esta en la tienda
    """
    @staticmethod   
    def search_product(shop: Shop, product:str):
        if product in Shop.products:
            return Shop.products[product]
        else:
            print(f"El producto {product} no existe en la tienda.")




###############################################################################
### DIFICULTAD EXTRA
###############################################################################
import logging

logging.basicConfig(level=logging.INFO)


class Library:
    """
    Registro de libros y usuarios de la biblioteca
    """
    def __init__(self):
        self.books = {}
        self.users = {}
        self.books_loaned = {}


class RegisterBooks:
    """
    Registra un libro en la biblioteca
    """
    @staticmethod
    def register_book(library: Library, title: str, author: str, amount: int):
        library.books[title] = [author, amount]
        logging.info(f"Book '{title}' by {author} has been registered with {amount} copies.")


class RegisterUser:
    """
    Registra a un usuario en la base de datos
    """
    def register_user(library: Library, user_name: str, user_id: int, email: str):
        library.users[user_name] = [user_id, email]
        logging.info(f"User '{user_name}' has been registered with ID {user_id} and email {email}.")


class LoanBooks:
    """
    Presta un libro a un usuario
    """
    @staticmethod
    def loan(library: Library, title, user_name):
        if title not in library.books:
            logging.info(f"The book '{title}' is not available in the library.")
            return
        if library.books[title][1] <= 0:
            logging.info(f"No copies of the book '{title}' are available.")
            return
        if user_name not in library.users:
            logging.info(f"The user '{user_name}' is not registered.")
            return       
        library.books_loaned[title] = user_name
        library.books[title][1] -= 1
        logging.info(f'The book "{title}" has been loaned to "{user_name}".')
        logging.info(f'{title}: {library.books[title]}')


class GiveBack:
    """
    Devuelve un libro prestado
    """
    @staticmethod
    def give_back(library: Library, title, user_name):
        if title not in library.books_loaned:
            logging.info(f'The book "{title}" is not currently loaned.')
            return
        if library.books_loaned[title] != user_name:
            logging.info(f'The book "{title}" was not loaned to "{user_name}".')
            return
        del library.books_loaned[title]
        library.books[title][1] += 1
        logging.info(f'The book "{title}" has been returned by "{user_name}".')
        logging.info(f'{title}: {library.books[title]}')
   

# Creamos nuestra biblioteca
mi_biblioteca = Library()
# Registramos un libro
RegisterBooks.register_book(mi_biblioteca, 'Atomic Habits', 'James Clear', 5)
# Registramos a un usuario
RegisterUser.register_user(mi_biblioteca, 'Dani', 1, 'dani@gmail.com')
# Le prestamos un libro
LoanBooks.loan(mi_biblioteca, 'Atomic Habits', 'Dani')
# Devuelve el libro
GiveBack.give_back(mi_biblioteca, 'Atomic Habits', 'Dani')