import java.text.SimpleDateFormat;
import java.time.Duration;
import java.time.LocalTime;
import java.util.Date;
import java.util.HashSet;
import java.util.Set;
import java.util.logging.ConsoleHandler;
import java.util.logging.Formatter;
import java.util.logging.Handler;
import java.util.logging.Level;
import java.util.logging.LogRecord;
import java.util.logging.Logger;

public class danhingar {
    private final static Logger log = Logger.getLogger(danhingar.class.getName());

    public static void main(String[] args) {

        configLog();

        log.info("LOG INFO");
        log.warning("LOG WARNING");
        log.severe("LOG SEVERE");
        log.config("LOG CONFIG");
        log.fine("LOG FINE");
        log.finest("LOG FINEST");
        log.finer("LOG FINER");

        TaskManager taskManager = new TaskManager();
        taskManager.listTasks();
        taskManager.addTask("Pan", "Comprar 5 barras de pan");
        taskManager.addTask("Python", "Estudiar Python");
        taskManager.listTasks();
        taskManager.deleteTask("Python");
        taskManager.listTasks();
        taskManager.addTask("Pan", "Comprar 5 barras de pan");
        taskManager.deleteTask("Python");
        taskManager.addTask("Task1", "Busqueda");
    }

    static void configLog() {

        ConsoleHandler consoleHandler = new ConsoleHandler();
        consoleHandler.setLevel(Level.ALL);

        consoleHandler.setFormatter(new CustomFormatter());

        log.addHandler(consoleHandler);

        log.setLevel(Level.ALL);

        // Eliminando los handler existentes
        Logger parentLogger = log.getParent();
        for (Handler handler : parentLogger.getHandlers()) {
            parentLogger.removeHandler(handler);
        }

    }

}

class CustomFormatter extends Formatter {
    @Override
    public String format(LogRecord record) {
        // Formato personalizado: timestamp - level - mensaje
        String timestamp = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss").format(new Date(record.getMillis()));
        String level = record.getLevel().getName();
        String message = formatMessage(record);

        return String.format("%s - %s - %s%n", timestamp, level, message);
    }
}

// EXTRA
class TaskManager {

    private final static Logger log = Logger.getLogger(danhingar.class.getName());

    private Set<Task> tasks;

    public TaskManager() {
        tasks = new HashSet<>();
    }

    public void addTask(String name, String description) {
        LocalTime start = LocalTime.now();
        if (tasks.stream().anyMatch(t -> t.getName().equals(name))) {
            log.warning(String.format("Se ha intentado añadir una tarea que ya existe: %s", name));
        }
        Task task = new Task(name, description);
        tasks.add(task);
        log.info(String.format("Tarea añadida: %s", name));
        log.fine(String.format("Número de tareas: %d", tasks.size()));
        LocalTime end = LocalTime.now();
        printTime(start, end);
    }

    public void listTasks() {
        LocalTime start = LocalTime.now();
        if (tasks.size() > 0) {
            log.info("Se va a imprimir el listado de tareas");
            for (Task task : tasks) {
                System.out.println(task.toString());
            }
        } else {
            log.info("No hay tareas para mostrar.");
        }
        LocalTime end = LocalTime.now();
        printTime(start, end);

    }

    public void deleteTask(String name) {
        LocalTime start = LocalTime.now();
        if (!tasks.stream().anyMatch(t -> t.getName().equals(name))) {
            log.warning(String.format("Se ha intentado eliminar una tarea que no existe:", name));
        } else {
            tasks.remove(tasks.stream().filter(t -> t.getName().equals(name)).findFirst().get());
            log.info(String.format("Se ha eliminado la tarea: %s", name));
            log.fine(String.format("Número de tareas: %d", tasks.size()));
        }
        LocalTime end = LocalTime.now();
        printTime(start, end);

    }

    private void printTime(LocalTime start, LocalTime end) {
        float time = (float) Duration.between(start, end).toNanos()/1000000000;
        log.finest(String.format("Tiempo de ejecución: %.6f", time));
    }

    static void configLog() {

        ConsoleHandler consoleHandler = new ConsoleHandler();
        consoleHandler.setLevel(Level.ALL);

        consoleHandler.setFormatter(new CustomFormatter());

        log.addHandler(consoleHandler);

        log.setLevel(Level.ALL);

        // Eliminando los handler existentes
        Logger parentLogger = log.getParent();
        for (Handler handler : parentLogger.getHandlers()) {
            parentLogger.removeHandler(handler);
        }

    }
}

class Task {
    private String name;
    private String description;

    public Task(String name, String description) {
        this.name = name;
        this.description = description;
    }

    @Override
    public String toString() {
        return "Task [name=" + name + ", description=" + description + "]";
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

}
