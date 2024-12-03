import java.util.ArrayList;
import java.util.Collections;
import java.util.Random;

class Fighter {
    private String nombre;
    private int velocidad;
    private int ataque;
    private int defensa;
    private int salud;
    private Random rand = new Random();

    public Fighter(String nombre, int velocidad, int ataque, int defensa) {
        this.nombre = nombre;
        this.velocidad = velocidad;
        this.ataque = ataque;
        this.defensa = defensa;
        this.salud = 100;
    }

    public String getNombre() {
        return nombre;
    }

    public int getVelocidad() {
        return velocidad;
    }

    public boolean estaVivo() {
        return salud > 0;
    }

    public void recibirDanio(int danio) {
        salud -= danio;
        if (salud < 0) {
            salud = 0;
        }
    }

    public void atacar(Fighter oponente) throws InterruptedException {
        if (rand.nextDouble() < 0.2) {
            // 20% de posibilidad de esquivar
            System.out.println(oponente.getNombre() + " esquivó el ataque!");
            Thread.sleep(4000); // Espera de 4 segundos entre golpes
            return;
        }

        int danio;
        if (this.ataque > oponente.defensa) {
            danio = this.ataque - oponente.defensa;
        } else {
            danio = (int) (0.1 * this.ataque); // 10% del daño de ataque si defensa > ataque
        }

        System.out.println(this.nombre + " ataca a " + oponente.getNombre() + " por " + danio + " de daño!");
        oponente.recibirDanio(danio);
        System.out.println(oponente.getNombre() + " tiene " + oponente.salud + " de salud restante.");
        Thread.sleep(4000); // Espera de 4 segundos entre golpes
    }

    @Override
    public String toString() {
        return nombre + " (Velocidad: " + velocidad + ", Ataque: " + ataque + ", Defensa: " + defensa + ", Salud: " + salud + ")";
    }
}

class Batalla {
    private Fighter luchador1;
    private Fighter luchador2;

    public Batalla(Fighter luchador1, Fighter luchador2) {
        this.luchador1 = luchador1;
        this.luchador2 = luchador2;
    }

    public Fighter iniciar() throws InterruptedException {
        System.out.println("Batalla: " + luchador1.getNombre() + " vs " + luchador2.getNombre());

        // Determinar quién ataca primero basado en la velocidad
        Fighter atacante = (luchador1.getVelocidad() >= luchador2.getVelocidad()) ? luchador1 : luchador2;
        Fighter defensor = (atacante == luchador1) ? luchador2 : luchador1;

        // Pelear hasta que uno de los luchadores pierda toda su salud
        while (luchador1.estaVivo() && luchador2.estaVivo()) {
            atacante.atacar(defensor);
            if (!defensor.estaVivo()) {
                System.out.println(defensor.getNombre() + " está fuera de combate!");
                break;
            }
            // Cambiar atacante y defensor
            Fighter temp = atacante;
            atacante = defensor;
            defensor = temp;
        }

        return luchador1.estaVivo() ? luchador1 : luchador2;
    }
}

class Torneo {
    private ArrayList<Fighter> luchadores;

    public Torneo(ArrayList<Fighter> luchadores) {
        if (!esPotenciaDeDos(luchadores.size())) {
            throw new IllegalArgumentException("El número de luchadores debe ser una potencia de 2.");
        }
        this.luchadores = luchadores;
    }

    private boolean esPotenciaDeDos(int n) {
        return (n > 0) && ((n & (n - 1)) == 0);
    }

    public Fighter iniciar() throws InterruptedException {
        System.out.println("Iniciando el torneo con " + luchadores.size() + " luchadores!");
        imprimirCuadro(luchadores);

        int ronda = 1;
        while (luchadores.size() > 1) {
            Collections.shuffle(luchadores); // Emparejamientos aleatorios en cada ronda
            ArrayList<Fighter> siguienteRonda = new ArrayList<>();

            System.out.println("\n---- RONDA " + ronda + " ----");
            for (int i = 0; i < luchadores.size(); i += 2) {
                Fighter luchador1 = luchadores.get(i);
                Fighter luchador2 = luchadores.get(i + 1);

                System.out.println(luchador1.getNombre() + " vs " + luchador2.getNombre());
                Batalla batalla = new Batalla(luchador1, luchador2);
                Fighter ganador = batalla.iniciar();
                System.out.println(ganador.getNombre() + " gana la batalla!\n");

                siguienteRonda.add(ganador);
                // Esperar 1 minuto entre las peleas
                System.out.println("Preparando la siguiente batalla... (esperando 1 minuto)");
                extracted();
            }

            luchadores = siguienteRonda; // Los ganadores avanzan a la siguiente ronda
            ronda++;
            imprimirCuadro(luchadores); // Imprimir el cuadro del torneo después de cada ronda
        }

        return luchadores.get(0); // El último luchador restante es el campeón
    }

    private void extracted() throws InterruptedException {
        Thread.sleep(60000); // 1 minuto (60 segundos) entre batallas
    }

    // Función para imprimir el cuadro del torneo
    public void imprimirCuadro(ArrayList<Fighter> luchadores) {
        int size = luchadores.size();
        String[] lineas = new String[size];

        // Inicializar líneas en blanco para mostrar el cuadro
        for (int i = 0; i < size; i++) {
            lineas[i] = "";
        }

        // Llenar las líneas con los nombres de los luchadores
        int indiceCombate = 0;
        for (int i = 0; i < size / 2; i++) {
            String luchador1 = luchadores.get(i * 2).getNombre();
            String luchador2 = luchadores.get(i * 2 + 1).getNombre();

            lineas[indiceCombate++] += String.format("%-15s vs %-15s", luchador1, luchador2);
        }

        System.out.println("\nCuadro del Torneo:");
        for (String linea : lineas) {
            System.out.println(linea);
        }
    }
}

public class MohamedElderkaoui {
    public static void main(String[] args)  {
        // Crear una lista de luchadores
        ArrayList<Fighter> luchadores = new ArrayList<>();
        luchadores.add(new Fighter("Goku", 90, 95, 85));
        luchadores.add(new Fighter("Vegeta", 88, 90, 80));
        luchadores.add(new Fighter("Piccolo", 70, 80, 90));
        luchadores.add(new Fighter("Freezer", 85, 85, 75));
        luchadores.add(new Fighter("Cell", 80, 88, 82));
        luchadores.add(new Fighter("Majin Buu", 75, 90, 90));
        luchadores.add(new Fighter("Gohan", 85, 89, 78));
        luchadores.add(new Fighter("Trunks", 80, 86, 80));

        // Crear e iniciar el torneo
        try {
            Torneo torneo = new Torneo(luchadores);
            Fighter campeon = torneo.iniciar();

            // Anunciar el ganador
            System.out.println("\nEl campeón del torneo es " + campeon.getNombre() + "!");
        } catch (InterruptedException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
    }
}
