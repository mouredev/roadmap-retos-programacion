from datetime import datetime


class SocialNetwork:

    def __init__(self):
        self.post_id = 0
        self.users = {}
        self.post = {}

    def register_user(self, user_id: str, name: str):

        if user_id in self.users:
            print(f"El usuario con el ID {user_id} ya existe.")
            return

        self.users[user_id] = {
            "name": name,
            "following": set(),
            "followers": set(),
            "post": []
        }
        print(
            f"Usuario con ID '{user_id}' y nombre '{
                name}' registrado correctamente."
        )

    def follow_user(self, user_id: str, follow_id: str):

        if user_id not in self.users or follow_id not in self.users:
            print("Alguno de los usuarios no existe. No se puede realizar el follow.")
            return

        self.users[user_id]["following"].add(follow_id)
        self.users[follow_id]["followers"].add(user_id)
        print(
            f"{self.users[user_id]["name"]} ahora sigue a {
                self.users[follow_id]["name"]}."
        )

    def unfollow_user(self, user_id: str, unfollow_id: str):

        if user_id not in self.users or unfollow_id not in self.users:
            print("Alguno de los usuarios no existe. No se puede realizar el unfollow.")
            return

        self.users[user_id]["following"].discard(unfollow_id)
        self.users[unfollow_id]["followers"].discard(user_id)
        print(
            f"{self.users[user_id]["name"]} ha dejado de seguir a {
                self.users[unfollow_id]["name"]}."
        )

    def create_post(self, user_id: str, text: str):

        if user_id not in self.users:
            print(f"El usuario '{user_id}' no existe.")
            return

        if len(text) > 200:
            print("El post no puede tener más de 200 caracteres.")
            return

        self.post_id += 1

        post_id = self.post_id

        self.post[post_id] = {
            "user_id": user_id,
            "text": text,
            "created_at": datetime.now(),
            "likes": set()
        }

        self.users[user_id]["post"].append(post_id)

        print("Post creado correctamente.")

    def delete_post(self, post_id: int):

        if post_id not in self.post:
            print(f"El post con ID {post_id} no existe.")
            return

        user_id = self.post[post_id]["user_id"]
        self.users[user_id]["post"].remove(post_id)
        del self.post[post_id]
        print("Post eliminado correctamente.")

    def like_post(self, user_id: str, post_id: int):

        if user_id not in self.users:
            print(f"El usuario '{user_id}' no existe.")
            return

        if post_id not in self.post:
            print(f"El post '{post_id}' no existe.")
            return

        self.post[post_id]["likes"].add(user_id)
        print(f"Nuevo like en post '{post_id}'.")

    def unlike_post(self, user_id: str, post_id: int):

        if user_id not in self.users:
            print(f"El usuario '{user_id}' no existe.")
            return

        if post_id not in self.post:
            print(f"El post '{post_id}' no existe.")
            return

        self.post[post_id]["likes"].discard(user_id)
        print(f"Like eliminado en post '{post_id}'.")

    def view_user_feed(self, user_id: str):

        if user_id not in self.users:
            print(f"El usuario '{user_id}' no existe.")
            return

        feed = sorted(
            (self.post[post_id] for post_id in self.users[user_id]["post"]),
            key=lambda x: x["created_at"],
            reverse=True
        )[:10]

        for post in feed:
            print(f"""
ID usuario: {post["user_id"]}
Usuario: {self.users[post["user_id"]]["name"]}
Texto: {post["text"]}
Fecha: {post["created_at"]}
Likes: {len(post["likes"])}
                    """)

    def view_following_feed(self, user_id: str):

        if user_id not in self.users:
            print(f"El usuario '{user_id}' no existe.")
            return

        following_post_ids = []

        for following_id in self.users[user_id]["following"]:
            following_post_ids.extend(self.users[following_id]["post"])

        feed = sorted(
            (self.post[post_id] for post_id in following_post_ids),
            key=lambda x: x["created_at"],
            reverse=True
        )[:10]

        for post in feed:
            print(f"""
ID usuario: {post["user_id"]}
Usuario: {self.users[post["user_id"]]["name"]}
Texto: {post["text"]}
Fecha: {post["created_at"]}
Likes: {len(post["likes"])}
                    """)


social_network = SocialNetwork()
social_network.register_user("mouredev", "Brais Moure")
social_network.register_user("manolo", "Manolo 87")

social_network.create_post("mouredev", "Hola mundo!")
social_network.create_post("mouredev", "Hola mundo 2!")
social_network.create_post("mouredev", "Hola mundo 3!")

social_network.create_post("manolo", "Hola mundo!")
social_network.create_post("manolo", "Hola mundo 2!")
social_network.create_post("manolo", "Hola mundo 3!")

social_network.follow_user("manolo", "mouredev")

social_network.like_post("manolo", 1)

social_network.view_user_feed("mouredev")
social_network.view_following_feed("manolo")

social_network.unlike_post("manolo", 1)

social_network.view_following_feed("manolo")
