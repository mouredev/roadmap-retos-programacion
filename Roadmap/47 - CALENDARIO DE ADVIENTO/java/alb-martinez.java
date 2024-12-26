import java.util.Scanner;

public class alb-martinez {

    private static final int TOTAL_DAYS = 24;
    private static final int ROWS = 4;
    private static final int COLS = 6;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Inicialización de los días (false = cerrado; true = abierto)
        boolean[] openDays = new boolean[TOTAL_DAYS];

        // Mostrar calendario inicial
        showCalendar(openDays);

        // Código para permitir al usuario seleccionar un día
        while (true) {
            int selectedDay = getUserSelection(scanner);

            if (selectedDay == 0) {
                break;
            }

            handleDaySelection(openDays, selectedDay);

            showCalendar(openDays);

        }
    }

    // Solicita y devuelve la selección del usuario
    private static int getUserSelection(Scanner scanner) {
        int selectedDay;

        while (true) {
            System.out.println("Selecciona un día (1-24) para abrir, o 0 para salir:");

            // Verificar si el input es un número
            if (scanner.hasNextInt()) {
                selectedDay = scanner.nextInt();
                // Validar que el número esté en el rango permitido
                if (selectedDay >= 0 && selectedDay <= TOTAL_DAYS) {
                    break;
                } else {
                    System.out.println("¡Entrada inválida! Ingresa un número entre 1 y 24, o 0 para salir.");
                }
            } else {
                // Si el input no es un número, lo ignoramos y pedimos uno nuevo
                System.out.println("¡Entrada inválida! Debes ingresar un número.");
                scanner.next();
            }
        }

        return selectedDay;
    }

    // Maneja la selección de un día
    private static void handleDaySelection(boolean[] openDays, int selectedDay) {
        // Comprobar si el día ya está abierto
        if (openDays[selectedDay - 1]) {
            System.out.println("¡Este día ya está abierto!");
        } else {
            openDays[selectedDay - 1] = true;
            System.out.println("¡Has abierto el día " + selectedDay + "!");
        }
    }

    // Método para mostrar el calendario
    private static void showCalendar(boolean[] openDays) {
        for (int row = 0; row < ROWS; row++) {
            printGridBorders();
            printDaysInRow(row, openDays);
            printGridBorders();
        }
    }

    // Imprimir los bordes de la cuadrícula (superior e inferior)
    private static void printGridBorders() {
        for (int col = 0; col < COLS; col++) {
            System.out.print("**** ");
        }
        System.out.println();
    }

    // Imprimir los días en una fila
    private static void printDaysInRow(int row, boolean[] openDays) {
        for (int col = 0; col < COLS; col++) {
            int dayIndex = row * COLS + col;
            if (dayIndex >= TOTAL_DAYS) break;

            // Si el día está abierto, mostramos "****", de lo contrario el número del día
            if (openDays[dayIndex]) {
                System.out.print("**** ");
            } else {
                System.out.print("*" + (dayIndex + 1 < 10 ? "0" + (dayIndex + 1) : (dayIndex + 1)) + "* ");
            }
        }
        System.out.println();
    }
}
