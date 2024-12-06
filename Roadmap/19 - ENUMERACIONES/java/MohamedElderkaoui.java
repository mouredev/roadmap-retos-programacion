// Clase principal
public class MohamedElderkaoui {
    public static void main(String[] args) {
        // Parte 1: Enum de días de la semana
        System.out.println("Días de la semana:");
        for (int i = 1; i <= 7; i++) {
            System.out.println("Día " + i + ": " + DiaSemana.obtenerDiaPorNumero(i));
        }

        // Parte 2: Sistema de gestión de pedidos
        Pedido pedido1 = new Pedido(1);
        Pedido pedido2 = new Pedido(2);

        // Interacción con los pedidos
        System.out.println("\nGestión de pedidos:");
        System.out.println(pedido1);
        pedido1.enviarPedido();
        System.out.println(pedido1);
        pedido1.entregarPedido();
        System.out.println(pedido1);

        System.out.println("\nEstado inicial del segundo pedido:");
        System.out.println(pedido2);
        pedido2.cancelarPedido();
        System.out.println(pedido2);
    }
}

// Enum para los días de la semana
enum DiaSemana {
    LUNES, MARTES, MIERCOLES, JUEVES, VIERNES, SABADO, DOMINGO;

    public static DiaSemana obtenerDiaPorNumero(int numero) {
        if (numero < 1 || numero > 7) {
            throw new IllegalArgumentException("El número debe estar entre 1 y 7.");
        }
        return DiaSemana.values()[numero - 1];
    }
}

// Enum para los estados de un pedido
enum EstadoPedido {
    PENDIENTE, ENVIADO, ENTREGADO, CANCELADO
}

// Clase que representa un pedido
class Pedido {
    private final int id;
    private EstadoPedido estado;

    public Pedido(int id) {
        this.id = id;
        this.estado = EstadoPedido.PENDIENTE;
    }

    public void enviarPedido() {
        if (estado == EstadoPedido.PENDIENTE) {
            estado = EstadoPedido.ENVIADO;
            System.out.println("El pedido #" + id + " ha sido enviado.");
        } else {
            System.out.println("No se puede enviar el pedido #" + id + " en su estado actual: " + estado);
        }
    }

    public void entregarPedido() {
        if (estado == EstadoPedido.ENVIADO) {
            estado = EstadoPedido.ENTREGADO;
            System.out.println("El pedido #" + id + " ha sido entregado.");
        } else {
            System.out.println("No se puede entregar el pedido #" + id + " en su estado actual: " + estado);
        }
    }

    public void cancelarPedido() {
        if (estado == EstadoPedido.PENDIENTE || estado == EstadoPedido.ENVIADO) {
            estado = EstadoPedido.CANCELADO;
            System.out.println("El pedido #" + id + " ha sido cancelado.");
        } else {
            System.out.println("No se puede cancelar el pedido #" + id + " en su estado actual: " + estado);
        }
    }

    @Override
    public String toString() {
        String descripcionEstado;
        switch (estado) {
            case PENDIENTE:
                descripcionEstado = "Pendiente de envío.";
                break;
            case ENVIADO:
                descripcionEstado = "Enviado, en espera de entrega.";
                break;
            case ENTREGADO:
                descripcionEstado = "Entregado al cliente.";
                break;
            case CANCELADO:
                descripcionEstado = "Pedido cancelado.";
                break;
            default:
                descripcionEstado = "Estado desconocido.";
        }
        return "Pedido #" + id + " - Estado: " + descripcionEstado;
    }
}
