<?php
/**
 * Implementación del patrón Singleton en PHP
 * 
 * Nota sobre las etiquetas PHP:
 * - En archivos que contienen solo código PHP, se recomienda omitir la etiqueta de cierre ?>
 * - Esto previene la inclusión accidental de espacios en blanco o caracteres después del cierre
 * - Sin embargo, si el archivo mezcla HTML y PHP, sí debes usar las etiquetas de cierre
 */

class BasicSingleton {
    // Instancia privada estática para almacenar la única instancia de la clase
    private static ?BasicSingleton $instance = null;
    
    // Constructor privado para evitar la creación de instancias con 'new'
    private function __construct() {}
    
    // Método público estático que controla el acceso a la instancia
    public static function getInstance(): BasicSingleton {
        // Si no existe la instancia, la crea
        if (self::$instance === null) {
            self::$instance = new self();
        }
        // Retorna la instancia única
        return self::$instance;
    }
    
    // Evitar la clonación del objeto
    private function __clone() {}
    
    // Evitar la deserialización del objeto
    public function __wakeup() {
        throw new Exception("No se puede deserializar un singleton.");
    }
}

/**
 * Ejercicio Extra: Singleton para Sesión de Usuario
 * ===============================================
 * Implementación de una clase de sesión de usuario utilizando el patrón Singleton
 */
class UserSession {
    // Instancia privada estática
    private static ?UserSession $instance = null;
    
    // Datos del usuario actual
    private ?array $userData = null;
    
    // Constructor privado
    private function __construct() {}
    
    // Método para obtener la instancia
    public static function getInstance(): UserSession {
        if (self::$instance === null) {
            self::$instance = new self();
        }
        return self::$instance;
    }
    
    /**
     * Método para establecer los datos del usuario
     * @param array $user Datos del usuario (id, username, name, email)
     */
    public function setUser(array $user): void {
        // Validar que el array contenga todos los campos requeridos
        $requiredFields = ['id', 'username', 'name', 'email'];
        foreach ($requiredFields as $field) {
            if (!isset($user[$field])) {
                throw new Exception("El campo {$field} es requerido");
            }
        }
        
        $this->userData = $user;
    }
    
    /**
     * Método para obtener los datos del usuario
     * @return array|null Datos del usuario o null si no hay sesión
     */
    public function getUser(): ?array {
        return $this->userData;
    }
    
    /**
     * Método para cerrar la sesión
     */
    public function logout(): void {
        $this->userData = null;
    }
    
    // Evitar la clonación del objeto
    private function __clone() {}
    
    // Evitar la deserialización del objeto
    public function __wakeup() {
        throw new Exception("No se puede deserializar un singleton.");
    }
}

// Ejemplo de uso:
// =============

try {
    // Ejemplo básico
    $singleton1 = BasicSingleton::getInstance();
    $singleton2 = BasicSingleton::getInstance();
    var_dump($singleton1 === $singleton2); // true
    
    // Ejemplo de sesión de usuario
    $session = UserSession::getInstance();
    
    // Crear un usuario de ejemplo
    $user = [
        'id' => 1,
        'username' => 'john_doe',
        'name' => 'John Doe',
        'email' => 'john@example.com'
    ];
    
    // Iniciar sesión
    $session->setUser($user);
    var_dump($session->getUser()); // Muestra los datos del usuario
    
    // Obtener la misma instancia en otro lugar del código
    $anotherSessionReference = UserSession::getInstance();
    var_dump($anotherSessionReference->getUser()); // Muestra los mismos datos
    
    // Cerrar sesión
    $session->logout();
    var_dump($session->getUser()); // null
    
} catch (Exception $e) {
    echo "Error: " . $e->getMessage();
}
?>