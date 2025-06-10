/*
 * TEORÍA SOBRE ENUMERACIONES EN JAVA
 * 
 * Las enumeraciones en Java son un tipo especial de clase que representa un grupo
 * de constantes (variables inmutables). Se definen usando la palabra clave 'enum'.
 * 
 * Características principales:
 * 1. Son implícitamente final y estáticas
 * 2. Pueden tener constructores, métodos y campos
 * 3. Implementan implícitamente java.lang.Comparable y java.io.Serializable
 * 4. Se utilizan comúnmente para representar un conjunto fijo de opciones
 */

public class eulogioep {
    // Enumeración para los días de la semana
    enum DiaSemana {
        LUNES, MARTES, MIERCOLES, JUEVES, VIERNES, SABADO, DOMINGO
    }

    // Enumeración para los estados de un pedido
    enum EstadoPedido {
        PENDIENTE, ENVIADO, ENTREGADO, CANCELADO
    }

    // Clase para gestionar pedidos
    static class Pedido {
        private final int id;
        private EstadoPedido estado;

        // Constructor
        public Pedido(int id) {
            this.id = id;
            this.estado = EstadoPedido.PENDIENTE;
        }

        // Método para enviar el pedido
        public boolean enviarPedido() {
            if (estado == EstadoPedido.PENDIENTE) {
                estado = EstadoPedido.ENVIADO;
                return true;
            }
            return false;
        }

        // Método para cancelar el pedido
        public boolean cancelarPedido() {
            if (estado == EstadoPedido.PENDIENTE || estado == EstadoPedido.ENVIADO) {
                estado = EstadoPedido.CANCELADO;
                return true;
            }
            return false;
        }

        // Método para entregar el pedido
        public boolean entregarPedido() {
            if (estado == EstadoPedido.ENVIADO) {
                estado = EstadoPedido.ENTREGADO;
                return true;
            }
            return false;
        }

        // Método para obtener descripción del estado
        public String obtenerDescripcionEstado() {
            return switch (estado) {
                case PENDIENTE -> "El pedido " + id + " está pendiente de envío.";
                case ENVIADO -> "El pedido " + id + " ha sido enviado y está en camino.";
                case ENTREGADO -> "El pedido " + id + " ha sido entregado con éxito.";
                case CANCELADO -> "El pedido " + id + " ha sido cancelado.";
            };
        }

        // Getter para el estado
        public EstadoPedido getEstado() {
            return estado;
        }
    }

    // Método para obtener el día de la semana según un número
    public static String obtenerDiaSemana(int numero) {
        if (numero < 1 || numero > 7) {
            return "Número inválido. Debe estar entre 1 y 7.";
        }
        return DiaSemana.values()[numero - 1].toString();
    }

    public static void main(String[] args) {
        // Prueba de días de la semana
        System.out.println("=== PRUEBA DE DÍAS DE LA SEMANA ===");
        for (int i = 1; i <= 7; i++) {
            System.out.println("Día " + i + ": " + obtenerDiaSemana(i));
        }

        // Prueba del sistema de gestión de pedidos
        System.out.println("\n=== PRUEBA DE GESTIÓN DE PEDIDOS ===");

        Pedido pedido1 = new Pedido(1);
        Pedido pedido2 = new Pedido(2);

        // Mostrar estado inicial
        System.out.println(pedido1.obtenerDescripcionEstado());

        // Enviar pedido1
        pedido1.enviarPedido();
        System.out.println(pedido1.obtenerDescripcionEstado());

        // Intentar entregar pedido2 (debería fallar)
        if (!pedido2.entregarPedido()) {
            System.out.println("No se puede entregar el pedido 2 porque no ha sido enviado.");
        }

        // Entregar pedido1
        pedido1.entregarPedido();
        System.out.println(pedido1.obtenerDescripcionEstado());

        // Cancelar pedido2
        pedido2.cancelarPedido();
        System.out.println(pedido2.obtenerDescripcionEstado());
    }
}