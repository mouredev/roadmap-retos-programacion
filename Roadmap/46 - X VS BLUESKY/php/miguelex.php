<?php

class SocialNetwork {
    private $users = [];
    private $posts = [];
    private $follows = [];
    private $likes = [];

    public function registerUser($userId, $username) {
        if (isset($this->users[$userId])) {
            echo "El usuario con ID $userId ya existe.\n";
        } else {
            $this->users[$userId] = $username;
            echo "Usuario $username registrado con éxito.\n";
        }
    }

    public function followUser($followerId, $followeeId) {
        if (!isset($this->users[$followerId]) || !isset($this->users[$followeeId])) {
            echo "Uno de los usuarios no existe.\n";
            return;
        }
        $this->follows[$followerId][$followeeId] = true;
        echo "Usuario $followerId ahora sigue a $followeeId.\n";
    }

    public function unfollowUser($followerId, $followeeId) {
        if (isset($this->follows[$followerId][$followeeId])) {
            unset($this->follows[$followerId][$followeeId]);
            echo "Usuario $followerId ha dejado de seguir a $followeeId.\n";
        } else {
            echo "El usuario $followerId no sigue a $followeeId.\n";
        }
    }

    public function createPost($userId, $postId, $text) {
        if (!isset($this->users[$userId])) {
            echo "El usuario no existe.\n";
            return;
        }
        if (strlen($text) > 200) {
            echo "El texto del post excede los 200 caracteres.\n";
            return;
        }
        $this->posts[$postId] = [
            'userId' => $userId,
            'text' => $text,
            'createdAt' => date('Y-m-d H:i:s'),
            'likes' => 0
        ];
        echo "Post creado con éxito.\n";
    }

    public function deletePost($postId) {
        if (isset($this->posts[$postId])) {
            unset($this->posts[$postId]);
            echo "Post eliminado con éxito.\n";
        } else {
            echo "El post no existe.\n";
        }
    }

    public function likePost($userId, $postId) {
        if (!isset($this->users[$userId])) {
            echo "El usuario no existe.\n";
            return;
        }
        if (!isset($this->posts[$postId])) {
            echo "El post no existe.\n";
            return;
        }
        $this->likes[$userId][$postId] = true;
        $this->posts[$postId]['likes']++;
        echo "Like añadido al post $postId.\n";
    }

    public function unlikePost($userId, $postId) {
        if (isset($this->likes[$userId][$postId])) {
            unset($this->likes[$userId][$postId]);
            $this->posts[$postId]['likes']--;
            echo "Like eliminado del post $postId.\n";
        } else {
            echo "El usuario no ha hecho like en el post $postId.\n";
        }
    }

    public function viewUserFeed($userId) {
        if (!isset($this->users[$userId])) {
            echo "El usuario no existe.\n";
            return;
        }
        $userPosts = array_filter($this->posts, function($post) use ($userId) {
            return $post['userId'] == $userId;
        });
        usort($userPosts, function($a, $b) {
            return strtotime($b['createdAt']) - strtotime($a['createdAt']);
        });
        $userPosts = array_slice($userPosts, 0, 10);
        foreach ($userPosts as $post) {
            echo "ID: {$post['userId']}, Usuario: {$this->users[$post['userId']]}, Texto: {$post['text']}, Fecha: {$post['createdAt']}, Likes: {$post['likes']}\n";
        }
    }

    public function viewFollowedFeed($userId) {
        if (!isset($this->users[$userId])) {
            echo "El usuario no existe.\n";
            return;
        }
        $followedPosts = [];
        if (isset($this->follows[$userId])) {
            foreach ($this->follows[$userId] as $followeeId => $value) {
                foreach ($this->posts as $postId => $post) {
                    if ($post['userId'] == $followeeId) {
                        $followedPosts[] = $post;
                    }
                }
            }
        }
        usort($followedPosts, function($a, $b) {
            return strtotime($b['createdAt']) - strtotime($a['createdAt']);
        });
        $followedPosts = array_slice($followedPosts, 0, 10);
        foreach ($followedPosts as $post) {
            echo "ID: {$post['userId']}, Usuario: {$this->users[$post['userId']]}, Texto: {$post['text']}, Fecha: {$post['createdAt']}, Likes: {$post['likes']}\n";
        }
    }
}

// Menú interactivo
$network = new SocialNetwork();

while (true) {
    echo "Seleccione una opción:\n";
    echo "1. Registrar usuario\n";
    echo "2. Seguir a un usuario\n";
    echo "3. Dejar de seguir a un usuario\n";
    echo "4. Crear post\n";
    echo "5. Eliminar post\n";
    echo "6. Hacer like en un post\n";
    echo "7. Eliminar like de un post\n";
    echo "8. Ver feed del usuario\n";
    echo "9. Ver feed de usuarios seguidos\n";
    echo "0. Salir\n";
    $option = readline("Opción: ");

    switch ($option) {
        case 1:
            $userId = readline("ID de usuario: ");
            $username = readline("Nombre de usuario: ");
            $network->registerUser($userId, $username);
            break;
        case 2:
            $followerId = readline("ID del seguidor: ");
            $followeeId = readline("ID del seguido: ");
            $network->followUser($followerId, $followeeId);
            break;
        case 3:
            $followerId = readline("ID del seguidor: ");
            $followeeId = readline("ID del seguido: ");
            $network->unfollowUser($followerId, $followeeId);
            break;
        case 4:
            $userId = readline("ID de usuario: ");
            $postId = readline("ID del post: ");
            $text = readline("Texto del post: ");
            $network->createPost($userId, $postId, $text);
            break;
        case 5:
            $postId = readline("ID del post: ");
            $network->deletePost($postId);
            break;
        case 6:
            $userId = readline("ID de usuario: ");
            $postId = readline("ID del post: ");
            $network->likePost($userId, $postId);
            break;
        case 7:
            $userId = readline("ID de usuario: ");
            $postId = readline("ID del post: ");
            $network->unlikePost($userId, $postId);
            break;
        case 8:
            $userId = readline("ID de usuario: ");
            $network->viewUserFeed($userId);
            break;
        case 9:
            $userId = readline("ID de usuario: ");
            $network->viewFollowedFeed($userId);
            break;
        case 0:
            exit("¡Hasta luego!\n");
        default:
            echo "Opción no válida. Intente de nuevo.\n";
            break;
    }
}

