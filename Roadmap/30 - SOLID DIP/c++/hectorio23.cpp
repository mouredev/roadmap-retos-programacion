// Autor: Héctor Adán
// GitHub: https://github.com/hectorio23
#include <iostream>
#include <memory>
#include <vector>

/*
 * EJERCICIO:
 * Explora el "Principio SOLID de Inversión de Dependencias (Dependency Inversion
 * Principle, DIP)" y crea un ejemplo simple donde se muestre su funcionamiento 
 * de forma correcta e incorrecta.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un sistema de notificaciones.
 * Requisitos:
 * 1. El sistema puede enviar Email, PUSH y SMS (implementaciones específicas).
 * 2. El sistema de notificaciones no puede depender de las implementaciones específicas.
 * Instrucciones:
 * 1. Crea la interfaz o clase abstracta.
 * 2. Desarrolla las implementaciones específicas.
 * 3. Crea el sistema de notificaciones usando el DIP.
 * 4. Desarrolla un código que compruebe que se cumple el principio.
*/

// Interfaz para el servicio de notificación
class NotificationService {
public:
    virtual void sendNotification(const std::string& message) const = 0;
    virtual ~NotificationService() = default;
};

// Implementación específica para Email
class EmailNotification : public NotificationService {
public:
    void sendNotification(const std::string& message) const override {
        std::cout << "[+] - Enviando Email: " << message << std::endl;
    }
};

// Implementación específica para PUSH
class PushNotification : public NotificationService {
public:
    void sendNotification(const std::string& message) const override {
        std::cout << "[+] - Enviando Push Notification: " << message << std::endl;
    }
};

// Implementación específica para SMS
class SMSNotification : public NotificationService {
public:
    void sendNotification(const std::string& message) const override {
        std::cout << "[+] - Enviando SMS: " << message << std::endl;
    }
};

// Sistema de Notificaciones usando DIP
class NotificationSystem {
private:
    std::vector<std::shared_ptr<NotificationService>> services;

public:
    void addService(const std::shared_ptr<NotificationService>& service) {
        services.push_back(service);
    }

    void notifyAll(const std::string& message) const {
        for (const auto& service : services) {
            service->sendNotification(message);
        }
    }
};

// Función principal para demostrar el DIP
int main() {
    // Correcto: El sistema de notificaciones no depende directamente de las implementaciones concretas
    std::shared_ptr<NotificationSystem> notificationSystem = std::make_shared<NotificationSystem>();

    notificationSystem->addService(std::make_shared<EmailNotification>());
    notificationSystem->addService(std::make_shared<PushNotification>());
    notificationSystem->addService(std::make_shared<SMSNotification>());

    notificationSystem->notifyAll("Mensaje de prueba.");

    // Incorrecto: Dependencia directa de las implementaciones concretas (violación del DIP)
    EmailNotification emailNotification;
    emailNotification.sendNotification("Mensaje directo sin sistema de notificaciones.");

    return 0;
}

