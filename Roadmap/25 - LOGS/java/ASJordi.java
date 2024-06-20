/*
    El Api de Java Logging proporciona una serie de métodos para registrar mensajes de aplicación (logs).
    Esto permite registrar mensajes que se pueden usar para monitorear y diagnosticar una aplicación.
    java.util.logging.Level define 7 niveles de registro de mensajes:
        - SEVERE (el más alto)
        - WARNING
        - INFO
        - CONFIG
        - FINE
        - FINER
        - FINEST (el más bajo)
    Existen otros 2 niveles: ALL y OFF. El primero se utiliza para habilitar todos los niveles de registro y el segundo para deshabilitar todos los niveles de registro.
    El Api de Java Logging proporciona una serie de clases para registrar mensajes de aplicación:
        - Logger: es la clase principal para registrar mensajes de aplicación.
        - Handler: es una clase que maneja los mensajes de registro.
        - Formatter: es una clase que formatea los mensajes de registro.
        - Filter: es una clase que filtra los mensajes de registro.
 */

import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;
import java.util.logging.FileHandler;
import java.util.logging.Level;
import java.util.logging.Logger;
import java.util.logging.XMLFormatter;

public class Main {

    public static void main(String[] args) {
//        useLogger();
        tasksManager();
    }

    /**
     * EJERCICIO:
     * Explora el concepto de "logging" en tu lenguaje. Configúralo y muestra
     * un ejemplo con cada nivel de "severidad" disponible.
     */
    static void useLogger() {
        // Crear un Logger
        Logger logger = Logger.getLogger(Main.class.getName());
        // Habilitar todos los niveles de registro
        logger.setLevel(Level.ALL);

        try {
            // Crear un FileHandler para registrar mensajes en un archivo
            FileHandler fileHandler = new FileHandler("logs.log");
            // Asignar el formateador XML al FileHandler
            fileHandler.setFormatter(new XMLFormatter());
            // Agregar el FileHandler al Logger
            logger.addHandler(fileHandler);

            // Registrar mensajes
            logger.severe("Mensaje de nivel SEVERE");
            logger.warning("Mensaje de nivel WARNING");
            logger.info("Mensaje de nivel INFO");
            logger.config("Mensaje de nivel CONFIG");
            logger.fine("Mensaje de nivel FINE");
            logger.finer("Mensaje de nivel FINER");
            logger.finest("Mensaje de nivel FINEST");
        } catch (Exception e) {
            logger.log(Level.SEVERE, "Mensaje de nivel SEVERE", e);
        }
    }

    /**
     * DIFICULTAD EXTRA (opcional):
     * Crea un programa ficticio de gestión de tareas que permita añadir, eliminar y listar dichas tareas.
     * - Añadir: recibe nombre y descripción.
     * - Eliminar: por nombre de la tarea.
     * Implementa diferentes mensajes de log que muestren información según la
     * tarea ejecutada (a tu elección).
     * Utiliza el log para visualizar el tiempo de ejecución de cada tarea.
     */
    static void tasksManager() {
        Logger logger = Logger.getLogger(Main.class.getName());
        logger.setLevel(Level.ALL);
        Scanner sc = new Scanner(System.in);
        sc.useDelimiter("\n");
        List<Task> tasks = new LinkedList<>();
        String option = "";

        while (!option.equals("4")) {
            showMenu();
            option = sc.nextLine();
            switch (option) {
                case "1" -> {
                    long s = System.currentTimeMillis();
                    System.out.println("Introduce el título de la tarea:");
                    String title = sc.nextLine();
                    System.out.println("Introduce la descripción de la tarea:");
                    String description = sc.nextLine();
                    Task task = new Task(title, description);
                    tasks.add(task);
                    long e = System.currentTimeMillis();
                    logger.log(Level.INFO, "Tarea creada: " + task);
                    logger.log(Level.INFO, "Tiempo de ejecución: " + (e - s) + "ms");
                }
                case "2" -> {
                    long s = System.currentTimeMillis();
                    System.out.println("Introduce el título de la tarea a eliminar:");
                    String title = sc.nextLine();
                    Task task = tasks.stream().filter(t -> t.title().equalsIgnoreCase(title)).findFirst().orElse(null);
                    if (task != null) {
                        tasks.remove(task);
                        logger.log(Level.INFO, "Tarea eliminada: " + task);
                    } else logger.log(Level.WARNING, "Tarea no encontrada");
                    long e = System.currentTimeMillis();
                    logger.log(Level.INFO, "Tiempo de ejecución: " + (e - s) + "ms");
                }
                case "3" -> {
                    long s = System.currentTimeMillis();
                    if (tasks.isEmpty()) logger.log(Level.WARNING, "No hay tareas");
                    else tasks.forEach(task -> logger.log(Level.INFO, task.toString()));
                    long e = System.currentTimeMillis();
                    logger.log(Level.INFO, "Tiempo de ejecución: " + (e - s) + "ms");
                }
                case "4" -> logger.log(Level.INFO, "Saliendo...");
                default -> logger.log(Level.WARNING, "Opción no válida");
            }
        }
    }

    public record Task(String title, String description) {}

    static void showMenu() {
        System.out.println("Selecciona una opción:");
        System.out.println("1. Crear tarea");
        System.out.println("2. Eliminar tarea");
        System.out.println("3. Mostar tareas");
        System.out.println("4. Salir");
    }
}
