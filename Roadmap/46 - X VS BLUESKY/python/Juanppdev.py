"""
 * EJERCICIO:
 * La alternativa descentralizada a X, Bluesky, comienza a atraer
 * a nuevos usuarios. ¿Cómo funciona una red de este estilo?
 * 
 * Implementa un sistema que simule el comportamiento de estas
 * redes sociales.
 * 
 * Debes crear las siguientes operaciones:
 * - crear login y register usando una base de datos usando json, pero que si el nombre de usuario ya existe decirlo
 * - crear un sistema de publicaciones
 * - crear un sistema de comentarios
 * - crear un sistema de likes
 * - crear un sistema de amigos
 * - poder buscar a amigos y seguirlos 
 * - hacer retuits a los posts
 * - Registrar un usuario por nombre e identificador único.
 * - Un usuario puede seguir/dejar de seguir a otro.
 * - Creación de post asociado a un usuario. Debe poseer
 *   texto (200 caracteres máximo), fecha de creación 
 *   e identificador único.
 * - Un usuario puede darle "me gusta" a un post.
 * - con una interface grafica  y con una sabe de datos json
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

 * Que hayan difrentes pantallas por ejemplo ["login", "register", "feed", "profile", "config", "friends", "ver posts"] y más
"""

import json
import os
import hashlib
from datetime import datetime
import tkinter as tk
from tkinter import messagebox, ttk

# Paths de las bases de datos
USERS_DB = "./data/usuarios.json"
POSTS_DB = "./data/posts.json"

# === Gestión de Usuarios ===

def load_users():
    if not os.path.exists("./data"):
        os.makedirs("./data")  # Crea la carpeta data si no existe
    if not os.path.exists(USERS_DB):
        with open(USERS_DB, "w") as db:
            json.dump({"usuarios": []}, db)
    with open(USERS_DB, "r") as db:
        return json.load(db)

def save_users(data):
    with open(USERS_DB, "w") as db:
        json.dump(data, db, indent=4)

def register(username, password):
    data = load_users()
    for user in data["usuarios"]:
        if user["username"] == username:
            return False, "El nombre de usuario ya existe."
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    new_user = {
        "id": len(data["usuarios"]) + 1,
        "username": username,
        "password": hashed_password,
        "friends": [],
        "following": [],
        "followers": []
    }
    data["usuarios"].append(new_user)
    save_users(data)
    return True, "Usuario registrado con éxito."

def login(username, password):
    data = load_users()
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    for user in data["usuarios"]:
        if user["username"] == username and user["password"] == hashed_password:
            return True, user["id"]
    return False, "Nombre de usuario o contraseña incorrectos."

def follow_user(current_user_id, target_user_id):
    data = load_users()
    current_user = next((u for u in data["usuarios"] if u["id"] == current_user_id), None)
    target_user = next((u for u in data["usuarios"] if u["id"] == target_user_id), None)

    if not current_user or not target_user:
        return False, "Usuario no encontrado."
    
    if target_user_id in current_user["following"]:
        current_user["following"].remove(target_user_id)
        target_user["followers"].remove(current_user_id)
        message = f"Dejaste de seguir a {target_user['username']}."
    else:
        current_user["following"].append(target_user_id)
        target_user["followers"].append(current_user_id)
        message = f"Ahora sigues a {target_user['username']}."
    
    save_users(data)
    return True, message

def search_users(username):
    data = load_users()
    return [u for u in data["usuarios"] if username.lower() in u["username"].lower()]

# === Gestión de Publicaciones ===

def load_posts():
    if not os.path.exists(POSTS_DB):
        with open(POSTS_DB, "w") as db:
            json.dump({"posts": []}, db)
    with open(POSTS_DB, "r") as db:
        return json.load(db)

def save_posts(data):
    with open(POSTS_DB, "w") as db:
        json.dump(data, db, indent=4)

def create_post(user_id, text):
    if len(text) > 200:
        return False, "El texto supera los 200 caracteres."
    data = load_posts()
    new_post = {
        "id": len(data["posts"]) + 1,
        "user_id": user_id,
        "text": text,
        "likes": [],
        "comments": [],
        "created_at": datetime.now().isoformat()
    }
    data["posts"].append(new_post)
    save_posts(data)
    return True, "Publicación creada con éxito."

def like_post(user_id, post_id):
    data = load_posts()
    for post in data["posts"]:
        if post["id"] == post_id:
            if user_id in post["likes"]:
                post["likes"].remove(user_id)
                message = "Like eliminado."
            else:
                post["likes"].append(user_id)
                message = "Like añadido."
            save_posts(data)
            return True, message
    return False, "Publicación no encontrada."

def retweet_post(user_id, post_id):
    data = load_posts()
    post = next((p for p in data["posts"] if p["id"] == post_id), None)

    if not post:
        return False, "Publicación no encontrada."
    
    retweeted_post = {
        "id": len(data["posts"]) + 1,
        "user_id": user_id,
        "text": f"RT: {post['text']}",
        "likes": [],
        "comments": [],
        "created_at": datetime.now().isoformat()
    }
    data["posts"].append(retweeted_post)
    save_posts(data)
    return True, "Retweet realizado con éxito."

def user_feed(user_id):
    data = load_posts()
    posts = [p for p in data["posts"] if p["user_id"] == user_id]
    return sorted(posts, key=lambda x: x["created_at"], reverse=True)[:10]

def following_feed(user_id):
    user_data = load_users()
    current_user = next((u for u in user_data["usuarios"] if u["id"] == user_id), None)
    if not current_user:
        return []

    data = load_posts()
    posts = [p for p in data["posts"] if p["user_id"] in current_user["following"]]
    return sorted(posts, key=lambda x: x["created_at"], reverse=True)[:10]

def general_feed():
    data = load_posts()
    return sorted(data["posts"], key=lambda x: x["created_at"], reverse=True)

# === Interfaz Gráfica ===

class App:
    def __init__(self, root):
        self.root = root
        self.user_id = None  # ID del usuario logueado
        self.setup_login()

    def setup_login(self):
        self.clear_window()

        tk.Label(self.root, text="Usuario:").pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()

        tk.Label(self.root, text="Contraseña:").pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack()

        tk.Button(self.root, text="Iniciar Sesión", command=self.login).pack()
        tk.Button(self.root, text="Registrar", command=self.register).pack()

    def setup_feed(self):
        self.clear_window()

        tk.Button(self.root, text="Crear Publicación", command=self.create_post_window).pack()
        tk.Button(self.root, text="Feed Personal", command=self.show_personal_feed).pack()  # Cambio aquí
        tk.Button(self.root, text="Feed General", command=self.show_general_feed).pack()
        tk.Button(self.root, text="Perfil", command=self.show_personal_feed).pack()
        tk.Button(self.root, text="Buscar Amigos", command=self.search_users_window).pack()

    def search_users_window(self):
        self.clear_window()

        tk.Label(self.root, text="Buscar usuarios por nombre:").pack()
        self.search_entry = tk.Entry(self.root)
        self.search_entry.pack()

        tk.Button(self.root, text="Buscar", command=self.search_users).pack()
        tk.Button(self.root, text="Volver", command=self.setup_feed).pack()

    def search_users(self):
        username = self.search_entry.get()
        users = search_users(username)
        self.clear_window()
        if users:
            for user in users:
                tk.Label(self.root, text=f"Usuario: {user['username']}").pack()
                follow_button = tk.Button(self.root, text="Seguir", command=lambda u=user: self.follow_user(u))
                follow_button.pack()
        else:
            tk.Label(self.root, text="No se encontraron usuarios.").pack()

        tk.Button(self.root, text="Volver", command=self.setup_feed).pack()

    def follow_user(self, user):
        success, message = follow_user(self.user_id, user["id"])
        messagebox.showinfo("Seguir Usuario", message)

    def show_personal_feed(self):  # Definir la función que muestra el feed personal
        self.clear_window()

        posts = user_feed(self.user_id)
        for post in posts:
            user = next((u for u in load_users()["usuarios"] if u["id"] == post["user_id"]), None)
            if user:
                post_text = f"{user['username']}: {post['text']} (Likes: {len(post['likes'])})"
                tk.Label(self.root, text=post_text).pack()

                def like_action(post_id=post["id"]):
                    success, message = like_post(self.user_id, post_id)
                    messagebox.showinfo("Like", message)

                tk.Button(self.root, text="Me Gusta", command=like_action).pack()

        tk.Button(self.root, text="Volver", command=self.setup_feed).pack()

    def show_general_feed(self):
        self.clear_window()

        posts = general_feed()
        for post in posts:
            user = next((u for u in load_users()["usuarios"] if u["id"] == post["user_id"]), None)
            if user:
                post_text = f"{user['username']}: {post['text']} (Likes: {len(post['likes'])})"
                tk.Label(self.root, text=post_text).pack()

                def like_action(post_id=post["id"]):
                    success, message = like_post(self.user_id, post_id)
                    messagebox.showinfo("Like", message)

                tk.Button(self.root, text="Me Gusta", command=like_action).pack()

        tk.Button(self.root, text="Volver", command=self.setup_feed).pack()

    def create_post_window(self):
        self.clear_window()

        tk.Label(self.root, text="Texto de la Publicación:").pack()
        self.post_text = tk.Entry(self.root)
        self.post_text.pack()

        tk.Button(self.root, text="Crear", command=self.create_post).pack()

    def create_post(self):
        text = self.post_text.get()
        success, message = create_post(self.user_id, text)
        messagebox.showinfo("Crear Publicación", message)
        self.setup_feed()

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        success, message = register(username, password)
        messagebox.showinfo("Registro", message)
        if success:
            self.setup_login()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        success, result = login(username, password)
        if success:
            self.user_id = result
            self.setup_feed()
        else:
            messagebox.showerror("Error", result)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# === Main ===

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Twitter Descentralizado")
    app = App(root)
    root.mainloop()
