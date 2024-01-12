public class nwpablodeveloper {

    public static void main(String[] args) {

        clearConsole();
        
        title("Manejo de Funciones con Java");
        System.out.println("");
        
        title("Funcion que imprime los parametros enviados");
        params("Pablo", 35, 100.20);
        System.out.println("");

        title("Funcione que retona null");
        String res = returnNull("Pablo");
        System.out.println(res);
        System.out.println("");

        title("Funcione que retona null");
        System.out.println(res);
        System.out.println("");

    }

    

    static String returnNull(String variable){
        return null;
    }

    static void params(String name, int age, double salary) {
        System.out.println("Soy " + name + " tengo " + age + " y cobro € " + salary + " el segundo");
    }


    public static void title(String titulo) {
        System.out.println("==========================================================================");
        System.out.println( titulo );
        System.out.println("----------------------------------------------");
    }


    public static void clearConsole(){
        // Esta función hace ejecuta el siguiente codigo para limpiar la consola
        System.out.print("\033[H\033[2J");  
        System.out.flush();  
    }
}
