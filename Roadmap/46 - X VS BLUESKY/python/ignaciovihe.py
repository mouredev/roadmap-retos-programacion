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
from __future__ import annotations
import uuid
from datetime import datetime
import os
import textwrap
from abc import ABC, abstractmethod

class PostSearchStrategy(ABC):
    @abstractmethod
    def get_posts(self, users: list["User"]) -> list["Post"]: # forward references, permite anotaciones de tipo de clases definidas mas anajo con ""
        pass

class AllPostsStrategy(PostSearchStrategy):
    def get_posts(self, users: list[User]) -> list[Post]:# Al haber importado "from __future__ import annotations" puedo ponerlo sin comillas.
        result = []
        for user in users:
            result = list(user.posts.values())
        return list(reversed(result))
    
class LastTenPostsStrategy(PostSearchStrategy):
    def get_posts(self, users: list["User"]) -> list["Post"]:
        result = []
        for user in users:
            result.extend(list(user.posts.values()))
        sorted_result = sorted(result ,key= lambda i: i.date, reverse=True)
        return sorted_result[0:10]
    
class OneSinglePostStrategy(PostSearchStrategy):
    def get_posts(self, users: list[User], id_post: str) -> list[Post]:
        result = []
        for user in users:
            result.extend(list(user.posts.values()))
        for post in result:
            if post.id == uuid.UUID(id_post):
                return [post]
            else:
                print("No hay ningun post que coincida con el id pasado.")
        return []




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
        self.likes = dict()


class Post:
    def __init__(self, user_id, text: str ) -> None:
        self.id = uuid.uuid4()
        self.user_id = user_id
        self.date = datetime.now()
        self.text = text
        self.likes = []


class UserManager:
    def __init__(self) -> None:
        self.users = dict()

    def register_user(self, user_name: str):
        new_user = User(user_name)
        self.users[new_user.name] = new_user
        print(f"Usuario con nombre {user_name} registrado con exito.")

    def get_user(self, user_name):
        return self.users[user_name]
    
    def search_users(self, name: str):
        results = []
        for id, user in self.users.items():
            if name:
                if name in id:
                    results.append(user)
            else:
                results.append(user)
        return results


class SessionManager:
    def __init__(self, user_manager: UserManager) -> None:
        self.user_manager = user_manager

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
    
    def log_in(self):
        while True:
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
                        return self.user_manager.get_user(active_name)

                case "2":
                    self.register_new_user()

                case "3":
                    return None
                

class ActiveSession:
    def __init__(self, user: User, user_manager: UserManager) -> None:
        self.user = user
        self.user_manager = user_manager
        self.posts_manager = PostsManager(self.user)
        self.followers_manager = FollowersManager(self.user, self.user_manager)

    def show_menu(self):
        clear_console()
        print(f"Sesion iniciada como: {self.user.name} - Followers: {len(self.user.followers)}")
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

        return option


class PostsManager:
    def __init__(self, user: User) -> None:
        self.active_user = user

    def show_posts(self, users: list[User], search_strategy: PostSearchStrategy):
        posts = search_strategy.get_posts(users)
        if posts:
            for post in posts:
                print(f"{'Post id: ' + str(post.id):<50}   {'Usuario:' + post.user_id:>47}")
                # Envolver el texto en líneas de 100 caracteres
                for line in textwrap.wrap(post.text, width=100):
                    print(f"{line:<{100}}")
                print(f"{str(post.date):<50}   {'Likes:' + str(len(post.likes)):>47}")
                print(f"{'=' * 100}")
            
        else:
            print("EL usuario no tiene mensajes que mostrar.")
        


    def create_post(self):
        while True:
            post_text = input("Introduce el texto del post. Debe ser entre 1 y 200 caracteres: ")
            if 0 < len(post_text) < 200:
                break
            else:
                print(f"Has escrito {len(post_text)} caracteres. Copia el mensaje y vuelve a intenetarlo.")
                print()
                print(post_text)
        new_post = Post(self.active_user.name, post_text)
        self.active_user.posts[new_post.id] = new_post
        print(f"El usuario {self.active_user.name} ha añadidio un nuevo post.")
        pausar()

    def delete_post(self):
        if not self.active_user.posts:
            print("El usuario activo todavia no ha escrito ningun post")
            pausar()
            return
        self.show_posts([self.active_user], AllPostsStrategy())
        id_post = input("Introduce el id del post a borrar. Copialo y pegalo para evitar fallos: ")
        try:
            id_post = uuid.UUID(id_post)
        
            if id_post in self.active_user.posts:
                del self.active_user.posts[id_post]
                print("Mensaje borrado con exito.")
            else:
                print("El id no coincide con ningun mensaje.")
        except Exception as e:
            print("El id no coincide con ningun mensaje.")
        pausar()

    def like_post(self, user_manager: UserManager):
        if self.active_user.following:
            option = "0"
            print("Quieres darle like a algun post?")
            print("1 - Si")
            print("2 - NO")
            while option not in ["1", "2"]:
                option = input("Introduce una opcion correcta: ")
            if option == "1":
                id =" "
                while id:
                    id = input("Introduce el id del post a dar like, o pulsa ENTER para volver al menu.")
                    if id not in self.active_user.likes:
                        if id:
                            post = OneSinglePostStrategy().get_posts(list(user_manager.users.values()), id)
                            if post:
                                liked_post = post[0]
                                liked_post.likes.append(self.active_user)
                                self.active_user.likes[id] = liked_post
                                print("'Like' realizado con exito")
                    else:
                        print("Ya te gusta ese post.")
                        pausar()
        else:
            pausar()
                    



class FollowersManager:
    def __init__(self, user: User, user_manager: UserManager) -> None:
        self.active_user = user
        self.user_manager = user_manager

    def follow_user(self):
        print("Introduce un nombre de usuario a buscar.")
        user_name_to_search = input("Puedes escribir parte del nombre, o no escribir nada para buscar todos los usuarios: ")
        results: list[User] = self.user_manager.search_users(user_name_to_search)
        if results:
            for i, found_user in enumerate(results):
                print(
                    f"{i + 1} - {found_user.name} "
                    f"{"(tú)" if found_user.name == self.active_user.name else ""} "
                    f"{"(ya seguido)" if found_user.name in self.active_user.following else ""} "
                )
            option = "0"
            valid_options = [str(i) for i in range(1, len(results) + 1)]
            while option not in valid_options:
                option = input("Introduce una opcion válida: ")
            selected_user = results[int(option) - 1]
            if selected_user.name != self.active_user.name:
                if selected_user.name not in self.active_user.following:
                    self.active_user.following[selected_user.name] = selected_user
                    selected_user.followers[self.active_user.name] = self.active_user
                    print(f"{self.active_user.name} ahora sigue a {selected_user.name}.")
                else:
                    print("Ya sigues a ese usuario.")
            else:
                print("No puedes segirte a ti mismo.")
        else:
            print("No hay usuarios que coincidan con el nomre introducido")
        pausar()

    def unfollow_user(self):
        if self.active_user.following:
            for i, (name, user) in enumerate(self.active_user.following.items()):
                print(
                    f"{i + 1} - {user.name} "
                    f"{"(tú)" if user.name == self.active_user.name else ""} "
                    f"{"(ya seguido)" if user.name in self.active_user.following else ""} "
                )
            option = "0"
            valid_options = [str(i) for i in range(1, len(self.active_user.following) + 1)]
            while option not in valid_options:
                option = input("Introduce una opcion válida: ")
            selected_user = list(self.active_user.following.values())[int(option) - 1]
            del(self.active_user.following[selected_user.name])
            del(selected_user.followers[self.active_user.name])
            print(f"{self.active_user.name} ya no sigue {selected_user.name}.")
        else:
            print("Todavía no sigues a nadie.")
        pausar()


class SocialNetwork:
    def __init__(self) -> None:
        self.user_manager = UserManager()
        self.session_manager = SessionManager(self.user_manager)
        self.active_user: User | None = None

    def log_in(self):
        self.active_user = self.session_manager.log_in()
        return self.active_user is None
                
    def run_program(self):
        if self.active_user:
            session = ActiveSession(self.active_user, self.user_manager)
            option = session.show_menu()

            match option:
                case "1":
                    session.posts_manager.create_post()

                case "2":
                    session.posts_manager.delete_post()

                case "3":
                    session.posts_manager.show_posts([self.active_user], LastTenPostsStrategy())
                    pausar()

                case "4":
                    session.posts_manager.show_posts(list(self.active_user.following.values()), LastTenPostsStrategy())
                    session.posts_manager.like_post(self.user_manager)

                case "5":
                    session.followers_manager.follow_user()

                case "6":
                    session.followers_manager.unfollow_user()

                case "7":
                    self.active_user = None

                case "8":
                    return True


my_social_network = SocialNetwork()
finish = False
while not finish:
    while not my_social_network.active_user and not finish:
        finish = my_social_network.log_in()

    while my_social_network.active_user and not finish:
        finish = my_social_network.run_program()