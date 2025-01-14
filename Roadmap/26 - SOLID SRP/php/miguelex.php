<?php

    // Ejercicio básico

    class User {
        private $name;
        private $role;

        public function __construct($name, $role){
            $this->name = $name;
            $this->role = $role;
        }

        public function getName(){
            return $this->name;
        }

        public function getRole(){
            return $this->role;
        }

        public function saveUser(){
            $file = fopen('usersBD.txt', 'a');
            fwrite($file, $this->name . ' is a  ' . $this->role . PHP_EOL);
            fclose($file);
        }
    }

    echo "\n\nVamos a mostrar primero una clase que no cumple el SRP. Esto se debe a que la clase, ademas de gestionar el usuario, realizar la inserccion en BD (en este caso simualdo con un txt)\n\n";
    $user1 = new User('Miguel', 'Admin');
    $user1->saveUser();
    $user2 = new User('Maria', 'user');
    $user2->saveUser();
    echo "\nSe ha creado el archivo y podemos ver se ha ineertado correctamente. Vamos a refactorizar ahora para cumplir el SRP\n\n";


    class Users {
        private $name;
        private $role;

        public function __construct($name, $role){
            $this->name = $name;
            $this->role = $role;
        }

        public function getName(){
            return $this->name;
        }

        public function getRole(){
            return $this->role;
        }
    }

    class UsersBD {
        private $path;

        public function __construct($path){
            $this->path = $path;
        }

        public function saveUser(Users $users){
            $file = fopen($this->path, 'a');
            fwrite($file, $users->getName() . ' is a  ' . $users->getRole() . PHP_EOL);
            fclose($file);
        }
    }

    echo "\n\nHemos refactorizado el codigo anterior, separando la parte de usuarios de la parte de BD\n\n";
    $user1 = new Users('Miguel', 'Admin');
    $user2 = new Users('Maria', 'user');
    $userBD = new UsersBD('userBDSRP.txt');
    $userBD->saveUser($user1);
    $userBD->saveUser($user2);
    echo "\nSe ha creado el archivo y podemos ver se ha insertado correctamente. A efectos de funcionamiento ambas solucioens funcionan igual pero la segunda es mas legible y mantenible\n\n";

    echo "\n\nEjercicio Extra\n\n";

    // Extra

   class Library {
    private $books = [];
    private $users = [];
    private $loans = [];

    public function addBook ($title, $author, $copies){
        $this->books[] = ['title' => $title, 'author' => $author, 'copies' => $copies];
    }

    public function addUser ($name, $id, $email){
        $this->users[] = ['name' => $name, 'id' => $id, 'email' => $email];
    }

    public function loanBook($userId, $bookTitle) {
        foreach ($this->books as &$book) {
            if ($book['title'] === $bookTitle && $book['copies'] > 0) {
                $this->loans[] = [
                    'userId' => $userId,
                    'bookTitle' => $bookTitle,
                    'date' => date('Y-m-d H:i:s')
                ];
                $book['copies']--;
                return "El libro ha sido prestado.";
            }
        }
        return "El libro no está disponible.";
    }

    public function returnBook($userId, $bookTitle) {
        foreach ($this->loans as $key => $loan) {
            if ($loan['userId'] === $userId && $loan['bookTitle'] === $bookTitle) {
                unset($this->loans[$key]);
                foreach ($this->books as &$book) {
                    if ($book['title'] === $bookTitle) {
                        $book['copies']++;
                        return "El libro ha sido devuelto.";
                    }
                }
            }
        }
        return "No se encontró el préstamo.";
   }

   public function getBooks(){
        return $this->books;
   }

   public function getUsers(){
        return $this->users;
   }

    public function getLoans(){
          return $this->loans;
    }
}

$myLibrary = new Library();

echo "\n\nVamos a mostrar un ejemplo de una clase que no cumple el SRP. En este caso es una clase que gestiona una biblioteca\n\n";

do {
    echo "\n\nMENÚ\n\n";
    echo "";
    echo "1. Añadir libro\n";
    echo "2. Añadir usuario\n";
    echo "3. Prestar libro\n";
    echo "4. Devolver libro\n";
    echo "5. Mostrar libros\n";
    echo "6. Mostrar usuarios\n";
    echo "7. Mostrar préstamos\n";
    echo "8. Salir\n";
    echo "";
    echo "Elija una opción: ";

    $option = readline();
    echo "";
    
    switch ($option) {
        case 1:
            echo "Título: ";
            $title = readline();
            echo "Autor: ";
            $author = readline();
            echo "Copias: ";
            $copies = readline();
            $myLibrary->addBook($title, $author, $copies);
            break;
        case 2:
            echo "Nombre: ";
            $name = readline();
            echo "ID: ";
            $id = readline();
            echo "Email: ";
            $email = readline();
            $myLibrary->addUser($name, $id, $email);
            break;
        case 3:
            echo "ID del usuario: ";
            $userId = readline();
            echo "Título del libro: ";
            $bookTitle = readline();
            echo $myLibrary->loanBook($userId, $bookTitle) . "\n";
            break;
        case 4:
            echo "ID del usuario: ";
            $userId = readline();
            echo "Título del libro: ";
            $bookTitle = readline();
            echo $myLibrary->returnBook($userId, $bookTitle) . "\n";
            break;
        case 5:
            print_r($myLibrary->getBooks());
            break;
        case 6:
            print_r($myLibrary->getUsers());
            break;
        case 7:
            print_r($myLibrary->getLoans());
            break;
    }
    
} while (($option != 8));


// Vamos ahora a refactorizar para aplicar el SRP. Ahora tnedremos una clase para los libros, otra para los autores y otra para los prestamos, asi como sus respectivos managers

class Books {
    private $title;
    private $author;
    private $copies;

    public function __construct($title, $author, $copies){
        $this->title = $title;
        $this->author = $author;
        $this->copies = $copies;
    }

    public function getTitle(){
        return $this->title;
    }

    public function getAuthor(){
        return $this->author;
    }

    public function getCopies(){
        return $this->copies;
    }

    public function loanBook(){
        if ($this->copies > 0) {
            $this->copies--;
            return true;
        } else {
            return false;
        }
    }

    public function returnBook(){
        $this->copies++;
    }
}

class UsersLibrary {
    private $name;
    private $id;
    private $email;

    public function __construct($name, $id, $email){
        $this->name = $name;
        $this->id = $id;
        $this->email = $email;
    }

    public function getName(){
        return $this->name;
    }

    public function getId(){
        return $this->id;
    }

    public function getEmail(){
        return $this->email;
    }

}

class Loan {
    private $userId;
    private $bookTitle;
    private $date;

    public function __construct($userId, $bookTitle){
        $this->userId = $userId;
        $this->bookTitle = $bookTitle;
        $this->date = date('Y-m-d H:i:s');
    }

    public function getUserId(){
        return $this->userId;
    }

    public function getBookTitle(){
        return $this->bookTitle;
    }

    public function getDate(){
        return $this->date;
    }
}

class BookManager {
    private $books = [];

    public function addBook(Books $book){
        $this->books[] = $book;
    }

    public function getBooks(){
        return $this->books;
    }

    public function findBookByTitle($title){
        foreach ($this->books as $book) {
            if ($book->getTitle() === $title) {
                return $book;
            }
        }
        return null;
    }
}

class UserManager{
    private $users = [];

    public function addUser(UsersLibrary $user){
        $this->users[] = $user;
    }

    public function getUsers(){
        return $this->users;
    }

    public function findUserById($id){
        foreach ($this->users as $user) {
            if ($user->getId() === $id) {
                return $user;
            }
        }
        return null;
    }
}

class LoanManager{
    private $loans = [];

    public function loanBook(UsersLibrary $user, Books $book){
        if ($book->loanBook()) {
            $this->loans[] = new Loan($user->getId(), $book->getTitle());
        } else {
            echo "No hay copias disponibles para el libro: " . $book->getTitle() . "\n";
        }
    }

    public function returnBook(UsersLibrary $user, Books $book){
        foreach ($this->loans as $key => $loan) {
            if ($loan->getUserId() === $user->getId() && $loan->getBookTitle() === $book->getTitle()) {
                $book->returnBook();
                unset($this->loans[$key]);
                echo "Libro devuelto correctamente.\n";
                return;
            }
        }
        echo "No se encontró el préstamo del libro para el usuario especificado.\n";
    }

    public function getLoans(){
        return $this->loans;
    }
}

$myBookManager = new BookManager();
$myUserManager = new UserManager();
$myLoanManager = new LoanManager();

echo "\n\nVamos a mostrar un ejemplo que si cumple SRP. En este caso es una clase que gestiona una biblioteca\n\n";

do {
    echo "\n\nMENÚ\n\n";
    echo "";
    echo "1. Añadir libro\n";
    echo "2. Añadir usuario\n";
    echo "3. Prestar libro\n";
    echo "4. Devolver libro\n";
    echo "5. Mostrar libros\n";
    echo "6. Mostrar usuarios\n";
    echo "7. Mostrar préstamos\n";
    echo "8. Salir\n";
    echo "";
    echo "Elija una opción: ";

    $option = readline();
    echo "";
    
    switch ($option) {
        case 1:
            echo "Título: ";
            $title = readline();
            echo "Autor: ";
            $author = readline();
            echo "Copias: ";
            $copies = readline();
            $myBookManager->addBook(new Books($title, $author, $copies));
            break;
        case 2:
            echo "Nombre: ";
            $name = readline();
            echo "ID: ";
            $id = readline();
            echo "Email: ";
            $email = readline();
            $myUserManager->addUser(new UsersLibrary($name, $id, $email));
            break;
        case 3:
            echo "ID del usuario: ";
            $userId = readline();
            echo "Título del libro: ";
            $bookTitle = readline();
            $user = $myUserManager->findUserById($userId);
            $book = $myBookManager->findBookByTitle($bookTitle);
            if ($user && $book) {
                $myLoanManager->loanBook($user, $book);
            } else {
                echo "Usuario o libro no encontrado.\n";
            }
            break;
        case 4:
            echo "ID del usuario: ";
            $userId = readline();
            echo "Título del libro: ";
            $bookTitle = readline();
            $user = $myUserManager->findUserById($userId);
            $book = $myBookManager->findBookByTitle($bookTitle);
            if ($user && $book) {
                $myLoanManager->returnBook($user, $book);
            } else {
                echo "Usuario o libro no encontrado.\n";
            }
            break;
        case 5:
            print_r($myBookManager->getBooks());
            break;
        case 6:
            print_r($myUserManager->getUsers());
            break;
        case 7:
            print_r($myLoanManager->getLoans());
            break;
    }
    
} while (($option != 8));
