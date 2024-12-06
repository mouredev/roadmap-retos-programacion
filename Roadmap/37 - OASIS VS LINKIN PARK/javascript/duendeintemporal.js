//#37 - OASIS VS LINKING PARK   
/*
 * EJERCICIO:
 * Oasis y Linkin Park han anunciado nueva gira, pero, ¿quién es más popular?
 * ¡Dos de las bandas más grandes de la historia están de vuelta!
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
 */

// Note: This code is written in TypeScript, a superset of JavaScript that adds optional static typing and other features. The code is almost identical to JavaScript, with the main difference being the addition of type annotations to reference values. This allows for better code completion, error checking, and maintainability.

// For example, the `getArtistId` function is annotated with the return type `Promise<string | null>`, indicating that it returns a promise that resolves to either a string or null. This helps catch type-related errors at compile-time rather than runtime.

// alert('Script is running!');



/* Instructions: You need to create a developer account on Spotify.
Run these commands in a console in a Node.js environment:

npm create vite@latest spotify-profile-demo -- --template vanilla-ts

cd spotify-profile-demo
npm install
npm run dev

Then, delete the files in the src and public folders. 

Replace the index.html file with the following code:

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Profile Data</title>
</head>
<body>
    <h1>Display Your Spotify Profile Data</h1>

<section id="profile">
<h2>Logged in as <span id="displayName"></span></h2>
<span id="avatar"></span>
<ul>
    <li>User ID: <span id="id"></span></li>
    <li>Email: <span id="email"></span></li>
    <li>Spotify URI: <a id="uri" href="#"></a></li>
    <li>Link: <a id="url" href="#"></a></li>
    <li>Profile Image: <span id="imgUrl"></span></li>
</ul>
<p id="result"></p>
</section>
<script src="./src/script.ts"></script>

</body>
</html>

*/

/* You will also need to create a new app and set the configuration settings as follows... 

Client ID
[insert your client_id here]
App Status
Development mode
App Name
RoadMapExercise37
App Description
It compares results from two bands and displays a prediction of which will be more popular...
Website
Redirect URIs
http://localhost:5173/callback
Bundle IDs
Android packages
APIs Used
Web API
*/

/* Then create a file named script.ts in the src folder with the following code: */
async function main() {
    const clientId = "use the app id_client code";
    const params = new URLSearchParams(window.location.href.split('?')[1]);
    const code = params.get("code");

    console.log("Authorization Code:", code); // Debugging log

    if (!code) {
        console.log("No authorization code found. Redirecting to auth flow...");
        sessionStorage.setItem("lastAuthAttempt", JSON.stringify({ timestamp: Date.now() }));
        redirectToAuthCodeFlow(clientId);
    } else {
        try {
            const accessToken = await getAccessToken(clientId, code);
            console.log("Access Token:", accessToken); // Debugging log

            const profile = await fetchProfile(accessToken);
            console.log("User Profile:", profile); // Debugging log
            populateUI(profile);
            sessionStorage.setItem("userProfile", JSON.stringify(profile)); // Store user profile

            const oasisId = await getArtistId(accessToken, "Oasis");
            const linkinParkId = await getArtistId(accessToken, "Linkin Park");
            console.log("Oasis ID:", oasisId);
            console.log("Linkin Park ID:", linkinParkId);

            if (oasisId && linkinParkId) {
                const oasisData = await getArtistData(accessToken, oasisId);
                const linkinParkData = await getArtistData(accessToken, linkinParkId);
        
                // Fetch top tracks for both artists
                const oasisTopTracks = await getTopTracks(accessToken, oasisId);
                const linkinParkTopTracks = await getTopTracks(accessToken, linkinParkId);
        
                // Add top tracks to the data objects
                oasisData.tracks = oasisTopTracks.tracks;
                linkinParkData.tracks = linkinParkTopTracks.tracks;

                if (oasisData && linkinParkData) {
                    compareArtists(oasisData, linkinParkData);
                }
            }
        } catch (error) {
            console.error("Failed to fetch profile or access token:", error);
            // Check if the error is related to fetching the access token or profile
            if (error instanceof Error && (error.message.includes("Failed to fetch profile") || error.message.includes("Failed to get access token"))) {
                redirectToAuthCodeFlow(clientId);
            } else {
                console.error("An unexpected error occurred:", error);
            }
        }
    }
}



async function getArtistId(accessToken: string, artistName: string): Promise<string | null> {
    const result = await fetch(`https://api.spotify.com/v1/search?q=${artistName}&type=artist`, {
        method: "GET",
        headers: { Authorization: `Bearer ${accessToken}` }
    });

    const data = await result.json();
    if (data.artists.items.length > 0) {
        return data.artists.items[0].id;
    } else {
        return null;
    }
}

interface TopTrack {
    name: string;
    popularity: number;
}

function compareArtists(oasisData: any, linkinParkData: any) {
    let oasisTopTrack: TopTrack | null = null;
    let linkinParkTopTrack: TopTrack | null = null;

    // Check if oasisData.tracks exists and has length
    if (oasisData.tracks && oasisData.tracks.length > 0) {
        oasisTopTrack = {
            name: oasisData.tracks[0].name,
            popularity: oasisData.tracks[0].popularity
        };
    }

    // Check if linkinParkData.tracks exists and has length
    if (linkinParkData.tracks && linkinParkData.tracks.length > 0) {
        linkinParkTopTrack = {
            name: linkinParkData.tracks[0].name,
            popularity: linkinParkData.tracks[0].popularity
        };
    }

    console.log("Oasis:");
    if (oasisTopTrack) {
        console.log(`Oasis top track: ${oasisTopTrack.name}, popularity: ${oasisTopTrack.popularity}`);
    } else {
        console.log("No top track found for Oasis.");
    }
    console.log(`Followers: ${oasisData.followers?.total ?? 'N/A'}`);
    console.log(`Popularity: ${oasisData.popularity ?? 'N/A'}`);
    console.log(`Genres: ${oasisData.genres?.join(", ") ?? 'N/A'}`);

    console.log("Linkin Park:");
    if (linkinParkTopTrack) {
        console.log(`Linkin Park top track: ${linkinParkTopTrack.name}, popularity: ${linkinParkTopTrack.popularity}`);
    } else {
        console.log("No top track found for Linkin Park.");
    }
    console.log(`Followers: ${linkinParkData.followers?.total ?? 'N/A'}`);
    console.log(`Popularity: ${linkinParkData.popularity ?? 'N/A'}`);
    console.log(`Genres: ${linkinParkData.genres?.join(", ") ?? 'N/A'}`);

    // Compare followers
    if (oasisData.followers && linkinParkData.followers) {
        if (oasisData.followers.total > linkinParkData.followers.total) {
            console.log("Oasis is more popular based on followers.");
        } else if (oasisData.followers.total < linkinParkData.followers.total) {
            console.log("Linkin Park is more popular based on followers.");
        } else {
            console.log("Both artists have the same number of followers.");
        }
    }

    // Compare popularity
    if (oasisData.popularity !== undefined && linkinParkData.popularity !== undefined) {
        if (oasisData.popularity > linkinParkData.popularity) {
            console.log("Oasis is more popular based on popularity score.");
        } else if (oasisData.popularity < linkinParkData.popularity) {
            console.log("Linkin Park is more popular based on popularity score.");
        } else {
            console.log("Both artists have the same popularity score.");
        }
    }

    // Compare top track popularity
    if (oasisTopTrack && linkinParkTopTrack) {
        if (oasisTopTrack.popularity > linkinParkTopTrack.popularity) {
            console.log("Oasis is more popular based on top track popularity score.");
        } else if (oasisTopTrack.popularity < linkinParkTopTrack.popularity) {
            console.log("Linkin Park is more popular based on top track popularity score.");
        } else {
            console.log("Both artists have the same top track popularity score.");
        }
    }

    document.getElementById("result")!.innerText = "Display the Console DeveloperTools to See all The result Comparations";
}


async function redirectToAuthCodeFlow(clientId: string) {
    
    const verifier = generateCodeVerifier(128);
    const challenge = await generateCodeChallenge(verifier);

    localStorage.setItem("verifier", verifier); // Store the verifier for later use

    const params = new URLSearchParams();
    params.append("client_id", clientId);
    params.append("response_type", "code");
    params.append("redirect_uri", "http://localhost:5173/callback"); // Ensure this matches your Spotify app settings
    params.append("scope", "user-read-private user-read-email user-top-read");
    params.append("code_challenge_method", "S256");
    params.append("code_challenge", challenge);

    // Redirect the user to the Spotify authorization page
    document.location = `https://accounts.spotify.com/authorize?${params.toString()}`;
}


function generateCodeVerifier(length: number) {
    let text = '';
    let possible = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';

    for (let i = 0; i < length; i++) {
        text += possible.charAt(Math.floor(Math.random() * possible.length));
    }
    return text;
}

async function generateCodeChallenge(codeVerifier: string) {
    const data = new TextEncoder().encode(codeVerifier);
    const digest = await window.crypto.subtle.digest('SHA-256', data);
    return btoa(String.fromCharCode.apply(null, [...new Uint8Array(digest)]))
        .replace(/\+/g, '-')
        .replace(/\//g, '_')
        .replace(/=+$/, '');
}

async function getArtistData(accessToken: string, artistId: string): Promise<any> {
    const result = await fetch(`https://api.spotify.com/v1/artists/${artistId}`, {
        method: "GET",
        headers: { Authorization: `Bearer ${accessToken}` }
    });

    if (!result.ok) {
        const errorData = await result.json();
        console.error("Failed to fetch artist data:", errorData);
        throw new Error(`Failed to fetch artist data: ${result.status} ${result.statusText}`);
    }

    return await result.json();
}

async function getTopTracks(accessToken: string, artistId: string, market: string = 'US'): Promise<any> {
    const response = await fetch(`https://api.spotify.com/v1/artists/${artistId}/top-tracks?market=${market}`, {
        method: "GET",
        headers: { Authorization: `Bearer ${accessToken}` }
    });

    if (!response.ok) {
        const errorData = await response.json();
        console.error("Failed to fetch top tracks:", errorData);
        throw new Error(`Failed to fetch top tracks: ${response.status} ${response.statusText}`);
    }

    return await response.json();
}


async function getAccessToken(clientId: string, code: string): Promise<string> {
    const primaryUrl = 'https://accounts.spotify.com/api/token';
    const verifier = localStorage.getItem("verifier");

    const params = new URLSearchParams();
    params.append("client_id", clientId);
    params.append("grant_type", "authorization_code");
    params.append("code", code);
    params.append("redirect_uri", "http://localhost:5173/callback");
    params.append("code_verifier", verifier!); // Use the verifier stored in local storage

    try {
        const result = await fetch(primaryUrl, {
            method: "POST",
            headers: { "Content-Type": "application/x-www-form-urlencoded" },
            body: params
        });

        if (result.ok) {
            const { access_token } = await result.json();
            return access_token;
        } else {
            const errorData = await result.json();
            console.error("Failed to get access token:", errorData);
            throw new Error(`Failed to get access token: ${result.status} ${errorData.error_description}`);
        }
    } catch (error: any) {
        console.error(`Error using primary URL: ${error.message}`);
        throw error; // Rethrow the error for further handling
    }
}


interface UserProfile {
    country: string;
    display_name: string;
    email: string;
    explicit_content: {
        filter_enabled: boolean,
        filter_locked: boolean
    },
    external_urls: { spotify: string; };
    followers: { href: string; total: number; };
    href: string;
    id: string;
    images: Image[];
    product: string;
    type: string;
    uri: string;
}

interface Image {
    url: string;
    height: number;
    width: number;
}

function populateUI(profile: UserProfile) {
    document.getElementById("displayName")!.innerText = profile.display_name;
    if (profile.images[0]) {
        const profileImage = new Image(200, 200);
        profileImage.src = profile.images[0].url;
        document.getElementById("avatar")!.appendChild(profileImage);
    }
    document.getElementById("id")!.innerText = profile.id;
    document.getElementById("email")!.innerText = profile.email;
    document.getElementById("uri")!.innerText = profile.uri;
    document.getElementById("uri")!.setAttribute("href", profile.external_urls.spotify);
    document.getElementById("url")!.innerText = profile.href;
    document.getElementById("url")!.setAttribute("href", profile.href);
    document.getElementById("imgUrl")!.innerText = profile.images[0]?.url ?? '(no profile image)';
}

async function fetchProfile(token: string): Promise<UserProfile> {
    const result = await fetch("https://api.spotify.com/v1/me", {
        method: "GET",
        headers: { Authorization: `Bearer ${token}` }
    });

    if (!result.ok) {
        const errorData = await result.json();
        console.error("Failed to fetch profile:", errorData);
        throw new Error(`Failed to fetch profile: ${result.status} ${result.statusText}`);
    }

    return await result.json();
}


// Start the main function
main();
