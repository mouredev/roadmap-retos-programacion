public class nwpablodeveloper {

    String nameGlobal = "Pabloasdfasdfsadf";

    public static void main(String[] args) {

        // Función para limpiar la consola "No tiene retorno"
        clearConsole();
        
        // Función que genera un titulo para la consola
        title("Esta función maqueta un titulo para la consola");
        lineSalt(); // Función para hacer un salto de linea en la consola

        //Función que recibe varios parametros
        title("Funcion que recibe varios parametros");
        withParams("Pablo", 35, 100.20);

        
        // Función que recibe parametros y retorna un valor.
        title("Funcion que imprime los parametros enviados");
        String resp = withParams("Pablo", 35, 100.20);
        System.out.println(resp);

        title("Funcione que retona null");
        String res = returnNull("Pablo");
        System.out.println(res);

        title("Funcione que retona null");
        System.out.println(res);

        title("Funcion que retorna una suma");
        int numbers[] = { 4 , 3, 3};
        int sum = calculateSum( numbers);
        System.out.println(sum);

        title("Funcion dentro de funcion");


    }




    static int calculateSum(int... numbers){

        int sum = 0;
        for(int num : numbers){
            sum += num;
        } 

        return sum;
    }

    static String returnNull(String variable){
        return null;
    }

    static String withParams(String name, int age, double salary) {
        // Función Estandar de Java para pasar de tipo Double a String
        return "Soy " + name + " tengo " + age + " y cobro: " + salary + " el segundo";
    }


    // La sigtuiente función como no tiene ningun retorno usamos "void"
    public static void title(String titulo) {
        System.out.println("==========================================================================");
        System.out.println( titulo );
        System.out.println("----------------------------------------------");
    }
    
    
    // La sig. función como no tiene ningun retorno usamos "void"
    public static void clearConsole(){
        // Esta función hace ejecuta el siguiente codigo para limpiar la consola
        System.out.print("\033[H\033[2J");  
        System.out.flush();  
    }

    public static void lineSalt(){
        System.out.println("\n");
    }
}
