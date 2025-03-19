<?php
/**
 * PRINCIPIO DE RESPONSABILIDAD ÚNICA (SRP)
 * 
 * El Principio de Responsabilidad Única establece que:
 * "Una clase debe tener una única razón para cambiar"
 * 
 * Este principio nos ayuda a:
 * - Crear código más mantenible
 * - Facilitar las pruebas unitarias
 * - Reducir el acoplamiento
 * - Mejorar la cohesión del código
 * - Facilitar la reutilización
 */

// ========== IMPLEMENTACIÓN INCORRECTA (Violando SRP) ==========

/**
 * Esta implementación viola el SRP porque la clase Library maneja múltiples responsabilidades:
 * 1. Gestión de libros
 * 2. Gestión de usuarios
 * 3. Gestión de préstamos
 */
class Library {
    private array $books = [];
    private array $users = [];
    private array $loans = [];

    // Gestión de libros
    public function addBook(string $title, string $author, int $copies): void {
        $book = new Book($title, $author, $copies);
        $this->books[] = $book;
    }

    public function removeBook(string $bookId): void {
        $this->books = array_filter(
            $this->books,
            fn($book) => $book->getId() !== $bookId
        );
    }

    // Gestión de usuarios
    public function registerUser(string $name, string $id, string $email): void {
        $user = new User($name, $id, $email);
        $this->users[] = $user;
    }

    public function removeUser(string $userId): void {
        $this->users = array_filter(
            $this->users,
            fn($user) => $user->getId() !== $userId
        );
    }

    // Gestión de préstamos
    public function loanBook(string $userId, string $bookId): void {
        $book = $this->findBook($bookId);
        $user = $this->findUser($userId);

        if (!$book || !$user) {
            throw new Exception("Libro o usuario no encontrado");
        }

        if ($book->getAvailableCopies() <= 0) {
            throw new Exception("No hay copias disponibles");
        }

        $book->decrementCopies();
        $this->loans[] = new Loan($userId, $bookId, new DateTime());
    }

    public function returnBook(string $userId, string $bookId): void {
        $loan = $this->findLoan($userId, $bookId);
        if (!$loan) {
            throw new Exception("Préstamo no encontrado");
        }

        $book = $this->findBook($bookId);
        if ($book) {
            $book->incrementCopies();
        }

        $this->removeLoan($userId, $bookId);
    }

    private function findBook(string $bookId): ?Book {
        foreach ($this->books as $book) {
            if ($book->getId() === $bookId) {
                return $book;
            }
        }
        return null;
    }

    private function findUser(string $userId): ?User {
        foreach ($this->users as $user) {
            if ($user->getId() === $userId) {
                return $user;
            }
        }
        return null;
    }

    private function findLoan(string $userId, string $bookId): ?Loan {
        foreach ($this->loans as $loan) {
            if ($loan->getUserId() === $userId && $loan->getBookId() === $bookId) {
                return $loan;
            }
        }
        return null;
    }

    private function removeLoan(string $userId, string $bookId): void {
        $this->loans = array_filter(
            $this->loans,
            fn($loan) => !($loan->getUserId() === $userId && $loan->getBookId() === $bookId)
        );
    }
}

// ========== IMPLEMENTACIÓN CORRECTA (Siguiendo SRP) ==========

/**
 * BookManager: Responsable únicamente de la gestión de libros
 */
class BookManager {
    private array $books = [];

    public function addBook(string $title, string $author, int $copies): void {
        $book = new Book($title, $author, $copies);
        $this->books[] = $book;
    }

    public function removeBook(string $bookId): void {
        $this->books = array_filter(
            $this->books,
            fn($book) => $book->getId() !== $bookId
        );
    }

    public function findBook(string $bookId): ?Book {
        foreach ($this->books as $book) {
            if ($book->getId() === $bookId) {
                return $book;
            }
        }
        return null;
    }

    public function updateBookCopies(string $bookId, int $change): void {
        $book = $this->findBook($bookId);
        if ($book) {
            if ($change > 0) {
                $book->incrementCopies();
            } else {
                $book->decrementCopies();
            }
        }
    }
}

/**
 * UserManager: Responsable únicamente de la gestión de usuarios
 */
class UserManager {
    private array $users = [];

    public function registerUser(string $name, string $id, string $email): void {
        $user = new User($name, $id, $email);
        $this->users[] = $user;
    }

    public function removeUser(string $userId): void {
        $this->users = array_filter(
            $this->users,
            fn($user) => $user->getId() !== $userId
        );
    }

    public function findUser(string $userId): ?User {
        foreach ($this->users as $user) {
            if ($user->getId() === $userId) {
                return $user;
            }
        }
        return null;
    }
}

/**
 * LoanManager: Responsable únicamente de la gestión de préstamos
 */
class LoanManager {
    private array $loans = [];

    public function __construct(
        private BookManager $bookManager,
        private UserManager $userManager
    ) {}

    public function loanBook(string $userId, string $bookId): void {
        $book = $this->bookManager->findBook($bookId);
        $user = $this->userManager->findUser($userId);

        if (!$book || !$user) {
            throw new Exception("Libro o usuario no encontrado");
        }

        if ($book->getAvailableCopies() <= 0) {
            throw new Exception("No hay copias disponibles");
        }

        $this->bookManager->updateBookCopies($bookId, -1);
        $this->loans[] = new Loan($userId, $bookId, new DateTime());
    }

    public function returnBook(string $userId, string $bookId): void {
        $loan = $this->findLoan($userId, $bookId);
        if (!$loan) {
            throw new Exception("Préstamo no encontrado");
        }

        $this->bookManager->updateBookCopies($bookId, 1);
        $this->removeLoan($userId, $bookId);
    }

    private function findLoan(string $userId, string $bookId): ?Loan {
        foreach ($this->loans as $loan) {
            if ($loan->getUserId() === $userId && $loan->getBookId() === $bookId) {
                return $loan;
            }
        }
        return null;
    }

    private function removeLoan(string $userId, string $bookId): void {
        $this->loans = array_filter(
            $this->loans,
            fn($loan) => !($loan->getUserId() === $userId && $loan->getBookId() === $bookId)
        );
    }
}

// Clases de modelo
class Book {
    private string $id;

    public function __construct(
        private string $title,
        private string $author,
        private int $availableCopies
    ) {
        $this->id = uniqid();
    }

    public function getId(): string {
        return $this->id;
    }

    public function getTitle(): string {
        return $this->title;
    }

    public function getAuthor(): string {
        return $this->author;
    }

    public function getAvailableCopies(): int {
        return $this->availableCopies;
    }

    public function incrementCopies(): void {
        $this->availableCopies++;
    }

    public function decrementCopies(): void {
        $this->availableCopies--;
    }
}

class User {
    public function __construct(
        private string $name,
        private string $id,
        private string $email
    ) {}

    public function getId(): string {
        return $this->id;
    }

    public function getName(): string {
        return $this->name;
    }

    public function getEmail(): string {
        return $this->email;
    }
}

class Loan {
    public function __construct(
        private string $userId,
        private string $bookId,
        private DateTime $loanDate
    ) {}

    public function getUserId(): string {
        return $this->userId;
    }

    public function getBookId(): string {
        return $this->bookId;
    }

    public function getLoanDate(): DateTime {
        return $this->loanDate;
    }
}

// Ejemplo de uso del sistema refactorizado
$bookManager = new BookManager();
$userManager = new UserManager();
$loanManager = new LoanManager($bookManager, $userManager);

// Registrar un libro
$bookManager->addBook("El Quijote", "Miguel de Cervantes", 5);

// Registrar un usuario
$userManager->registerUser("Juan Pérez", "USER001", "juan@email.com");

// Realizar un préstamo
$loanManager->loanBook("USER001", "BOOK001");
?>