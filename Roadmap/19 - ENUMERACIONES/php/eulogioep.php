<?php
// Resumen sobre Enumeraciones
// Las enumeraciones (Enums) en PHP 8.1 permiten definir un tipo de dato con un conjunto finito de valores posibles. 
// Son útiles para representar datos categóricos que tienen un número limitado de valores, como los días de la semana o el estado de un pedido.

enum DiasSemana: int
{
    case Lunes = 1;
    case Martes = 2;
    case Miercoles = 3;
    case Jueves = 4;
    case Viernes = 5;
    case Sabado = 6;
    case Domingo = 7;
}

// Función para obtener el nombre del día a partir de un número entero
function obtenerNombreDia(int $numeroDia): string
{
    return DiasSemana::from($numeroDia)->name;
}

// Ejemplo de uso de la función obtenerNombreDia
echo obtenerNombreDia(1); // Salida: Lunes
echo "\n";
echo obtenerNombreDia(7); // Salida: Domingo

// Dificultad Extra: Sistema de gestión del estado de pedidos
enum EstadoPedido: string
{
    case Pendiente = 'Pendiente';
    case Enviado = 'Enviado';
    case Entregado = 'Entregado';
    case Cancelado = 'Cancelado';
}

class Pedido
{
    private int $id;
    private EstadoPedido $estado;

    public function __construct(int $id, EstadoPedido $estado = EstadoPedido::Pendiente)
    {
        $this->id = $id;
        $this->estado = $estado;
    }

    public function enviar(): void
    {
        if ($this->estado === EstadoPedido::Pendiente) {
            $this->estado = EstadoPedido::Enviado;
        } else {
            echo "El pedido no se puede enviar.\n";
        }
    }

    public function entregar(): void
    {
        if ($this->estado === EstadoPedido::Enviado) {
            $this->estado = EstadoPedido::Entregado;
        } else {
            echo "El pedido no se puede entregar.\n";
        }
    }

    public function cancelar(): void
    {
        if ($this->estado !== EstadoPedido::Entregado) {
            $this->estado = EstadoPedido::Cancelado;
        } else {
            echo "El pedido no se puede cancelar.\n";
        }
    }

    public function obtenerDescripcionEstado(): string
    {
        return "El estado actual del pedido {$this->id} es {$this->estado->value}.\n";
    }
}

// Ejemplo de interacción con diferentes pedidos
$pedido1 = new Pedido(1);
$pedido2 = new Pedido(2);

$pedido1->enviar();
echo $pedido1->obtenerDescripcionEstado(); // Salida: El estado actual del pedido 1 es Enviado.

$pedido1->entregar();
echo $pedido1->obtenerDescripcionEstado(); // Salida: El estado actual del pedido 1 es Entregado.

$pedido2->cancelar();
echo $pedido2->obtenerDescripcionEstado(); // Salida: El estado actual del pedido 2 es Cancelado.

$pedido3 = new Pedido(3);
$pedido3->enviar();
$pedido3->cancelar(); // Esto no debería ser posible, y se verá reflejado en el mensaje.

echo $pedido3->obtenerDescripcionEstado(); // Salida: El estado actual del pedido 3 es Enviado.
