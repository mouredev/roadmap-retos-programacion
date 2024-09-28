import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class simonguzman {

    private static ExecutorService executor = Executors.newFixedThreadPool(3);

    public  static void main(String[] args) {
        executeThreads();
    }

    public static void executeThreads(){
        CompletableFuture<Void> futureC = executeAsync("C", 3);
        CompletableFuture<Void> futureB = executeAsync("B", 2);
        CompletableFuture<Void> futureA = executeAsync("A", 1);

        CompletableFuture.allOf(futureC, futureB, futureA).thenRun(()->{
            executeAsync("D", 1);
        }).thenRun(()->{
            executor.shutdown();
        });
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
