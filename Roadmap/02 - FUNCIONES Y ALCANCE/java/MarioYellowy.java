import java.util.Arrays;

public class MarioYellowy {
    public static void main(String[] args) {
        greeting();
        System.out.println(farewell());
        System.out.println(call("Mario"));
        System.out.println(sum(25,26));
        play();
        play("Belen", "Ignacio", "Xochitl");
        dance("Mauricio", "Jessica", "Yuridia");
        meet();

        //Funciones del lenguaje
        System.out.println("Hello from building function");
        showGlobal();
        excercise("Dios", "Plan");
    }

    //Funcion sin argumento ni tipo de retorno
    private static void greeting() {
        System.out.println("Hello from Mario Yellowy!");
    }

    //Funcion si argumento pero con retorno
    private static String farewell() {
        String message = "Vay vay From Mario Yellowy";
        return message;
    }

    //Con un argumento y retorno
    private static String call(String name) {
        name = name.toUpperCase();
        String message = "Calling to " + name;
        return message;
    }

    //Varios argumentos
    private static int sum(int a, int b) {
        return a + b;
    }

    //En Java no se le puede asignar un valor por defecto a los parametros
    //Lo que se puede hacer en este caso, es usar la "Sobrecarga de metodos"
    //De igual manera que gardamos el valor por defecto podemos combinar la funcion con
    //que no se sabe el numero de argumentos que recibira

    private static void play(){  //Si no le pasa ningun argumento por defecto jugara
        play("Juan");    //con Juan
    }
    private static void play(String... names) {
        System.out.println(STR."Tu/s companhero para jugar es: \{Arrays.toString(names)}");
    }

    //Funcion con argumentos variables
    private static void dance(String... names) {
        System.out.println(STR."Las personas que van a bailar son: \{Arrays.toString(names)}");
    }

    //Funcion dentro de funcion
    private static void meet() {
        System.out.println("The person in the meeting is:");
        getName("Joaquin");
    }
    public static void getName(String name) {
        System.out.println(name);
    }

    //Variables locales y globales
    //Para este punto todas las variables que he creado dentro de las funciones
    //se quedan dentro de las funciones pero si quiero llamarlas desde otro lado
    //no es posible
    //si quiero usar una variable global tengo que declararla afuera de las funciones

    static String globalVariable = "Cualquier funcion puede usarla";

    private static void showGlobal() {
        System.out.println(globalVariable);
    }

    /*
    * Extra
    * */

    private static void excercise(String first, String second) {
        int firstTimes = 0;
        int secondTimes = 0;
        int bothTimes = 0;
        int numberTimes = 0;
        for (int i = 1; i <= 100; i++) {
            if(i % 3 == 0 && i % 5 == 0 ) {
                bothTimes++;
            } else if (i % 3 == 0) {
                firstTimes++;
            } else if (i % 5 == 0) {
                secondTimes++;
            } else {
                numberTimes++;
            }
        }
        System.out.println(firstTimes);
        System.out.println(secondTimes);
        System.out.println(bothTimes);
        System.out.println(numberTimes);
    }
}
