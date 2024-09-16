/*
╔═══════════════════════════════════════╗
║ Autor:  Kenys Alvarado                ║
║ GitHub: https://github.com/Kenysdev   ║
║ 2024 -  Rust                          ║
╚═══════════════════════════════════════╝
-----------------------------------------
* PETICIONES HTTP
-----------------------------------------
https://crates.io/crates/reqwest

[dependencies]
tokio = { version = "1.37.0", features = ["full"] }
serde = { version = "1.0.197", features = ["derive"] }
reqwest = { version = "0.12.4", features = ["json"] }
*/

/*
* EJERCICIO:
* Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
* una petición a la web que tú quieras, verifica que dicha petición
* fue exitosa y muestra por consola el contenido de la web.
*/
use reqwest;
use serde::Deserialize;

#[derive(Deserialize, Debug)]
struct User {
    id: u32,
    name: String,
    username: String,
    email: String,
    phone: String,
}

async fn get_user(user_id: u32) -> Result<Option<User>, reqwest::Error> {
    let url = format!("https://jsonplaceholder.typicode.com/users/{}", user_id);
    let response = reqwest::get(&url).await?;

    if response.status().is_success() {
        let user: User = response.json().await?;
        Ok(Some(user))
    } else {
        println!("Id: {} No encontrado", user_id);
        println!("status_code: {}", response.status());
        Ok(None)
    }
}

fn print_user(user_data: Option<User>) {
    if let Some(user) = user_data {
        println!(
            "Usuario con id: '{}':\n\
             Nombre: {}\n\
             Usuario: {}\n\
             Email: {}\n\
             Teléfono: {}\n",
            user.id, user.name, user.username, user.email, user.phone
        );
    }
}

#[tokio::main]
async fn main() -> Result<(), reqwest::Error> {

    let u1 = get_user(1).await?;
    print_user(u1);

    let u2 = get_user(2).await?;
    print_user(u2);

    let u3 = get_user(777).await?; // xD-error
    print_user(u3);

    Ok(())
}
