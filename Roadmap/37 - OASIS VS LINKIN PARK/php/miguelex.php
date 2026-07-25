<?php

$clientId = '';
$clientSecret = '';

function getAccessToken() {
    global $clientId, $clientSecret;
    
    $auth = base64_encode($clientId . ':' . $clientSecret);
    $options = [
        'http' => [
            'header' => "Content-Type: application/x-www-form-urlencoded\r\n" .
                        "Authorization: Basic " . $auth . "\r\n",
            'method'  => 'POST',
            'content' => http_build_query(['grant_type' => 'client_credentials']),
        ]
    ];
    
    $context  = stream_context_create($options);
    $result = file_get_contents('https://accounts.spotify.com/api/token', false, $context);
    
    if ($result === FALSE) {
        die('Error getting access token.');
    }
    
    $data = json_decode($result, true);
    return $data['access_token'];
}

function getArtistData($token, $artistName) {
    $artistName = urlencode($artistName);
    $options = [
        'http' => [
            'header' => "Authorization: Bearer " . $token . "\r\n",
            'method'  => 'GET',
        ]
    ];

    $context  = stream_context_create($options);
    $result = file_get_contents("https://api.spotify.com/v1/search?q=$artistName&type=artist", false, $context);
    
    if ($result === FALSE) {
        die('Error getting artist data.');
    }
    
    $data = json_decode($result, true);
    return $data['artists']['items'][0];  
}

function getArtistStats($artistId, $token) {
    $options = [
        'http' => [
            'header' => "Authorization: Bearer " . $token . "\r\n",
            'method'  => 'GET',
        ]
    ];

    $context  = stream_context_create($options);
    $result = file_get_contents("https://api.spotify.com/v1/artists/$artistId", false, $context);
    
    if ($result === FALSE) {
        die('Error getting artist stats.');
    }
    
    $data = json_decode($result, true);
    return [
        'name' => $data['name'],
        'followers' => $data['followers']['total'],
        'popularity' => $data['popularity'],
        'genres' => $data['genres'],
    ];
}

function getArtistTopTracks($artistId, $token) {
    $options = [
        'http' => [
            'header' => "Authorization: Bearer " . $token . "\r\n",
            'method'  => 'GET',
        ]
    ];

    $context  = stream_context_create($options);
    $result = file_get_contents("https://api.spotify.com/v1/artists/$artistId/top-tracks?market=US", false, $context);
    
    if ($result === FALSE) {
        die('Error getting top tracks.');
    }
    
    $data = json_decode($result, true);
    $mostPopularTrack = $data['tracks'][0];  
    return [
        'name' => $mostPopularTrack['name'],
        'playCount' => $mostPopularTrack['popularity'], 
        'album' => $mostPopularTrack['album']['name']
    ];
}

function compareBands($band1, $band2) {
    $token = getAccessToken();
    
    $band1Data = getArtistData($token, $band1);
    $band2Data = getArtistData($token, $band2);
    
    $band1Stats = getArtistStats($band1Data['id'], $token);
    $band2Stats = getArtistStats($band2Data['id'], $token);
    
    $band1TopTrack = getArtistTopTracks($band1Data['id'], $token);
    $band2TopTrack = getArtistTopTracks($band2Data['id'], $token);
    
    echo "\n{$band1} Stats:\n";
    print_r($band1Stats);
    echo "Canción más popular de {$band1}: ";
    print_r($band1TopTrack);
    
    echo "\n{$band2} Stats:\n";
    print_r($band2Stats);
    echo "Canción más popular de {$band2}: ";
    print_r($band2TopTrack);
    
    $moreFollowers = ($band1Stats['followers'] > $band2Stats['followers'])
        ? $band1
        : $band2;
    
    $morePopularTrack = ($band1TopTrack['playCount'] > $band2TopTrack['playCount'])
        ? $band1
        : $band2;
    
    echo "\nLa banda con más seguidores es: {$moreFollowers}\n";
    echo "La banda con la canción más popular es: {$morePopularTrack}\n";
}

echo "Introduce el nombre del primer grupo: ";
$band1 = trim(fgets(STDIN));

echo "Introduce el nombre del segundo grupo: ";
$band2 = trim(fgets(STDIN));

compareBands($band1, $band2);