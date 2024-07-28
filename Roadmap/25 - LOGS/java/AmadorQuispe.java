package com.amsoft.roadmap.example25;

import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Map;
import java.util.Scanner;
import java.util.TreeMap;
import java.util.logging.Logger;
import java.util.logging.Formatter;
import java.util.logging.LogRecord;
import java.util.logging.FileHandler;
import java.util.logging.ConsoleHandler;
import java.util.logging.LogManager;
import java.util.logging.Level;

public class ExampleMain {
    private final static Logger LOGGER = LoggerConfig.getLogger(ExampleMain.class);
    public static void logs() {
        LOGGER.severe("Severe Log");
        LOGGER.warning("Warning Log");
        LOGGER.info("Info Log");
        LOGGER.config("Config Log");
        LOGGER.fine("Fine Log");
        LOGGER.finer("Finer Log");
        LOGGER.finest("Finest Log");
    }

    public static void main(String[] args) {
        logs();
        TaskManager taskManager =  new TaskManager();
        taskManager.init();
    }
}

class TaskManager {
    Logger logger = LoggerConfig.getLogger(TaskManager.class);
    public void init(){
        logger.info("administrador de tareas iniciado.");
        Scanner sc = new Scanner(System.in);
        sc.useDelimiter("\n");
        TreeMap<String,String> tasks = new TreeMap<>();
        String  option = "";
        while (!option.equals("4")){
            long timeStart;
            long timeEnd;
            menu();
            System.out.println("Ingrese en número de la opción:");
            option = sc.nextLine();
            switch (option){
                case "1":
                    System.out.println("Tareas registradas");
                    timeStart = System.currentTimeMillis();
                    if(tasks.isEmpty()) System.out.println("No hay tareas registradas");
                    tasks.forEach((k,v)->System.out.println(k + " - " + v ));
                    timeEnd = System.currentTimeMillis();
                    logger.info("Tiempo de ejecución en listado " + (timeEnd - timeStart) + "ms");
                    break;
                case "2":
                    System.out.println("Agregar una tarea");
                    timeStart = System.currentTimeMillis();
                    System.out.print("Ingrese nombre de la tarea:");
                    String name = sc.nextLine();
                    System.out.print("Ingrese descripción de la tarea:");
                    String description = sc.nextLine();
                    tasks.put(name,description);
                    timeEnd = System.currentTimeMillis();
                    logger.info("Tarea creada " + name + " Tiempo de ejecución " + (timeEnd - timeStart) + "ms");
                    break;
                case "3":
                    System.out.println("Eliminar una tarea");
                    timeStart = System.currentTimeMillis();
                    System.out.print("Ingrese nombre de la tarea a eliminar:");
                    String nameToDelete = sc.nextLine();
                    if(tasks.remove(nameToDelete)!=null){
                        timeEnd = System.currentTimeMillis();
                        logger.info("Tarea eliminada " + nameToDelete + " Tiempo de ejecución " + (timeEnd - timeStart) + "ms");
                    }else{
                        timeEnd = System.currentTimeMillis();
                        logger.info("Tarea no registrada " + nameToDelete + " Tiempo de ejecución " + (timeEnd - timeStart) + "ms");
                    }
                    break;
                case "4":
                    System.out.println("Gracias por usar");
                    logger.info("Saliendo del sistema");
                    break;
                default:
                    System.out.println("Opción no disponible");
                    logger.warning("Opción no valida :"+option);
                    break;
            }
        }
    }
    private void menu(){
        System.out.println("=".repeat(29));
        System.out.println("|| ADMINISTRADOR DE TAREAS ||");
        System.out.println("=".repeat(29));
        System.out.println("Opciones disponibles");
        System.out.println("[1] Mostrar tareas");
        System.out.println("[2] Agregar una tarea");
        System.out.println("[3] Eliminar una tarea");
        System.out.println("[4] Salir");
    }
}

class LogFormatter extends Formatter {
    private static final String PATTERN = "yyyy-MM-dd'T'HH:mm:ss.SSSZ";
    private final SimpleDateFormat dateFormat = new SimpleDateFormat(PATTERN);
    private static final int LEVEL_NAME_LENGTH = 7;

    @Override
    public String format(LogRecord record) {
        StringBuilder sb = new StringBuilder();
        String formattedDate = dateFormat.format(new Date(record.getMillis()));
        sb.append("\u001B[30m");
        sb.append(formattedDate).append(" ");
        String levelName = record.getLevel().getLocalizedName();
        sb.append(padRight(levelName)).append(" ");
        sb.append(record.getLongThreadID()).append(" --- ");
        sb.append("[").append(record.getLoggerName()).append("] ");
        sb.append(": ").append(formatMessage(record));
        sb.append("\u001B[0m");
        sb.append("\n");
        return sb.toString();
    }

    private String padRight(String s) {
        return String.format("%1$-" + LEVEL_NAME_LENGTH + "s", s);
    }
}

class LoggerConfig {
    static {
        try {
            FileHandler fileHandler = new FileHandler("Logging.txt");
            fileHandler.setFormatter(new LogFormatter());
            ConsoleHandler consoleHandler = new ConsoleHandler();
            consoleHandler.setFormatter(new LogFormatter());
            LogManager.getLogManager().reset();
            Logger rootLogger = Logger.getLogger("");
            rootLogger.setLevel(Level.ALL);
            rootLogger.addHandler(fileHandler);
            rootLogger.addHandler(consoleHandler);
        } catch (IOException e) {
            throw new RuntimeException("Error al configurar el logger", e);
        }
    }

    public static Logger getLogger(Class<?> clazz) {
        return Logger.getLogger(clazz.getName());
    }
}