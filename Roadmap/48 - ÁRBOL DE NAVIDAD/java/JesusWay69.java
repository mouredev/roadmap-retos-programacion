package reto_49;

import java.util.ArrayList;
import java.util.Scanner;

public class JesusWay69 {

    public static ArrayList<Integer> coordinates = new ArrayList<>();

    public static void main(String[] args) {

        char[][] myTree = null;

        do {
            Scanner sc = new Scanner(System.in);
            System.out.println("""
              1- Crear nuevo árbol
              2- Añadir estrella 
              3- Eliminar estrella 
              4- Añadir 2 bolas aleatoriamente
              5- Quitar todas las bolas
              6- Añadir 3 luces aleatoriamente 
              7- Encender las luces
              8- Apagar las luces
                             """);
            System.out.print("Elija una opción (enter para salir): ");
            String option = sc.nextLine();
            if (option.equals(""))  break;

            switch (option) {
                case "1" -> {
                    System.out.print("Introduzca la altura del árbol (mayor de 3): ");
                    int hight = sc.nextInt();
                    myTree = createTree(hight);
                    showTree(myTree);
                }
                case "2" -> showTree(topStar(myTree, true));               
                case "3" -> showTree(topStar(myTree, false));               
                case "4" -> showTree(addBalls(myTree));              
                case "5" -> showTree(removeBalls(myTree));               
                case "6" -> showTree(addLights(myTree));           
                case "7" -> showTree(turnOnLights(myTree, coordinates));              
                case "8" ->showTree(turnOffLigths(myTree));
                default -> System.out.println("El dato tiene que ser numérico del 1 al 8\n");               
            }
        } while (true);
    }

    public static ArrayList<Integer> storageCoordinates(int x, int y) {
        coordinates.add(x);
        coordinates.add(y);
        return coordinates;
    }

    public static char[][] createTree(int files) {
        int columns = files * 2 - 1;
        int branch = 1;
        char[][] tree = new char[files + 2][columns];

        if (files <= 3) {
            System.out.println("No se puede crear un árbol de menos de 4 alturas");
            tree = null;
            return tree;
        }
        for (int i = 0; i < files; i++) {
            for (int j = 0; j < columns / 2; j++) tree[i][j] = ' '; 
            for (int k = columns / 2; k < columns / 2 + branch; k++) tree[i][k] = '*';
            for (int l = columns / 2 + branch; l < files * 2 - 1; l++) tree[i][l] = ' ';
            columns -= 2;
            branch += 2;
        }
        for (int m = 0; m < 2; m++) {
            for (int n = 0; n < files - 2; n++) tree[files + m][n] = ' ';
            for (int p = files - 2; p < files + 1; p++) tree[files + m][p] = '|';
            for (int q = files + 1; q < files * 2 - 1; q++) tree[files + m][q] = ' ';   
        }
        return tree;
    }
    public static void showTree(char[][] tree) {
        if (tree != null) {
            int i = 0;
            for (char[] branch : tree) {
                i++;
                for (char c : branch) System.out.print(c);
                System.out.println();
            }
        }
    }

    public static char[][] topStar(char[][] tree, boolean switchStar) {
        if (tree == null) {
            System.out.println("ERROR: Hay que crear un árbol antes de poder modificarlo (opción 1)");
            return null;
        } else if (switchStar) {
            tree[0][tree[0].length / 2] = '@';
            System.out.println("\n--- ESTRELLA AÑADIDA ---");
        } else {
            tree[0][tree[0].length / 2] = '*';
            System.out.println("\n--- ESTRELLA ELIMINADA ---");
        }
        return tree;
    }

    public static char[][] addBalls(char[][] tree) {
        if (tree == null) {
            System.out.println("ERROR: Hay que crear un árbol antes de poder modificarlo (opción 1)");
            return null;
        }
        for (int i = 0; i < 2; i++) {
            int randomFile = (int) (Math.random() * tree.length - 2 + 1);
            int randomColumn = (int) (Math.random() * tree[0].length);
            if (tree[randomFile][randomColumn] == '*') tree[randomFile][randomColumn] = 'O';      
            else i--;   
        }
        System.out.println("\n--- SE AÑADEN 2 BOLAS DE ADORNO ---");
        return tree;
    }

    public static char[][] removeBalls(char[][] tree) {
        if (tree == null) {
            System.out.println("ERROR: Hay que crear un árbol antes de poder modificarlo (opción 1)");
            return null;
        }
        for (int i = 1; i < tree.length - 2; i++) {
            for (int j = 0; j < tree[i].length; j++) {
                if (tree[i][j] == 'O') tree[i][j] = '*';      
            }
        }
        System.out.println("\n--- BOLAS DE ADORNO ELIMINADAS ---");
        return tree;
    }

    public static char[][] addLights(char[][] tree) {
        if (tree == null) {
            System.out.println("ERROR: Hay que crear un árbol antes de poder modificarlo (opción 1)");
            return null;
        }
        for (int i = 0; i < 3; i++) {
            int randomFile = (int) (Math.random() * tree.length - 2) + 1;
            int randomColumn = (int) (Math.random() * tree[0].length);
            if (tree[randomFile][randomColumn] == '*') {
                tree[randomFile][randomColumn] = 'X';
                storageCoordinates(randomFile, randomColumn);
            } else i--;   
        }
        System.out.println("\n--- AÑADIDAS 3 LUCES ENCENDIDAS AL ÁRBOL ---");
        return tree;
    }

    public static char[][] turnOnLights(char[][] tree, ArrayList<Integer> coordinates) {
        if (tree == null) {
            System.out.println("ERROR: Hay que crear un árbol antes de poder modificarlo (opción 1)");
            return null;
        }
        int x = 0;
        for (int j = 0; j < coordinates.size(); j++) {
            if (j % 2 == 0) {
                x = coordinates.get(j);
            } else {
                int y = coordinates.get(j);
                tree[x][y] = 'X';
            }
        }
        System.out.println("\n--- TODAS LAS LUCES ENCENDIDAS ---");
        return tree;
    }

    public static char[][] turnOffLigths(char[][] tree) {
        if (tree == null) {
            System.out.println("ERROR: Hay que crear un árbol antes de poder modificarlo (opción 1)");
            return null;
        }
        for (int i = 1; i < tree.length - 2; i++) {
            for (int j = 0; j < tree[i].length; j++) {
                if (tree[i][j] == 'X') tree[i][j] = '*';   
            }
        }
        System.out.println("\n--- TODAS LAS LUCES APAGADAS ---");
        return tree;
    }
}
