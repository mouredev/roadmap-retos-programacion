import java.util.Scanner;

public class miguelex {

    private static final int GRID_WIDTH = 4;
    private static final int GRID_HEIGHT = 3;
    private static final int DAYS = 24;
    private static boolean[] discovered = new boolean[DAYS];

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        while (true) {
            drawCalendar();

            System.out.print("\nSeleccione un día (1-" + DAYS + ") para descubrir o escriba 0 para salir: ");
            String input = scanner.nextLine();

            if (input.equals("0")) {
                System.out.println("¡Gracias por participar en el aDEViento!");
                break;
            }

            try {
                int day = Integer.parseInt(input);
                if (day < 1 || day > DAYS) {
                    System.out.println("Por favor, elija un número válido entre 1 y " + DAYS + ".");
                } else if (discovered[day - 1]) {
                    System.out.println("El día " + day + " ya ha sido descubierto.");
                } else {
                    discovered[day - 1] = true;
                    System.out.println("¡Has descubierto el día " + day + "!");
                }
            } catch (NumberFormatException e) {
                System.out.println("Entrada inválida. Por favor, ingrese un número válido.");
            }
        }

        scanner.close();
    }

    private static void drawCalendar() {
        for (int row = 0; row < Math.ceil(DAYS / 6.0); row++) {
            for (int line = 0; line < GRID_HEIGHT; line++) {
                StringBuilder rowOutput = new StringBuilder();

                for (int col = 0; col < 6; col++) {
                    int day = row * 6 + col + 1;
                    if (day > DAYS) break;

                    switch (line) {
                        case 0, 2 -> rowOutput.append("**** ");
                        case 1 -> {
                            rowOutput.append("*");
                            if (discovered[day - 1]) {
                                rowOutput.append("**");
                            } else {
                                String dayStr = String.format("%02d", day);
                                rowOutput.append(dayStr);
                            }
                            rowOutput.append("* ");
                        }
                    }
                }
                System.out.println(rowOutput);
            }
        }
    }
}
