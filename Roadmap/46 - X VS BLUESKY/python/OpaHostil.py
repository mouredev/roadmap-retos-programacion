from random import randint
from datetime import datetime
import os, platform

#Variables globales para simluar la base de datos

posts_repo = {}
users_repo = {}

# Clase Post
class Post:

    # Constructor
    def __init__(self):
        self.__text = None
        self.__creation_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.__likes = 0
        self.__id = self._generate_id()

    # Metodo para generar identificadores aleatorios y unicos
    def _generate_id(self):
        try:
            while True:
                unique_id = randint(1, 20000)
                if unique_id not in posts_repo:
                    posts_repo[unique_id] =  self
                    return unique_id
        except:
            input("Numero maximo de post publicados.\nPulsa una tecla para volver al menu de inicio.")
    
    # Metodos getters y setters del texto
    def _get_text(self):
        return self.__text
    
    def _set_text(self, text):
        self.__text = text
    
    def _get_likes(self):
        return self.__likes
    
    def _set_likes(self):
        self.__likes += 1
    
    def _get_id(self):
        return self.__id

    def _get_creation_date(self):
        return self.__creation_date
    
    # Metodo para imprimir los datos de un post que nos solicitan
    def _print_post(self):
        return f"Text: {self._get_text()}\nCreacion: {self._get_creation_date()}\nLikes: {self._get_likes()}"

# Clase User
class User:

    #Constructor
    def __init__(self, name):
        self.__name = name
        self.__id = self._generate_id()
        self.__follows = list()
        self.__posts = list()
    
    # Metodo para generar identificadores aleatorios y unicos
    def _generate_id(self):
        try:
            while True:
                unique_id = randint(1,2000)
                if unique_id not in users_repo:
                    users_repo[unique_id] = self
                    return unique_id
        except:
            clean_console()
            print("Numero maximo de usuarios permitidos")
            input("Pulsa una tecla para volver al menu inicial")

    # Metodos getters       
    def _get_id(self):
        return self.__id
            
    def _get_name(self):
        return self.__name
    
    def _get_posts(self):
        return self.__posts

    def _get_follows(self):
        return self.__follows

    # Funcion para añadir un post
    def _add_post(self, post):
        self.__posts.append(post)
    
    def _add_follows(self, user):
        self.__follows.append(user)

    # Metodo para imprimir datos del usuario
    def _print_user(self):
        return f"ID usuario: {self._get_id()}\nName: {self._get_name()}\nFollows: {self._get_follows()}\nPosts: {self._get_posts()}"

# Funcion menu inicial
def welcome_menu():

    clean_console()
    print("Bienvenido a MoureXSky\n\n1. Iniciar sesion\n2. Crear usuario\n3. Cerrar sesion\n")
    opcion = input("Elige una opcion: ")
    if opcion == "1":
        login_user()
    elif opcion == "2":
        create_user()
    elif opcion == "3":
        clean_console()
        print("Hasta pronto! Recuerda lavarte las manos despues de mear")
        quit()
    elif opcion == "4":
        print(users_repo)
        input()
    else:
        print("Opcion incorrecta.")
        input("Pulsa cualquier tecla para volver al menu.. ")
        
# Funcion para crear usuario
def create_user():
    clean_console()
    name = input("Introduce nombre: ")
    if search_user(name):
        input("Usuario en uso. Pulse una tecla para volver al menu.. ")
    else:
        user = User(name)
        input(f"Usuario {user._get_name()} creado satisfactoriamente con el ID {user._get_id()}")
 
# Funcion para buscar usuario en el diccionario
def search_user(name):
    for user in users_repo.values():
        if user._get_name() == name:
            return user
    return False    
    
# Funcion para limpiar cl
def clean_console():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clean")

# Funcion de login
def login_user():
    clean_console()
    name = input("Introduce usuario: ")
    user = search_user(name)
    if not user:
        input("No se encuentra el usuario. Pulse una tecla para volver al menu")
    else:
        user_menu(user)
        
# Funcion para el Menu de usuario
def user_menu(user : User):
    
    option = 0
    while option != None:
        clean_console()
        print(f"Usuario logado: {user._get_name()}")
        print("1. Crear un post")
        print("2. Eliminar un post")
        print("3. Ver post de un usuario")
        print("4. Ver post de usuarios que sigues")
        print("5. Cerrar sesion usuario\n")
        option = input("Elige una opcion: ")
        if option == "1":
            new_post(user)
        elif option == "2":
            delete_post(user)
        elif option == "3":
            view_user_post(user)
        elif option == "4":
            view_follows_post(user)
        elif option == "5":
            clean_console()
            input("Cerrando sesion de usuario, pulse una tecla para volver al inicio")
            welcome_menu()
        else:
            input("Opcion incorrecta. Pulse una tecla para nueva opcion")
            
# Funcion de crear un post
def new_post(user : User):
    text = input("Escribe el texto del post ( max 200 caracteres, no se tendran en cuenta los caracteries que superen ): \n"[:200])
    post = Post()
    post._set_text(text)
    user._add_post(post)
    clean_console()
    post._print_post()
    input(f"Añadido post con ID {post._get_id()} al usuario {user._get_name()}\n ")

# Funcion para ver los post de un usuario
def view_user_post(user_logado : User):
    clean_console()
    name = input("Introduce el usuario del que quieres ver los post: ")
    user = search_user(name)
    if user:
        for index, post in enumerate(reversed(user._get_posts())):
            if index == 10:
                break
            print(f"ID Usuaio: {user._get_id()}\nNombre Usuario: {user._get_name()}\nText: {post._get_text()}\nFecha de creacion: {post._get_creation_date()}\nLikes: {post._get_likes()}")
            choice = input("Quieres darle like al post?(s/n): ")
            if choice.upper() == 'S':
                post._set_likes()
            clean_console()
        choice = input("Te gustaria seguir a este usuario?(s/n): ")
        if choice.upper() == 'S':
            user_logado._add_follows(user)
    else:
        input("Usuario no encontrado, pulsa una tecla para volver al menu")
    
# Funcion Eliminar post
def delete_post(user):
    clean_console()
    print("Estos son los post que tienes:")
    for post in user._get_posts():
        print(f"ID: {post._get_id()} - Breve texto: {post._get_text()[:20]}...")
    while True:
        try:
            id = int(input("Introduce el ID del post que quieres eliminar, 0 para salir sin borrar ninguno: "))
            if id == 0:
                break
            elif not int(id) in posts_repo.keys():
                print("El Id introducino no corresponde a ningun post.")
            else:
                del posts_repo[id]
                for post in user._get_posts():
                    if id == post._get_id():
                        user._get_posts().remove(post)         
                input("Post eliminado, Pulsa cualquie tecla para volver al menu.")
                break
        except ValueError:
            input("Valor introducido no soportado. Pulsa una tecla para intentarlo de nuevo")

# Funcion para ver post de follows
def view_follows_post(user : User):

    followers_list = user._get_follows()
    for index, follower_user in enumerate(reversed(followers_list)):
        if index == 10:
            break
        print("---------------------------------")
        print(f"Post del usuario {follower_user._get_name()}:")
        print("---------------------------------")
        for follower_post in follower_user._get_posts():
            print(follower_post._print_post())
            print("---------------------------------")
    input("Pulsa cualquier tecla para volver al menu.")

    
# Inicio de aplicacion
while True:
    welcome_menu()