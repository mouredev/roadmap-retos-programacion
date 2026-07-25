import java.util.Objects;
import java.util.Scanner;

public class danhingar {

    public static void main(String[] args) {

        String[][] maze = { { "🐭", "⬛", "⬛", "⬛", "⬛", "⬜" },
                { "⬜", "⬛", "⬜", "⬛", "⬜", "⬜" },
                { "⬜", "⬜", "⬜", "⬛", "⬜", "⬛" },
                { "⬜", "⬛", "⬜", "⬜", "⬜", "⬛" },
                { "⬜", "⬜", "⬛", "⬜", "⬜", "⬜" },
                { "⬜", "⬛", "⬛", "⬛", "⬛", "🚪" } };

        print(maze);

        int[] mickey = { 0, 0 };
        Scanner sc = new Scanner(System.in);
        while (Boolean.TRUE) {
            System.out.println("¿Hacia dónde se mueve Mickey?");
            System.out.println("[u] Arriba");
            System.out.println("[d] Abajo");
            System.out.println("[l] Izquierda");
            System.out.println("[r] Derecha");
            System.out.print("Dirección: ");

            String direction = sc.nextLine();

            int currentRow = mickey[0], currentColumn = mickey[1];
            int newRow = currentRow, newColumn = currentColumn;

            switch (direction) {
                case "u":
                    newRow = currentRow - 1;
                    break;
                case "d":
                    newRow = currentRow + 1;
                    break;
                case "r":
                    newColumn = currentColumn + 1;
                    break;
                case "l":
                    newColumn = currentColumn - 1;
                    break;
                default:
                    System.out.println("Dirección no válida.\n");
                    break;
            }

            if ((newRow < 0 || newRow > 5) || (newColumn < 0 || newColumn > 5)) {
                System.out.println("No puedes desplazarte fuera del Laberinto.\n");
            } else if (Objects.equals(maze[newRow][newColumn], "⬛")) {
                System.out.println("!En esa dirección hay un obstáculo!\n");
                continue;
            } else if (Objects.equals(maze[newRow][newColumn], "🚪")) {
                System.out.println("!Has encontrado la salida!");
                break;
            } else {
                maze[currentRow][currentColumn] = "⬜";
                maze[newRow][newColumn] = "🐭";
                mickey[0] = newRow;
                mickey[1] = newColumn;
                print(maze);
            }

        }
        sc.close();
    }

    public static void print(String[][] maze) {
        for (int i = 0; i < 6; i++) {
            for (int j = 0; j < 6; j++) {
                System.out.print("".concat(maze[i][j]));

            }
            System.out.println();
        }
    }
}
