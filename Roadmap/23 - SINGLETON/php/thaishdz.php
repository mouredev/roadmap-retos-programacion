<?php

/*
* Decidí separar responsabilidades (La S de SOLID bien dentro del peshito) por eso tengo 2 clases :
* User
* Session
*/

class User
{
    private string $id;
    private static $instance = null;


    // Constructor con Promoted Properties (no sé me apeteció usarlo)
    private function __construct(
        private string $username,
        private string $name,
        private string $email,
    )
    {
        $this->id = bin2hex(random_bytes(16)); // "random_bytes" genera una cadena de 16 bytes y "bin2hex" la convierte a hexadecimal
    }

    public static function getInstance(string $username,string $name,string $email)
    {
        if (is_null(self::$instance))
        {
            self::$instance = new self($username, $name, $email);
        }
        return self::$instance;
    }

    public function data(): array
    {
        return [
            'ID'        => $this->id,
            'Username'  => $this->username,
            'Name'      => $this->name,
            'Email'     => $this->email
        ];
    }

    public function reset(): void
    {
        $this->id = '';
        $this->username = '';
        $this->name = '';
        $this->email = '';
    }

    private function __clone() {}

    public function __wakeup() 
    {
        throw new \Exception('Cannot unserialize a Singleton');
    }
}

// --------------------------------------------------------------------
class Session
{
    private string $id;
    private User $user;


    public function __construct(
        private string $username,
        private string $name,
        private string $email,
    )
    {
        $this->id = bin2hex(random_bytes(16)); 
        $this->user = User::getInstance($username, $name, $email);
    }

    public function id()
    {
        return $this->id;
    }

    public function user()
    {
        $userData = $this->user->data();

        // Solo añadir 'SessionID' si la sesión está activa
        if ($this->id) {
            $userData['SessionID'] = $this->id;
        }
        return $userData;
    }

    public function logout()
    {
       $this->id = '';
       return $this->user->reset();
    }

}

// --------------------------------------------------------------------

$session = new Session("toxicPlayer69", "Eufemio", "toxicPlayer@gmail.com");

var_dump($session->user());
$session->logout();
var_dump($session->user());
