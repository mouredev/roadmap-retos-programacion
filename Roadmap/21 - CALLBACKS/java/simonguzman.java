public class simonguzman {
    public static void main(String[] args) {
        callbackExample();
    }

    public static void callbackExample(){
        System.out.println("Iniciando el programa...");
        Processor processor = new Processor();
        processor.process(message -> System.out.println("Callback recibido: " + message));
        System.out.println("Programa finalizado.");
    }

    public static interface Callback{
        void execute(String message);
    }

    public static class Processor{
        public void process(Callback callback){
            System.out.println("Procesando...");
            try {
                Thread.sleep(2000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            callback.execute("Proceso completo");
        }
    }
}
