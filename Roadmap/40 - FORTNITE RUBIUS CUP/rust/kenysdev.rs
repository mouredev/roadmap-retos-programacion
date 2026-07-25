/*
_____________________________________
https://github.com/kenysdev
2024 - Rust
_____________________________________
40 FORTNITE RUBIUS CUP
------------------------------------

* EJERCICIO:
* ¡Rubius tiene su propia skin en Fortnite!
* Y va a organizar una competición para celebrarlo.
* Esta es la lista de participantes:
* https://x.com/Rubiu5/status/1840161450154692876
*
* Desarrolla un programa que obtenga el número de seguidores en
* Twitch de cada participante, la fecha de creación de la cuenta
* y ordene los resultados en dos listados.
* - Usa el API de Twitch: https://dev.twitch.tv/docs/api/reference
*   (NO subas las credenciales de autenticación)
* - Crea un ranking por número de seguidores y por antigüedad.
* - Si algún participante no tiene usuario en Twitch, debe reflejarlo.

[dependencies]
chrono = { version = "0.4.37", features = ["serde"] }
dotenvy = "0.15.7"
itertools = "0.13.0"
reqwest = { version = "0.12.9", features = ["json"] }
serde = { version = "1.0.215", features = ["derive"] }
serde_json = "1.0.133"
tokio = { version = "1.41.1", features = ["full"] }
*/

use chrono::{DateTime, Utc};
use dotenvy::dotenv;
use std::env;
use itertools::Itertools;
use reqwest::Client;
use serde::{Deserialize, Serialize};

pub struct Twitch {
    client_id: String,
    client_secret: String,
    access_token: Option<String>,
}

#[derive(Debug, Serialize, Deserialize)]
pub struct UserData {
    username: String,
    created_at: DateTime<Utc>,
    followers: i32,
}

impl Twitch {
    pub fn new(client_id: String, client_secret: String) -> Self {
        Self {
            client_id,
            client_secret,
            access_token: None,
        }
    }

    async fn ensure_access_token(&mut self) -> Result<(), Box<dyn std::error::Error>> {
        if self.access_token.is_none() {
            let client = Client::new();

            let params = [
                ("client_id", self.client_id.as_str()),
                ("client_secret", self.client_secret.as_str()),
                ("grant_type", "client_credentials"),
            ];

            let res = client
                .post("https://id.twitch.tv/oauth2/token")
                .form(&params)
                .send()
                .await?;

            if !res.status().is_success() {
                return Err(format!("Error al obtener el token: {}", res.status()).into());
            }

            let token_data: serde_json::Value = res.json().await?;
            self.access_token = Some(
                token_data["access_token"]
                    .as_str()
                    .ok_or("Token no encontrado.")?
                    .to_string(),
            );
        }
        Ok(())
    }

    pub fn access_token(&mut self) -> &str {
        self.access_token.as_ref().unwrap()
    }

    async fn get_followers(
        &mut self,
        client: &reqwest::Client, 
        id_user: &str, 
    ) -> Result<i32, Box<dyn std::error::Error>> {
        let url = format!("https://api.twitch.tv/helix/channels/followers?broadcaster_id={}", id_user);
        
        let response = client
            .get(&url)
            .header("Client-Id", self.client_id.as_str())
            .header("Authorization", format!("Bearer {}", self.access_token()))
            .send()
            .await?;
        
        let json: serde_json::Value = response.json().await?;
        let total = json["total"].as_u64().unwrap_or(0) as u32;
        Ok(total as i32)
    }

    async fn get_user_data(
        &mut self,
        user_name: &str,
    ) -> Result<Option<UserData>, Box<dyn std::error::Error>> {
        let client = reqwest::Client::new();
        let url = format!("https://api.twitch.tv/helix/users?login={}", user_name);

        let response = client
            .get(&url)
            .header("Client-Id", self.client_id.as_str())
            .header("Authorization", format!("Bearer {}", self.access_token()))
            .send()
            .await?;

        let json: serde_json::Value = response.json().await?;

        let user_data = json["data"]
            .as_array()
            .and_then(|data_array| data_array.first())
            .ok_or("No user data found")?;

        let id_user = user_data["id"]
            .as_str()
            .ok_or("Invalid user ID")?;

        let created_at_str = user_data["created_at"]
            .as_str()
            .ok_or("Missing creation date")?;

        let created_at = DateTime::parse_from_rfc3339(created_at_str)
            .map_err(|_| "Failed to parse date")?
            .with_timezone(&Utc);

        let total_followers = self.get_followers(&client, id_user).await?;

        Ok(Some(UserData {
            username: user_name.to_string(),
            created_at,
            followers: total_followers,
        }))
    }
}

fn print_rankings(users_data: &[UserData]) {
    let by_followers = users_data
        .iter()
        .sorted_by(|a, b| b.followers.cmp(&a.followers))
        .collect::<Vec<_>>();

    let by_date = users_data
        .iter()
        .sorted_by_key(|x| x.created_at)
        .collect::<Vec<_>>();

    println!("\nRanking por número de seguidores:");
    by_followers
        .iter()
        .enumerate()
        .for_each(|(i, user)| {
            println!("{} - {}: {} seguidores", 
                i + 1, 
                user.username, 
                user.followers
            )
        });

    println!("\nRanking por antigüedad:");
    by_date
        .iter()
        .enumerate()
        .for_each(|(i, user)| {
            println!("{} - {}: Creado el {}", 
                i + 1, 
                user.username, 
                user.created_at.format("%d/%m/%Y")
            )
        });
}

async fn process_users(users: &[String], tw: &mut Twitch) -> Result<(), Box<dyn std::error::Error>> {
    let mut users_data = Vec::new();
    let mut not_found_users = Vec::new();
    println!("Obteniendo datos...");

    for name in users {
        match tw.get_user_data(name).await {
            Ok(Some(user_data)) => users_data.push(user_data),
            Ok(None) => not_found_users.push(name.clone()),
            Err(_) => not_found_users.push(name.clone()),
        }
    }

    print_rankings(&users_data);

    if !not_found_users.is_empty() {
        println!("\nUsuarios no encontrados:");
        not_found_users.iter().for_each(|user| println!("{}", user));
    }

    Ok(())
}

#[tokio::main]
async fn main() {
    dotenv().expect("No se encontró archivo .env");
    let client_id = env::var("TWITCH_CLIENT_ID").expect("CLIENT_ID no encontrado");
    let client_secret = env::var("TWITCH_CLIENT_SECRET").expect("CLIENT_SECRET no encontrado");

    let mut twitch = Twitch::new(client_id.clone(), client_secret);
    if let Err(e) = twitch.ensure_access_token().await {
        eprintln!("Error: {}", e);
        return;
    }
    
    let users: Vec<String> = vec![
    "abby", "ache", "adricontreras", "agustin", "alexby", "ampeter", "ander", 
    "arigameplays", "arigeli", "auronplay", "axozer", "beniju", "bycalitos", 
    "byviruzz", "carrera", "celopan", "cheeto", "crystalmolly", "darioemehache", 
    "dheyo", "djmario", "doble", "elvisa", "elyas360", "folagor", "grefg", 
    "guanyar", "hika", "hiper", "ibai", "ibelky", "illojuan", "imantado", 
    "irinaisasia", "jesskiu", "jopa", "jordiwild", "kenaisouza", "keroro", 
    "kiddkeo", "kikorivera", "knekro", "koko", "kronnozomber", "leviathan", 
    "litkillah", "lolalolita", "lolito", "luh", "luzu", "mangel", "mayichi", 
    "melo", "missasinonia", "mixwell", "mrjagger", "nategentile", "nexxuz", 
    "nia", "nilojeda", "nissaxter", "ollie", "orslok", "outconsumer", "papigavi", 
    "paracetamor", "patica", "paulagonu", "pausenpaii", "perxitaa", "plex", 
    "polispol", "quackity", "recuerdop", "reven", "rivers", "robertpg", "roier", 
    "rojuu", "rubius", "shadoune", "silithur", "spoksponha", "spreen", "spursito", 
    "staxx", "suzyroxx", "vicens", "vituber", "werlyb", "xavi", "xcry", "xokas", 
    "zarcort", "zeling", "zorman"
    ].iter().map(|&s| s.to_string()).collect();

    if let Err(e) = process_users(&users, &mut twitch).await {
        eprintln!("Error: {}", e);
        return;
    }    
}
