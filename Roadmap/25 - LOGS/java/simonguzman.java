
import java.util.ArrayList;
import java.util.InputMismatchException;
import java.util.List;
import java.util.Scanner;
import java.util.concurrent.TimeUnit;
import java.util.logging.ConsoleHandler;
import java.util.logging.Level;
import java.util.logging.Logger;

public class simonguzman{
    public static void main(String[] args) {
        sintaxisLogger();
        exampleLog();
        advancedLoggingExample();
        adittionalExercise();
    }
    /************************ ejercicio adicional************************/
    public static void adittionalExercise(){
        List<Task> tasks = new ArrayList<>();
        Logger logger = Logger.getLogger(simonguzman.class.getName());
        Scanner sc = new Scanner(System.in);
        int option = 0;
        do{
            menu();
            System.out.println("Ingrese una opcion");
            try {
                option = sc.nextInt();
                sc.nextLine();
                optionsMenu(option, sc, tasks, logger);
            } catch (InputMismatchException e) {
                System.out.println("ERROR: Entrada invalida, solo ingresar valores numericos");
                sc.next();
            }
        }while(option != 4);    
        sc.close();
    }

    public static void optionsMenu(int option, Scanner sc, List<Task> tasks, Logger logger){
        
        switch (option) {
            case 1:
                addTaskMenu(sc, tasks, logger);
                break;
            case 2:
                removeTaskMenu(sc, tasks, logger);
                break;
            case 3:
                listTasks(tasks, logger);
                break;
            case 4:
                outSystem();
                break;
            default:
                System.out.println("ERROR: Opcion no valida...");
        }
    }

    public static void outSystem(){
        System.out.println("Saliendo....");
    }

    public static void menu(){
        System.out.println("------------Gestion de tareas------------");
        System.out.println("1. Añadir tarea");
        System.out.println("2. Eliminar tarea");
        System.out.println("3. Listar tareas");
        System.out.println("4. Salir");
    }

    public static void addTaskMenu(Scanner sc, List<Task> tasks, Logger logger){
        System.out.print("Introduce el nombre de la tarea: ");
        String name = sc.next();
        System.out.print("Introduce la descripción de la tarea: ");
        String description = sc.next();
        addTask(name, description, tasks, logger);
    }

    public static void removeTaskMenu(Scanner sc, List<Task> tasks, Logger logger){
        System.out.println("Introduce el nombre de la tarea a eliminar: ");
        String name = sc.next();
        removeTask(name, tasks, logger);
    }

    public static void addTask(String name, String description, List<Task> tasks, Logger logger){
        long startTime = System.currentTimeMillis();
        Task task = new Task(name, description);
        tasks.add(task);
        logger.info("Tarea añadida: "+task.getName()+ ", Description: "+task.getDescription());
        long endTime = System.currentTimeMillis();
        logger.info("Tiempo de ejecucion para añadir la tarea: "+(endTime - startTime));
    }

    public static  void removeTask(String name, List<Task> tasks, Logger logger){
        long startTime = System.currentTimeMillis();
        boolean removed = tasks.removeIf(task -> task.getName().equalsIgnoreCase(name));
        if(removed){
            logger.info("Tarea eliminada: "+name);
        }else{
            logger.warning("No se encontro la tarea con nombre: "+name);
        }
        long endTime = System.currentTimeMillis();
        logger.info("Tiempo de ejecucion para eliminar la tarea: "+(endTime - startTime)+ " ms");
    }

    public static void listTasks(List<Task> tasks, Logger logger) {
        long startTime = System.currentTimeMillis();
        if(tasks.isEmpty()){
            logger.warning("No hay tareas para listar.");
        }else{
            logger.info("Listado de tareas: ");
            tasks.forEach(task -> logger.info(task.toString()));
        }
        long endTime = System.currentTimeMillis();
        logger.info("Tiempo de ejecucion para listar tareas " +(endTime - startTime)+ " ms");
    }

    static class Task{
        private String name;
        private String description;

        public Task(){

        }

        public Task(String name, String description){
            this.name = name;
            this.description = description;
        }

        public String getName() {
            return name;
        }

        public String getDescription() {
            return description;
        }

        @Override
        public String toString() {
            return "Tarea: "+ name +", Descripcion: "+description;
        }
        
    }
    /************************ ejemplo del log mas avanzado************************/
    public static void advancedLoggingExample(){
        Logger logger = Logger.getLogger(simonguzman.class.getName());
        logger.setLevel(Level.ALL);
        try {
            startTask("Tarea 1");
            TimeUnit.SECONDS.sleep(2);
            endTask("Tarea 1");
            
            startTask("Tarea 2");
            TimeUnit.SECONDS.sleep(1);
            endTask("Tarea 2");
        } catch (InterruptedException e) {
            logger.severe("Error en la ejecucion de las tareas..."+e.getMessage());
        }
    }

    public static void startTask(String taskName){
        System.out.println("Iniciando "+taskName);
    }

    public static void endTask(String taskName){
        System.out.println("Finalizando "+taskName);
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