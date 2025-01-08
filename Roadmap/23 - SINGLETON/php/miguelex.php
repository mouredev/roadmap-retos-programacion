<?php
class Singleton {
    private static $instance = null;
    private static $contador = 0; // COntador con el numero de instancias que tenemos

    public static function getInstance() {
        self::$contador++;
        if (self::$instance === null) {
            self::$instance = new Singleton();
        }
        return self::$instance;
    }

    public function getContador() {
        return self::$contador;
    }
}

$singleton = Singleton::getInstance();
echo $singleton->getContador() . "\n";  // Debería imprimir 1

$singleton2 = Singleton::getInstance();
echo $singleton2->getContador() . "\n";  // Debería imprimir 2

$singleton3 = Singleton::getInstance();
echo $singleton3->getContador() . "\n";  // Debería imprimir 3

// Extra

echo "\n\nEJERCICIO EXTRA\n\n";

class UserSession {
    private static $instance = null;
    private $userData = [];

    public static function getInstance() {
        if (self::$instance === null) {
            self::$instance = new UserSession();
        }
        return self::$instance;
    }

    public function setUser($id, $username, $name, $email) {
        $this->userData[$id] = [
            'id' => $id,
            'username' => $username,
            'name' => $name,
            'email' => $email
        ];
    }

    public function getUser($id) {
        return isset($this->userData[$id]) ? $this->userData[$id] : null;
    }

    public function clearUser($id) {
        if (isset($this->userData[$id])) {
            unset($this->userData[$id]);
        }
    }

    public function getAllUsers() {
        return $this->userData;
    }

    public function clearAllUsers() {
        $this->userData = [];
    }
}


$session = UserSession::getInstance();

$session->setUser(1, 'miguelex', 'miguelex dm', 'miguelex@example.com');
$session->setUser(2, 'DrJones', 'Indiana Jones', 'indy@example.com');

echo "\n\nCreamos una segunda sesion y mostramos la lista de sesiones\n\n";
$session2 = UserSession::getInstance();
$allUsers = $session2->getAllUsers();
print_r($allUsers); 

echo "\n\nRecuperamos los datos del priemr usuario desde la primera sesion\n\n";
$userData1 = $session->getUser(1);
print_r($userData1);  

echo "\n\nRecuperamos los datos del segundo usuario desde la segunda sesion\n\n";
$userData2 = $session2->getUser(2);
print_r($userData2);  

echo "\n\nBorramos los datos del primer usuario desde la primera sesion\n\n";
$session->clearUser(1);
$userData1 = $session->getUser(1);
print_r($userData1);  

echo "\n\nMostramos la lista de usuarios de la primera sesion\n\n";
$allUsers = $session->getAllUsers();
print_r($allUsers);  

echo "\n\nBorramos todos los usuarios de la segunda sesion\n\n";
$session->clearAllUsers();
$allUsers = $session2->getAllUsers();
print_r($allUsers); 