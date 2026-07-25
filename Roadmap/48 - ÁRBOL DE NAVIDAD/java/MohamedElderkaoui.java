import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.Scanner;
public class MohamedElderkaoui {
    private int altura;
    private boolean tieneEstrella;
    private boolean lucesEncendidas;
    private List<String[]> arbol;

    public ArbolNavidad(int altura) {
        this.altura = altura;
        this.tieneEstrella = false;
        this.lucesEncendidas = false;
        this.arbol = new ArrayList<>();
        generarArbolBase();
    }

    private void generarArbolBase() {
        arbol.clear();
        for (int i = 0; i < altura; i++) {
            int ancho = 1 + 2 * i;
            char[] fila = new char[altura + i];
            for (int j = 0; j < fila.length; j++) {
                fila[j] = (j >= altura - i - 1 && j < altura + i) ? '*' : ' ';
            }
            arbol.addAll(new String(fila).toCharArray());
        }
        // Agregar el tronco
        for (int i = 0; i < 2; i++) {
            char[] tronco = new char[2 * altura - 1];
            for (int j = 0; j < tronco.length; j++) {
                tronco[j] = (j >= altura - 2 && j <= altura) ? '|' : ' ';
            }
            arbol.add(tronco);
        }
    }

    public void toggleEstrella() {
        if (tieneEstrella) {
            arbol.get(0)[altura - 1] = '*';
            System.out.println("Se ha eliminado la estrella del árbol.");
        } else {
            arbol.get(0)[altura - 1] = '@';
            System.out.println("Se ha añadido la estrella al árbol.");
        }
        tieneEstrella = !tieneEstrella;
    }

    public void añadirBolas(int cantidad) {
        Random rand = new Random();
        for (int i = 0; i < cantidad; i++) {
            int fila;
            int columna;
            do {
                fila = rand.nextInt(altura);
                columna = rand.nextInt(altura + fila);
            } while (arbol.get(fila)[columna] != '*');
            arbol.get(fila)[columna] = 'o';
        }
        System.out.println(cantidad + " bola(s) añadida(s).");
    }

    public void eliminarBolas(int cantidad) {
        int eliminadas = 0;
        for (int i = 0; i < altura; i++) {
            for (int j = 0; j < arbol.get(i).length; j++) {
                if (arbol.get(i)[j] == 'o') {
                    arbol.get(i)[j] = '*';
                    eliminadas++;
                    if (eliminadas == cantidad) break;
                }
            }
        }
        System.out.println(eliminadas + " bola(s) eliminada(s).");
    }

    public void añadirLuces(int cantidad) {
        Random rand = new Random();
        for (int i = 0; i < cantidad; i++) {
            int fila;
            int columna;
            do {
                fila = rand.nextInt(altura);
                columna = rand.nextInt(altura + fila);
            } while (arbol.get(fila)[columna] != '*');
            arbol.get(fila)[columna] = '+';
        }
        System.out.println(cantidad + " luz/luces añadida(s).");
    }

    public void eliminarLuces(int cantidad) {
        int eliminadas = 0;
        for (int i = 0; i < altura; i++) {
            for (int j = 0; j < arbol.get(i).length; j++) {
                if (arbol.get(i)[j] == '+') {
                    arbol.get(i)[j] = '*';
                    eliminadas++;
                    if (eliminadas == cantidad) break;
                }
            }
        }
        System.out.println(eliminadas + " luz/luces eliminada(s).");
    }

    public void encenderApagarLuces() {
        for (int i = 0; i < altura; i++) {
            for (int j = 0; j < arbol.get(i).length; j++) {
                if (arbol.get(i)[j] == '+') {
                    arbol.get(i)[j] = lucesEncendidas ? '*' : '+';
                }
            }
        }
        lucesEncendidas = !lucesEncendidas;
        System.out.println(lucesEncendidas ? "Luces encendidas." : "Luces apagadas.");
    }

    public void mostrarArbol() {
        for (char[] fila : arbol) {
            System.out.println(new String(fila));
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Introduce la altura del árbol: ");
        int altura = sc.nextInt();
        ArbolNavidad arbol = new ArbolNavidad(altura);

        int opcion;
        do {
            System.out.println("\nOpciones:");
            System.out.println("1. Alternar estrella");
            System.out.println("2. Añadir bolas (2)");
            System.out.println("3. Eliminar bolas (2)");
            System.out.println("4. Añadir luces (3)");
            System.out.println("5. Eliminar luces (3)");
            System.out.println("6. Encender/Apagar luces");
            System.out.println("7. Mostrar árbol");
            System.out.println("0. Salir");
            System.out.print("Selecciona una opción: ");
            opcion = sc.nextInt();

            switch (opcion) {
                case 1 -> arbol.toggleEstrella();
                case 2 -> arbol.añadirBolas(2);
                case 3 -> arbol.eliminarBolas(2);
                case 4 -> arbol.añadirLuces(3);
                case 5 -> arbol.eliminarLuces(3);
                case 6 -> arbol.encenderApagarLuces();
                case 7 -> arbol.mostrarArbol();
                case 0 -> System.out.println("¡Feliz Navidad!");
                default -> System.out.println("Opción inválida.");
            }
        } while (opcion != 0);

        sc.close();
    }    
}
