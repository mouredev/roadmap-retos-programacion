import java.util.Scanner;

public class Main {

    private static final int FILAS = 4;
    private static final int COLUMNAS = 6;
    private static final int DIAS = 24;
    private boolean[] descubiertos = new boolean[DIAS];

    public static void main(String[] args) {
        Main m = new Main();
        Scanner sc = new Scanner(System.in);

        while (true) {
            m.dibujarCalendario();
            System.out.print("Selecciona un día para descubrir (1-24) o 0 para salir: ");
            int dia = sc.nextInt();
            if (dia == 0) break;
            m.seleccionarDia(dia);
        }

        sc.close();
    }

    public void dibujarCalendario() {
        for (int i = 0; i < FILAS; i++) {
            for (int j = 0; j < COLUMNAS; j++) {
                int dia = i * COLUMNAS + j + 1;
                if (dia > DIAS) break;
                System.out.print("**** ");
            }
            System.out.println();
            for (int j = 0; j < COLUMNAS; j++) {
                int dia = i * COLUMNAS + j + 1;
                if (dia > DIAS) break;
                if (descubiertos[dia - 1]) {
                    System.out.print("**** ");
                } else {
                    System.out.printf("*%02d* ", dia);
                }
            }
            System.out.println();
            for (int j = 0; j < COLUMNAS; j++) {
                int dia = i * COLUMNAS + j + 1;
                if (dia > DIAS) break;
                System.out.print("**** ");
            }
            System.out.println();
            System.out.println();
        }
    }

    public void seleccionarDia(int dia) {
        if (dia < 1 || dia > DIAS) {
            System.out.println("Día inválido.");
            return;
        }
        if (descubiertos[dia - 1]) {
            System.out.println("El día " + dia + " ya ha sido descubierto.");
        } else {
            descubiertos[dia - 1] = true;
            System.out.println("Has descubierto el día " + dia + "!");
        }
    }
}
