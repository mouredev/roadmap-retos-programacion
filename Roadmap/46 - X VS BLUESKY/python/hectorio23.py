# Autor: Héctor Adán
# GitHub: https://github.com/hectorio23

from datetime import datetime
from collections import defaultdict

class SocialNetwork:
    def __init__(self):
        self.users = {}
        self.posts = {}
        self.following = defaultdict(set)

    def register_user(self, user_id, name):
        if user_id in self.users:
            raise ValueError("User ID already exists.")
        self.users[user_id] = name

    def toggle_follow(self, follower_id, followed_id):
        if follower_id not in self.users or followed_id not in self.users:
            raise ValueError("User ID not found.")
        if followed_id in self.following[follower_id]:
            self.following[follower_id].remove(followed_id)
        else:
            self.following[follower_id].add(followed_id)

    def create_post(self, user_id, post_id, text):
        if user_id not in self.users:
            raise ValueError("User ID not found.")
        if post_id in self.posts:
            raise ValueError("Post ID already exists.")
        if len(text) > 200:
            raise ValueError("Text exceeds maximum length of 200 characters.")
        self.posts[post_id] = {
            "user_id": user_id,
            "text": text,
            "created_at": datetime.now(),
            "likes": 0
        }

    def delete_post(self, post_id):
        if post_id not in self.posts:
            raise ValueError("Post ID not found.")
        del self.posts[post_id]

    def toggle_like(self, post_id):
        if post_id not in self.posts:
            raise ValueError("Post ID not found.")
        self.posts[post_id]["likes"] += 1 if self.posts[post_id]["likes"] == 0 else -1

    def get_user_feed(self, user_id):
        if user_id not in self.users:
            raise ValueError("User ID not found.")
        user_posts = [post for post in self.posts.values() if post["user_id"] == user_id]
        user_posts.sort(key=lambda x: x["created_at"], reverse=True)
        self._display_feed(user_posts[:10])

    def get_following_feed(self, user_id):
        if user_id not in self.users:
            raise ValueError("User ID not found.")
        feed = []
        for followed_id in self.following[user_id]:
            feed.extend([post for post in self.posts.values() if post["user_id"] == followed_id])
        feed.sort(key=lambda x: x["created_at"], reverse=True)
        self._display_feed(feed[:10])

    def _display_feed(self, posts):
        for post in posts:
            user_name = self.users[post["user_id"]]
            print(f"User ID: {post['user_id']}, Name: {user_name}, Text: {post['text']}, "
                  f"Created At: {post['created_at']}, Likes: {post['likes']}")


# Example Usage
if __name__ == "__main__":
    sn = SocialNetwork()
    sn.register_user("u1", "Alice")
    sn.register_user("u2", "Bob")

    sn.toggle_follow("u1", "u2")

    sn.create_post("u1", "p1", "Hello, this is Alice!")
    sn.create_post("u2", "p2", "Hi, this is Bob's post.")
    sn.toggle_like("p2")

    print("\n[+] - User Feed for Alice:")
    sn.get_user_feed("u1")

    print("\n[+] - Following Feed for Alice:")
    sn.get_following_feed("u1")

    sn.delete_post("p1")
    print("\n[+] - After Deleting Alice's Post:")
    sn.get_user_feed("u1")
