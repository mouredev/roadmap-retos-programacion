import java.util.*;

public class alb-martinez {

    static class ArbolNavidad {
        private int altura;
        private char[][] arbol;
        private boolean estrellaCopa;
        private List<int[]> bolas;
        private List<int[]> luces;

        public ArbolNavidad(int altura) {
            this.altura = altura;
            this.arbol = new char[altura + 2][2 * altura - 1];
            this.bolas = new ArrayList<>();
            this.luces = new ArrayList<>();
            this.estrellaCopa = false;
            contruirArbol();
        }

        private void contruirArbol() {
            for (int i = 0; i < arbol.length; i++) {
                for (int j = 0; j < arbol[i].length; j++) {
                    arbol[i][j] = ' ';
                }
            }

            for (int i = 0; i < altura; i++) {
                for (int j = altura - i - 1; j <= altura + i - 1; j++) {
                    arbol[i][j] = '*';
                }
            }

            int troncoInicio = (arbol[altura].length - 3) / 2;
            for (int i = altura; i < altura + 2; i++) {
                for (int j = troncoInicio; j < troncoInicio + 3; j++) {
                    arbol[i][j] = '|';
                }
            }
        }

        public void imprimirArbol() {

            for (int i = 0; i < altura; i++) {
                for (int j = 0; j < arbol[i].length; j++) {
                    System.out.print(arbol[i][j]);;
                }
                System.out.println();
            }

            for (int i = altura; i < altura + 2; i++) {
                for (int j = 0; j < arbol[i].length; j++) {
                    System.out.print(arbol[i][j]);
                }
                System.out.println();
            }

        }

        public void añadirEstrella() {
            if (!estrellaCopa) {
                arbol[0][altura - 1] = '@';
                estrellaCopa = true;
                System.out.println("Se ha añadido una estrella en la copa del arbol.");
            } else {
                System.out.println("Ya existe una estrella en la copa");
            }
        }

        public void eliminarEstrella() {
            if (estrellaCopa) {
                arbol[0][altura - 1] = '*';
                estrellaCopa = false;
                System.out.println("Se ha eliminado la estrella de la copa del arbol.");
            } else {
                System.out.println("No hay entrella en la copa del arbol.");
            }
        }

        public void añadirBola() {
            Random random = new Random();
            int x, y;
            do {
                x = random.nextInt(altura);
                y = random.nextInt(2 * altura - 1);
            } while (arbol[x][y] != '*' || contieneBolaOLuces(x, y));

            arbol[x][y] = 'o';
            bolas.add(new int[]{x, y});
            System.out.println("Se ha añadido una bola en la posición (" + x + ", " + y + ").");
        }

        public void eliminarBola() {
            if (bolas.isEmpty()) {
                System.out.println("No hay bolas para eliminar");
                return;
            }

            int [] bola = bolas.remove(bolas.size() - 1);
            arbol[bola[0]][bola[1]] = '*';
            System.out.println("Se ha eliminado una bola en la posición (" + bola[0] + ", " + bola[1] + ").");
        }

        public void añadirLuz() {
            Random random = new Random();
            int x, y;
            do {
                x = random.nextInt(altura);
                y = random.nextInt(2 * altura - 1);
            } while (arbol[x][y] != '*' || contieneBolaOLuces(x, y));

            arbol[x][y] = '+';
            luces.add(new int[]{x, y});
            System.out.println("Se ha añadido una luz en la posición (" + x + ", " + y + ").");
        }

        public void eliminarLuz() {
            if (luces.isEmpty()) {
                System.out.println("No hay luces para eliminar.");
                return;
            }

            int[] luz = luces.remove(luces.size() - 1);
            arbol[luz[0]][luz[1]] = '*';
            System.out.println("Se ha eliminado una luz en la posición (" + luz[0] + ", " + luz[1] + ").");
        }

        private boolean contieneBolaOLuces(int x, int y) {
            for (int[] bola : bolas) {
                if (bola[0] == x && bola[1] == y) return true;
            }
            for (int[] luz : luces) {
                if (luz[0] == x && luz[1] == y) return true;
            }
            return false;
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int altura = 0;
        boolean entradaValida = false;
        while (!entradaValida) {
            System.out.print("Introduce la altura del árbol: ");
            if (scanner.hasNextInt()) {
                altura = scanner.nextInt();
                if (altura > 0) {
                    entradaValida = true;
                } else {
                    System.out.println("Por favor, introduce un número positivo.");
                }
            } else {
                System.out.println("Entrada no válida. Debes introducir un número.");
                scanner.next();
            }
        }

        ArbolNavidad arbol = new ArbolNavidad(altura);

        boolean salir = false;
        while (!salir) {
            arbol.imprimirArbol();
            System.out.println("\n¿Qué acción deseas realizar?");
            System.out.println("1. Añadir estrella");
            System.out.println("2. Eliminar estrella");
            System.out.println("3. Añadir Bola");
            System.out.println("4. Eliminar Bola");
            System.out.println("5. Añadir luz");
            System.out.println("6. Eliminar luz");
            System.out.println("7. Salir");

            int opcion = 0;
            boolean opcionValida = false;
            while (!opcionValida) {
                if (scanner.hasNextInt()) {
                    opcion = scanner.nextInt();
                    if (opcion >= 1 && opcion <= 7) {
                        opcionValida = true;
                    } else {
                        System.out.println("Opción no válida. Introduce un número entre 1 y 7.");
                    }
                } else {
                    System.out.println("Entrada no válida. Debes introducir un número.");
                    scanner.next();
                }
            }

            switch (opcion) {
                case 1 -> arbol.añadirEstrella();
                case 2 -> arbol.eliminarEstrella();
                case 3 -> arbol.añadirBola();
                case 4 -> arbol.eliminarBola();
                case 5 -> arbol.añadirLuz();
                case 6 -> arbol.eliminarLuz();
                case 7 -> salir = true;
                default -> System.out.println("Opción no válida.");
            }
        }
        scanner.close();
    }
}
