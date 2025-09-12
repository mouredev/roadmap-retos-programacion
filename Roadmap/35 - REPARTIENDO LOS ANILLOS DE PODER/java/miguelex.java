import java.util.Scanner;

public class miguelex {
    
    public static boolean esPrimo(int num) {
        if (num <= 1) return false;
        if (num == 2) return true;
        if (num % 2 == 0) return false;
        
        for (int i = 3; i <= Math.sqrt(num); i += 2) {
            if (num % i == 0) return false;
        }
        return true;
    }

    public static String repartirAnillos(int totalAnillos) {
        if (totalAnillos < 4) {
            return "Error: No hay suficientes anillos para cumplir con los requisitos.";
        }

        int anillosSauron = 1;
        totalAnillos -= 1;
        
        int mejorDiferencia = Integer.MAX_VALUE;
        int[] mejorReparto = null;
        
        for (int anillosElfos = 1; anillosElfos <= totalAnillos; anillosElfos += 2) {
            for (int anillosEnanos = 2; anillosEnanos <= totalAnillos; anillosEnanos++) {
                if (esPrimo(anillosEnanos)) {
                    int anillosHombres = totalAnillos - anillosElfos - anillosEnanos;
                    
                    if (anillosHombres > 0 && anillosHombres % 2 == 0) {
                        int diferencia = Math.max(anillosElfos, Math.max(anillosEnanos, anillosHombres)) - Math.min(anillosElfos, Math.min(anillosEnanos, anillosHombres));
                        
                        if (diferencia < mejorDiferencia) {
                            mejorDiferencia = diferencia;
                            mejorReparto = new int[]{ anillosElfos, anillosEnanos, anillosHombres, anillosSauron };
                        }
                    }
                }
            }
        }
        
        if (mejorReparto != null) {
            return String.format("Reparto exitoso: Elfos = %d, Enanos = %d, Hombres = %d, Sauron = %d", mejorReparto[0], mejorReparto[1], mejorReparto[2], mejorReparto[3]);
        } else {
            return "Error: No se encontró una combinación válida para repartir los anillos.";
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Ingresa el número total de anillos: ");
        int totalAnillos = scanner.nextInt();
        
        String resultado = repartirAnillos(totalAnillos);
        System.out.println(resultado);
    }
}
