/* ╔══════════════════════════════════════╗
   ║ Autor:  Amador Q                     ║
   ║ Web  : https://amsoft.dev            ║
   ║ 2024                                 ║
   ╚══════════════════════════════════════╝
*/

enum DiaSemana {
    LUNES("Lunes", 1),
    MARTES("Martes", 2),
    MIERCOLES("Miércoles", 3),
    JUEVES("Jueves", 4),
    VIERNES("Viernes", 5),
    SABADO("Sabado", 6),
    DOMINGO("Domingo", 7);

    private String nombreDia;
    private int numeroDia;

    private DiaSemana(String nombreDia, int numeroDia) {
        this.nombreDia = nombreDia;
        this.numeroDia = numeroDia;
    }

    public String getNombreDia() {
        return nombreDia;
    }

    public int getNumeroDia() {
        return numeroDia;
    }

}

enum Estado {
    PENDIENTE, ENVIADO, ENTREGADO, CANCELADO
}

public class Main {
    public static void main(String[] args) {
        System.out.println(DiaSemana.DOMINGO);

        // EXTRA
        Pedido pedido1 = new Pedido("0001", Estado.PENDIENTE);
        pedido1.enviar();
        pedido1.enviar();
        pedido1.entregar();
        pedido1.mostrarEstado();

        Pedido pedido2 = new Pedido("0002", Estado.PENDIENTE);
        pedido2.cancelar();
        pedido2.mostrarEstado();
        pedido2.enviar();
    }
}

class Pedido {
    private String id;
    private Estado estado;

    public Pedido(String id, Estado estado) {
        this.id = id;
        this.estado = estado;
    }

    public void enviar() {
        if (estado == Estado.PENDIENTE) {
            estado = Estado.ENVIADO;
            System.out.println("El pedido # " + id + " ha sido enviado.");
        } else {
            System.out.println("El pedido # " + id + " no se puede enviar porque su estado actual es: " + estado);
        }
    }

    public void cancelar() {
        if (estado == Estado.PENDIENTE) { // Solo se puede cancelar si no ha sido enviada
            estado = Estado.CANCELADO;
            System.out.println("El pedido # " + id + " ha sido cancelado.");
        } else {
            System.out.println("El pedido # " + id + " no se puede cancelar porque su estado actual es: " + estado);
        }
    }

    public void entregar() {
        if (estado == Estado.ENVIADO) {
            estado = Estado.ENTREGADO;
            System.out.println("El pedido # " + id + " ha sido entregado.");
        } else {
            System.out.println("El pedido # " + id + " no se puede entregar porque su estado actual es: " + estado);
        }
    }

    public void mostrarEstado() {
        System.out.println("Estado del pedido # " + id + ": " + estado);
    }

}
