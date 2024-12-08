/*
_____________________________________
https://github.com/kenysdev
2024 - Rust
_____________________________________
46 X VS BLUESKY
------------------------------------

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

[dependencies]
chrono = "0.4.37"
log = "0.4.22"
simple_logger = "5.0.0"
*/

use chrono::{DateTime, Local};
use log::{error, info, warn};
use simple_logger::SimpleLogger;
use std::collections::{HashMap, HashSet};

#[derive(Clone)]
struct PostData {
    content: String,
    timestamp: DateTime<Local>,
    likes: HashSet<i32>,
}

struct Posts {
    post_dt: HashMap<i32, HashMap<i32, PostData>>,
}

impl Posts {
    fn new() -> Self {
        Posts {
            post_dt: HashMap::new(),
        }
    }

    fn verify_post(&self, id_user: i32, id_post: i32, name_func: &str) -> bool {
        if !self.post_dt.contains_key(&id_user) {
            error!("'{}': El ID {} no tiene posts.", name_func, id_user);
            return false;
        }

        if !self.post_dt[&id_user].contains_key(&id_post) {
            error!("'{}': El Post ({}) no existe.", name_func, id_post);
            return false;
        }

        true
    }

    fn create_post(&mut self, id_user: i32, content: &str) {
        if content.len() > 200 {
            error!("'create_post': content > 200 caracteres.");
            return;
        }

        let user_posts = self.post_dt.entry(id_user).or_insert_with(HashMap::new);
        let id_post = user_posts.len() as i32 + 1;

        user_posts.insert(
            id_post,
            PostData {
                content: content.to_string(),
                timestamp: Local::now(),
                likes: HashSet::new(),
            },
        );

        info!("El ID {} creó un post(ID: {}).", id_user, id_post);
    }

    fn delete_post(&mut self, id_user: i32, id_post: i32) {
        if self.verify_post(id_user, id_post, "delete_post") {
            self.post_dt.get_mut(&id_user).unwrap().remove(&id_post);
            info!(
                "El post: {} de usuario: {} ha sido eliminado.",
                id_post, id_user
            );
        }
    }

    fn like_post(&mut self, id_user: i32, id_author: i32, id_post: i32) {
        if self.verify_post(id_author, id_post, "like_post") {
            self.post_dt
                .get_mut(&id_author)
                .unwrap()
                .get_mut(&id_post)
                .unwrap()
                .likes
                .insert(id_user);

            info!(
                "El usuario {} dio like al post {} de usuario {}.",
                id_user, id_post, id_author
            );
        }
    }

    fn remove_like(&mut self, id_user: i32, id_author: i32, id_post: i32) {
        if self.verify_post(id_author, id_post, "remove_like") {
            self.post_dt
                .get_mut(&id_author)
                .unwrap()
                .get_mut(&id_post)
                .unwrap()
                .likes
                .remove(&id_user);

            info!(
                "El usuario {} anuló el like al post {} de usuario {}.",
                id_user, id_post, id_author
            );
        }
    }

    fn get_recent_posts(&self, id_user: i32, limit: usize) -> Vec<PostData> {
        if let Some(user_posts) = self.post_dt.get(&id_user) {
            let mut posts: Vec<_> = user_posts.values().cloned().collect();
            posts.sort_by(|a, b| b.timestamp.cmp(&a.timestamp));
            posts.truncate(limit);
            posts
        } else {
            Vec::new()
        }
    }
}

struct UserData {
    name: String,
    following: HashSet<i32>,
    followers: HashSet<i32>,
}

struct Users {
    users_dt: HashMap<i32, UserData>,
}

impl Users {
    fn new() -> Self {
        Users {
            users_dt: HashMap::new(),
        }
    }

    fn id_exists(&self, id: i32, name_func: &str) -> bool {
        if self.users_dt.contains_key(&id) {
            return true;
        }

        warn!("'{}': ID: {} no encontrada.", name_func, id);
        false
    }

    fn add_user(&mut self, name: &str) {
        let id = self.users_dt.len() as i32 + 1;
        self.users_dt.insert(
            id,
            UserData {
                name: name.to_string(),
                following: HashSet::new(),
                followers: HashSet::new(),
            },
        );

        info!("Usuario {}-{} registrado.", id, name);
    }

    fn follow_user(&mut self, id: i32, to_id: i32) {
        if self.id_exists(id, "follow_user") && self.id_exists(to_id, "follow_user") {
            self.users_dt.get_mut(&id).unwrap().following.insert(to_id);
            self.users_dt.get_mut(&to_id).unwrap().followers.insert(id);
            info!("ID: {} está siguiendo a ID: {}.", id, to_id);
        }
    }

    fn unfollow_user(&mut self, id: i32, to_id: i32) {
        if self.id_exists(id, "unfollow_user") && self.id_exists(to_id, "unfollow_user") {
            self.users_dt.get_mut(&id).unwrap().following.remove(&to_id);
            self.users_dt.get_mut(&to_id).unwrap().followers.remove(&id);
            info!("El ID: {} dejó de seguir al ID: {}.", id, to_id);
        }
    }

    fn get_name(&self, id_user: i32) -> String {
        if self.id_exists(id_user, "get_name") {
            self.users_dt[&id_user].name.clone()
        } else {
            String::new()
        }
    }
}

struct Program {
    posts: Posts,
    users: Users,
}

impl Program {
    fn new() -> Self {
        Program {
            posts: Posts::new(),
            users: Users::new(),
        }
    }

    fn print_feed(&self, id_user: i32) {
        let name = self.users.get_name(id_user);
        if name.is_empty() {
            println!("Usuario ID: {} no encontrado.", id_user);
            return;
        }

        let last_10 = self.posts.get_recent_posts(id_user, 10);
        println!("\nFeed\n_______\nID: '{}' - Nombre: '{}'", id_user, name);

        if last_10.is_empty() {
            println!("No tiene publicaciones.");
            return;
        }

        for post in last_10 {
            println!("_______\n{}", post.content);
            println!("Creado: '{}'", post.timestamp);
            println!("Likes: '{}'", post.likes.len());
        }
    }

    fn run(&self) {
        // CLI
    }

    fn tests(&mut self) {
        self.users.add_user("Ken"); // id=1
        self.users.add_user("Zoe"); // id=2

        self.users.follow_user(1, 2);
        self.users.follow_user(2, 1);
        self.users.unfollow_user(2, 1);

        self.posts.create_post(2, "Primer post."); // id=1
        self.posts.create_post(2, "Segundo post."); // id=2
        self.posts.delete_post(2, 2);
        self.posts.create_post(2, "Otro post."); // id=2
        self.posts.like_post(1, 2, 1);
        self.posts.remove_like(1, 2, 1);
        self.posts.like_post(1, 2, 2);

        self.print_feed(2);
        self.print_feed(1);
    }
}

fn main() {
    SimpleLogger::new().init().unwrap();

    let mut program = Program::new();
    program.tests();
    //program.run();
}
