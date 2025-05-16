import java.util.*;
import java.util.stream.Collectors;

public class miguelex {

    private static void displayTree(List<String> tree) {
        for (String line : tree) {
            System.out.println(line);
        }
    }

    private static List<String> createTree(int height, boolean hasStar, Map<Integer, Map<Integer, String>> decorations, boolean lightsOn) {
        List<String> tree = new ArrayList<>();

        // Estrella opcional
        if (hasStar) {
            tree.add(" ".repeat(height - 1) + "@");
        }

        // Ramas
        for (int i = 1; i <= height; i++) {
            StringBuilder line = new StringBuilder(" ".repeat(height - i));
            for (int j = 0; j < 2 * i - 1; j++) {
                String deco = decorations.getOrDefault(i, Collections.emptyMap()).get(j);
                line.append(deco != null ? deco : "*");
            }
            tree.add(line.toString());
        }

        // Tronco
        String trunkPadding = " ".repeat(height - 2);
        tree.add(trunkPadding + "|||");
        tree.add(trunkPadding + "|||");

        return tree;
    }

    private static void addRandomDecoration(Map<Integer, Map<Integer, String>> decorations, int height, String type, int count) {
        Random random = new Random();
        int added = 0;

        while (added < count) {
            int row = random.nextInt(height) + 1;
            int col = random.nextInt(2 * row - 1);

            decorations.putIfAbsent(row, new HashMap<>());
            if (!decorations.get(row).containsKey(col)) {
                decorations.get(row).put(col, type);
                added++;
            }
        }
    }

    private static void removeRandomDecoration(Map<Integer, Map<Integer, String>> decorations, String type, int count) {
        int removed = 0;

        for (Integer row : new ArrayList<>(decorations.keySet())) {
            for (Integer col : new ArrayList<>(decorations.get(row).keySet())) {
                if (decorations.get(row).get(col).equals(type) && removed < count) {
                    decorations.get(row).remove(col);
                    removed++;
                }
            }
        }
    }

    private static void toggleLights(Map<Integer, Map<Integer, String>> decorations, boolean lightsOn) {
        for (Map<Integer, String> row : decorations.values()) {
            for (Map.Entry<Integer, String> entry : row.entrySet()) {
                if (entry.getValue().equals("+")) {
                    entry.setValue(lightsOn ? "+" : "*");
                }
            }
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Ingrese la altura del árbol: ");
        int height = scanner.nextInt();

        boolean hasStar = true;
        Map<Integer, Map<Integer, String>> decorations = new HashMap<>();
        boolean lightsOn = true;

        while (true) {
            List<String> tree = createTree(height, hasStar, decorations, lightsOn);
            displayTree(tree);

            System.out.println("\nOpciones:");
            System.out.println("1. Añadir/Eliminar estrella");
            System.out.println("2. Añadir bolas (o)");
            System.out.println("3. Eliminar bolas (o)");
            System.out.println("4. Añadir luces (+)");
            System.out.println("5. Eliminar luces (+)");
            System.out.println("6. Apagar/Encender luces");
            System.out.println("7. Salir");

            System.out.print("Seleccione una opción: ");
            int option = scanner.nextInt();

            switch (option) {
                case 1:
                    hasStar = !hasStar;
                    System.out.println(hasStar ? "Estrella añadida." : "Estrella eliminada.");
                    break;
                case 2:
                    addRandomDecoration(decorations, height, "o", 2);
                    System.out.println("Bolas añadidas.");
                    break;
                case 3:
                    removeRandomDecoration(decorations, "o", 2);
                    System.out.println("Bolas eliminadas.");
                    break;
                case 4:
                    addRandomDecoration(decorations, height, "+", 3);
                    System.out.println("Luces añadidas.");
                    break;
                case 5:
                    removeRandomDecoration(decorations, "+", 3);
                    System.out.println("Luces eliminadas.");
                    break;
                case 6:
                    lightsOn = !lightsOn;
                    toggleLights(decorations, lightsOn);
                    System.out.println(lightsOn ? "Luces encendidas." : "Luces apagadas.");
                    break;
                case 7:
                    System.out.println("¡Feliz Navidad!");
                    scanner.close();
                    return;
                default:
                    System.out.println("Opción no válida.");
            }
        }
    }
}
