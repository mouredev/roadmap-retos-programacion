/*
_____________________________________
https://github.com/kenysdev
2024 - Rust
_____________________________________
45 GITHUB OCTOVERSE
------------------------------------

 * EJERCICIO:
 * GitHub ha publicado el Octoverse 2024, el informe
 * anual del estado de la plataforma:
 * https://octoverse.github.com
 *
 * Utilizando el API de GitHub, crea un informe asociado
 * a un usuario concreto.
 * 
 * - Se debe poder definir el nombre del usuario
 *   sobre el que se va a generar el informe.
 *   
 * - Crea un informe de usuario basándote en las 5 métricas
 *   que tú quieras, utilizando la informración que te
 *   proporciona GitHub. Por ejemplo:
 *   - Lenguaje más utilizado
 *   - Cantidad de repositorios
 *   - Seguidores/Seguidos
 *   - Stars/forks
 *   - Contribuciones
 *   (lo que se te ocurra)
*/

use std::collections::HashMap;
use reqwest;
use serde_json::Value;
use std::error::Error;

struct GitHubApi {
    user_data: HashMap<String, Value>,
}

impl GitHubApi {
    async fn new(user_name: &str) -> Result<Self, Box<dyn Error>> {
        let url = format!("https://api.github.com/users/{}", user_name);
        let client = reqwest::Client::new();
        let user_data: HashMap<String, Value> = client.get(&url)
            .header("User-Agent", "Mozilla/5.0")
            .send()
            .await?
            .json()
            .await?;

        Ok(Self { user_data })
    }

    fn verify_status(&self) -> bool {
        match self.user_data.get("status") {
            Some(status) if status.as_str() == Some("404") => {
                println!("Usuario no encontrado.");
                false
            }
            _ => true
        }
    }

    fn get_repo_info(repo: &Value) -> String {
        format!(
            "Lang: {}\nRepo: {}\nStars: {}\nForks: {}",
            repo.get("full_name").and_then(|v| v.as_str()).unwrap_or("Desconocido"),
            repo.get("language").and_then(|v| v.as_str()).unwrap_or("Desconocido"),
            repo.get("stargazers_count").and_then(|v| v.as_u64()).unwrap_or(0),
            repo.get("forks_count").and_then(|v| v.as_u64()).unwrap_or(0)
        )
    }

    fn print_basic_info(&self) {
        if !self.verify_status() { return; }

        println!(
            "-------------------------------------------\n\
            Nombre: {}\n\
            Creación: {}\n\
            Repos: {}\n\
            Gists: {}\n\
            Seguidores: {}\n\
            Seguidos: {}\n\
            -------------------------------------------",
            self.user_data.get("name").and_then(|v| v.as_str()).unwrap_or("Desconocido"),
            self.user_data.get("created_at").and_then(|v| v.as_str()).unwrap_or("Desconocido"),
            self.user_data.get("public_repos").and_then(|v| v.as_u64()).unwrap_or(0),
            self.user_data.get("public_gists").and_then(|v| v.as_u64()).unwrap_or(0),
            self.user_data.get("followers").and_then(|v| v.as_u64()).unwrap_or(0),
            self.user_data.get("following").and_then(|v| v.as_u64()).unwrap_or(0)
        );
    }

    async fn print_repos_info(&self) -> Result<(), Box<dyn Error>> {
        if !self.verify_status() { return Ok(()); }

        if let Some(repos_url) = self.user_data.get("repos_url").and_then(|v| v.as_str()) {
            let client = reqwest::Client::new();
            let repos: Vec<Value> = client.get(repos_url)
                .header("User-Agent", "Mozilla/5.0")
                .send()
                .await?
                .json()
                .await?;

            let mut languages: HashMap<String, u32> = HashMap::new();
            println!("Repositorios publicos:");

            for repo in &repos {
                println!("\n{}", Self::get_repo_info(repo));

                if let Some(language) = repo.get("language").and_then(|v| v.as_str()) {
                    *languages.entry(language.to_string()).or_insert(0) += 1;
                }
            }

            let most_used_lang = languages.iter()
                .max_by_key(|&(_, count)| *count)
                .map(|(lang, count)| (lang, *count));

            println!("________\nTotal de repositorios: '{}'", repos.len());
            if let Some((lang, count)) = most_used_lang {
                println!("El lenguaje más utilizado: '{}' ({})", lang, count);
            }
        }

        Ok(())
    }
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    println!("Informe sobre los datos del usuario en GitHub");
    print!("Usuario: ");
    
    use std::io::{self, Write};
    io::stdout().flush()?;

    let mut user_name = String::new();
    io::stdin().read_line(&mut user_name)?;
    let user_name = user_name.trim();

    let github = GitHubApi::new(user_name).await?;
    github.print_repos_info().await?;
    github.print_basic_info();

    Ok(())
}
