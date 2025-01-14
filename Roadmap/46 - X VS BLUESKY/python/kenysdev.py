# _____________________________________
# https://github.com/kenysdev
# 2024 - Python
# _____________________________________
# #46 X VS BLUESKY
# ------------------------------------

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

# ____________________________________________________________________________
import logging
from datetime import datetime
from operator import itemgetter

# ____________
class Posts:
    def __init__(self) -> None:
        self.__post_dt: dict = {}

    def __verify_post(self, id_user: int, id_post, name_func: str) -> bool:
        if id_user not in self.__post_dt:
            logging.error("'%s': El ID %s no tiene posts.", name_func, id_user)
            return False

        if id_post not in self.__post_dt[id_user]:
            logging.error("'%s': El Post (%s) no existe.", name_func, id_post)
            return False

        return True

    def create_post(self, id_user: int, content: str) -> None:
        if len(content) > 200:
            logging.error("'create_post': content > 200 caracteres.")
            return

        if id_user not in self.__post_dt:
            self.__post_dt[id_user] = {}

        id_post = len(self.__post_dt[id_user]) + 1
        self.__post_dt[id_user][id_post] = {
            "content": content,
            "timestamp": datetime.now(),
            "likes": set()
        }

        logging.info("El ID %s creó un post(ID: %s).", id_user, id_post)

    def delete_post(self, id_user: int, id_post: int) -> None:
        if self.__verify_post(id_user, id_post, "delete_post"):
            del self.__post_dt[id_user][id_post]
            logging.info(
                "El post: %s de usuario: %s ha sido eliminado.", id_post, id_user
            )

    def like_post(self, id_user: int, id_author: int, id_post: int) -> None:
        if self.__verify_post(id_author, id_post, "like_post"):
            self.__post_dt[id_author][id_post]["likes"].add(id_user)
            logging.info(
                "El usuario %s dio like al post %s de usuario %s.", 
                id_user, id_post, id_author
            )

    def remove_like(self, id_user: int, id_author: int, id_post: int) -> None:
        if self.__verify_post(id_author, id_post, "remove_like"):
            self.__post_dt[id_author][id_post]["likes"].discard(id_user)
            logging.info(
                "El usuario %s anuló el like al post %s de usuario %s.", 
                id_user, id_post, id_author
            )

    def get_recent_posts(self, id_user: int, limit=10) -> list:
        if id_user in self.__post_dt:        
            sorted_posts: list = sorted(
                self.__post_dt[id_user].values(), 
                key=itemgetter('timestamp'), 
                reverse=True
            )

            return sorted_posts[:limit]
        
        return []

# ____________
class Users:
    def __init__(self) -> None:
        self.__users_dt: dict = {}
    
    def __id_exists(self, id_: int, name_func: str = "") -> bool:
        if id_ in self.__users_dt:
            return True

        logging.warning("'%s': ID: %s no encontrada.", name_func, id_)
        return False
    
    def add_user(self, name) -> None:
        id_ = len(self.__users_dt) + 1
        self.__users_dt[id_] = {
            "name": name,
            "following": set(),
            "followers": set(),
        }

        logging.info("Usuario %s-%s registrado.", id_, name)

    def follow_user(self, id_: int, to_id: int) -> None:
        if (
            self.__id_exists(id_, "follow_user")
            and self.__id_exists(to_id, "follow_user")
        ):
            self.__users_dt[id_]["following"].add(to_id)
            self.__users_dt[to_id]["followers"].add(id_)
            logging.info("ID: %s está siguiendo a ID: %s.", id_, to_id)

    def unfollow_user(self, id_: int, to_id: int) -> None:
        if (
            self.__id_exists(id_, "unfollow_use") 
            and self.__id_exists(to_id, "unfollow_use")
        ):
            self.__users_dt[id_]["following"].discard(to_id)
            self.__users_dt[to_id]["followers"].discard(id_)
            logging.info("El ID: %s dejó de seguir al ID: %s.", id_, to_id)

    def get_name(self, id_user: int) -> str:
        if self.__id_exists(id_user, "get_name"):
            return self.__users_dt[id_user]["name"]

        return ""

# ____________________________________________________________________________
# ____________
class Program:
    def __init__(self, posts, users) -> None:
        self.__posts = posts()
        self.__users = users()

    def __print_feed(self, id_user: int):
        name: str = self.__users.get_name(id_user)
        if not name:
            print(f"Usuario ID: {id_user} no encontrado.")
            return

        last_10: dict = self.__posts.get_recent_posts(id_user, limit=10)
        print(f"\nFeed\n_______\nID: '{id_user}' - Nombre: '{name}'")
        if not last_10:
            print("No tiene publicaciones.")
            return
        for post in last_10:
            print(f"_______\n{post['content']}")
            print(f"Creado: '{post['timestamp']}'")
            print(f"Likes: '{len(post['likes'])}'")
    
    def run(self):
        # CLI
        pass

    def tests(self):
        self.__users.add_user(name="Ken") # id=1
        self.__users.add_user("Zoe") # id=2

        self.__users.follow_user(id_=1, to_id=2)
        self.__users.follow_user(2, 1)
        self.__users.unfollow_user(2, 1)

        self.__posts.create_post(id_user=2, content="Primer post.") # id=1
        self.__posts.create_post(2, "Segundo post.") # id=2
        self.__posts.delete_post(id_user=2, id_post=2)
        self.__posts.create_post(2, "Otro post.") # id=2
        self.__posts.like_post(id_user=1, id_author=2, id_post=1)
        self.__posts.remove_like(1, 2, 1)
        self.__posts.like_post(1, 2, 2)

        self.__print_feed(id_user=2)
        self.__print_feed(id_user=1)

# ____________
if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG, 
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    program = Program(Posts, Users)
    program.tests()
    #program.run()
