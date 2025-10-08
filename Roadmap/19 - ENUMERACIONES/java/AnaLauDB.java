public class AnaLauDB {

    // Enum para los días de la semana
    public enum DiaSemana {
        LUNES, MARTES, MIERCOLES, JUEVES, VIERNES, SABADO, DOMINGO
    }

    // Enum para el estado del pedido
    public enum EstadoPedido {
        PENDIENTE, ENVIADO, ENTREGADO, CANCELADO
    }

    // Clase Pedido
    public static class Pedido {
        private int id;
        private EstadoPedido estado;

        public Pedido(int id) {
            this.id = id;
            this.estado = EstadoPedido.PENDIENTE;
        }

        public void enviar() {
            if (estado == EstadoPedido.PENDIENTE) {
                estado = EstadoPedido.ENVIADO;
                System.out.println("Pedido " + id + " enviado.");
            } else {
                System.out.println("No se puede enviar el pedido " + id + " en estado " + estado);
            }
        }

        public void cancelar() {
            if (estado == EstadoPedido.PENDIENTE || estado == EstadoPedido.ENVIADO) {
                estado = EstadoPedido.CANCELADO;
                System.out.println("Pedido " + id + " cancelado.");
            } else {
                System.out.println("No se puede cancelar el pedido " + id + " en estado " + estado);
            }
        }

        public void entregar() {
            if (estado == EstadoPedido.ENVIADO) {
                estado = EstadoPedido.ENTREGADO;
                System.out.println("Pedido " + id + " entregado.");
            } else {
                System.out.println("No se puede entregar el pedido " + id + " en estado " + estado);
            }
        }

        public void mostrarEstado() {
            switch (estado) {
                case PENDIENTE:
                    System.out.println("Pedido " + id + " está pendiente de envío.");
                    break;
                case ENVIADO:
                    System.out.println("Pedido " + id + " ha sido enviado.");
                    break;
                case ENTREGADO:
                    System.out.println("Pedido " + id + " ha sido entregado.");
                    break;
                case CANCELADO:
                    System.out.println("Pedido " + id + " ha sido cancelado.");
                    break;
            }
        }
    }

    // Mostrar el nombre del día según número (1-7)
    public static void mostrarDia(int numero) {
        if (numero < 1 || numero > 7) {
            System.out.println("Número de día inválido.");
            return;
        }
        DiaSemana dia = DiaSemana.values()[numero - 1];
        System.out.println("Día " + numero + ": " + dia);
    }

    public static void main(String[] args) {
        // Ejemplo Enum días de la semana
        for (int i = 1; i <= 7; i++) {
            mostrarDia(i);
        }

        System.out.println("\n--- Gestión de pedidos ---");
        Pedido p1 = new Pedido(101);
        Pedido p2 = new Pedido(102);

        p1.mostrarEstado();
        p1.enviar();
        p1.entregar();
        p1.mostrarEstado();

        p2.mostrarEstado();
        p2.cancelar();
        p2.entregar(); // No debe permitir entregar
        p2.mostrarEstado();
    }
}
