
import java.util.logging.Level;
import java.util.logging.Logger;

public class simonguzman{
    public static void main(String[] args) {
        sintaxisLogger();
    }
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