import java.util.Random;
import java.util.Scanner;

public class Main {

    private static Random random = new Random();

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Introduce la altura del árbol: ");
        int altura = scanner.nextInt();
        scanner.nextLine();

        boolean estrella = true;
        boolean lucesEncendidas = true;
        char[][] arbol = crearArbol(altura, estrella);

        while (true) {
            imprimirArbol(arbol, lucesEncendidas);
            System.out.println("Selecciona una acción:");
            System.out.println("1. Añadir/eliminar estrella");
            System.out.println("2. Añadir/eliminar bolas");
            System.out.println("3. Añadir/eliminar luces");
            System.out.println("4. Apagar/encender luces");
            System.out.println("5. Salir");

            int opcion = scanner.nextInt();
            scanner.nextLine();

            switch (opcion) {
                case 1 -> {
                    estrella = !estrella;
                    arbol = crearArbol(altura, estrella);
                }
                case 2 -> modificarBolas(arbol);
                case 3 -> modificarLuces(arbol);
                case 4 -> lucesEncendidas = !lucesEncendidas;
                case 5 -> {
                    return;
                }
                default -> System.out.println("Opción no válida");
            }
        }
    }

    private static char[][] crearArbol(int altura, boolean estrella) {
        char[][] arbol = new char[altura + 2][altura * 2 - 1];

        for (int i = 0; i < altura; i++) {
            for (int j = 0; j < altura * 2 - 1; j++) {
                if (j >= altura - 1 - i && j <= altura - 1 + i) {
                    arbol[i][j] = '*';
                } else {
                    arbol[i][j] = ' ';
                }
            }
        }

        if (estrella) arbol[0][altura - 1] = '@';

        for (int i = 0; i < altura * 2 - 1; i++) {
            arbol[altura][i] = ' ';
            arbol[altura + 1][i] = ' ';
        }

        arbol[altura][altura - 1] = '|';
        arbol[altura + 1][altura - 1] = '|';

        return arbol;
    }

    private static void imprimirArbol(char[][] arbol, boolean lucesEncendidas) {
        for (char[] fila : arbol) {
            for (char c : fila) {
                if (c == '+' && !lucesEncendidas) System.out.print('*');
                else System.out.print(c);
            }
            System.out.println();
        }
    }

    private static void modificarBolas(char[][] arbol) {
        for (int i = 1; i < arbol.length - 2; i++) {
            for (int j = 0; j < arbol[i].length; j++) {
                if (arbol[i][j] == '*' && random.nextBoolean()) arbol[i][j] = 'o';
                else if (arbol[i][j] == 'o' && random.nextBoolean()) arbol[i][j] = '*';
            }
        }
    }

    private static void modificarLuces(char[][] arbol) {
        for (int i = 1; i < arbol.length - 2; i++) {
            for (int j = 0; j < arbol[i].length; j++) {
                if (arbol[i][j] == '*' && random.nextBoolean()) arbol[i][j] = '+';
                else if (arbol[i][j] == '+' && random.nextBoolean()) arbol[i][j] = '*';
            }
        }
    }
}
