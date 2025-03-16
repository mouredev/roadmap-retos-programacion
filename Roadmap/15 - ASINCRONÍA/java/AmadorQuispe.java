/* ╔══════════════════════════════════════╗
   ║ Autor:  Amador Q                     ║
   ║ Web  : https://amsoft.dev            ║
   ║ 2024                                 ║
   ╚══════════════════════════════════════╝
*/


public class Main {
    public static void main(String[] args) throws InterruptedException {
        Thread functionX = createAsyncFunction("Funcion X", 4);
        Thread functionA = createAsyncFunction("Funcion A", 1);
        Thread functionB = createAsyncFunction("Funcion B", 2);
        Thread functionC = createAsyncFunction("Funcion C", 3);
        Thread functionD = createAsyncFunction("Funcion D", 1);
        // Inicia la ejecución de las tres funciones
        functionX.start();
        functionC.start();
        functionB.start();
        functionA.start();
        // Espera que se ejecuten (join)
        functionC.join();
        functionB.join();
        functionA.join();

        System.out.println("Regresamos a main para continuar");
        // Iniciamos la función D se aseguró que las funciones A,B,C ya terminaaron
        functionD.start();
    }

    public static Thread createAsyncFunction(String functionName, int secondsToRun) {
        return new Thread(() -> {
            System.out.println(functionName + " empezó.");
            long startTime = System.currentTimeMillis();
            try {
                Thread.sleep(secondsToRun * 1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }

            long endTime = System.currentTimeMillis();
            System.out.println(functionName + " duró " + secondsToRun + " segundos.");
            System.out.println(functionName + " finalizó. Tiempo total: " + (endTime - startTime) + " milisegundos.");
        });
    }
}
