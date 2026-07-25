import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

class Luchador {
    String nombre;
    int velocidad;
    int ataque;
    int defensa;
    int salud = 100;

    public Luchador(String nombre, int velocidad, int ataque, int defensa) {
        this.nombre = nombre;
        this.velocidad = velocidad;
        this.ataque = ataque;
        this.defensa = defensa;
    }

    public boolean esquivar() {
        return Math.random() < 0.2;
    }
}

public class miguelex {
    public static Luchador batalla(Luchador luchador1, Luchador luchador2) {
        System.out.println("¡Batalla entre " + luchador1.nombre + " y " + luchador2.nombre + "!");
        Luchador atacante = (luchador1.velocidad >= luchador2.velocidad) ? luchador1 : luchador2;
        Luchador defensor = (atacante == luchador1) ? luchador2 : luchador1;

        while (luchador1.salud > 0 && luchador2.salud > 0) {
            if (defensor.esquivar()) {
                System.out.println(defensor.nombre + " esquivó el ataque de " + atacante.nombre + "!");
            } else {
                int danio = atacante.ataque - defensor.defensa;
                if (danio <= 0) {
                    danio = (int) (atacante.ataque * 0.1);
                }
                defensor.salud -= danio;
                System.out.println(atacante.nombre + " ataca a " + defensor.nombre + " y causa " + danio + " de daño. Salud restante de " + defensor.nombre + ": " + defensor.salud);
            }
            Luchador temp = atacante;
            atacante = defensor;
            defensor = temp;
        }

        Luchador ganador = (luchador1.salud > 0) ? luchador1 : luchador2;
        System.out.println("¡" + ganador.nombre + " es el ganador de la batalla!\n");
        return ganador;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<Luchador> luchadores = new ArrayList<>();

        System.out.print("Ingrese el número de luchadores (debe ser una potencia de 2): ");
        int numLuchadores = scanner.nextInt();
        scanner.nextLine(); // Consumir nueva línea

        if ((numLuchadores & (numLuchadores - 1)) != 0 || numLuchadores <= 0) {
            System.out.println("El número de luchadores debe ser una potencia de 2.");
            return;
        }

        for (int i = 0; i < numLuchadores; i++) {
            System.out.print("Ingrese el nombre del luchador " + (i + 1) + ": ");
            String nombre = scanner.nextLine();

            System.out.print("Ingrese la velocidad de " + nombre + " (0-100): ");
            int velocidad = scanner.nextInt();

            System.out.print("Ingrese el ataque de " + nombre + " (0-100): ");
            int ataque = scanner.nextInt();

            System.out.print("Ingrese la defensa de " + nombre + " (0-100): ");
            int defensa = scanner.nextInt();
            scanner.nextLine(); // Consumir nueva línea

            luchadores.add(new Luchador(nombre, velocidad, ataque, defensa));
        }

        System.out.println("¡Comienza el torneo de Dragon Ball: Sparking! ZERO!\n");
        while (luchadores.size() > 1) {
            ArrayList<Luchador> ganadores = new ArrayList<>();
            Collections.shuffle(luchadores);

            for (int i = 0; i < luchadores.size(); i += 2) {
                Luchador ganador = batalla(luchadores.get(i), luchadores.get(i + 1));
                ganadores.add(ganador);
            }
            luchadores = ganadores;
        }

        System.out.println("¡El ganador del torneo es " + luchadores.get(0).nombre + "!");
        scanner.close();
    }
}

