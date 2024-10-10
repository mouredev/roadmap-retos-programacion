import java.util.Arrays;
import java.util.Scanner;

public class Main {

    private static final String EMPTY = "⬜";
    private static final String BARRIER = "⬛";
    private static final String MICKEY = "\uD83D\uDC2D";
    private static final String EXIT = "\uD83D\uDEAA";
    private static String[][] board = {
            {MICKEY, EMPTY, EMPTY, EMPTY, EMPTY, BARRIER},
            {EMPTY, BARRIER, EMPTY, EMPTY, BARRIER, EMPTY},
            {EMPTY, BARRIER, EMPTY, BARRIER, EMPTY, EMPTY},
            {EMPTY, EMPTY, EMPTY, EMPTY, BARRIER, EMPTY},
            {BARRIER, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY},
            {EMPTY, BARRIER, EMPTY, EMPTY, EMPTY, EXIT}
    };

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Welcome to the maze game! Find the exit to help Mickey Mouse escape!");
        System.out.println("Movements available: W (up), A (left), S (down), D (right)");
        System.out.println("Write 'exit' to quit the game");
        System.out.println("Good luck!");
        System.out.println("Where do you want to move?");

        String input = "";

        while (!input.equalsIgnoreCase("exit")) {
            printBoard();
            input = sc.nextLine();
            if (move(input)) break;
        }
    }

    private static boolean move(String direction) {
        int[] mickeyPosition = findMickey();
        int x = mickeyPosition[0];
        int y = mickeyPosition[1];

        if (x == board.length - 1 && y == board[0].length - 1) {
            System.out.println("Congratulations! You helped Mickey Mouse escape!");
            return true;
        }

        switch (direction) {
            case "W":
                if (x > 0 && !board[x - 1][y].equals(BARRIER)) {
                    board[x][y] = EMPTY;
                    board[x - 1][y] = MICKEY;
                }
                break;
            case "A":
                if (y > 0 && !board[x][y - 1].equals(BARRIER)) {
                    board[x][y] = EMPTY;
                    board[x][y - 1] = MICKEY;
                }
                break;
            case "S":
                if (x < board.length - 1 && !board[x + 1][y].equals(BARRIER)) {
                    board[x][y] = EMPTY;
                    board[x + 1][y] = MICKEY;
                }
                break;
            case "D":
                if (y < board[0].length - 1 && !board[x][y + 1].equals(BARRIER)) {
                    board[x][y] = EMPTY;
                    board[x][y + 1] = MICKEY;
                }
                break;
            case "EXIT":
                System.out.println("Thanks for playing!");
                break;
            default:
                System.out.println("Invalid input. Please try again.");
        }

        return false;
    }

    private static int[] findMickey() {
        int[] mickeyPosition = new int[2];

        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                if (board[i][j].equals(MICKEY)) {
                    mickeyPosition[0] = i;
                    mickeyPosition[1] = j;
                    break;
                }
            }
        }

        return mickeyPosition;
    }

    static void printBoard() {
        for (String[] strings : board) {
            System.out.println(Arrays.toString(strings));
        }
    }
}
