public class h4ckxel{

public static void main(String[] args) {
    try {
        exercise();
        extra();

    } catch (Exception e) {
        System.out.println(e.getMessage());
    }
}

private static Thread asynFunction(String funcitonName, int duration) {
    return new Thread(() -> {

    long startTime = System.currentTimeMillis();
    System.out.println(
        funcitonName + " started. Time: " + startTime +
              " milliseconds. Should take " + duration * 1000 + " milliseconds.");
    try {
        Thread.sleep((long) duration * 1000);
    } catch (InterruptedException e) {
        System.out.println(e.getMessage());
    }

    long endTime = System.currentTimeMillis();
    System.out.println(funcitonName + " has done. Time: " + (endTime - startTime) + " milliseconds");

    });
}

private static void exercise() {
    System.out.println("EXERCISE:");
    Thread thread = asynFunction("my function1", 20);
    thread.start();
    try {

    thread.join();
    } catch (InterruptedException e) {
    e.printStackTrace();
    }

}

private static void extra() {

    System.out.println();
    System.out.println("EXTRA:");

    Thread threadA = asynFunction("Function A", 1);
    Thread threadB = asynFunction("Function B", 2);
    Thread threadC = asynFunction("Function C", 3);
    Thread threadD = asynFunction("Function D", 1);

    try {
    threadA.start();
    threadB.start();
    threadC.start();

    threadA.join(5000);
    threadB.join(5000);
    threadC.join(5000);

    System.out.println("Starting Function D...");
    threadD.start();
    threadD.join();

    } catch (InterruptedException e) {
    System.out.println(e.getMessage());
    }

    }
}
