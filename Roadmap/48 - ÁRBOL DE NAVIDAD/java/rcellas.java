
import java.util.Random;
import java.util.Scanner;


public class rcellas {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        Random random = new Random();

        // declaración de la altura del arbol
        System.out.println("¿De cuantas altura quieres tu árbol de navidad?");
        int heightTree = Integer.parseInt(scanner.nextLine());

        System.out.println("\n¿Cómo de largo quieres tú tronco?");
        int trunkTree = Integer.parseInt(scanner.nextLine());

        System.out.println("\n¿Quieres añadir una estrella (@) en la copa del árbol? (s/n)");
        boolean starTree = scanner.nextLine().equalsIgnoreCase("s");

        System.out.println("\n¿Quieres añadir la decoración (o) al árbol? (s/n)");
        boolean  ballsTree = scanner.nextLine().equalsIgnoreCase("s");

        System.out.println("\n¿Quieres añadir las luces (+) al árbol? (s/n)");
        boolean  lightTree = scanner.nextLine().equalsIgnoreCase("s");

        System.out.println("\n¿Has sido bueno durante este años? (s/n)");
        boolean presentTrunk = scanner.nextLine().equalsIgnoreCase("s");

        // tree
        for (int rows =0; rows < heightTree; rows++){
            for(int space =0;space < (heightTree-rows-1);space++){
                System.out.print(" ");
            }

            if(rows ==0 && starTree){
                System.out.print("\u001B[33m@");
            }else{
                for(int asterisk =0;asterisk<(rows*2)+1;asterisk++){
                    String symbol = "\u001b[32m*";
                    if(lightTree && asterisk %2 == 0 && random.nextBoolean()){
                        symbol = "\u001B[31mo";
                    }
                    if(ballsTree && asterisk %2 == 1 && random.nextBoolean()){
                        symbol = "\u001B[34m+";
                    }
                    System.out.print(symbol);
                }
            }
            System.out.println(" ");

        }

        //trunk
        for (int base= 0; base <trunkTree;base++){
            for(int space = 0;space<(heightTree-2);space++){
                System.out.print(" ");
            }
            for(int tronco=0;tronco<3;tronco++){
                System.out.print("|");
            }
            System.out.println(" ");
        }

        // presents
        if(presentTrunk){
            for (int base= 0; base <heightTree;base++){
                System.out.print("\u001B[35m[ ]");
            }
        }else{
            System.out.print(" ");
        }
        scanner.close();

    }
}