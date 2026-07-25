"""
# 46 - Bluesky vs X
"""
# Implementa un sistema que simule el comportamiento de estas redes sociales.
# Debes crear las siguientes operaciones:
    # Registrar un usuario por nombre e identificador único.
    # Un usuario puede seguir/dejar de seguir a otro.
    # Creación de post asociado a un usuario. Debe poseer texto (200 caracteres máximo), fecha de creación e identificador único.  
    # Eliminación de un post.
    # Posibilidad de hacer like (y eliminarlo) en un post.
    # Visualización del feed de un usuario con sus 10 publicaciones más actuales ordenadas desde la más reciente.
    # Visualización del feed de un usuario con las 10 publicaciones más actuales de los usuarios que sigue ordenadas desde la más reciente.
    # Cuando se visualiza un post, debe mostrarse:
    # ID de usuario
    # nombre de usuario
    # texto del post,
    # fecha de creación
    # número total de likes.
# Controla errores en duplicados o acciones no permitidas.
import datetime

class SocialMedia():
    def __init__(self):
        self.users = {} # Id User {name: user name} 
        self.posts = {} # {post: [id, description, created date]}
        self.followers = {} # {user: [# followers]}

    
    def create_user(self):
        username = input("Ingresa tu nombre de usuario: ")

        if username in self.users:
            print(f"Lo sentimos el nombre de usuario {username} no esta disponible")
            return False
        
        user_id = len(self.users) + 1

        self.users[username] = {"id": user_id, "name":username}
        self.followers[username] = []

        print(f"Usuario {username} creado exitosamente con el ID: {user_id}")
        return True
    

    def create_post(self):
        username = input("Ingresa tu usuario: ")

        if username not in self.users:
            print(f"Lo sentimos el usuario {username} no se encuentra registrado")
            return False
        
        post_text = input("Ingresa el post (maximo 200 caracteres): ")

        if len(post_text) > 200:
            print("Lo sentimos el post excede el numero de caracteres. (Maximo 200)")
            return False
        
        post_id = len(self.posts) + 1

        creation_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        self.posts[post_id] = {
            "id": post_id,
            "user_id": self.users[username]["id"],
            "username": username,
            "text": post_text,
            "created_at": creation_date,
            "likes": []
        }

        print(f"Post con ID: {post_id} creado exitosamente.")
        return True
    
    def follow_user(self):
        follower = input("Ingresa tu nombre de usuario: ")
        
        if follower not in self.users:
            print(f"Lo sentimos, el usuario {follower} no existe")
            return False
        
        to_follow = input("Ingresa el nombre del usuario que deseas seguir: ")
        
        if to_follow not in self.users:
            print(f"Lo sentimos, el usuario {to_follow} no existe")
            return False
        
        if follower == to_follow:
            print("No puedes seguirte a ti mismo")
            return False
            
        if to_follow in self.followers[follower]:
            print(f"Ya estás siguiendo a {to_follow}")
            return False
            
        self.followers[follower].append(to_follow)
        print(f"Ahora estás siguiendo a {to_follow}")
        return True
    
    def unfollow_user(self):
        follower = input("Ingresa tu nombre de usuario: ")
        
        if follower not in self.users:
            print(f"Lo sentimos, el usuario {follower} no existe")
            return False
        
        to_unfollow = input("Ingresa el nombre del usuario que deseas dejar de seguir: ")
        
        if to_unfollow not in self.followers[follower]:
            print(f"No estás siguiendo a {to_unfollow}")
            return False
            
        self.followers[follower].remove(to_unfollow)
        print(f"Has dejado de seguir a {to_unfollow}")
        return True
    
    def delete_post(self):
        username = input("Ingresa tu nombre de usuario: ")
        
        if username not in self.users:
            print(f"Lo sentimos, el usuario {username} no existe")
            return False
        
        post_id = input("Ingresa el ID del post que deseas eliminar: ")
        
        try:
            post_id = int(post_id)
        except ValueError:
            print("El ID del post debe ser un número")
            return False
            
        if post_id not in self.posts:
            print(f"El post con ID {post_id} no existe")
            return False
            
        if self.posts[post_id]["username"] != username:
            print("No puedes eliminar un post que no te pertenece")
            return False
            
        del self.posts[post_id]
        print(f"Post con ID {post_id} eliminado exitosamente")
        return True
    
    def like_post(self):
        username = input("Ingresa tu nombre de usuario: ")
        
        if username not in self.users:
            print(f"Lo sentimos, el usuario {username} no existe")
            return False
        
        post_id = input("Ingresa el ID del post que deseas dar like: ")
        
        try:
            post_id = int(post_id)
        except ValueError:
            print("El ID del post debe ser un número")
            return False
            
        if post_id not in self.posts:
            print(f"El post con ID {post_id} no existe")
            return False
            
        if username in self.posts[post_id]["likes"]:
            print("Ya has dado like a este post")
            return False
            
        self.posts[post_id]["likes"].append(username)
        print(f"Has dado like al post con ID {post_id}")
        return True
    
    def unlike_post(self):
        username = input("Ingresa tu nombre de usuario: ")
        
        if username not in self.users:
            print(f"Lo sentimos, el usuario {username} no existe")
            return False
        
        post_id = input("Ingresa el ID del post que deseas quitar like: ")
        
        try:
            post_id = int(post_id)
        except ValueError:
            print("El ID del post debe ser un número")
            return False
            
        if post_id not in self.posts:
            print(f"El post con ID {post_id} no existe")
            return False
            
        if username not in self.posts[post_id]["likes"]:
            print("No has dado like a este post")
            return False
            
        self.posts[post_id]["likes"].remove(username)
        print(f"Has quitado el like al post con ID {post_id}")
        return True
    
    def show_post(self, post_id):
        if post_id not in self.posts:
            print(f"El post con ID {post_id} no existe")
            return False
            
        post = self.posts[post_id]
        print(f"ID de usuario: {post['user_id']}")
        print(f"Nombre de usuario: {post['username']}")
        print(f"Texto: {post['text']}")
        print(f"Fecha de creación: {post['created_at']}")
        print(f"Número de likes: {len(post['likes'])}")
        return True
    
    def user_feed(self):
        username = input("Ingresa tu nombre de usuario: ")
        
        if username not in self.users:
            print(f"Lo sentimos, el usuario {username} no existe")
            return False
            
        # Encuentra todos los posts del usuario
        user_posts = []
        for post_id, post in self.posts.items():
            if post["username"] == username:
                user_posts.append((post_id, post["created_at"]))
                
        # Ordena por fecha de creación (más reciente primero)
        user_posts.sort(key=lambda x: x[1], reverse=True)
        
        # Obtiene los 10 posts más recientes
        recent_posts = user_posts[:10]
        
        if not recent_posts:
            print(f"El usuario {username} no tiene publicaciones")
            return False
            
        print(f"Feed de {username} (publicaciones propias):")
        for idx, (post_id, _) in enumerate(recent_posts, 1):
            print(f"\nPost {idx}:")
            self.show_post(post_id)
            
        return True
    
    def following_feed(self):
        username = input("Ingresa tu nombre de usuario: ")
        
        if username not in self.users:
            print(f"Lo sentimos, el usuario {username} no existe")
            return False
            
        # Obtiene la lista de usuarios seguidos
        following = self.followers[username]
        
        if not following:
            print(f"El usuario {username} no sigue a nadie")
            return False
            
        # Encuentra todos los posts de los usuarios seguidos
        followed_posts = []
        for post_id, post in self.posts.items():
            if post["username"] in following:
                followed_posts.append((post_id, post["created_at"]))
                
        # Ordena por fecha de creación (más reciente primero)
        followed_posts.sort(key=lambda x: x[1], reverse=True)
        
        # Obtiene los 10 posts más recientes
        recent_posts = followed_posts[:10]
        
        if not recent_posts:
            print(f"Los usuarios seguidos por {username} no tienen publicaciones")
            return False
            
        print(f"Feed de {username} (publicaciones de usuarios seguidos):")
        for idx, (post_id, _) in enumerate(recent_posts, 1):
            print(f"\nPost {idx}:")
            self.show_post(post_id)
            
        return True
    
    def main_menu(self):
        menu = """
        SISTEMA DE REDES SOCIALES
        ------------------------
        1. Crear usuario
        2. Crear post
        3. Seguir a un usuario
        4. Dejar de seguir a un usuario
        5. Eliminar post
        6. Dar like a un post
        7. Quitar like a un post
        8. Ver feed propio
        9. Ver feed de usuarios seguidos
        0. Salir
        
        Selecciona una opción: """
        
        while True:
            option = input(menu)
            
            if option == "1":
                self.create_user()
            elif option == "2":
                self.create_post()
            elif option == "3":
                self.follow_user()
            elif option == "4":
                self.unfollow_user()
            elif option == "5":
                self.delete_post()
            elif option == "6":
                self.like_post()
            elif option == "7":
                self.unlike_post()
            elif option == "8":
                self.user_feed()
            elif option == "9":
                self.following_feed()
            elif option == "0":
                print("¡Hasta pronto!")
                break
            else:
                print("Opción no válida. Intenta de nuevo.")
                
            input("\nPresiona Enter para continuar...")

# Ejecutar el programa
if __name__ == "__main__":
    app = SocialMedia()
    app.main_menu()