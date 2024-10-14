import java.util.*;

public class MohamedElderkaoui{

    public static void main(String[] args) {
        Laberinto.main(args);
    }
}
 class Laberinto {

    public static void main(String[] args) {
        final int SIZE = 6;
        char[][] laberinto = generarLaberinto(SIZE);
        int mickeyRow = 0;
        int mickeyCol = 0;
        int salidaRow = 0;
        int salidaCol = 0;

        // Encuentra la posición inicial de Mickey y la salida
        for (int i = 0; i < SIZE; i++) {
            for (int j = 0; j < SIZE; j++) {
                if (laberinto[i][j] == 'M') {
                    mickeyRow = i;
                    mickeyCol = j;
                }
                if (laberinto[i][j] == 'S') {
                    salidaRow = i;
                    salidaCol = j;
                }
            }
        }

        Scanner scanner = new Scanner(System.in);
        int maxMoves = 50;  // Límite de movimientos
        int moves = 0;

        while (moves < maxMoves) {
            mostrarLaberinto(laberinto, mickeyRow, mickeyCol);

            if (mickeyRow == salidaRow && mickeyCol == salidaCol) {
                System.out.println("¡Felicidades! Mickey ha encontrado la salida.");
                break;
            }

            System.out.print("¿Hacia dónde quieres moverte? (arriba/abajo/izquierda/derecha): ");
            String movimiento = scanner.nextLine().toLowerCase();

            int nuevaFila = mickeyRow;
            int nuevaColumna = mickeyCol;

            switch (movimiento) {
                case "arriba":
                    nuevaFila--;
                    break;
                case "abajo":
                    nuevaFila++;
                    break;
                case "izquierda":
                    nuevaColumna--;
                    break;
                case "derecha":
                    nuevaColumna++;
                    break;
                default:
                    System.out.println("Movimiento no válido. Intenta de nuevo.");
                    continue;
            }

            if (esMovimientoValido(nuevaFila, nuevaColumna, laberinto)) {
                laberinto[mickeyRow][mickeyCol] = ' ';
                mickeyRow = nuevaFila;
                mickeyCol = nuevaColumna;
                laberinto[mickeyRow][mickeyCol] = 'M';
                moves++;
            } else {
                System.out.println("Movimiento no válido. Hay un obstáculo o estás fuera del laberinto.");
            }

            System.out.println("Movimientos restantes: " + (maxMoves - moves));
        }

        if (moves >= maxMoves) {
            System.out.println("¡Se acabaron los movimientos! Mickey no ha encontrado la salida.");
        }

        scanner.close();
    }

    private static char[][] generarLaberinto(int size) {
        char[][] laberinto = new char[size][size];
        Random rand = new Random();

        // Inicializa el laberinto con celdas vacías
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                laberinto[i][j] = ' ';
            }
        }

        // Coloca los obstáculos y la salida de manera aleatoria
        int numObstaculos = size;  // Número de obstáculos
        for (int i = 0; i < numObstaculos; i++) {
            int fila = rand.nextInt(size);
            int columna = rand.nextInt(size);
            if (laberinto[fila][columna] == ' ' && !(fila == 0 && columna == 0) && !(fila == size - 1 && columna == size - 1)) {
                laberinto[fila][columna] = 'O';  // Obstáculo representado por 'O'
            }
        }

        // Coloca la salida en una posición fija
        int salidaFila = size - 1;
        int salidaColumna = size - 1;
        laberinto[salidaFila][salidaColumna] = 'S';  // Salida representada por 'S'

        // Coloca a Mickey en una posición fija
        int mickeyFila, mickeyColumna;
        do {
            mickeyFila = rand.nextInt(size);
            mickeyColumna = rand.nextInt(size);
        } while (laberinto[mickeyFila][mickeyColumna] != ' ');

        laberinto[mickeyFila][mickeyColumna] = 'M';  // Mickey representado por 'M'

        return laberinto;
    }

    private static void mostrarLaberinto(char[][] laberinto, int mickeyRow, int mickeyCol) {
        System.out.println("Laberinto:");
        for (int i = 0; i < laberinto.length; i++) {
            for (int j = 0; j < laberinto[i].length; j++) {
                if (i == mickeyRow && j == mickeyCol) {
                    System.out.print('M' + " ");
                } else {
                    System.out.print(laberinto[i][j] + " ");
                }
            }
            System.out.println();
        }
    }

    private static boolean esMovimientoValido(int fila, int columna, char[][] laberinto) {
        return fila >= 0 && fila < laberinto.length && columna >= 0 && columna < laberinto[0].length && laberinto[fila][columna] != 'O';
    }
}
