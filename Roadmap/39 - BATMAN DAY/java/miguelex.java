import java.time.LocalDate;
import java.time.temporal.TemporalAdjusters;
import java.time.DayOfWeek;
import java.util.Random;

public class miguelex {
    
    // RETO 1: Cálculo de Batman Day hasta su 100 aniversario
    public static void calcularBatmanDay(int anioInicio, int anioFinal) {
        System.out.println("Fechas del Batman Day hasta su 100 aniversario:");
        for (int anio = anioInicio; anio <= anioFinal; anio++) {
            LocalDate tercerSabado = LocalDate.of(anio, 9, 1)
                    .with(TemporalAdjusters.dayOfWeekInMonth(3, DayOfWeek.SATURDAY));
            System.out.println("Batman Day en el año " + anio + ": " + tercerSabado);
        }
    }
    
    // RETO 2: Sistema de seguridad de la Batcueva
    public static void activarSistemaSeguridad(int[][] sensores) {
        int tamanoMapa = 20;
        int umbralSeguridad = 20;
        int mejorSumaAmenazas = 0;
        int[] mejorCentro = null;

        for (int i = 0; i <= tamanoMapa - 3; i++) {
            for (int j = 0; j <= tamanoMapa - 3; j++) {
                int sumaAmenazas = 0;
                for (int x = i; x < i + 3; x++) {
                    for (int y = j; y < j + 3; y++) {
                        sumaAmenazas += sensores[x][y];
                    }
                }
                if (sumaAmenazas > mejorSumaAmenazas) {
                    mejorSumaAmenazas = sumaAmenazas;
                    mejorCentro = new int[]{i + 1, j + 1};
                }
            }
        }
        if (mejorCentro != null) {
            int distanciaABatcueva = Math.abs(mejorCentro[0]) + Math.abs(mejorCentro[1]);
            System.out.println("\nArea más amenazada en coordenadas (" + mejorCentro[0] + ", " + mejorCentro[1] + ")");
            System.out.println("Suma de amenazas: " + mejorSumaAmenazas);
            System.out.println("Distancia a la Batcueva: " + distanciaABatcueva);

            if (mejorSumaAmenazas > umbralSeguridad) {
                System.out.println("¡Protocolo de seguridad activado!");
            } else {
                System.out.println("Protocolo de seguridad NO activado.");
            }
        }
    }

    public static void main(String[] args) {
        // Ejecutar el reto 1
        int anioInicio = 2024;
        int anioFinal = 2024 + (100 - 85);
        calcularBatmanDay(anioInicio, anioFinal);

        // Ejecutar el reto 2
        Random random = new Random();
        int[][] sensores = new int[20][20];
        for (int i = 0; i < 20; i++) {
            for (int j = 0; j < 20; j++) {
                sensores[i][j] = random.nextInt(11);
            }
        }
        activarSistemaSeguridad(sensores);
    }
}
