package com.amsoft.roadmap.example33;

public class Example33 {
    private static final String EMPTY = "⬜";
    private static final String BARRIER = "⬛";
    private static final String EXIT = "🚪";
    private static final String PLAYER = "🐭";
    private static final int ROWS = 6;
    private static final int COLUMNS = 6;
    private static String[][] map = new String[ROWS][COLUMNS];


    public static void main(String[] args) {
        initializeMap();
        int[] playerPosition = {0, 0};
        movePlayer(playerPosition, playerPosition);
        while (true) {
            var scanner = new java.util.Scanner(System.in);
            System.out.println("Enter the direction: ");
            System.out.println("[w]: up, [s]: down, [a]: left, [d]: right or [q]: quit");
            System.out.print("Press a key: ");
            String direction = scanner.nextLine();
            int[] newPosition;
            switch (direction) {
                case "w":
                    newPosition = new int[]{playerPosition[0] - 1, playerPosition[1]};
                    if (movePlayer(playerPosition, newPosition)) {
                        playerPosition = newPosition;
                    }
                    break;
                case "s":
                    newPosition = new int[]{playerPosition[0] + 1, playerPosition[1]};
                    if (movePlayer(playerPosition, newPosition)) {
                        playerPosition = newPosition;
                    }
                    break;
                case "a":
                    newPosition = new int[]{playerPosition[0], playerPosition[1] - 1};
                    if (movePlayer(playerPosition, newPosition)) {
                        playerPosition = newPosition;
                    }
                    break;
                case "d":
                    newPosition = new int[]{playerPosition[0], playerPosition[1] + 1};
                    if (movePlayer(playerPosition, newPosition)) {
                        playerPosition = newPosition;
                    }
                    break;
                case "q":
                    System.out.println("Bye!");
                    System.exit(0);
                default:
                    System.out.println("Invalid direction");
                    break;
            }
        }
    }

    private static boolean movePlayer(int[] currentPosition, int[] newPosition) {
        if (newPosition[0] < 0 || newPosition[0] >= ROWS || newPosition[1] < 0 || newPosition[1] >= COLUMNS) {
            throw new IllegalArgumentException("Invalid player position");
        }

        if (map[newPosition[0]][newPosition[1]].equals(EXIT)) {
            System.out.println("You won!");
            System.exit(0);
        }

        if (map[newPosition[0]][newPosition[1]].equals(BARRIER)) {
            System.out.println("You can't move there");
            return false;
        }

        map[currentPosition[0]][currentPosition[1]] = EMPTY;
        map[newPosition[0]][newPosition[1]] = PLAYER;


        for (int i = 0; i < ROWS; i++) {
            var row = map[i];
            for (int j = 0; j < COLUMNS; j++) {
                System.out.print(row[j] + " ");
            }
            System.out.println();
        }
        return true;
    }

    public static void initializeMap() {
        map = new String[][]{
                {PLAYER, BARRIER, EMPTY, EMPTY, BARRIER, BARRIER},
                {EMPTY, EMPTY, EMPTY, BARRIER, EMPTY, BARRIER},
                {BARRIER, EMPTY, EMPTY, BARRIER, EMPTY, BARRIER},
                {BARRIER, BARRIER, EMPTY, BARRIER, EMPTY, BARRIER},
                {BARRIER, EMPTY, EMPTY, EMPTY, EMPTY, BARRIER},
                {BARRIER, BARRIER, BARRIER, BARRIER, EXIT, BARRIER}
        };
    }
}
