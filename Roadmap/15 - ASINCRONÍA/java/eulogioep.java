import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

public class eulogioep {
    
    /**
     * Método principal que demuestra el uso de asincronía en Java
     */
    public static void main(String[] args) {
        // Demostración básica
        System.out.println("=== Demostración Básica ===");
        ejecutarTareaAsincrona("TareaEjemplo", 2);
        
        // Para asegurar que la demostración básica termine antes de la extra
        try {
            Thread.sleep(3000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        
        // Dificultad Extra
        System.out.println("\n=== Dificultad Extra ===");
        dificultadExtra();
    }
    
    /**
     * Ejecuta una tarea asíncrona con un nombre y duración especificados
     * @param nombre Nombre de la tarea
     * @param segundos Duración de la tarea en segundos
     * @return CompletableFuture<Void> que representa la tarea asíncrona
     */
    public static CompletableFuture<Void> ejecutarTareaAsincrona(String nombre, int segundos) {
        return CompletableFuture.runAsync(() -> {
            try {
                System.out.println(nombre + " - Iniciando...");
                System.out.println(nombre + " - Durará " + segundos + " segundos");
                Thread.sleep(segundos * 1000);
                System.out.println(nombre + " - Finalizada");
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        });
    }
    
    /**
     * Implementación de la dificultad extra
     * Ejecuta las tareas C, B y A en paralelo y luego D cuando las anteriores terminan
     */
    public static void dificultadExtra() {
        // Crear un ExecutorService para manejar los hilos
        ExecutorService executor = Executors.newFixedThreadPool(3);
        
        // Crear las tareas asíncronas
        CompletableFuture<Void> tareaC = ejecutarTareaAsincrona("Tarea C", 3);
        CompletableFuture<Void> tareaB = ejecutarTareaAsincrona("Tarea B", 2);
        CompletableFuture<Void> tareaA = ejecutarTareaAsincrona("Tarea A", 1);
        
        // Esperar a que todas las tareas terminen y luego ejecutar D
        CompletableFuture.allOf(tareaC, tareaB, tareaA)
            .thenRun(() -> ejecutarTareaAsincrona("Tarea D", 1));
        
        // Esperar a que todo termine antes de cerrar el programa
        try {
            executor.shutdown();
            executor.awaitTermination(10, TimeUnit.SECONDS);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}