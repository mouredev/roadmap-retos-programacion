import java.time.LocalTime;
import java.util.concurrent.CompletableFuture;

public class AnaLauDB {

    // Función asíncrona parametrizable
    public static CompletableFuture<Void> tareaAsync(String nombre, int segundos) {
        return CompletableFuture.runAsync(() -> {
            System.out.println("[" + LocalTime.now() + "] " + nombre + " inicia. Duración: " + segundos + " segundos.");
            try {
                Thread.sleep(segundos * 1000L);
            } catch (InterruptedException e) {
                System.out.println(nombre + " fue interrumpida.");
            }
            System.out.println("[" + LocalTime.now() + "] " + nombre + " finaliza.");
        });
    }

    public static void main(String[] args) {
        // DIFICULTAD EXTRA
        // C (3s), B (2s), A (1s) en paralelo, luego D (1s) cuando todas acaben

        CompletableFuture<Void> tareaC = tareaAsync("Función C", 3);
        CompletableFuture<Void> tareaB = tareaAsync("Función B", 2);
        CompletableFuture<Void> tareaA = tareaAsync("Función A", 1);

        // Cuando C, B y A terminen, ejecutar D
        CompletableFuture<Void> todas = CompletableFuture.allOf(tareaC, tareaB, tareaA)
                .thenRun(() -> {
                    tareaAsync("Función D", 1).join();
                });

        // Esperar a que todo termine antes de salir
        todas.join();
        System.out.println("Programa finalizado.");
    }
}
