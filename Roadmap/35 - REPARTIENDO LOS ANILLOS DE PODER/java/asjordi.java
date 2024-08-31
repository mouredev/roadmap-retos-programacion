public class Main {

    public static void main(String[] args) {
        int totalRings = 10;
        distribuirAnillos(totalRings);
    }

    public static void distribuirAnillos(int totalAnillos) {
        if (totalAnillos < 4) {
            System.out.println("Error: Se necesitan al menos 4 anillos para distribuir.");
            return;
        }

        int anillosSauron = 1;
        int anillosRestantes = totalAnillos - anillosSauron;

        for (int anillosElfos = 1; anillosElfos < anillosRestantes; anillosElfos += 2) {
            for (int anillosEnanos = 2; anillosEnanos < anillosRestantes - anillosElfos; anillosEnanos++) {
                if (esPrimo(anillosEnanos)) {
                    int anillosHombres = anillosRestantes - anillosElfos - anillosEnanos;
                    if (anillosHombres % 2 == 0) {
                        System.out.println("Reparto exitoso:");
                        System.out.println("Elfos: " + anillosElfos);
                        System.out.println("Enanos: " + anillosEnanos);
                        System.out.println("Hombres: " + anillosHombres);
                        System.out.println("Sauron: " + anillosSauron);
                        return;
                    }
                }
            }
        }

        System.out.println("Error: No se pudo encontrar una distribución válida para " + totalAnillos + " anillos.");
    }

    private static boolean esPrimo(int number) {
        if (number <= 1) return false;
        if (number <= 3) return true;
        if (number % 2 == 0 || number % 3 == 0) return false;
        for (int i = 5; i * i <= number; i += 6) {
            if (number % i == 0 || number % (i + 2) == 0) return false;
        }
        return true;
    }

}
