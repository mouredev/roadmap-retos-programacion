import java.util.HashMap;
import java.util.Map;
import java.util.Random;
import java.util.logging.ConsoleHandler;
import java.util.logging.Handler;
import java.util.logging.Level;
import java.util.logging.Logger;

public class Josegs95 {
    private static final Logger logger = Logger.getLogger(Josegs95.class.getName());

    public static void main(String[] args) {
        //Ejercicio
        //Desactivo el uso de los handlers por defecto para que no salga duplicado
        //los mensajes por consola
        logger.setUseParentHandlers(false);

        Handler consoleHandler = new ConsoleHandler();
        logger.setLevel(Level.ALL); //Le digo que maneje todos los tipos de mensajes
        consoleHandler.setLevel(Level.ALL); //Idem, pero en concreto al handler que muestra por consola
        logger.addHandler(consoleHandler);

//        System.out.println("Tipos de mensaje 'logging' de mas leve a mas grave:");
//        logger.finest("Mensaje Finest");
//        logger.finer("Mensaje Finer");
//        logger.fine("Mensaje Fine");
//        logger.config("Mensaje Config");
//        logger.info("Mensaje Info");
//        logger.warning("Mensaje Warning");
//        logger.severe("Mensaje Severe");

        //Reto
        retoFinal();
    }

    private static Random rnd;
    private static Map<String, String> taskMap;

    public static void retoFinal(){
        rnd = new Random();
        taskMap = new HashMap<>();

        addTask("Limpiar", "Limpiar la casa");
        addTask("Cocinar", "Preparar el almuerzo");
        addTask("Comprar", "Comprar lo que haga falta");
        addTask("Lavadora", "Hacer una lavadora");

        showTasks();

        deleteTask("Afeitarse");
        deleteTask("Comprar");

        showTasks();
    }

    private static void addTask(String name, String description){
        long start = System.currentTimeMillis();
        try{
            Thread.sleep(rnd.nextInt(3) * 1000);
            taskMap.put(name, description);
            logger.fine("Tarea " + name + " añadida correctamente.");
        } catch (InterruptedException e) {
            logger.warning(e.getMessage());
        }
        long end = System.currentTimeMillis();
        logger.finest(String.format("Tiempo de ejecución %.4fs.", (end - start) / 1000.0));
    }

    private static void deleteTask(String name){
        long start = System.currentTimeMillis();
        try{
            Thread.sleep(rnd.nextInt(3) * 1000);
            if (taskMap.get(name) == null){
                logger.info("No se ha borrado la tarea " + name + " porque no existe en el registro");
                return;
            }
            taskMap.remove(name);
            logger.fine("Tarea " + name + " añadida correctamente.");
        } catch (InterruptedException e) {
            logger.warning(e.getMessage());
        }
        long end = System.currentTimeMillis();
        logger.finest(String.format("Tiempo de ejecución %.4fs.", (end - start) / 1000.0));
    }

    private static void showTasks(){
        long start = System.currentTimeMillis();
        if (taskMap.size() == 0){
            logger.info("El registro de tareas está vacío");
            return;
        }
        try{
            Thread.sleep(rnd.nextInt(3) * 1000);
            for(Map.Entry<String, String> entry : taskMap.entrySet())
                System.out.println("Tarea: " + entry.getKey() + ", " + entry.getValue());
        } catch (InterruptedException e) {
            logger.warning(e.getMessage());
        }
        long end = System.currentTimeMillis();
        logger.finest(String.format("Tiempo de ejecución %.4fs.", (end - start) / 1000.0));
    }
}
