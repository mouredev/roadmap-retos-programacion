// Autor: Héctor Adán 
// GitHub: https://github.com/hectorio23

#include <iostream>
#include <string>
#include <vector>
#include <cstdlib>

/*
 * EJERCICIO:
 * Explora el "Principio SOLID de Responsabilidad Única (Single Responsibility
 * Principle, SRP)" y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
 *
 * DIFICULTAD EXTRA:
 * Desarrolla un sistema de gestión para una biblioteca. El sistema necesita
 * manejar diferentes aspectos como el registro de libros, la gestión de usuarios
 * y el procesamiento de préstamos de libros.
 * Requisitos:
 * 1. Registrar libros: El sistema debe permitir agregar nuevos libros con 
 * información básica como título, autor y número de copias disponibles.
 * 2. Registrar usuarios: El sistema debe permitir agregar nuevos usuarios con
 * información básica como nombre, número de identificación y correo electrónico.
 * 3. Procesar préstamos de libros: El sistema debe permitir a los usuarios
 * tomar prestados y devolver libros.
*/

class Book {
public:
    std::string title;
    std::string author;
    int copies;

    Book(const std::string& _title, const std::string& _author, int _copies) : title(_title), author(_author), copies(_copies) {}
};


class BookManager {
private:
    std::vector<Book> books;

public:

    void addBook() {
        std::system("clear");
        std::string title, author;
        int copies;
        std::cout << "Ingrese el título del libro: ";
        std::cin.ignore();
        std::getline(std::cin, title);
        std::cout << "Ingrese el autor del libro: ";
        std::getline(std::cin, author);
        std::cout << "Ingrese el número de copias: ";
        std::cin >> copies;
        books.push_back(Book(title, author, copies));
        std::cout << "Libro agregado exitosamente.\n";
    }

    void listBooks() const {
        std::system("clear");
        if (books.empty()) {
            std::cout << "No hay libros disponibles.\n";
            return;
        }
        for (const auto& book : books) {
            std::cout << "Título: " << book.title << ", Autor: " << book.author << ", Copias: " << book.copies << std::endl;
        }
    }
};


class User {
public:
    std::string name;
    long id;
    std::string email;

    User(const std::string& n, long i, const std::string& e) : name(n), id(i), email(e) {}
};


class UserManager {
private:
    std::vector<User> users;

public:
    void addUser() {
        std::system("clear");
        std::string name, email;
        long id;
        std::cout << "Ingrese el nombre del usuario: ";
        std::cin.ignore();
        std::getline(std::cin, name);
        std::cout << "Ingrese el ID del usuario: ";
        std::cin >> id;
        std::cout << "Ingrese el correo electrónico del usuario: ";
        std::cin.ignore();
        std::getline(std::cin, email);
        users.push_back(User(name, id, email));
        std::cout << "Usuario agregado exitosamente.\n";
    }

    void listUsers() const {
        std::system("clear");
        if (users.empty()) {
            std::cout << "No hay usuarios registrados.\n";
            return;
        }
        for (const auto& user : users) {
            std::cout << "Nombre: " << user.name << ", ID: " << user.id << ", Correo: " << user.email << std::endl;
        }
    }
};


class LoanManager {
public:
    void lendBook(UserManager& userManager, BookManager& bookManager) {
        std::system("clear");
        std::string bookTitle;
        long userId;
        std::cout << "Ingrese el ID del usuario: ";
        std::cin >> userId;
        std::cout << "Ingrese el título del libro a prestar: ";
        std::cin.ignore();
        std::getline(std::cin, bookTitle);

        // Lógica de préstamo
        std::cout << "Libro '" << bookTitle << "' prestado al usuario ID " << userId << ".\n";
    }

    void returnBook(UserManager& userManager, BookManager& bookManager) {
        std::system("clear");
        std::string bookTitle;
        long userId;
        std::cout << "Ingrese el ID del usuario: ";
        std::cin >> userId;
        std::cout << "Ingrese el título del libro a devolver: ";
        std::cin.ignore();
        std::getline(std::cin, bookTitle);

        // Lógica de devolución
        std::cout << "Libro '" << bookTitle << "' devuelto por el usuario ID " << userId << ".\n";
    }
};

void displayMenu() {
    // std::system("clear");
    std::cout << "******** Menú de la Biblioteca ********\n";
    std::cout << "[1] - Agregar un libro\n";
    std::cout << "[2] - Listar libros\n";
    std::cout << "[3] - Agregar un usuario\n";
    std::cout << "[4] - Listar usuarios\n";
    std::cout << "[5] - Prestar un libro\n";
    std::cout << "[6] - Devolver un libro\n";
    std::cout << "[7] - Salir\n";
    std::cout << "Seleccione una opción: ";
}


int main() {
    BookManager bookManager;
    UserManager userManager;
    LoanManager loanManager;
    int option;

    do {
        displayMenu();
        std::cin >> option;

        switch (option) {
            case 1:
                bookManager.addBook();
                break;
            case 2:
                bookManager.listBooks();
                break;
            case 3:
                userManager.addUser();
                break;
            case 4:
                userManager.listUsers();
                break;
            case 5:
                loanManager.lendBook(userManager, bookManager);
                break;
            case 6:
                loanManager.returnBook(userManager, bookManager);
                break;
            case 7:
                std::cout << "Saliendo del sistema...\n";
                break;
            default:
                std::cout << "Opción no válida. Intente de nuevo.\n";
        }

    } while (option != 7);

    return EXIT_SUCCESS;
}
