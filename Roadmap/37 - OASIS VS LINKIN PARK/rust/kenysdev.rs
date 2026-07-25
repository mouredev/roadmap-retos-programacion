/*
_____________________________________
https://github.com/kenysdev
2024 - Rust
_____________________________________
37 OASIS VS LINKIN PARK
------------------------------------
* ¡Dos de las bandas más grandes de la historia están de vuelta!
* Oasis y Linkin Park han anunciado nueva gira, pero, ¿quién es más popular?
* Desarrolla un programa que se conecte al API de Spotify y los compare.
* Requisitos:
* 1. Crea una cuenta de desarrollo en https://developer.spotify.com.
* 2. Conéctate al API utilizando tu lenguaje de programación.
* 3. Recupera datos de los endpoint que tú quieras.
* Acciones:
* 1. Accede a las estadísticas de las dos bandas.
*    Por ejemplo: número total de seguidores, escuchas mensuales,
*    canción con más reproducciones...
* 2. Compara los resultados de, por lo menos, 3 endpoint.
* 3. Muestra todos los resultados por consola para notificar al usuario.
* 4. Desarrolla un criterio para seleccionar qué banda es más popular.

[dependencies]
tokio = { version = "1.37.0", features = ["full"] }
dotenv = "0.15.0"
rspotify = "0.13.3"
*/

use dotenv::dotenv;
use rspotify::{
    model::{ArtistId, FullArtist, SearchType, SearchResult},
    prelude::*,
    ClientCredsSpotify, Credentials,
};

struct Spotify {
    sp: ClientCredsSpotify,
}

impl Spotify {
    async fn new() -> Result<Self, Box<dyn std::error::Error>> {
        dotenv().ok();
        let creds = Credentials::from_env().unwrap();
        let sp = ClientCredsSpotify::new(creds);
        sp.request_token().await?;
        Ok(Self { sp })
    }

    async fn get_most_popular_artist(&self, name: &str) -> Result<FullArtist, Box<dyn std::error::Error>> {
    let search_result = self.sp.search(
        name,
        SearchType::Artist,
        None,
        None,
        Some(3),
        None,
    ).await?;

    match search_result {
        SearchResult::Artists(page) => {
            page.items.into_iter().max_by_key(|artist| artist.popularity)
                .ok_or_else(|| format!("No artists found for '{}'", name).into())
        },
        _ => Err(format!("Unexpected search result for '{}'", name).into()),
    }
}

    async fn artist_top_tracks(&self, id_artist: ArtistId<'_>) -> Option<Vec<rspotify::model::FullTrack>> {
        self.sp.artist_top_tracks(id_artist, None).await.ok()
    }
    
}

struct Versus {
    a1: FullArtist,
    a2: FullArtist,
    sp: Spotify,
    a1_score: u32,
    a2_score: u32,
}

impl Versus {
    fn new(artist1: FullArtist, artist2: FullArtist, spotify_instance: Spotify) -> Self {
        Self {
            a1: artist1,
            a2: artist2,
            sp: spotify_instance,
            a1_score: 0,
            a2_score: 0,
        }
    }

    fn popularity(&mut self) {
        let a1_pop = self.a1.popularity;
        let a2_pop = self.a2.popularity;

        println!("Popularidad: {} vs {}", a1_pop, a2_pop);
        if a1_pop > a2_pop {
            self.a1_score += 1;
        } else if a2_pop > a1_pop {
            self.a2_score += 1;
        }
    }

    fn followers(&mut self) {
        let a1_foll = self.a1.followers.total;
        let a2_foll = self.a2.followers.total;

        println!("Seguidores: {} vs {}", a1_foll, a2_foll);
        if a1_foll > a2_foll {
            self.a1_score += 1;
        } else if a2_foll > a1_foll {
            self.a2_score += 1;
        }
    }

    async fn top3_tracks(&mut self) -> Result<(), Box<dyn std::error::Error>> {
        let a1_top = self.sp.artist_top_tracks(self.a1.id.clone()).await.unwrap_or_default();
        let a2_top = self.sp.artist_top_tracks(self.a2.id.clone()).await.unwrap_or_default();
        let a1_pop: u32 = a1_top.iter().take(3).map(|track| track.popularity).sum();
        let a2_pop: u32 = a2_top.iter().take(3).map(|track| track.popularity).sum();
        println!("Popularidad Top 3 canciones: {} vs {}", a1_pop, a2_pop);

        if a1_pop > a2_pop {
            self.a1_score += 1;
        } else if a2_pop > a1_pop {
            self.a2_score += 1;
        }
        Ok(())
    }

    fn final_result(&self) {
        println!("\nRESULTADO FINAL:");
        println!("{}: {} puntos", self.a1.name, self.a1_score);
        println!("{}: {} puntos", self.a2.name, self.a2_score);

        if self.a1_score > self.a2_score {
            println!("\n¡'{}' gana el versus!", self.a1.name);
        } else if self.a2_score > self.a1_score {
            println!("\n¡'{}' gana el versus!", self.a2.name);
        } else {
            println!("\n¡Es un empate!");
        }
    }

    async fn start(&mut self) -> Result<(), Box<dyn std::error::Error>> {
        println!("{} vs {}", self.a1.name, self.a2.name);
        self.popularity();
        self.followers();
        self.top3_tracks().await?;
        self.final_result();
        Ok(())
    }
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    println!("VERSUS");
    let sp = Spotify::new().await?;
    
    let artist1 = sp.get_most_popular_artist("Oasis").await?;
    let artist2 = sp.get_most_popular_artist("Linkin Park").await?;

    let mut vs = Versus::new(artist1, artist2, sp);
    vs.start().await?;

    Ok(())
}
