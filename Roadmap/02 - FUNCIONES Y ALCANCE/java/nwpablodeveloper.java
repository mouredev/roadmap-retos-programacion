public class nwpablodeveloper {

    String nameGlobal = "Pabloasdfasdfsadf";

    public static void main(String[] args) {

        // Función para limpiar la consola "No tiene retorno"
        clearConsole();
        
        // Función que genera un titulo para la consola
        title("1. Esta función maqueta un titulo para la consola");
        lineSalt(); // Función para hacer un salto de linea en la consola

        //Función que recibe varios parametros
        title("2. Funcion que recibe varios parametros");
        withParams("Pablo", 35, 100.20);
        lineSalt();

        
        // Función que recibe parametros y retorna un valor.
        title("3. Funcion que imprime los parametros enviados");
        String resp = withParamsAndReturn( "Pablo", 6, 7, 7);
        System.out.println(resp);
        lineSalt();

    }

    static String withParamsAndReturn(String name, int... numbers){

        int sum = 0;
        for(int i = 0; i < numbers.length; i++){
            sum += numbers[i]; 
        }

        int otraSuma = 0;
        for(int num : numbers ){
            otraSuma += num;
        }
        return "Nombre: " + name + " \nNumeros: "+  sum + "\nOtra suma: " + otraSuma;
    }


    static int calculateSum(int... numbers){

        int sum = 0;
        for(int num : numbers){
            sum += num;
        } 

        return sum;
    }


    static void withParams(String name, int age, double salary) {
        System.out.println( "Soy " + name + " tengo " + age + " y cobro: " + salary + " el segundo");
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
