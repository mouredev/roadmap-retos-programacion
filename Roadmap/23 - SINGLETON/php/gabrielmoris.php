<?php
/*
* EXERCISE:
* Explore the "singleton" design pattern and show how to create it
* with a generic example.
*/
class Singleton
{
    // private: To dont modify it out of the class
    // static: Belongs to the class instead of to the instances (Only one ocopyof $instance is shared across all Singleton Objects)
    // ?self:  $instance can be a object type $self or null
    private static ?self $instance = null;

    // Private constructor to prevent direct object creation
    private function __construct()
    {
    }

    public static function getInstance(): self
    {
        if (self::$instance === null) {
            self::$instance = new self();
        }
        return self::$instance;
    }

    public function someMethod()
    {
        echo "This is a method from the singleton instance!\n";
    }
}

// Usage

$instance1 = Singleton::getInstance(); // The construct is provate, so I call the public static function
$instance2 = Singleton::getInstance();

if ($instance1 === $instance2) {
    echo "Both instances are the same object\n";
} else {
    echo "Something went wrong - instances are different\n";
}

$instance1->someMethod();

/*
* EXTRA DIFFICULTY (optional):
* Use the "singleton" design pattern to represent a class that
* references the user session of a fictitious application.
* The session should allow assigning a user (id, username, name and email),
* retrieving the user's data and deleting the session data.
*/

class Session
{
    private static ?self $instance = null;
    private int $id;
    private string $username;
    private string $name;
    private string $email;

    private function __construct(int $id, string $username, string $name, string $email)
    {
        $this->id = $id;
        $this->username = $username;
        $this->name = $name;
        $this->email = $email;
    }

    public static function getInstance(): self
    {
        if (self::$instance === null) {
            self::$instance = new self(1, "", "", ""); // Initial empty session
        }
        return self::$instance;
    }

    public function setNewSession(string $username, string $name, string $email): void
    {
        $this->username = $username;
        $this->name = $name;
        $this->email = $email;

        echo "Session Updated with id " . $this->id . "\n";
    }

    public function getUsername(): string
    {
        return $this->username;
    }

    public function getName(): string
    {
        return $this->name;
    }

    public function getEmail(): string
    {
        return $this->email;
    }
}

$session1 = Session::getInstance();
$session1->setNewSession("gabrielcmoris", "gabriel", "gabrielcmoris@gabrielcmoris.com");
$dataSession1 = $session1->getUsername(); // Use getId()
var_dump($dataSession1);
