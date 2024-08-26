import java.util.Scanner;

public class MohamedElderkaoui{
        public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Ingresa el número total de anillos: ");
        int totalAnillos = scanner.nextInt();

        // Sauron siempre recibe 1 anillo, descontamos eso.
        int anillosRestantes = totalAnillos - 1;

        if (anillosRestantes <= 0) {
            System.out.println("Error: No hay suficientes anillos para repartir.");
            return;
        }

        boolean encontrado = false;

        // Iteramos para encontrar los valores correctos.
        for (int elfos = 1; elfos < anillosRestantes; elfos += 2) {  // Impar
            for (int enanos = 2; enanos < anillosRestantes; enanos++) {  // Primos
                if (esPrimo(enanos)) {
                    int hombres = anillosRestantes - elfos - enanos;
                    if (hombres > 0 && hombres % 2 == 0) {  // Par
                        System.out.println("Reparto encontrado:");
                        System.out.println("Elfos: " + elfos);
                        System.out.println("Enanos: " + enanos);
                        System.out.println("Hombres: " + hombres);
                        System.out.println("Sauron: 1");
                        encontrado = true;
                        break;
                    }
                }
            }
            if (encontrado) break;
        }

        if (!encontrado) {
            System.out.println("No   encontró un reparto válido para el número de anillos dado.");
        }

        scanner.close();
    }

    // Método para verificar si un número es primo
    private static boolean esPrimo(int numero) {
        if (numero < 2) return false;
        for (int i = 2; i <= Math.sqrt(numero); i++) {
            if (numero % i != 0) return false;
        }
        return true;
    }
}