import java.util.*;

public class Josegs95 {
    public static void main(String[] args) {
        new Josegs95().createChristmasTree();
    }

    private char[][] tree;
    private char[][] trunk;
    private int treeHeight;
    private int treeWidth;

    private Random rnd = new Random();
    final private Scanner sc = new Scanner(System.in);
    private List<TreeDecoration> decorationList = new ArrayList<>();
    private boolean isLightON = true;

    public void createChristmasTree(){
        try(sc){
            System.out.print("Selecciona la altura del árbol de navidad (+2): ");
            treeHeight = Integer.parseInt(sc.nextLine());
            treeWidth = treeHeight * 2 - 1;

            tree = new char[treeHeight][treeWidth];
            trunk = new char[2][treeWidth];

            createBasicTree();
            createTrunk();

            app:
            while(true){
                printChristmasTree();
                printMenu();
                System.out.print("Selecciona una opción: ");
                String option = sc.nextLine();
                switch (option){
                    case "1" -> addTreeTopper(true);
                    case "2" -> addTreeTopper(false);
                    case "3" -> addDecoration(TreeDecoration.Type.BALL, 2);
                    case "4" -> deleteDecoration(TreeDecoration.Type.BALL, 2);
                    case "5" -> addDecoration(TreeDecoration.Type.LIGHT, 3);
                    case "6" -> deleteDecoration(TreeDecoration.Type.LIGHT, 3);
                    case "7" -> turnLightON(!isLightON);
                    case "8" -> {
                        System.out.println("Saliendo de la aplicación...");
                        break app;
                    }
                    default -> System.out.println("Error, opción no válida.");
                }
                System.out.println();
            }
        }
    }

    private void printMenu(){
        System.out.println("========= Menu =========");
        System.out.println("1. Añadir la estrella en la copa del árbol");
        System.out.println("2. Eliminar la estrella en la copa del árbol");
        System.out.println("3. Añadir bolas de Navidad (cantidad: 2)");
        System.out.println("4. Eliminar bolas de Navidad (cantidad: 2)");
        System.out.println("5. Añadir luces de Navidad (cantidad: 3)");
        System.out.println("6. Eliminar luces de Navidad (cantidad: 3)");
        System.out.println("7. Encender/apagar luces de Navidad");
        System.out.println("8. Salir de la aplicación");
        System.out.println("========================");
    }

    private void addTreeTopper(boolean addOperation){
        tree[0][treeWidth / 2] = addOperation ? '@' : '*';
    }

    private void addDecoration(TreeDecoration.Type type, int amount){
        if (decorationList.size() + amount > Math.pow(treeHeight, 2) - 1){
            System.out.println("No caben esa cantidad de objetos en el árbol");
            return;
        }

        loop:
        for (int i = 0; i < amount; i++){
            int a = rnd.nextInt(1, treeHeight);
            int b = rnd.nextInt(treeWidth / 2 - a, treeWidth / 2 + a + 1);

            TreeDecoration decoration = new TreeDecoration(type, b, a);

            for (TreeDecoration aux : decorationList){
                if (decoration.isInSamePlace(aux)){
                    i--;
                    continue loop;
                }
            }

            decorationList.add(decoration);
        }
    }

    private void deleteDecoration(TreeDecoration.Type type, int amount){
        List<TreeDecoration> auxList = new ArrayList<>(decorationList.stream()
                .filter(x -> x.getType() == type)
                .toList());
        if (auxList.size() < amount){
            System.out.println("El árbol de Navidad no tiene suficientes objetos que quitar");
            return;
        }

        Collections.shuffle(auxList);
        for (int i = 0; i < amount; i++)
            decorationList.remove(auxList.get(i));
    }

    private void turnLightON(boolean turnLights){
        isLightON = turnLights;
    }

    private char[][] decorateChristmasTree(char[][] tree){
        for (TreeDecoration decoration :  decorationList) {
            tree[decoration.getYCoord()][decoration.getXCoord()] = decoration.getIcon(isLightON);
        }

        return tree;
    }

    private void createBasicTree(){
        Arrays.stream(tree).forEach(x -> Arrays.fill(x, ' '));

        for (int i = 0; i < treeHeight; i++){
            int aux = 1 + 2 * i;
            for (int j = 0; j < aux; j++){
                tree[i][treeWidth / 2 - i + j] = '*';
            }
        }
    }

    private void createTrunk(){
        Arrays.stream(trunk).forEach(x -> Arrays.fill(x, ' '));

        for (int i = 0; i < 2; i++){
            for (int j = 0; j < 3; j++){
                trunk[i][treeWidth / 2 - 1 + j] = '|';
            }
        }
    }

    private void printChristmasTree(){
        char[][] cloneTree = Arrays.stream(tree).map(char[]::clone).toArray(char[][]::new);
        printGrid(decorateChristmasTree(cloneTree));
        printGrid(trunk);
        System.out.println();
    }

    private void printGrid(char[][] grid){
        for (int i = 0; i < grid.length; i++){
            for (int j = 0; j < grid[0].length; j++){
                System.out.print(grid[i][j]);
            }
            System.out.println();
        }
    }

    public class TreeDecoration{
        enum Type {
            BALL,
            LIGHT
        }

        private Type type;
        private int xCoord;
        private int yCoord;

        public TreeDecoration(Type type, int x, int y) {
            this.type = type;
            this.xCoord = x;
            this.yCoord = y;
        }

        public boolean isInSamePlace(TreeDecoration other) {
            return xCoord == other.getXCoord() && yCoord == other.getYCoord();
        }

        public char getIcon(boolean isLightON){
            switch (type){
                case BALL -> {
                    return 'o';
                }
                case LIGHT -> {
                    return isLightON ? '+' : '*';
                }
                default -> {
                    return ' ';
                }
            }
        }

        public Type getType() {
            return type;
        }

        public int getXCoord() {
            return xCoord;
        }

        public int getYCoord() {
            return yCoord;
        }
    }
}
