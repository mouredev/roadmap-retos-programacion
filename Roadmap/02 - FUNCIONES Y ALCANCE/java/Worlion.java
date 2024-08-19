import java.util.logging.ConsoleHandler;
import java.util.logging.LogRecord;
import java.util.logging.Logger;
import java.util.logging.SimpleFormatter;

public class Worlion {
    private static Logger log = Logger.getLogger(Worlion.class.getName());
    static {
        log.setUseParentHandlers(false);
        ConsoleHandler consoleHandler = new ConsoleHandler();
        consoleHandler.setFormatter(new SimpleFormatter() {
            @Override
            public String format(LogRecord record) {
                return record.getMessage() + "\n";
            }
        });
        log.addHandler(consoleHandler);
    }

    /*
    * EJERCICIO: FUNCIONES Y ALCANCE
    */


    public static void main(String[] args) {
        log.info(" \nFUNCIONES Y ALCANCE:\n");

        funcionSinRetornoNiParametro();
        funcionConUnParametro("con un parámetro");
        funcionConVariosParametros("con varios", "parámetros");
        log.info("Funcion con retorno: " + funcionConRetorno());
        funcionConFuncion();
        funcionesDeJava();
        variableLocal();


        log.info(" \n ---- 🌩 DIFICULTAD EXTRA 🌩 ----\n");
        log.info("Ejercicio Extra: " + extra("chori", "pan"));

    }

    private static void funcionSinRetornoNiParametro(){
        log.info("Funcion sin retorno ni parametro: sólo hace este print");
    }

    private static void funcionConUnParametro(String parametro){
        log.info("Funcion con un parametro: " + parametro);
    }

    private static void funcionConVariosParametros(String parametro1, String parametro2){
        log.info("Funcion con varios parametros: " + parametro1 + " " + parametro2);
    }

    private static String funcionConRetorno(){
        return "Funcion con retorno: devuelve este texto";
    }

    private static void funcionConFuncion(){
        class InnerClass {
            public static void innerMethod() {
                log.info("Este es un método interno.");
            }
        }
        log.info("Esto es, hasta donde yo sé, lo más parecido a definir funciones dentro de funciones.");
        InnerClass.innerMethod();
    }

    private static void funcionesDeJava() {
        log.info("Funciones de Java: Math.random() = " + Math.random());
        log.info("Funciones de Java: Math.min(5, 10) = " + Math.min(5, 10));
    }

    private static String variableGlobal = "Soy una variable global";

    private static void variableLocal() {
        String variableLocal = "Soy una variable local";
        log.info(variableGlobal);
        log.info(variableLocal);
    }


    /*
    * DIFICULTAD EXTRA (opcional):
    * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
    * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
    *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
    *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
    *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
    *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
    *
    * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
    * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
    */
    private static int extra(String str1, String str2){
        int count = 0;
        for(int i = 1; i <= 100; i++){
            if(i % 3 == 0 && i % 5 == 0){
                log.info(str1 + str2);
            } else if(i % 3 == 0){
                log.info(str1);
            } else if(i % 5 == 0){
                log.info(str2);
            } else {
                log.info(String.valueOf(i));
                count ++;
            }
        }
        return count;
    }


}
