public class mariovelascodev {
    //Variable Global
    static String miVariableGlobal = "Hola Mundo";//Accesible desde cualquier lugar de la clase

    public static void main(String[] args) {
       funcionSinArgumentos();
       funcionConArgumentos("Mario");
       funcionConArgumentos("Sandra", 37);
       System.out.println(funcionConRetorno());
       System.out.println(funcionConRetorno(17));
       miFuncion();
       miFuncion("Javier");

       //Llamamos a la variable global
       mariovelascodev.miVariableGlobal = "Hola    ";
       System.out.println("El valor de la variable global ahora es: "+miVariableGlobal);

       //Funciones del lenguaje
       //Métodos String
       System.out.println(miVariableGlobal.length()); //Cuenta el número de caracteres de la cadena de texto
       System.out.println(miVariableGlobal.toLowerCase());//Pone la cadena de texto en minusculas
       System.out.println(miVariableGlobal.toUpperCase());//Pone la cadena de texto en mayusculas
       System.out.println(miVariableGlobal.trim());//Quita los espacios en blanco de ambos lados

       //EXTRA
       int counter = miFuncion("Fizz", "Buzz");
       System.out.println("El número de veces que no se ha impreso texto es: "+counter);

    }

    //Función sin argumentos ni retorno
    public static void funcionSinArgumentos(){
        System.out.println("Esta es una función sin parametros ni argumentos");
    };

    //Función con argumentos sin retorno
    public static void funcionConArgumentos(String name){
        System.out.println("Hola me llamo "+name);
    }

    public static void funcionConArgumentos(String name, int age){
        System.out.println("Hola me llamo "+name+" y tengo "+age+" años");
    }

    //Función sin argumentos con retorno
    public static String funcionConRetorno(){
        return "Función con retorno sin argumentos";
    }

    //Función con argumentos y con retorno
    public static boolean funcionConRetorno(int age){
        return age >= 18; //Si se cumple la condición muestra true si no false
    }

    //Función dentro de función
    public static void miFuncion(){
        String miVariableLocal = "Hola Java";
        System.out.println("La variable global contiene: "+mariovelascodev.miVariableGlobal+"\nLa variable local contiene: "
                +miVariableLocal);//La variable local no se puede utilizar fuera del ámbito de la funcion
        funcionSinArgumentos();
    }

    public static void miFuncion(String name){
        funcionConArgumentos(name);
    }

    //EXTRA
    public static int miFuncion(String param1, String param2){
        int contador = 0;

        for(int i=1; i < 100; i++){
            if (i % 3 == 0 && i % 5 == 0) {
                System.out.println(param1+ " "+param2);
            }
            else if(i % 3 == 0){
                System.out.println(param1);
            } else if (i % 5 == 0) {
                System.out.println(param2);
            } else {
                System.out.println(i);
                contador++;
            }
        }
        return contador;
    }
}
