<?php
function obtenerTokenOAuth($clientId, $clientSecret) {
    $url = 'https://id.twitch.tv/oauth2/token';
    
    $data = [
        'client_id' => $clientId,
        'client_secret' => $clientSecret,
        'grant_type' => 'client_credentials'
    ];

    $options = [
        'http' => [
            'header'  => "Content-type: application/x-www-form-urlencoded\r\n",
            'method'  => 'POST',
            'content' => http_build_query($data)
        ]
    ];

    $context  = stream_context_create($options);
    $result = file_get_contents($url, false, $context);
    
    if ($result === FALSE) {
        die('Error al obtener el token OAuth');
    }

    $response = json_decode($result, true);
    return $response['access_token'];
}

function obtenerInfoUsuarioTwitch($accessToken, $clientId, $username) {
    $username = preg_replace('/[^a-zA-Z0-9_]/', '', $username);
    
    $url = "https://api.twitch.tv/helix/users?login=" . urlencode($username);

    $options = [
        'http' => [
            'header' => [
                "Authorization: Bearer $accessToken",
                "Client-ID: $clientId"
            ]
        ]
    ];

    $context = stream_context_create($options);
    $result = @file_get_contents($url, false, $context);
    
    if ($result === FALSE) {
        return null;
    }

    $response = json_decode($result, true);
    return $response['data'][0] ?? null;
}

function obtenerNumeroSeguidoresTwitch($accessToken, $clientId, $userId) {
    
    $url = "https://api.twitch.tv/helix/channels/followers?broadcaster_id=" . $userId;

    $options = [
        'http' => [
            'header' => [
                "Authorization: Bearer $accessToken",
                "Client-ID: $clientId"
            ]
        ]
    ];

    $context = stream_context_create($options);
    $result = @file_get_contents($url, false, $context);
    
    if ($result === FALSE) {
        return 0; 
    }

    $response = json_decode($result, true);
    return $response['total'] ?? 0; 
}

$participantes = [
    'Abby', 'Ache', 'Adri Contreras', 'Agustin', 'Alexby', 'Ampeter', 'Ander', 'Ari Gameplays', 'Arigely', 'Auronplay',
    'Axozer', 'Beniju', 'By Calitos', 'Byviruzz', 'Carrera', 'Celopan', 'Cheto', 'CrystalMolly', 'Dario Eme Hache', 'Dheyo',
    'DjMariio', 'Doble', 'Elvisa', 'Elyas360', 'Folagor', 'Grefg', 'Guanyar', 'Hika', 'Hiper', 'Ibai', 'Ibelky',
    'Illojuan', 'Imantado', 'Irina Isasia', 'JessKiu', 'Jopa', 'JordiWild', 'Kenai Souza', 'Keroro', 'Kidd Keo', 'Kiko Rivera',
    'Knekro', 'Koko', 'KronnoZomber', 'Leviathan', 'Lit Killah', 'Lola Lolita', 'Lolito', 'Luh', 'Luzu', 'Mangel',
    'Mayichi', 'Melo', 'MissaSinfonia', 'Mixwell', 'Mr. Jagger', 'Nate Gentile', 'Nexxuz', 'Nia', 'Nil Ojeda', 'NissaXter',
    'Ollie', 'Orslok', 'Outconsumer', 'Papi Gavi', 'Paracetamor', 'Patica', 'Paula Gonu', 'Pausenpaii', 'Perxitaa', 'Plex',
    'Polispol', 'Quackity', 'RecueroDP', 'Reven', 'Rivers', 'RobertPG', 'Roier', 'Rojuu', 'Rubius', 'Shadoune',
    'Silithur', 'SpokSponha', 'Spreen', 'Spursito', 'Staxx', 'SuzyRoxx', 'Vicens', 'Vituber', 'Werlyb', 'Xavi',
    'Xcry', 'Xokas', 'Zarcort', 'Zeling', 'Zorman'
];

$clientId = 'TU_CLIENT_ID';
$clientSecret = 'TU_CLIENT_SECRET';

$accessToken = obtenerTokenOAuth($clientId, $clientSecret);

$infoUsuarios = [];
$errores = [];

foreach ($participantes as $participante) {
    $usuario = obtenerInfoUsuarioTwitch($accessToken, $clientId, $participante);

    if ($usuario) {
        $seguidores = obtenerNumeroSeguidoresTwitch($accessToken, $clientId, $usuario['id']);
        
        $infoUsuarios[] = [
            'username' => $usuario['display_name'],
            'followers' => $seguidores, 
            'creation_date' => $usuario['created_at']
        ];
    } else {
        $errores[] = "El participante $participante no tiene usuario en Twitch.";
    }
}

$rankingPorSeguidores = $infoUsuarios;
usort($rankingPorSeguidores, function($a, $b) {
    return $b['followers'] <=> $a['followers'];
});

$rankingPorAntiguedad = $infoUsuarios;
usort($rankingPorAntiguedad, function($a, $b) {
    return strtotime($a['creation_date']) <=> strtotime($b['creation_date']);
});

echo "Ranking por número de seguidores:\n";
foreach ($rankingPorSeguidores as $usuario) {
    echo $usuario['username'] . " - " . $usuario['followers'] . " seguidores\n";
}

echo "\nRanking por antigüedad de la cuenta:\n";
foreach ($rankingPorAntiguedad as $usuario) {
    echo $usuario['username'] . " - Cuenta creada el " . date('d-m-Y', strtotime($usuario['creation_date'])) . "\n";
}

if (!empty($errores)) {
    echo "\nErrores:\n";
    foreach ($errores as $error) {
        echo $error . "\n";
    }
}