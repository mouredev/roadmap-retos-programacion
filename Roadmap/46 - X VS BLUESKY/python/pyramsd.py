from datetime import datetime
from collections import defaultdict

class RedSocial:
    def __init__(self):
        self.usuarios = {}
        self.posts = {}
        self.siguiendo = defaultdict(set)

    def registrar_usuario(self, user_id, name):
        if user_id in self.usuarios:
            raise ValueError("ID de usuario ya existente")
        self.usuarios[user_id] = name

    def seguir_usuario(self, follower_id, followed_id):
        if follower_id not in self.usuarios or followed_id not in self.usuarios:
            raise ValueError("ID de usuario no encontrado")
        if followed_id in self.siguiendo[follower_id]:
            self.siguiendo[follower_id].remove(followed_id)
        else:
            self.siguiendo[follower_id].add(followed_id)

    def crear_post(self, user_id, post_id, text):
        if user_id not in self.usuarios:
            raise ValueError("ID de usuario no encontrado")
        if post_id in self.posts:
            raise ValueError("ID de post ya existente")
        if len(text) > 200:
            raise ValueError("Execede de los 200 carácteres")
        self.posts[post_id] = {
            "user_id": user_id,
            "text": text,
            "created_at": datetime.now(),
            "likes": 0
        }

    def delete_post(self, post_id):
        if post_id not in self.posts:
            raise ValueError("ID de post no encontrado")
        del self.posts[post_id]

    def dar_like(self, post_id):
        if post_id not in self.posts:
            raise ValueError("ID de post no encontrado")
        self.posts[post_id]["likes"] += 1 if self.posts[post_id]["likes"] == 0 else -1

    def get_usuario_feed(self, user_id):
        if user_id not in self.usuarios:
            raise ValueError("ID de usuario no encontrado")
        user_posts = [post for post in self.posts.values() if post["user_id"] == user_id]
        user_posts.sort(key=lambda x: x["created_at"], reverse=True)
        self._display_feed(user_posts[:10])

    def get_following_feed(self, user_id):
        if user_id not in self.usuarios:
            raise ValueError("ID de usuario no encontrado")
        feed = []
        for followed_id in self.siguiendo[user_id]:
            feed.extend([post for post in self.posts.values() if post["user_id"] == followed_id])
        feed.sort(key=lambda x: x["created_at"], reverse=True)
        self._display_feed(feed[:10])

    def _display_feed(self, posts):
        for post in posts:
            user_name = self.usuarios[post["user_id"]]
            print(f"User ID: {post['user_id']}, Name: {user_name}, Text: {post['text']}, "
                  f"Created At: {post['created_at']}, Likes: {post['likes']}")


# Example Usage
if __name__ == "__main__":
    sn = RedSocial()
    sn.registrar_usuario("u1", "Alice")
    sn.registrar_usuario("u2", "Bob")

    sn.seguir_usuario("u1", "u2")

    sn.crear_post("u1", "p1", "Soy Alice!")
    sn.crear_post("u2", "p2", "Hola, esto es de Bob")
    sn.dar_like("p2")
    sn.dar_like("p1")

    print("\n[+] - Feed de Alice:")
    sn.get_usuario_feed("u1")
    sn.get_usuario_feed("u2")

    print("\n[+] - Following Feed de Alice:")
    sn.get_following_feed("u1")
