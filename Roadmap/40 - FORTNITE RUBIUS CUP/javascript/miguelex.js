async function obtenerTokenOAuth(clientId, clientSecret) {
    const url = 'https://id.twitch.tv/oauth2/token';
    
    const data = new URLSearchParams();
    data.append('client_id', clientId);
    data.append('client_secret', clientSecret);
    data.append('grant_type', 'client_credentials');

    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: data
    });

    if (!response.ok) {
        throw new Error('Error al obtener el token OAuth');
    }

    const result = await response.json();
    return result.access_token;
}

async function obtenerInfoUsuarioTwitch(accessToken, clientId, username) {
    username = username.replace(/[^a-zA-Z0-9_]/g, '');
    
    const url = `https://api.twitch.tv/helix/users?login=${encodeURIComponent(username)}`;
    
    const response = await fetch(url, {
        method: 'GET',
        headers: {
            'Authorization': `Bearer ${accessToken}`,
            'Client-ID': clientId
        }
    });

    if (!response.ok) {
        return null;
    }

    const result = await response.json();
    return result.data[0] || null;
}

async function obtenerNumeroSeguidoresTwitch(accessToken, clientId, userId) {
    const url = `https://api.twitch.tv/helix/channels/followers?broadcaster_id=${userId}`;

    const response = await fetch(url, {
        method: 'GET',
        headers: {
            'Authorization': `Bearer ${accessToken}`,
            'Client-ID': clientId
        }
    });

    if (!response.ok) {
        return 0;
    }

    const result = await response.json();
    return result.total || 0;
}

(async () => {
    const participantes = [
        'Abby', 'Ache', 'Adri Contreras', 'Agustin', 'Alexby', 'Ampeter', 'Ander', 'Ari Gameplays',
        'Arigely', 'Auronplay', 'Axozer', 'Beniju', 'By Calitos', 'Byviruzz', 'Carrera', 'Celopan',
        'Cheto', 'CrystalMolly', 'Dario Eme Hache', 'Dheyo', 'DjMariio', 'Doble', 'Elvisa', 'Elyas360',
        'Folagor', 'Grefg', 'Guanyar', 'Hika', 'Hiper', 'Ibai', 'Ibelky', 'Illojuan', 'Imantado',
        'Irina Isasia', 'JessKiu', 'Jopa', 'JordiWild', 'Kenai Souza', 'Keroro', 'Kidd Keo', 'Kiko Rivera',
        'Knekro', 'Koko', 'KronnoZomber', 'Leviathan', 'Lit Killah', 'Lola Lolita', 'Lolito', 'Luh',
        'Luzu', 'Mangel', 'Mayichi', 'Melo', 'MissaSinfonia', 'Mixwell', 'Mr. Jagger', 'Nate Gentile',
        'Nexxuz', 'Nia', 'Nil Ojeda', 'NissaXter', 'Ollie', 'Orslok', 'Outconsumer', 'Papi Gavi',
        'Paracetamor', 'Patica', 'Paula Gonu', 'Pausenpaii', 'Perxitaa', 'Plex', 'Polispol', 'Quackity',
        'RecueroDP', 'Reven', 'Rivers', 'RobertPG', 'Roier', 'Rojuu', 'Rubius', 'Shadoune', 'Silithur',
        'SpokSponha', 'Spreen', 'Spursito', 'Staxx', 'SuzyRoxx', 'Vicens', 'Vituber', 'Werlyb', 'Xavi',
        'Xcry', 'Xokas', 'Zarcort', 'Zeling', 'Zorman'
    ];

    const clientId = 'TU_CLIENT_ID';
    const clientSecret = 'TU_CLIENT_SECRET';

    try {
        const accessToken = await obtenerTokenOAuth(clientId, clientSecret);

        const infoUsuarios = [];
        const errores = [];

        for (const participante of participantes) {
            const usuario = await obtenerInfoUsuarioTwitch(accessToken, clientId, participante);

            if (usuario) {
                const seguidores = await obtenerNumeroSeguidoresTwitch(accessToken, clientId, usuario.id);

                infoUsuarios.push({
                    username: usuario.display_name,
                    followers: seguidores,
                    creation_date: usuario.created_at
                });
            } else {
                errores.push(`El participante ${participante} no tiene usuario en Twitch.`);
            }
        }

        // Ordenar por número de seguidores
        const rankingPorSeguidores = [...infoUsuarios].sort((a, b) => b.followers - a.followers);

        console.log("Ranking por número de seguidores:");
        rankingPorSeguidores.forEach(usuario => {
            console.log(`${usuario.username} - ${usuario.followers} seguidores`);
        });

        // Ordenar por antigüedad
        const rankingPorAntiguedad = [...infoUsuarios].sort((a, b) => new Date(a.creation_date) - new Date(b.creation_date));

        console.log("\nRanking por antigüedad de la cuenta:");
        rankingPorAntiguedad.forEach(usuario => {
            console.log(`${usuario.username} - Cuenta creada el ${new Date(usuario.creation_date).toLocaleDateString()}`);
        });

        if (errores.length > 0) {
            console.log("\nErrores:");
            errores.forEach(error => console.log(error));
        }

    } catch (error) {
        console.error('Error:', error);
    }
})();
