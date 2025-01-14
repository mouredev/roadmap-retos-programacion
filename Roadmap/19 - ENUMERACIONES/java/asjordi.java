/**
 * Un ENUM es un tipo de dato que se utiliza para definir un conjunto fijo de constantes.
 * Es útil cuando se tiene un conjunto de valores que no cambian durante toda la ejecución del programa.
 * Por ejemplo, los días de la semana, los meses del año, los colores, etc.
 */
public class Main {
    public static void main(String[] args) {
        System.out.println(Day.getDayName(11)); // -> MONDAY
        manejarPedidos();
    }

    /**
     * Crea un Enum que represente los días de la semana del lunes
     * al domingo, en ese orden. Con ese Enum, crea una operación
     * que muestre el nombre del día de la semana dependiendo del número entero
     * utilizado (del 1 al 7).
     */
    public enum Day{
        MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY;

        public static String getDayName(int n){
            return switch (n) {
                case 1 -> MONDAY.name();
                case 2 -> TUESDAY.name();
                case 3 -> WEDNESDAY.name();
                case 4 -> THURSDAY.name();
                case 5 -> FRIDAY.name();
                case 6 -> SATURDAY.name();
                case 7 -> SUNDAY.name();
                default -> throw new IllegalArgumentException("Invalid day number: " + n);
            };
        }
    }

    /**
     * DIFICULTAD EXTRA (opcional):
     * Crea un pequeño sistema de gestión del estado de pedidos.
     * Implementa una clase que defina un pedido con las siguientes características:
     * - El pedido tiene un identificador y un estado.
     * - El estado es un Enum con estos valores: PENDIENTE, ENVIADO, ENTREGADO y CANCELADO.
     * - Implementa las funciones que sirvan para modificar el estado:
     *  - Pedido enviado
     *  - Pedido cancelado
     *  - Pedido entregado
     * (Establece una lógica, por ejemplo, no se puede entregar si no se ha enviado, etc...)
     * - Implementa una función para mostrar un texto descriptivo según el estado actual.
     * - Crea diferentes pedidos y muestra cómo se interactúa con ellos.
     */

    static class Pedido {
        private Integer id;
        private Estado estado;

        public Pedido(Integer id, Estado estado) {
            this.id = id;
            this.estado = estado;
        }

        public void enviar() {
            if (estado == Estado.PENDIENTE) {
                estado = Estado.ENVIADO;
            } else {
                throw new IllegalStateException("No se puede enviar un pedido que no está pendiente.");
            }
        }

        public void entregar() {
            if (estado == Estado.ENVIADO) {
                estado = Estado.ENTREGADO;
            } else {
                throw new IllegalStateException("No se puede entregar un pedido que no está enviado.");
            }
        }

        public void cancelar() {
            if (estado == Estado.PENDIENTE) {
                estado = Estado.CANCELADO;
            } else {
                throw new IllegalStateException("No se puede cancelar un pedido que no está pendiente.");
            }
        }

        public String getEstado() {
            return switch (estado) {
                case PENDIENTE -> "El pedido está pendiente.";
                case ENVIADO -> "El pedido está enviado.";
                case ENTREGADO -> "El pedido está entregado.";
                case CANCELADO -> "El pedido está cancelado.";
            };
        }
    }

    public enum Estado {
        PENDIENTE, ENVIADO, ENTREGADO, CANCELADO;
    }

    public static void manejarPedidos() {
        Pedido pedido1 = new Pedido(1, Estado.PENDIENTE);
        System.out.println(pedido1.getEstado()); // -> El pedido está pendiente.
        pedido1.enviar();
        System.out.println(pedido1.getEstado()); // -> El pedido está enviado.
        pedido1.entregar();
        System.out.println(pedido1.getEstado()); // -> El pedido está entregado.

        Pedido pedido2 = new Pedido(2, Estado.PENDIENTE);
        System.out.println(pedido2.getEstado()); // -> El pedido está pendiente.
        pedido2.cancelar();
        System.out.println(pedido2.getEstado()); // -> El pedido está cancelado.
    }
}
