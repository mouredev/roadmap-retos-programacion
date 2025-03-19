import java.util.Scanner;

public class ArmentaAngel {

    public static void main(String[] args) {
        Juego juego = new Juego();
        juego.jugar();
    }
}

enum TipoCelda {
    VACIO("Vacio", " "),
    OBSTACULO("Obstaculo", "#"),
    MICKEY("Mickey", "M"),
    SALIDA("Salida", "S");

    final String tipo;
    final String simbolo;

    TipoCelda(String contenido, String simbolo) {
        this.tipo = contenido;
        this.simbolo = simbolo;
    }
}

class Celda {
    TipoCelda tipo;
    boolean oculta;

    public Celda(TipoCelda tipo, boolean oculta) {
        this.tipo = tipo;
        this.oculta = oculta;
    }
}

class Posicion {
    int x;
    int y;

    public Posicion(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

class Juego {
    private static final Celda[][] laberinto = new Celda[6][6];
    private int numMovimientos = 0;
    private final Posicion posMickey = new Posicion(0, 0);
    private boolean salidaEncontrada = false;

    public Juego() {
        creaLaberinto();
    }

    private void creaLaberinto() {
        // 0 [#M #S#]
        laberinto[0][0] = new Celda(TipoCelda.OBSTACULO, true);
        laberinto[0][1] = new Celda(TipoCelda.MICKEY, false);
        posMickey.x = 0;
        posMickey.y = 1;
        laberinto[0][2] = new Celda(TipoCelda.VACIO, false);
        laberinto[0][3] = new Celda(TipoCelda.OBSTACULO, true);
        laberinto[0][4] = new Celda(TipoCelda.SALIDA, false);
        laberinto[0][5] = new Celda(TipoCelda.OBSTACULO, true);

        // 1 [  #   ]
        laberinto[1][0] = new Celda(TipoCelda.VACIO, false);
        laberinto[1][1] = new Celda(TipoCelda.VACIO, false);
        laberinto[1][2] = new Celda(TipoCelda.OBSTACULO, true);
        laberinto[1][3] = new Celda(TipoCelda.VACIO, false);
        laberinto[1][4] = new Celda(TipoCelda.VACIO, false);
        laberinto[1][5] = new Celda(TipoCelda.VACIO, false);

        // 2 [# ##  ]
        laberinto[2][0] = new Celda(TipoCelda.OBSTACULO, true);
        laberinto[2][1] = new Celda(TipoCelda.VACIO, false);
        laberinto[2][2] = new Celda(TipoCelda.VACIO, false);
        laberinto[2][3] = new Celda(TipoCelda.OBSTACULO, true);
        laberinto[2][4] = new Celda(TipoCelda.OBSTACULO, true);
        laberinto[2][5] = new Celda(TipoCelda.VACIO, false);

        // 3 [#  #  ]
        laberinto[3][0] = new Celda(TipoCelda.OBSTACULO, true);
        laberinto[3][1] = new Celda(TipoCelda.VACIO, false);
        laberinto[3][2] = new Celda(TipoCelda.VACIO, false);
        laberinto[3][3] = new Celda(TipoCelda.OBSTACULO, true);
        laberinto[3][4] = new Celda(TipoCelda.VACIO, false);
        laberinto[3][5] = new Celda(TipoCelda.VACIO, false);

        // 4 [ #   #]
        laberinto[4][0] = new Celda(TipoCelda.VACIO, false);
        laberinto[4][1] = new Celda(TipoCelda.OBSTACULO, true);
        laberinto[4][2] = new Celda(TipoCelda.VACIO, false);
        laberinto[4][3] = new Celda(TipoCelda.VACIO, false);
        laberinto[4][4] = new Celda(TipoCelda.VACIO, false);
        laberinto[4][5] = new Celda(TipoCelda.OBSTACULO, true);

        // 5 [      ]
        laberinto[5][0] = new Celda(TipoCelda.VACIO, false);
        laberinto[5][1] = new Celda(TipoCelda.VACIO, false);
        laberinto[5][2] = new Celda(TipoCelda.VACIO, false);
        laberinto[5][3] = new Celda(TipoCelda.VACIO, false);
        laberinto[5][4] = new Celda(TipoCelda.VACIO, false);
        laberinto[5][5] = new Celda(TipoCelda.VACIO, false);
    }

    public void jugar() {
        bienvenida();

        Scanner scanner = new Scanner(System.in);
        do {
            System.out.print("Introduce tu movimiento: ");
            ejecutaMovimiento(scanner.nextLine());
        } while (!salidaEncontrada);
    }

    private void ejecutaMovimiento(String movimiento) {
        boolean movimientoValido = true;
        switch (movimiento.toLowerCase()) {
            case "q":
                arriba();
                break;
            case "a":
                abajo();
                break;
            case "o":
                izquierda();
                break;
            case "p":
                derecha();
                break;
            default:
                movimientoNoValido(movimiento);
                movimientoValido = false;
        }
        if (movimientoValido) {
            numMovimientos++;
        }
    }

    private void arriba() {
        Posicion posicionDeseada = new Posicion(posMickey.x - 1, posMickey.y);
        evaluaMovimiento(posicionDeseada, "arriba");
    }

    private void abajo() {
        Posicion posicionDeseada = new Posicion(posMickey.x + 1, posMickey.y);
        evaluaMovimiento(posicionDeseada, "abajo");
    }

    private void izquierda() {
        Posicion posicionDeseada = new Posicion(posMickey.x, posMickey.y - 1);
        evaluaMovimiento(posicionDeseada, "izquierda");
    }

    private void derecha() {
        Posicion posicionDeseada = new Posicion(posMickey.x, posMickey.y + 1);
        evaluaMovimiento(posicionDeseada, "derecha");
    }

    private void evaluaMovimiento(Posicion posicionDesada, String direccion) {
        if (posicionDesada.x < 0 || posicionDesada.x > 5 || posicionDesada.y < 0 || posicionDesada.y > 5) {
            movimientoContraPared(direccion);
        } else if (laberinto[posicionDesada.x][posicionDesada.y].tipo.tipo.equals(TipoCelda.OBSTACULO.tipo)) {
            movimientoContraObstaculo(posicionDesada);
        } else if (laberinto[posicionDesada.x][posicionDesada.y].tipo.tipo.equals(TipoCelda.SALIDA.tipo)) {
            movimientoGanador();
        } else {
            // Solo puede ser VACIO
            movimientoCorrecto(posicionDesada);
        }
    }

    private void movimientoCorrecto(Posicion posicionDesada) {
        System.out.printf("¡Muy bien! has alcanzado una nueva posición%n");
        cambiaPosicionMickey(posicionDesada);
        pintaLaberinto(false);
    }

    private void movimientoNoValido(String movimiento) {
        System.out.printf("'%s' no es un movimiento válido %n", movimiento);
        System.out.printf("Recuerda las teclas:%n -> q=arriba%n -> a=abajo%n -> o=izquierda%n -> p=derecha%n");
    }

    private void movimientoContraObstaculo(Posicion posicionDeseada) {
        System.out.printf("¡Vaya!, en esa dirección hay un obstáculo. ¡Prueba con otro movimiento!%n");
        laberinto[posicionDeseada.x][posicionDeseada.y].oculta = false;
        pintaLaberinto(false);
    }

    private void movimientoContraPared(String direccion) {
        System.out.printf("No puedes moverte dirección %s, es una pared del laberinto. ¡Prueba con otro movimiento!%n", direccion);
        laberinto[0][0].oculta = false;
    }

    private void movimientoGanador() {
        System.out.printf("¡Lo conseguiste! ¡Alcanzaste la SALIDA en %d movimientos!%n", numMovimientos);
        salidaEncontrada = true;
    }

    private void cambiaPosicionMickey(Posicion nuevaPosicion) {
        laberinto[posMickey.x][posMickey.y].tipo = TipoCelda.VACIO;
        laberinto[nuevaPosicion.x][nuevaPosicion.y].tipo = TipoCelda.MICKEY;

        posMickey.x = nuevaPosicion.x;
        posMickey.y = nuevaPosicion.y;
    }

    private void bienvenida() {
        System.out.printf("%n¡Bienvenido al laberinto!. ¿Serás capaz de conducir a Mickey hasta la salida?%n");
        System.out.printf("A continuación, se te revelará tu posición y la de la salida en el laberinto. ¡Pero no es tan fácil!, hay obstaculos ocultos%n");
        pintaLaberinto(false);
        System.out.printf("Usa las siguientes teclas para moverte cuando se te solicite:%n -> q=arriba%n -> a=abajo%n -> o=izquierda%n -> p=derecha%n");
        System.out.printf("¡En marcha!%n%n");
    }

    private void pintaLaberinto(boolean muestraOcultos) {
        for (int i = 0; i < laberinto.length + 2 ; i++) {
            System.out.print("-");
        }
        System.out.printf("%n");

        for (Celda[] celdas : laberinto) {
            System.out.print("|");
            for (Celda celda : celdas) {
                if (muestraOcultos || !celda.oculta) {
                    System.out.print(celda.tipo.simbolo);
                } else {
                    System.out.print(TipoCelda.VACIO.simbolo);
                }
            }
            System.out.printf("|%n");
        }

        for (int i = 0; i < laberinto.length + 2 ; i++) {
            System.out.print("-");
        }
        System.out.printf("%n");
    }
}
