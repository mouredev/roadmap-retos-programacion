import datetime

class User:
    def __init__(self, user_id, name):
        self.id = user_id
        self.name = name
        self.following = []
        self.posts = []

    def follow(self, user):
        if user.id in self.following:
            print(f"{self.name} ya sigue a {user.name}.")
            return
        self.following.append(user.id)
        print(f"{self.name} comenzó a seguir a {user.name}.")

    def unfollow(self, user):
        if user.id not in self.following:
            print(f"{self.name} no sigue a {user.name}.")
            return
        self.following.remove(user.id)
        print(f"{self.name} dejó de seguir a {user.name}.")

class Post:
    def __init__(self, post_id, text, user_id):
        self.id = post_id
        self.text = text[:200]
        self.user_id = user_id
        self.created_at = datetime.datetime.now()
        self.likes = 0

    def like(self):
        self.likes += 1

    def unlike(self):
        if self.likes > 0:
            self.likes -= 1

class SocialNetwork:
    def __init__(self):
        self.users = {}
        self.posts = {}

    def register_user(self, user_id, name):
        if user_id in self.users:
            print(f"El usuario con ID {user_id} ya existe.")
            return
        self.users[user_id] = User(user_id, name)
        print(f"Usuario {name} registrado con éxito.")

    def create_post(self, user_id, text):
        if user_id not in self.users:
            print(f"El usuario con ID {user_id} no existe.")
            return
        post_id = f"post_{len(self.posts) + 1}"
        post = Post(post_id, text, user_id)
        self.posts[post_id] = post
        self.users[user_id].posts.append(post)
        print("Post creado con éxito.")

    def delete_post(self, post_id):
        if post_id not in self.posts:
            print(f"El post con ID {post_id} no existe.")
            return
        post = self.posts[post_id]
        self.users[post.user_id].posts = [p for p in self.users[post.user_id].posts if p.id != post_id]
        del self.posts[post_id]
        print("Post eliminado con éxito.")

    def like_post(self, post_id):
        if post_id not in self.posts:
            print(f"El post con ID {post_id} no existe.")
            return
        self.posts[post_id].like()
        print(f"Post {post_id} recibió un like.")

    def unlike_post(self, post_id):
        if post_id not in self.posts:
            print(f"El post con ID {post_id} no existe.")
            return
        self.posts[post_id].unlike()
        print(f"Like eliminado del post {post_id}.")

    def view_feed(self, user_id):
        if user_id not in self.users:
            print(f"El usuario con ID {user_id} no existe.")
            return
        posts = sorted(self.users[user_id].posts, key=lambda p: p.created_at, reverse=True)
        print(f"Feed de {self.users[user_id].name}:")
        for post in posts[:10]:
            self.display_post(post)

    def view_followed_feed(self, user_id):
        if user_id not in self.users:
            print(f"El usuario con ID {user_id} no existe.")
            return
        followed_posts = []
        for followed_id in self.users[user_id].following:
            if followed_id in self.users:
                followed_posts.extend(self.users[followed_id].posts)
        followed_posts = sorted(followed_posts, key=lambda p: p.created_at, reverse=True)
        print(f"Feed de usuarios seguidos por {self.users[user_id].name}:")
        for post in followed_posts[:10]:
            self.display_post(post)

    def display_post(self, post):
        print(f"ID: {post.id}, Usuario: {post.user_id}, Texto: {post.text}, Fecha: {post.created_at}, Likes: {post.likes}")

    def interactive_menu(self):
        while True:
            print("\n--- Menú Principal ---")
            print("1. Registrar usuario")
            print("2. Crear post")
            print("3. Eliminar post")
            print("4. Dar like a un post")
            print("5. Quitar like de un post")
            print("6. Ver feed del usuario")
            print("7. Ver feed de usuarios seguidos")
            print("8. Seguir a un usuario")
            print("9. Dejar de seguir a un usuario")
            print("10. Salir")
            option = input("Seleccione una opción: ")
            if option == "1":
                user_id = input("Ingrese ID del usuario: ")
                name = input("Ingrese nombre del usuario: ")
                self.register_user(user_id, name)
            elif option == "2":
                user_id = input("Ingrese ID del usuario: ")
                text = input("Ingrese texto del post: ")
                self.create_post(user_id, text)
            elif option == "3":
                post_id = input("Ingrese ID del post: ")
                self.delete_post(post_id)
            elif option == "4":
                post_id = input("Ingrese ID del post: ")
                self.like_post(post_id)
            elif option == "5":
                post_id = input("Ingrese ID del post: ")
                self.unlike_post(post_id)
            elif option == "6":
                user_id = input("Ingrese ID del usuario: ")
                self.view_feed(user_id)
            elif option == "7":
                user_id = input("Ingrese ID del usuario: ")
                self.view_followed_feed(user_id)
            elif option == "8":
                follower_id = input("Ingrese tu ID: ")
                follow_id = input("Ingrese ID del usuario a seguir: ")
                if follower_id in self.users and follow_id in self.users:
                    self.users[follower_id].follow(self.users[follow_id])
                else:
                    print("Usuario no encontrado.")
            elif option == "9":
                unfollower_id = input("Ingrese tu ID: ")
                unfollow_id = input("Ingrese ID del usuario a dejar de seguir: ")
                if unfollower_id in self.users and unfollow_id in self.users:
                    self.users[unfollower_id].unfollow(self.users[unfollow_id])
                else:
                    print("Usuario no encontrado.")
            elif option == "10":
                print("Saliendo...")
                break
            else:
                print("Opción no válida.")

if __name__ == "__main__":
    network = SocialNetwork()
    network.interactive_menu()
