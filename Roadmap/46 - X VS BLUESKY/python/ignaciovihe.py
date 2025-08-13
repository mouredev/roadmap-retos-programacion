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

# =========================
# Estrategias de búsqueda
# =========================
class PostSearchStrategy(ABC):
    @abstractmethod
    def get_posts(self, users: list[User], **filters) -> list[Post]:
        pass

class AllPostsStrategy(PostSearchStrategy):
    def get_posts(self, users: list[User], **filters) -> list[Post]:
        result = []
        for user in users:
            result.extend(user.posts.values())
        return list(reversed(result))

class LastTenPostsStrategy(PostSearchStrategy):
    def get_posts(self, users: list[User], **filters) -> list[Post]:
        result = []
        for user in users:
            result.extend(user.posts.values())
        sorted_result = sorted(result, key=lambda i: i.date, reverse=True)
        return sorted_result[:10]

class OneSinglePostStrategy(PostSearchStrategy):
    def get_posts(self, users: list[User], **filters) -> list[Post]:
        id_post = filters.get("id_post")
        if not id_post:
            return []
        result = []
        for user in users:
            result.extend(user.posts.values())
        for post in result:
            if post.id == uuid.UUID(id_post):
                return [post]
        return []

class LikedPostStrategy(PostSearchStrategy):
    def get_posts(self, users: list[User], **filters) -> list[Post]:
        result = []
        for user in users:
            result.extend(user.likes.values())
        return result


# =========================
# Funciones de utilidad
# =========================
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    input("ENTER para continuar")


# =========================
# Entidades
# =========================
class User:
    def __init__(self, name: str) -> None:
        self.name = name
        self.following = dict()
        self.followers = dict()
        self.posts = dict()
        self.likes = dict()

class Post:
    def __init__(self, user_id, text: str) -> None:
        self.id = uuid.uuid4()
        self.user_id = user_id
        self.date = datetime.now()
        self.text = text
        self.likes = []


# =========================
# Lógica de negocio de posts
# =========================
class PostService:
    def __init__(self, user: User):
        self.user = user

    def create_post(self, text: str) -> Post:
        if not (0 < len(text) < 200):
            raise ValueError("El texto debe tener entre 1 y 200 caracteres.")
        new_post = Post(self.user.name, text)
        self.user.posts[new_post.id] = new_post
        return new_post

    def delete_post(self, post_id: uuid.UUID) -> bool:
        if post_id in self.user.posts:
            del self.user.posts[post_id]
            return True
        return False

    def like_post(self, post: Post) -> bool:
        post_id_str = str(post.id)
        if post_id_str not in self.user.likes:
            post.likes.append(self.user.name)
            self.user.likes[post_id_str] = post
            return True
        return False

    def unlike_post(self, post: Post) -> bool:
        post_id_str = str(post.id)
        if post_id_str in self.user.likes:
            del self.user.likes[post_id_str]
            if self.user.name in post.likes:
                post.likes.remove(self.user.name)
            return True
        return False


# =========================
# Presentación en consola de posts
# =========================
class PostConsoleUI:

    def show_posts(self, posts: list[Post]):
        if not posts:
            print("No hay posts para mostrar.")
            return
        for post in posts:
            print(f"{'Post id: ' + str(post.id):<50}   {'Usuario:' + post.user_id:>47}")
            for line in textwrap.wrap(post.text, width=100):
                print(f"{line:<100}")
            print(f"{str(post.date):<50}   {'Likes:' + str(len(post.likes)):>47}")
            print("=" * 100)


# =========================
# Gestión de usuarios
# =========================
class UserManager:
    def __init__(self) -> None:
        self.users = dict()

    def register_user(self, user_name: str):
        new_user = User(user_name)
        self.users[new_user.name] = new_user
        print(f"Usuario con nombre {user_name} registrado con éxito.")

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


# =========================
# Gestión de sesión
# =========================
class SessionManager:
    def __init__(self, user_manager: UserManager) -> None:
        self.user_manager = user_manager

    def register_new_user(self):
        user_name = ""
        while not user_name or user_name in self.user_manager.users:
            user_name = input("Introduce un nombre de usuario nuevo a registrar: ")
            if not user_name:
                print("El nombre de usuario no puede estar vacío. Elige otro.")
            if user_name in self.user_manager.users:
                print("El nombre de usuario ya existe. Elige otro.")
        self.user_manager.register_user(user_name)
        pausar()

    def start_new_session(self):
        if not self.user_manager.users:
            print("Todavía no hay usuarios registrados. Registra uno primero.")
            pausar()
            return
        user_name = ""
        while not user_name or user_name not in self.user_manager.users:
            user_name = input("Introduce un nombre de usuario con el que iniciar sesión: ")
            if not user_name:
                print("El nombre de usuario no puede estar vacío. Elige otro.")
            if user_name not in self.user_manager.users:
                print("El nombre de usuario no existe. Elige otro o crea uno nuevo.")
                option = "0"
                while option not in ["1", "2"]:
                    print("\t1. Probar otro nombre")
                    print("\t2. Registrar nuevo usuario")
                    option = input("Introduce una opción correcta: ")
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
                option = input("Introduce una opción correcta:  ")
            
            match option:
                case "1":
                    active_name = self.start_new_session()
                    if active_name:
                        return self.user_manager.get_user(active_name)
                case "2":
                    self.register_new_user()
                case "3":
                    return None


# =========================
# Gestión de seguidores
# =========================
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
                    f"{'(tú)' if found_user.name == self.active_user.name else ''} "
                    f"{'(ya seguido)' if found_user.name in self.active_user.following else ''} "
                )
            option = "0"
            valid_options = [str(i) for i in range(1, len(results) + 1)]
            while option not in valid_options:
                option = input("Introduce una opción válida: ")
            selected_user = results[int(option) - 1]
            if selected_user.name != self.active_user.name:
                if selected_user.name not in self.active_user.following:
                    self.active_user.following[selected_user.name] = selected_user
                    selected_user.followers[self.active_user.name] = self.active_user
                    print(f"{self.active_user.name} ahora sigue a {selected_user.name}.")
                else:
                    print("Ya sigues a ese usuario.")
            else:
                print("No puedes seguirte a ti mismo.")
        else:
            print("No hay usuarios que coincidan con el nombre introducido")
        pausar()

    def unfollow_user(self):
        if self.active_user.following:
            for i, (name, user) in enumerate(self.active_user.following.items()):
                print(
                    f"{i + 1} - {user.name} "
                    f"{'(tú)' if user.name == self.active_user.name else ''} "
                    f"{'(ya seguido)' if user.name in self.active_user.following else ''} "
                )
            option = "0"
            valid_options = [str(i) for i in range(1, len(self.active_user.following) + 1)]
            while option not in valid_options:
                option = input("Introduce una opción válida: ")
            selected_user = list(self.active_user.following.values())[int(option) - 1]
            del self.active_user.following[selected_user.name]
            del selected_user.followers[self.active_user.name]
            print(f"{self.active_user.name} ya no sigue a {selected_user.name}.")
        else:
            print("Todavía no sigues a nadie.")
        pausar()


# =========================
# Sesión activa
# =========================
class ActiveSession:
    def __init__(self, user: User, user_manager: UserManager) -> None:
        self.user = user
        self.user_manager = user_manager
        self.post_service = PostService(self.user)
        self.post_ui = PostConsoleUI()
        self.followers_manager = FollowersManager(self.user, self.user_manager)

    def show_menu(self):
        clear_console()
        print(f"Sesión iniciada como: {self.user.name} - Followers: {len(self.user.followers)}")
        print()
        print("\t1. Crear nuevo post.")
        print("\t2. Borrar post.")
        print("\t3. Ver post propios.")
        print("\t4. Ver post de usuarios seguidos.")
        print("\t5. Eliminar like.")
        print("\t6. Seguir usuario.")
        print("\t7. Dejar de seguir usuario")
        print("\t8. Cerrar sesión.")
        print("\t9. Salir")

        option = "0"
        while option not in map(str, range(1, 10)):
            option = input("Introduce una opción correcta: ")

        return option


# =========================
# Aplicación principal
# =========================
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
                    text = input("Introduce el texto del post: ")
                    try:
                        session.post_service.create_post(text)
                        print("Post creado con éxito.")
                    except ValueError as e:
                        print(e)
                    pausar()

                case "2":
                    posts = AllPostsStrategy().get_posts([self.active_user])
                    session.post_ui.show_posts(posts)
                    id_post = input("Introduce el id del post a borrar: ")
                    try:
                        if session.post_service.delete_post(uuid.UUID(id_post)):
                            print("Post borrado con éxito.")
                        else:
                            print("No se encontró un post con ese ID.")
                    except Exception:
                        print("ID inválido.")
                    pausar()

                case "3":
                    posts = LastTenPostsStrategy().get_posts([self.active_user])
                    session.post_ui.show_posts(posts)
                    pausar()

                case "4":
                    posts = LastTenPostsStrategy().get_posts(list(self.active_user.following.values()))
                    session.post_ui.show_posts(posts)
                    option_like = input("¿Quieres darle like a algún post? (s/n): ")
                    if option_like.lower() == "s":
                        id_post = input("Introduce el id del post a dar like: ")
                        found = OneSinglePostStrategy().get_posts(list(self.user_manager.users.values()), id_post=id_post)
                        if found:
                            if session.post_service.like_post(found[0]):
                                print("Like realizado con éxito.")
                            else:
                                print("Ya habías dado like a este post.")
                        else:
                            print("No se encontró el post.")
                    pausar()

                case "5":
                    posts = LikedPostStrategy().get_posts([self.active_user])
                    session.post_ui.show_posts(posts)
                    id_post = input("Introduce el id del post para quitar el like: ")
                    found = OneSinglePostStrategy().get_posts(list(self.user_manager.users.values()), id_post=id_post)
                    if found:
                        if session.post_service.unlike_post(found[0]):
                            print("Like eliminado con éxito.")
                        else:
                            print("No tenías like en este post.")
                    pausar()

                case "6":
                    session.followers_manager.follow_user()

                case "7":
                    session.followers_manager.unfollow_user()

                case "8":
                    self.active_user = None

                case "9":
                    return True


# =========================
# Ejecución
# =========================
my_social_network = SocialNetwork()
finish = False
while not finish:
    while not my_social_network.active_user and not finish:
        finish = my_social_network.log_in()

    while my_social_network.active_user and not finish:
        finish = my_social_network.run_program()