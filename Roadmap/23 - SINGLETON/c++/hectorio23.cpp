// Autor: Héctor Adán
// GitHub: https://github.com/hectorio23

#include <iostream>
#include <string>
#include <optional>

/////////////////////////////////////////////////
/////////////////// EJERCICIO 1 /////////////////
/////////////////////////////////////////////////

class NotDuplicity {
public:
    static NotDuplicity& getInstance() {
        static NotDuplicity instance;
        return instance;
    }

    // Eliminamos los métodos de copia y asignación para evitar múltiples instancias
    NotDuplicity(NotDuplicity const&) = delete;
    void operator=(NotDuplicity const&) = delete;

private:
    NotDuplicity() {}  // Constructor privado
};

/////////////////////////////////////////////////
///////////////// EJERCICIO EXTRA ///////////////
/////////////////////////////////////////////////

class UserSession {
public:
    struct UserData {
        int id;
        std::string username;
        std::string name;
        std::string email;
    };

    static UserSession& getInstance() {
        static UserSession instance;
        return instance;
    }

    // Eliminamos los métodos de copia y asignación para evitar múltiples instancias
    UserSession(UserSession const&) = delete;
    void operator=(UserSession const&) = delete;

    void setUser(int userId, const std::string& username, const std::string& name, const std::string& email) {
        userData = UserData{userId, username, name, email};
    }

    std::optional<UserData> getUser() const {
        return userData;
    }

    void clearUser() {
        userData.reset();
    }

private:
    std::optional<UserData> userData;

    UserSession() {}  // Constructor privado
};

int main() {
    // Ejercicio 1: Singleton Genérico
    NotDuplicity& obj1 = NotDuplicity::getInstance();
    NotDuplicity& obj2 = NotDuplicity::getInstance();

    std::cout << "ID Objeto 1 => " << &obj1 << std::endl;
    std::cout << "ID Objeto 2 => " << &obj2 << std::endl;
    std::cout << "¿Los objetos 1 y 2 son iguales? " << (&obj1 == &obj2) << std::endl;

    std::cout << "\n********************************\n";

    // Ejercicio Extra: Sesión de Usuario
    UserSession& session = UserSession::getInstance();
    session.setUser(1, "hectorio23", "Adán", "adan_example@example.com");

    auto user = session.getUser();
    if (user) {
        std::cout << "Usuario: " << user->username << ", Nombre: " << user->name << ", Email: " << user->email << std::endl;
    }

    session.clearUser();

    user = session.getUser();
    if (!user) {
        std::cout << "Datos del usuario borrados" << std::endl;
    }

    // Verificación de singleton:
    UserSession& anotherSession = UserSession::getInstance();
    std::cout << "¿Las sesiones son iguales? " << (&session == &anotherSession) << std::endl;

    return 0;
}