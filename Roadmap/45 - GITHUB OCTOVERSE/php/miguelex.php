<?php

class GitHubUserReport
{
    private $username;
    private $baseApiUrl = "https://api.github.com";
    private $headers = [
        "User-Agent: GitHub-Report-App",
        "Accept: application/vnd.github.v3+json"
    ];

    public function __construct($username)
    {
        $this->username = $username;
    }

    private function apiRequest($endpoint)
    {
        $url = $this->baseApiUrl . $endpoint;
        $curl = curl_init($url);

        curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($curl, CURLOPT_HTTPHEADER, $this->headers);
        curl_setopt($curl, CURLOPT_SSL_VERIFYPEER, false); // Asegura la validación SSL

        $response = curl_exec($curl);
        $httpCode = curl_getinfo($curl, CURLINFO_HTTP_CODE);
        $curlError = curl_error($curl);

        curl_close($curl);

        if ($response === false) {
            die("Error de conexión: $curlError\n");
        }

        if ($httpCode !== 200) {
            die("Error al conectar con la API de GitHub (HTTP $httpCode). Verifica el nombre de usuario.\n");
        }

        return json_decode($response, true);
    }


    private function getUserInfo()
    {
        return $this->apiRequest("/users/{$this->username}");
    }

    // Obtener todos los repositorios del usuario
    private function getUserRepos()
    {
        return $this->apiRequest("/users/{$this->username}/repos");
    }

    // Generar el informe
    public function generateReport()
    {
        $userInfo = $this->getUserInfo();
        $repos = $this->getUserRepos();

        $totalRepos = count($repos);
        $followers = $userInfo['followers'];
        $following = $userInfo['following'];

        // Analizar lenguajes utilizados
        $languages = [];
        foreach ($repos as $repo) {
            if (!empty($repo['language'])) {
                $languages[] = $repo['language'];
            }
        }
        $mostUsedLanguage = $languages ? array_count_values($languages) : [];
        arsort($mostUsedLanguage);
        $topLanguage = $mostUsedLanguage ? array_key_first($mostUsedLanguage) : "N/A";

        // Calcular estrellas totales y forks
        $totalStars = array_sum(array_column($repos, 'stargazers_count'));
        $totalForks = array_sum(array_column($repos, 'forks_count'));


        echo "=== Informe de GitHub para el usuario: {$this->username} ===\n";
        echo "Nombre: {$userInfo['name']}\n";
        echo "Bio: {$userInfo['bio']}\n";
        echo "Ubicación: {$userInfo['location']}\n";
        echo "Total de repositorios: $totalRepos\n";
        echo "Seguidores: $followers\n";
        echo "Seguidos: $following\n";
        echo "Lenguaje más utilizado: $topLanguage\n";
        echo "Total de estrellas: $totalStars\n";
        echo "Total de forks: $totalForks\n";
    }
}


echo "Ingrese el nombre de usuario de GitHub: ";
$username = trim(fgets(STDIN));

if (empty($username)) {
    die("Debe ingresar un nombre de usuario.\n");
}

$report = new GitHubUserReport($username);
$report->generateReport();
