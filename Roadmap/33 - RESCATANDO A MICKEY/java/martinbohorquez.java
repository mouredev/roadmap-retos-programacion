import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

/**
 * #33 RESCATANDO A MICKEY
 *
 * @author martinbohorquez
 */
public class martinbohorquez {

    static Scanner sc = new Scanner(System.in);

    static List<List<String>> maze = new ArrayList<>(
            Arrays.asList(
                    Arrays.asList("🐭", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"),
                    Arrays.asList("⬜️", "⬛️", "⬛️", "⬛️", "⬜️", "⬛️"),
                    Arrays.asList("⬜️", "⬛️", "⬛️", "⬛️", "⬜️", "⬛️"),
                    Arrays.asList("⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️"),
                    Arrays.asList("⬛️", "⬜️", "⬛️", "⬜️", "⬛️", "⬛️"),
                    Arrays.asList("⬛️", "⬜️", "⬛️", "⬜️", "⬜️", "🚪")
            )
    );

    static Position mickey = new Position("Mickey");
    static boolean flag = false;

    public static void main(String[] args) {

        while (!flag) {
            System.out.println("<-------------- JUEGO DE MICKY ------------------>");
            printMaze(maze);
            System.out.println("""
                    ¿Hacia dónde se mueve Mickey?
                    [w] arriba
                    [s] abajo
                    [a] izquierda
                    [d] derecha
                    """);
            System.out.print("Dirección: ");
            String direction = sc.nextLine().toLowerCase();

            mickey.move(direction);
        }
    }

    private static void printMaze(List<List<String>> maze) {
        maze.forEach(row -> {
            row.forEach(cell -> System.out.print(cell + " "));
            System.out.println();
        });
    }

    static class Position {
        private String name;
        private Integer row;
        private Integer column;

        public Position(String name) {
            this.name = name;
            this.row = 0;
            this.column = 0;
        }

        private String getName() {
            return name;
        }

        private Integer getRow() {
            return row;
        }

        private void setRow(Integer row) {
            this.row = row;
        }

        private Integer getColumn() {
            return column;
        }

        private void setColumn(Integer column) {
            this.column = column;
        }

        private void move(String direction) {
            switch (direction) {
                case "w" -> update(-1, 0);
                case "s" -> update(1, 0);
                case "a" -> update(0, -1);
                case "d" -> update(0, 1);
                default -> System.out.printf("Dirección '%s' es incorrecta!%n", direction);
            }
        }

        private void update(int i, int j) {
            if (getRow() + i < 0 || getRow() + i > maze.size() || getColumn() + j < 0 || getColumn() + j > maze.getFirst().size())
                System.out.println("¡No puedes desplazarte fuera del laberinto!");
            else if (maze.get(getRow() + i).get(getColumn() + j).equals("⬛️"))
                System.out.println("¡En esa dirección hay un obstáculo!");
            else {
                maze.get(getRow()).set(getColumn(), "⬜️");
                setRow(getRow() + i);
                setColumn(getColumn() + j);
                if (maze.get(getRow()).get(getColumn()).equals("🚪")) {
                    System.out.printf("¡%s ha encontrado la salida!%n", mickey.getName());
                    flag = true;
                }
                maze.get(getRow()).set(getColumn(), "🐭");
            }
        }
    }
}
