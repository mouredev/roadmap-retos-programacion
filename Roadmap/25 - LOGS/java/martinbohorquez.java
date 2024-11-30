import java.time.Duration;
import java.time.LocalTime;
import java.util.LinkedList;
import java.util.List;
import java.util.logging.*;

public class martinbohorquez {
    private static final Logger logger = Logger.getLogger(martinbohorquez.class.getName());

    public static void main(String[] args) {
        loggerLevel();
        /*
         * DIFICULTAD EXTRA
         */
        Task task1 = new Task("tarea 1", "Diseño de BBDD");
        Task task2 = new Task("tarea 2", "Desarrollo de API");
        Task task4 = new Task("tarea 2", "Conexión a la BBDD");
        Task task3 = new Task("tarea 3", "Despliegue en AWS");

        TaskManager tm = new TaskManager();
        tm.listTask();
        tm.addTask(task1)
                .addTask(task2)
                .addTask(task4)
                .addTask(task3);
        tm.listTask();
        tm.deleteTask("tarea 2");
        tm.listTask();
        tm.deleteTask("tarea 2");
        tm.listTask();


    }

    private static void loggerLevel() {
        // Eliminar manejadores predeterminados
        for (Handler handler : logger.getHandlers()) {
            logger.removeHandler(handler);
        }
        // Configuración del logger
        ConsoleHandler consoleHandler = new ConsoleHandler();
        consoleHandler.setLevel(Level.ALL);
        consoleHandler.setFormatter(new SimpleFormatter() {
            @Override
            public synchronized String format(LogRecord lr) {
                return String.format("%1$tF %1$tT - %2$s - %3$s%n", lr.getMillis(), lr.getLevel(), lr.getMessage());
            }
        });
        logger.addHandler(consoleHandler);
        logger.setLevel(Level.ALL);

        // Eliminar manejadores de loggers padres
        Logger parentLogger = logger.getParent();
        for (Handler handler : parentLogger.getHandlers()) {
            parentLogger.removeHandler(handler);
        }

        // Mensajes de log
        logger.fine("Esto es un mensaje de FINE");
        logger.finer("Esto es un mensaje de FINER");
        logger.finest("Esto es un mensaje de FINEST");
        logger.config("Esto es un mensaje de CONFIG");
        logger.info("Esto es un mensaje de INFO");
        logger.warning("Esto es un mensaje de WARNING");
        logger.severe("Esto es un mensaje de SEVERE");
        logger.log(Level.OFF, "Esto es un mensaje de OFF");
    }

    private record Task(String name, String description) {

        @Override
        public String toString() {
            return "Task{name='" + name + "', description='" + description + "'}";
        }
    }

    private static class TaskManager {
        private final List<Task> taskSet;

        public TaskManager() {
            this.taskSet = new LinkedList<>();
        }

        private TaskManager addTask(Task task) {
            List<String> taskNames = taskSet.stream().map(Task::name).toList();
            LocalTime startTime = LocalTime.now();
            if (!taskNames.contains(task.name())) {
                taskSet.add(task);
                logger.info("Tarea añadida: " + task);
            } else logger.warning("Se ha intentado añadir una tarea que ya existe!");
            logger.fine("Número de tareas: " + taskSet.size());
            LocalTime endtTime = LocalTime.now();
            printExecutionTime(startTime, endtTime);
            return this;
        }

        private void deleteTask(String name) {
            List<String> taskNames = taskSet.stream().map(Task::name).toList();
            LocalTime startTime = LocalTime.now();
            if (taskNames.contains(name)) {
                this.taskSet.removeIf(t -> t.name().equals(name));
                logger.info("Tarea eliminada: " + name);
            } else logger.severe("Se ha intentado eliminar una tarea que no existe: " + name);
            logger.fine("Número de tareas: " + taskSet.size());
            LocalTime endtTime = LocalTime.now();
            printExecutionTime(startTime, endtTime);
        }

        private void listTask() {
            LocalTime startTime = LocalTime.now();
            if (!taskSet.isEmpty()) {
                logger.info("Se va imprimir la lista de tareas.");
                this.taskSet.forEach(System.out::println);
            } else logger.warning("No hay tareas para mostrar!");
            LocalTime endtTime = LocalTime.now();
            printExecutionTime(startTime, endtTime);
        }

        private void printExecutionTime(LocalTime startTime, LocalTime endtTime) {
            float time = (float) Duration.between(startTime, endtTime).toNanos() / (1000 * 1000);
            System.out.printf("El tiempo de ejecución es: %.3f%n", time);
        }
    }
}
