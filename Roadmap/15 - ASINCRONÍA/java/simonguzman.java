import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class simonguzman {

    private static ExecutorService executor = Executors.newFixedThreadPool(3);

    public  static void main(String[] args) {
        CompletableFuture<Void> future = executeAsync("test", 2);

        executor.shutdown();

    }
    public static CompletableFuture<Void> executeAsync(String name, int durationSeconds){
        return CompletableFuture.runAsync(() -> {
            long startTime = System.currentTimeMillis();   
            System.out.println(name + " started at "+ startTime);
            System.out.println(name + " will take "+durationSeconds+" seconds to complete");
            try {
                Thread.sleep(durationSeconds * 1000);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
            long endTime = System.currentTimeMillis();
            long difference = endTime - startTime;
            System.out.println(name + " finished at "+endTime);
            System.out.println(name + " took "+difference+ " milliseconds to complete"); 
            }, executor);
     }  
}
