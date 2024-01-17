class JerrySantana {
    public static String variable = "Esto es una variable global.";
    
    public static void main(String[] args) {
        funcionSimple();
        funcionUnParametro("Hola mundo");
        funcionVariosParametros("Hola mundo", 10, 1.5f, 'g', false);
        System.out.println(funcionRetorno());
        System.out.println(funcionParametrosRetorno("Hola mundo", 10, 1.5f, 'g', false));
        funcionAnidada();
        funcionesLenguaje();
        variablesLocalGlobal();
        funcionExtra("Lorem", "Ipsum");
    }
    
    static void funcionSimple() {
        System.out.println("Esto es una funcion sencilla, no recibe parametros ni retorna ningun valor.");
        System.out.println("Solamente ejecuta el codigo dentro de ella.");
        System.out.println("----------------------------------------------------------------------------");
    }
    
    static void funcionUnParametro(String parametro) {
        System.out.println("Esta es una funcion que recibe solamente un parametro.");
        System.out.println("El parametro en este caso es solamente un objeto de tipo String (cadena de caracteres).");
        System.out.println("Este es el valor del parametro recibido: '" + parametro + "'.");
        System.out.println("Este parametro es una variable local, y solamente existe durante la ejecución de la función, una vez que finaliza desaparece.");
        System.out.println("----------------------------------------------------------------------------");
    }
    
    static void funcionVariosParametros(String parametro, int numero, float decimal, char caracter, boolean bool) {
        System.out.println("Esta es una funcion que recibe varios parametros, todos son diferentes.");
        System.out.println("Recibimos un parametro de tipo String, otro de tipo short, uno de tipo float, uno de tipo char y uno de tipo booleano.");
        System.out.println("El valor del parametro String es: '" + parametro + "'.");
        System.out.println("El valor del parametro int es: '" + numero + "'.");
        System.out.println("El valor del parametro float es: '" + decimal + "'.");
        System.out.println("El valor del parametro char es: '" + caracter + "'.");
        System.out.println("El valor del parametro booleano es: '" + bool + "'.");
        System.out.println("Estos parametros son variables locales, solamente existen durante la ejecución de la función, una vez que finaliza desaparecen.");
        System.out.println("----------------------------------------------------------------------------");
    }
    
    static String funcionRetorno() {
        return "Esta es una funcion que retorna un valor, el valor de retorno puede ser de cualquier tipo y depende del tipo de retorno asignado a la funcion.\n" +
                "Este valor retornado puede ser el contenido de una variable o un valor especifico. A pesar de eso, las variables creadas y retornadas dentro \n" +
                "de esta funcion, son variables locales, ya que su valor es reasignado a otra variable antes de desaparecer al finalizar la ejecucion.\n" +
                "Las funciones en Java solamente pueden retornar un solo valor de un solo tipo.\n" +
                "----------------------------------------------------------------------------";
    }
    
    static String funcionParametrosRetorno(String parametro, int numero, float decimal, char caracter, boolean bool) {
        return "Se pueden hacer combinaciones de las anteriores, como una funcion que reciba uno o mas parametros y retorno un valor.\n" +
                "En este caso la funcion recibe un parametro de tipo String, otro de tipo int, uno de tipo float, uno de tipo char y uno de tipo booleano.\n" +
                "Los parametros son los siguientes:\n String: '" + parametro + "'\nint: '" + numero + "'\nfloat: '" + decimal + "'\nchar: '" + caracter +"'\nbooleano: '" + bool + "'.\n" +
                "----------------------------------------------------------------------------";
    }
    
    static void funcionAnidada() {
        Anidada.anidada(() -> {
            System.out.println("Inicio funcion lambda...\n" +
                    "Las funciones lambda o expresiones lambda son funciones anonimas. Pueden recibir uno o mas parametros dentro de ellas y retornar un valor.\n" +
                    "Al ser declaradas al mismo tiempo de ser usadas, puede acceder a las variables locales del ambito al que pertenece pero sin poder modificarlas.\n" +
                    "Esta es una forma de declarar funciones dentro de otra funcion.\n" +
                    "Fin funcion lambda...\n");
        });
        System.out.println("----------------------------------------------------------------------------");
    }
    
    static void funcionesLenguaje() {
        System.out.println("La funcion 'System.out.prinln()' es una función que recibe como parametros un valor y lo imprime en terminal. Esta es una funcion propia del lenguaje.");
        int[] numeros = {9, 6, 3, 2, 4};
        System.out.println("La funcion length es propia del lenguaje y nos permite conocer el numero de elementos dentro de un arreglo. En este caso nuestro arreglo es: {9, 6, 3, 2, 4}, y su longitud es: " + numeros.length + ".");
        System.out.println("----------------------------------------------------------------------------");
    }
    
    static void variablesLocalGlobal() {
        String variable = "Esto es una varible local.";
        System.out.println("Las variables globales son accesibles desde cualquier parte del programa, y duran mientras el programa se ejecute.");
        System.out.println("Las variables locales son accesibles solamente dentro de la funcion o clase donde son declaradas, y solamente duran hasta que ya no son utilizadas por la funcion o clase que las llama.");
        System.out.println("Este es el valor de la variable global: " + JerrySantana.variable);
        System.out.println("Este es el valor de la variable local: " + variable);
        System.out.println("----------------------------------------------------------------------------");
    }
    
    interface Lambda {
        void lambda();
    }
    
    class Anidada {
        public static void anidada(Lambda funcion) {
            funcion.lambda();
        }
    }
    
    static int funcionExtra(String cadenaUno, String cadenaDos) {
        int contador = 0;
        
        for(int i = 0; i < 101; i++) {
            if (i % 3 == 0 && i % 5 == 0) {
                System.out.println(cadenaUno + " " + cadenaDos + ".");
            } else if(i % 3 == 0) {
                System.out.println(cadenaUno);
            } else if(i % 5 == 0) {
                System.out.println(cadenaDos);
            } else {
                System.out.println(i);
                contador++;
            }
        }
        
        return contador;
    }
}
