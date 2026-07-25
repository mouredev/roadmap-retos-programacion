/* 🔥 EJERCICIO:
¡Dos de las bandas más grandes de la historia están de vuelta!
Oasis y Linkin Park han anunciado nueva gira, pero, ¿quién es más popular?
Desarrolla un programa que se conecte al API de Spotify y los compare.
Requisitos:
1. Crea una cuenta de desarrollo en https://developer.spotify.com.
2. Conéctate al API utilizando tu lenguaje de programación.
3. Recupera datos de los endpoint que tú quieras.
Acciones:
1. Accede a las estadísticas de las dos bandas.
   Por ejemplo: número total de seguidores, escuchas mensuales,
   canción con más reproducciones...
2. Compara los resultados de, por lo menos, 3 endpoint.
3. Muestra todos los resultados por consola para notificar al usuario.
4. Desarrolla un criterio para seleccionar qué banda es más popular.
 */
// 🔥 SIMULADOR: Comparador de Popularidad entre Oasis y Linkin Park 🔥
// Para ejecutar este programa, necesitarás Node.js y una cuenta en Spotify Developer.

const axios = require("axios"); // npm install axios

// Configuración del API de Spotify
const CLIENT_ID = "TU_CLIENT_ID"; // Reemplaza con tu Client ID de Spotify
const CLIENT_SECRET = "TU_CLIENT_SECRET"; // Reemplaza con tu Client Secret de Spotify
let accessToken = null;

// Función principal del programa
async function compararBandas() {
    console.log("🎸 ¡Bienvenido al comparador de popularidad entre Oasis y Linkin Park! 🎤");

    try {
        // Paso 1: Obtener el token de acceso
        await obtenerAccessToken();

        // Paso 2: Buscar información de las bandas
        const oasis = await buscarArtista("Oasis");
        const linkinPark = await buscarArtista("Linkin Park");

        if (!oasis || !linkinPark) {
            console.log("❌ No se pudo encontrar información de una o ambas bandas.");
            return;
        }

        // Paso 3: Obtener estadísticas de las bandas
        const statsOasis = await obtenerEstadisticas(oasis.id);
        const statsLinkinPark = await obtenerEstadisticas(linkinPark.id);

        // Paso 4: Mostrar resultados
        console.log("\n--- ESTADÍSTICAS DE LAS BANDAS ---");
        console.log(`Oasis: ${statsOasis.seguidores} seguidores, ${statsOasis.popularidad} de popularidad`);
        console.log(`Linkin Park: ${statsLinkinPark.seguidores} seguidores, ${statsLinkinPark.popularidad} de popularidad`);

        // Paso 5: Comparar y determinar la banda más popular
        const ganador = determinarGanador(statsOasis, statsLinkinPark);
        console.log(`\n🏆 ¡${ganador} es la banda más popular según los criterios establecidos! 🏆`);
    } catch (error) {
        console.error("❌ Error durante la ejecución:", error.message);
    }
}

// Función para obtener el token de acceso
async function obtenerAccessToken() {
    const authOptions = {
        url: "https://accounts.spotify.com/api/token",
        method: "post",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded",
            Authorization: `Basic ${Buffer.from(`${CLIENT_ID}:${CLIENT_SECRET}`).toString("base64")}`,
        },
        data: "grant_type=client_credentials",
    };

    const response = await axios(authOptions);
    accessToken = response.data.access_token;
}

// Función para buscar un artista por nombre
async function buscarArtista(nombre) {
    const response = await axios.get("https://api.spotify.com/v1/search", {
        headers: { Authorization: `Bearer ${accessToken}` },
        params: { q: nombre, type: "artist" },
    });

    const artistas = response.data.artists.items;
    return artistas.find(artista => artista.name.toLowerCase() === nombre.toLowerCase());
}

// Función para obtener estadísticas de un artista
async function obtenerEstadisticas(idArtista) {
    const response = await axios.get(`https://api.spotify.com/v1/artists/${idArtista}`, {
        headers: { Authorization: `Bearer ${accessToken}` },
    });

    const artista = response.data;
    return {
        seguidores: artista.followers.total,
        popularidad: artista.popularity,
    };
}

// Función para determinar la banda más popular
function determinarGanador(statsOasis, statsLinkinPark) {
    let puntosOasis = 0;
    let puntosLinkinPark = 0;

    // Criterio 1: Número de seguidores
    if (statsOasis.seguidores > statsLinkinPark.seguidores) {
        puntosOasis += 1;
    } else if (statsOasis.seguidores < statsLinkinPark.seguidores) {
        puntosLinkinPark += 1;
    }

    // Criterio 2: Popularidad
    if (statsOasis.popularidad > statsLinkinPark.popularidad) {
        puntosOasis += 1;
    } else if (statsOasis.popularidad < statsLinkinPark.popularidad) {
        puntosLinkinPark += 1;
    }

    // Determinar ganador
    if (puntosOasis > puntosLinkinPark) {
        return "Oasis";
    } else if (puntosOasis < puntosLinkinPark) {
        return "Linkin Park";
    } else {
        return "Empate";
    }
}

compararBandas();