// Autor: Héctor Adán
// GitHub: https://github.com/hectorio23
#include <iostream>
#include <string>

/*
 * EJERCICIO:
 * Empleando tu lenguaje, explora la definición del tipo de dato
 * que sirva para definir enumeraciones (Enum).
 * Crea un Enum que represente los días de la semana del lunes
 * al domingo, en ese orden. Con ese enumerado, crea una operación
 * que muestre el nombre del día de la semana dependiendo del número entero
 * utilizado (del 1 al 7).
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un pequeño sistema de gestión del estado de pedidos.
 * Implementa una clase que defina un pedido con las siguientes características:
 * - El pedido tiene un identificador y un estado.
 * - El estado es un Enum con estos valores: PENDIENTE, ENVIADO, ENTREGADO y CANCELADO.
 * - Implementa las funciones que sirvan para modificar el estado:
 *   - Pedido enviado
 *   - Pedido cancelado
 *   - Pedido entregado
 *   (Establece una lógica, por ejemplo, no se puede entregar si no se ha enviado, etc...)
 * - Implementa una función para mostrar un texto descriptivo según el estado actual.
 * - Crea diferentes pedidos y muestra cómo se interactúa con ellos. 
*/


// Definición del enum para los días de la semana
// Usamos enum class para tener un mejor manejo de ámbitos
enum class DiaSemana { 
    Lunes = 1,
    Martes,
    Miercoles,
    Jueves,
    Viernes,
    Sabado,
    Domingo
};

// Función para obtener el nombre del día de la semana a partir del número
std::string obtenerNombreDiaSemana(int numeroDia) {
    switch(numeroDia) {
        case static_cast<int>(DiaSemana::Lunes):
            return "Lunes";
        case static_cast<int>(DiaSemana::Martes):
            return "Martes";
        case static_cast<int>(DiaSemana::Miercoles):
            return "Miércoles";
        case static_cast<int>(DiaSemana::Jueves):
            return "Jueves";
        case static_cast<int>(DiaSemana::Viernes):
            return "Viernes";
        case static_cast<int>(DiaSemana::Sabado):
            return "Sábado";
        case static_cast<int>(DiaSemana::Domingo):
            return "Domingo";
        default:
            return "Número de día inválido";
    }
}

// Definición del Enum para los estados de pedido
enum class EstadoPedido {
    PENDIENTE,
    ENVIADO,
    ENTREGADO,
    CANCELADO
};

// Clase Pedido
class Pedido {
private:
    int id;
    EstadoPedido estado;

public:
    // Constructor
    Pedido(int _id) : id(_id), estado(EstadoPedido::PENDIENTE) {}

    // Función para marcar el pedido como enviado
    void marcarEnviado() {
        if (estado == EstadoPedido::PENDIENTE) {
            estado = EstadoPedido::ENVIADO;
            std::cout << "El pedido con ID " << id << " ha sido enviado.\n";
        } else {
            std::cout << "El pedido con ID " << id << " no se puede enviar en su estado actual.\n";
        }
    }

    // Función para marcar el pedido como entregado
    void marcarEntregado() {
        if (estado == EstadoPedido::ENVIADO) {
            estado = EstadoPedido::ENTREGADO;
            std::cout << "El pedido con ID " << id << " ha sido entregado.\n";
        } else {
            std::cout << "El pedido con ID " << id << " no se puede entregar en su estado actual.\n";
        }
    }

    // Función para cancelar el pedido
    void cancelarPedido() {
        if (estado != EstadoPedido::CANCELADO) {
            estado = EstadoPedido::CANCELADO;
            std::cout << "El pedido con ID " << id << " ha sido cancelado.\n";
        } else {
            std::cout << "El pedido con ID " << id << " ya está cancelado.\n";
        }
    }

    // Función para mostrar el estado del pedido
    void mostrarEstado() {
        std::string estado_str;
        switch(estado) {
            case EstadoPedido::PENDIENTE:
                estado_str = "Pendiente";
                break;
            case EstadoPedido::ENVIADO:
                estado_str = "Enviado";
                break;
            case EstadoPedido::ENTREGADO:
                estado_str = "Entregado";
                break;
            case EstadoPedido::CANCELADO:
                estado_str = "Cancelado";
                break;
        }
        std::cout << "Estado del pedido con ID " << id << ": " << estado_str << "\n";
    }
};

int main() {

    std::cout << "******** EJERCICIO ********\n";
    int numeroDia;

    std::cout << "Ingrese un número de día de la semana (del 1 al 7): ";
    std::cin >> numeroDia;

    // Mostrar el nombre del día de la semana correspondiente
    std::cout << "El día de la semana es: " << obtenerNombreDiaSemana(numeroDia) << "\n";


    std::cout << "\n********** EJERCICIO EXTRA **********\n";
    // Crear pedidos
    Pedido pedido1(1);
    Pedido pedido2(2);

    // Mostrar el estado inicial de los pedidos
    pedido1.mostrarEstado();
    pedido2.mostrarEstado();

    // Interactuar con los pedidos
    pedido1.marcarEnviado();
    pedido2.marcarEnviado();
    pedido1.marcarEntregado();
    pedido2.cancelarPedido();

    // Mostrar el estado final de los pedidos
    pedido1.mostrarEstado();
    pedido2.mostrarEstado();

    return 0;
}