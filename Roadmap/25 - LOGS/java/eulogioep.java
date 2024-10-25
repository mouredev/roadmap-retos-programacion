/**
 * Implementación de un sistema de logging y gestión de tareas en Java.
 * 
 * TEORÍA SOBRE LOGGING EN JAVA:
 * Java proporciona un framework de logging nativo (java.util.logging) que ofrece:
 * - Diferentes niveles de severidad (SEVERE, WARNING, INFO, etc.)
 * - Capacidad de escribir en múltiples destinos (consola, archivo)
 * - Formato personalizable de mensajes
 * - Filtros y handlers configurables
 * 
 * Niveles de logging en java.util.logging:
 * - SEVERE: Para errores críticos
 * - WARNING: Para advertencias
 * - INFO: Para información general
 * - CONFIG: Para mensajes de configuración
 * - FINE, FINER, FINEST: Para depuración con diferentes niveles de detalle
 */

 import java.io.IOException;
 import java.time.LocalDateTime;
 import java.time.format.DateTimeFormatter;
 import java.util.ArrayList;
 import java.util.List;
 import java.util.logging.*;
 import java.util.stream.Collectors;
 
 public class eulogioep {
     /**
      * Clase para manejar el logging personalizado
      */
     static class CustomLogger {
         private static final Logger LOGGER = Logger.getLogger(CustomLogger.class.getName());
         
         static {
             try {
                 // Configurar el logger para escribir en un archivo
                 FileHandler fileHandler = new FileHandler("tareas.log", true);
                 fileHandler.setFormatter(new SimpleFormatter());
                 LOGGER.addHandler(fileHandler);
                 
                 // Configurar el logger para escribir en consola
                 ConsoleHandler consoleHandler = new ConsoleHandler();
                 consoleHandler.setFormatter(new SimpleFormatter());
                 LOGGER.addHandler(consoleHandler);
                 
                 // Establecer el nivel de logging
                 LOGGER.setLevel(Level.ALL);
             } catch (IOException e) {
                 e.printStackTrace();
             }
         }
         
         public static void severe(String message) {
             LOGGER.severe(formatMessage(message));
         }
         
         public static void warning(String message) {
             LOGGER.warning(formatMessage(message));
         }
         
         public static void info(String message) {
             LOGGER.info(formatMessage(message));
         }
         
         public static void config(String message) {
             LOGGER.config(formatMessage(message));
         }
         
         public static void fine(String message) {
             LOGGER.fine(formatMessage(message));
         }
         
         private static String formatMessage(String message) {
             return String.format("[%s] %s",
                 LocalDateTime.now().format(DateTimeFormatter.ISO_LOCAL_DATE_TIME),
                 message);
         }
     }
     
     /**
      * Clase que representa una tarea
      */
     static class Task {
         private final String name;
         private final String description;
         private final LocalDateTime createdAt;
         
         public Task(String name, String description) {
             this.name = name;
             this.description = description;
             this.createdAt = LocalDateTime.now();
         }
         
         public String getName() {
             return name;
         }
         
         public String getDescription() {
             return description;
         }
         
         public LocalDateTime getCreatedAt() {
             return createdAt;
         }
         
         @Override
         public String toString() {
             return String.format("Tarea: %s - %s (Creada: %s)",
                 name,
                 description,
                 createdAt.format(DateTimeFormatter.ISO_LOCAL_DATE_TIME));
         }
     }
     
     /**
      * Clase para la gestión de tareas
      */
     static class TaskManager {
         private final List<Task> tasks;
         
         public TaskManager() {
             this.tasks = new ArrayList<>();
         }
         
         /**
          * Mide el tiempo de ejecución de una operación
          */
         private void measureExecutionTime(Runnable operation, String operationName) {
             long startTime = System.nanoTime();
             try {
                 operation.run();
                 long endTime = System.nanoTime();
                 double executionTime = (endTime - startTime) / 1_000_000.0; // Convertir a millisegundos
                 CustomLogger.fine(String.format("Tiempo de ejecución %s: %.2fms", 
                     operationName, executionTime));
             } catch (Exception e) {
                 CustomLogger.severe(String.format("Error en %s: %s", 
                     operationName, e.getMessage()));
             }
         }
         
         /**
          * Añade una nueva tarea
          */
         public void addTask(String name, String description) {
             measureExecutionTime(() -> {
                 // Verificar si ya existe una tarea con el mismo nombre
                 if (tasks.stream().anyMatch(t -> t.getName().equals(name))) {
                     CustomLogger.warning(String.format("La tarea '%s' ya existe", name));
                     return;
                 }
                 
                 Task task = new Task(name, description);
                 tasks.add(task);
                 CustomLogger.info(String.format("Tarea '%s' añadida exitosamente", name));
             }, "addTask");
         }
         
         /**
          * Elimina una tarea por su nombre
          */
         public void removeTask(String name) {
             measureExecutionTime(() -> {
                 int initialSize = tasks.size();
                 tasks.removeIf(task -> task.getName().equals(name));
                 
                 if (tasks.size() == initialSize) {
                     CustomLogger.warning(String.format("No se encontró la tarea '%s'", name));
                 } else {
                     CustomLogger.info(String.format("Tarea '%s' eliminada exitosamente", name));
                 }
             }, "removeTask");
         }
         
         /**
          * Lista todas las tareas existentes
          */
         public void listTasks() {
             measureExecutionTime(() -> {
                 if (tasks.isEmpty()) {
                     CustomLogger.info("No hay tareas registradas");
                     return;
                 }
                 
                 CustomLogger.info("Lista de tareas:");
                 tasks.forEach(task -> CustomLogger.info("- " + task.toString()));
             }, "listTasks");
         }
     }
     
     /**
      * Método principal para demostrar el uso del sistema
      */
     public static void main(String[] args) {
         CustomLogger.info("Iniciando sistema de gestión de tareas");
         
         // Demostración de diferentes niveles de logging
         CustomLogger.severe("Ejemplo de mensaje SEVERE");
         CustomLogger.warning("Ejemplo de mensaje WARNING");
         CustomLogger.info("Ejemplo de mensaje INFO");
         CustomLogger.config("Ejemplo de mensaje CONFIG");
         CustomLogger.fine("Ejemplo de mensaje FINE");
         
         // Crear instancia del gestor de tareas
         TaskManager taskManager = new TaskManager();
         
         // Ejemplos de uso del sistema
         taskManager.addTask("Estudiar Java", "Aprender sobre logging y POO");
         taskManager.addTask("Hacer ejercicio", "30 minutos de cardio");
         taskManager.addTask("Estudiar Java", "Tarea duplicada"); // Intentar añadir duplicada
         taskManager.listTasks();
         taskManager.removeTask("Estudiar Java");
         taskManager.listTasks();
         taskManager.removeTask("Tarea inexistente");
         
         CustomLogger.info("Finalizando sistema de gestión de tareas");
     }
 }