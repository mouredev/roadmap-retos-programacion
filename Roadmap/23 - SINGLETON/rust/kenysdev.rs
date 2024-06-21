/*
╔═══════════════════════════════════════╗
║ Autor:  Kenys Alvarado                ║
║ GitHub: https://github.com/Kenysdev   ║
║ 2024 -  Rust                          ║
╚═══════════════════════════════════════╝
-----------------------------------------
* PATRONES DE DISEÑO: SINGLETON
-----------------------------------------

* EJERCICIO #1:
* Explora el patrón de diseño "singleton" y muestra cómo crearlo
* con un ejemplo genérico.
*/

// https://doc.rust-lang.org/std/sync/struct.Once.html
use std::sync::Once;

struct Singleton {
    field1: u32,
    field2: String,
}

impl Singleton {
    // Función asociada que devuelve la única instancia de la estructura
    fn instance() -> &'static Singleton {
        static mut INSTANCE: *const Singleton = 0 as *const Singleton;
        static ONCE: Once = Once::new();

        unsafe {
            ONCE.call_once(|| {
                // Inicialización de la instancia única
                let instance = Singleton {
                    field1: 42,
                    field2: String::from("str"),
                };
                INSTANCE = Box::into_raw(Box::new(instance));
            });
            &*INSTANCE
        }
    }
}

/*
____________________________________
* EJERCICIO #2:
* Utiliza el patrón de diseño "singleton" para representar una clase que
* haga referencia a la sesión de usuario de una aplicación ficticia.
* La sesión debe permitir asignar un usuario (id, username, nombre y email),
* recuperar los datos del usuario y borrar los datos de la sesión.
*/

use std::collections::HashMap;

struct UserSession {
    user_id: i32,
    user_name: String,
    name: String,
    email: String,
}

impl UserSession {
    fn instance() -> &'static mut UserSession {
        static mut INSTANCE: *mut UserSession = std::ptr::null_mut();
        static ONCE: std::sync::Once = std::sync::Once::new();

        unsafe {
            ONCE.call_once(|| {
                let instance = UserSession {
                    user_id: 0,
                    user_name: String::new(),
                    name: String::new(),
                    email: String::new(),
                };
                INSTANCE = Box::into_raw(Box::new(instance));
            });
            &mut *INSTANCE
        }
    }

    fn set_user(&mut self, user_id: i32, user_name: &str, name: &str, email: &str) {
        self.user_id = user_id;
        self.user_name = user_name.to_string();
        self.name = name.to_string();
        self.email = email.to_string();
    }

    fn get_user(&self) -> HashMap<String, String> {
        let mut user_details = HashMap::new();
        user_details.insert(String::from("id"), self.user_id.to_string());
        user_details.insert(String::from("username"), self.user_name.clone());
        user_details.insert(String::from("name"), self.name.clone());
        user_details.insert(String::from("email"), self.email.clone());
        user_details
    }

    fn logout(&mut self) {
        self.user_id = 0;
        self.user_name.clear();
        self.name.clear();
        self.email.clear();
    }
}

//____________________________________
fn main() {
    println!("EJERCICIO #1");
    let singleton1 = Singleton::instance();
    // singleton2 accede a la misma instancia que singleton1.
    let singleton2 = Singleton::instance();

    println!("Singleton campo1: {}", singleton1.field1);
    println!("Singleton campo2: {}", singleton2.field2);
    
    // Comprobación de igualdad de referencias.
    println!("{:?}", std::ptr::eq(singleton1, singleton2));   

    //____________________________________
    println!("EJERCICIO #2");

    let login_user1 = UserSession::instance();

    login_user1.set_user(1, "Zoe_1", "Zoe", "Zoe@gm.com");

    let user_details1 = login_user1.get_user();
    for (key, value) in user_details1.iter() {
        println!("{}: {}", key, value);
    }

    login_user1.logout();

    //____________________________________

    let login_user2 = UserSession::instance();

    login_user2.set_user(2, "Ben_1", "Ben", "Ben@gm.com");

    let user_details2 = login_user2.get_user();
    for (key, value) in user_details2.iter() {
        println!("{}: {}", key, value);
    }

    login_user2.logout();
    
}
