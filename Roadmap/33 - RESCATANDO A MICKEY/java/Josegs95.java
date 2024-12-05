import java.util.Scanner;

public class Josegs95 {
    public static void main(String[] args) {
        new Josegs95().rescueMickey();
    }

    private String[][] maze;
    private int mickeyYCoord = 4;
    private int mickeyXCoord = 0;

    final private Scanner sc = new Scanner(System.in);

    public void rescueMickey(){
        maze = initMaze();

        try(sc){
            boolean exit = false;
            while(!exit){
                printMaze();
                String direction = askDirection();
                switch (direction){
                    case "arriba":
                        exit = moveMickey(-1, 0);
                        break;
                    case "abajo":
                        exit = moveMickey(1, 0);
                        break;
                    case "derecha":
                        exit = moveMickey(0, 1);
                        break;
                    case "izquierda":
                        exit = moveMickey(0, -1);
                        break;
                }
                System.out.println();
            }
            printMaze();
        }
    }

    private String[][] initMaze(){
        String[][] maze = {
                {" ", " ", " ", " ", " ", " "},
                {" ", "X", " ", " ", "X", " "},
                {" ", " ", "X", " ", "X", " "},
                {"X", " ", "X", " ", "X", " "},
                {"M", " ", "X", "X", "X", " "},
                {"X", "X", "S", " ", " ", " "}
        };

        return maze;
    }

    private String askDirection(){
        while (true){
            System.out.print("¿A dónde se quiere desplazar (arriba/abajo/izquierda/derecha)?: ");
            String input = sc.nextLine().strip().toLowerCase();
            switch (input){
                case "arriba":
                case "abajo":
                case "derecha":
                case "izquierda":
                    return input;
                default:
                    System.out.println("Opción no válida");
            }
        }
    }

    public boolean moveMickey(int iChange, int jChange){
        if (iChange != 0){
            if (iChange > 0){
                if (mickeyYCoord == maze.length - 1){
                    System.out.println("No se puede bajar más");
                    return false;
                }
            }else{
                if (mickeyYCoord == 0){
                    System.out.println("No se puede subir más");
                    return false;
                }
            }
        } else{
            if (jChange > 0){
                if (mickeyXCoord == maze[0].length - 1){
                    System.out.println("No se puede ir más a la derecha");
                    return false;
                }
            }else{
                if (mickeyXCoord == 0){
                    System.out.println("No se puede ir más a la izquierda");
                    return false;
                }
            }
        }

        if(maze[mickeyYCoord + iChange][mickeyXCoord + jChange].equals("X")){
            System.out.println("Camino bloqueado, no se puede pasar.");
            return false;
        }
        if (maze[mickeyYCoord + iChange][mickeyXCoord + jChange].equals("S")) {
            maze[mickeyYCoord][mickeyXCoord] = " ";
            maze[mickeyYCoord + iChange][mickeyXCoord + jChange] = "M";
            System.out.println("¡Felicidades, has llegado a la salida!");
            return true;
        }

        maze[mickeyYCoord][mickeyXCoord] = " ";
        maze[mickeyYCoord + iChange][mickeyXCoord + jChange] = "M";
        mickeyYCoord += iChange;
        mickeyXCoord += jChange;

        return false;
    }

    private void printMaze(){
        for (int i = 0; i < maze.length; i++){
            for (int j = 0; j < maze[0].length; j++)
                System.out.print("[" + maze[i][j] + "]");
            System.out.println();
        }
    }
}
