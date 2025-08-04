"""
* EJERCICIO:
 * La alternativa descentralizada a X, Bluesky, comienza a atraer
 * a nuevos usuarios. ¿Cómo funciona una red de este estilo?
 * 
 * Implementa un sistema que simule el comportamiento de estas
 * redes sociales.
 * 
 * Debes crear las siguientes operaciones:
 * - Registrar un usuario por nombre e identificador único.
 * - Un usuario puede seguir/dejar de seguir a otro.
 * - Creación de post asociado a un usuario. Debe poseer
 *   texto (200 caracteres máximo), fecha de creación 
 *   e identificador único.   
 * - Eliminación de un post.
 * - Posibilidad de hacer like (y eliminarlo) en un post.
 * - Visualización del feed de un usuario con sus 10 publicaciones
 *   más actuales ordenadas desde la más reciente.
 * - Visualización del feed de un usuario con las 10 publicaciones
 *   más actuales de los usuarios que sigue ordenadas 
 *   desde la más reciente.
 *   
 * Cuando se visualiza un post, debe mostrarse:
 * ID de usuario, nombre de usuario, texto del post, 
 * fecha de creación y número total de likes.
 * 
 * Controla errores en duplicados o acciones no permitidas.
"""
import uuid
from datetime import datetime
import os

def clear_console():
    """
    Limpia la consola, tneiendo en cuenta el sistema operativo.
    """
    os.system('cls' if os.name =='nt' else 'clear')

def pausar():
    input("ENTER para continuar")

class User:
    def __init__(self, name: str) -> None:
        self.name = name # Será el id de ususario
        self.following = dict()
        self.followers = dict()
        self.posts = dict()


class Post:
    def __init__(self, user_id, text: str ) -> None:
        self.id = uuid.uuid4()
        self.user_id = user_id
        self.date = datetime.now()
        self.text = text


class User_Manager:
    def __init__(self) -> None:
        self.users = dict()

    def register_user(self, user_name: str):
        new_user = User(user_name)
        self.users[new_user.name] = new_user
        print(f"Usuario con nombre {user_name} registrado con exito.")

    def get_user(self, user_name):
        return self.users[user_name]


class Posts_manager:
    def __init__(self, user: User) -> None:
        self.user = user

    def create_post(self):
        while True:
            post_text = input("Introduce el texto del post. Debe ser entre 1 y 200 caracteres: ")
            if 0 < len(post_text) < 200:
                break
            else:
                print(f"Has escrito {len(post_text)} caracteres. Copia el mensaje y vuelve a intenetarlo.")
                print()
                print(post_text)
        new_post = Post(self.user.name, post_text)
        self.user.posts[new_post.id] = new_post
        print(f"El ususairo {self.user.name} ha añadidio un nuevo post.")

    def delete_post(self, post_id):
        pass


class Social_Network:
    def __init__(self) -> None:
        self.user_manager = User_Manager()
        self.active_user: User | None = None

    def start_new_session(self):
        if not self.user_manager.users:
            print("Todavia no hay usuarios registrados. Registra uno primero.")
            pausar()
            return
        user_name = ""
        while not user_name or user_name not in self.user_manager.users:
            user_name = input("Introduce un nombre se usuario con el que iniciar sesión: ")
            if not user_name:
                print("El nombre de usuario no puede estar vacio. Elige otro.")
            if user_name not in self.user_manager.users:
                print("El nombre de usuario no existe. Elige otro o crea uno nuevo.")
                option= "0"
                while option not in ["1", "2"]:
                    print("\t1. Probar otro nombre")
                    print("\t2. Registrar nuevo usuario")
                    option = input("Introduce una opcion correcta: ")
                if option == "1":
                    continue
                else:
                    self.register_new_user()
                    user_name = ""

        return user_name

    def register_new_user(self):
        user_name = ""
        while not user_name or user_name in self.user_manager.users:
            user_name = input("Introduce un nombre de usuario nuevo a registrar: ")
            if not user_name:
                print("El nombre de usuario no puede estar vacio. Elige otro.")
            if user_name in self.user_manager.users:
                print("El nombre de usuario ya existe. Elige otro.")
        self.user_manager.register_user(user_name)
        pausar()

    def log_in(self):

        while not self.active_user:
            clear_console()
            print("Bienvenido a 'J' la nueva red social de microblogging.")
            print("\t1. Inicia sesión.")
            print("\t2. Registrar nuevo usuario")
            print("\t3. Salir")
            option = "0"
            while option not in ["1", "2", "3"]:
                option = input("Introduce una opcion correcta:  ")
            
            match option:
                case "1":
                    active_name = self.start_new_session()
                    if active_name:
                        self.active_user = self.user_manager.get_user(active_name)

                case "2":
                    self.register_new_user()

                case "3":
                    return True
                
    def run_program(self):
        clear_console()
        if self.active_user:
            print(f"Sesion iniciada como: {self.active_user.name}")
            print()
            print("\t1. Crear nuevo post.")
            print("\t2. Borrar post.")
            print("\t3. Ver post propios.")
            print("\t4. Ver post de usuarios seguidos.")
            print("\t5. Seguir usuario.")
            print("\t6. Dejar de seguir usuario")
            print("\t7. Cerrar sesión.")
            print("\t8. Salir")

            option = "0"
            while option not in map(str, range(1,9)):
                option = input("Introduce una opcion correcta: ")
            
            match option:
                case "1":
                    pass

                case "2":
                    pass

                case "8":
                    return True


my_social_network = Social_Network()
finish = False
while not finish:
    while not my_social_network.active_user and not finish:
        finish = my_social_network.log_in()

    while my_social_network.active_user and not finish:
        finish = my_social_network.run_program()