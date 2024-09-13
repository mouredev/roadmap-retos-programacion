
import java.util.logging.ConsoleHandler;
import java.util.logging.Level;
import java.util.logging.Logger;

public class simonguzman{
    public static void main(String[] args) {
        //sintaxisLogger();
        exampleLog();
    }

    /************************ ejemplo del log************************/
    public static void exampleLog(){
        Logger logger = Logger.getLogger(simonguzman.class.getName());
        logger.setLevel(Level.ALL);

        // Configuracion del handler para que se acepten todos los niveles
        ConsoleHandler handler = new ConsoleHandler();
        handler.setLevel(Level.ALL);
        logger.addHandler(handler);

        logger.info("Inicio del programa.");
        logger.config("Configuracion de la aplicacion completada.");

        try {
            int result = split(10, 2, logger);
            logger.info("Resultado de la division: "+result);

            result = split(10, 0, logger);
            logger.info("Resultado de la segunda division: "+result);

        } catch (ArithmeticException e) {
            logger.severe("ERROR: Division por cero..."+e.getMessage());
        }

        logger.fine("Operaciones menores completadas.");
        logger.finer("Nivel de depuracion mas detallado");
        logger.finest("Nivel de depuracion mas minucioso");
        logger.warning("Advertencia: fin del programa");
    }
    
    public static int split(int num1, int num2, Logger logger){
        logger.fine("Dividiendo "+num1+" entre "+num2);
        return num1 / num2;
    }


    /************************ Sintaxis del log************************/
    static void sintaxisLogger(){
        //Creacion del logger
        Logger logger = Logger.getLogger(simonguzman.class.getName());
        //Habilitar todos los niveles de registro
        logger.setLevel(Level.ALL);
        logger.severe("Mensaje de nivel SEVERE");
        logger.warning("Mensaje de nivel WARNING");
        logger.info("Mensaje de nivel INFO");
        logger.config("Mensaje de nivel CONFIG");
        logger.fine("Mensaje de nivel FINE");
        logger.finer("Mensaje de nivel FINER");
        logger.finest("Mensaje de nivel FINEST");
    }
}