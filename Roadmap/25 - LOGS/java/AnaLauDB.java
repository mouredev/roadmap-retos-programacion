import java.util.logging.*;
import java.util.*;
import java.io.IOException;

public class AnaLauDB {

    // Logger para la clase
    private static final Logger logger = Logger.getLogger(AnaLauDB.class.getName());

    // Clase para representar una tarea
    static class Tarea {
        private String nombre;
        private String descripcion;
        private Date fechaCreacion;

        public Tarea(String nombre, String descripcion) {
            this.nombre = nombre;
            this.descripcion = descripcion;
            this.fechaCreacion = new Date();
        }

        // Getters
        public String getNombre() {
            return nombre;
        }

        public String getDescripcion() {
            return descripcion;
        }

        public Date getFechaCreacion() {
            return fechaCreacion;
        }

        @Override
        public String toString() {
            return String.format("Tarea{nombre='%s', descripcion='%s', fecha=%s}",
                    nombre, descripcion, fechaCreacion);
        }
    }

    // Gestor de tareas
    static class GestorTareas {
        private List<Tarea> tareas;
        private Logger logger;

        public GestorTareas() {
            this.tareas = new ArrayList<>();
            this.logger = Logger.getLogger(GestorTareas.class.getName());
            configurarLogger();
        }

        private void configurarLogger() {
            try {
                // Crear handler para archivo
                FileHandler fileHandler = new FileHandler("tareas.log", true);
                fileHandler.setFormatter(new SimpleFormatter());
                logger.addHandler(fileHandler);

                // Handler para consola
                ConsoleHandler consoleHandler = new ConsoleHandler();
                consoleHandler.setFormatter(new SimpleFormatter());
                logger.addHandler(consoleHandler);

                logger.setLevel(Level.ALL);

            } catch (IOException e) {
                System.err.println("Error configurando logger: " + e.getMessage());
            }
        }

        public void añadirTarea(String nombre, String descripcion) {
            long inicio = System.currentTimeMillis();

            logger.info("Iniciando proceso de añadir tarea: " + nombre);

            // Validaciones
            if (nombre == null || nombre.trim().isEmpty()) {
                logger.warning("Intento de añadir tarea con nombre vacío");
                throw new IllegalArgumentException("El nombre no puede estar vacío");
            }

            // Verificar si ya existe
            for (Tarea t : tareas) {
                if (t.getNombre().equals(nombre)) {
                    logger.warning("Intento de añadir tarea duplicada: " + nombre);
                    throw new IllegalArgumentException("La tarea ya existe");
                }
            }

            // Simular procesamiento
            try {
                Thread.sleep(100); // Simular trabajo
            } catch (InterruptedException e) {
                logger.severe("Proceso interrumpido al añadir tarea: " + e.getMessage());
                return;
            }

            Tarea nuevaTarea = new Tarea(nombre, descripcion);
            tareas.add(nuevaTarea);

            long fin = System.currentTimeMillis();
            logger.info(String.format("Tarea '%s' añadida exitosamente en %d ms",
                    nombre, (fin - inicio)));
            logger.fine("Detalles de la tarea: " + nuevaTarea);
        }

        public boolean eliminarTarea(String nombre) {
            long inicio = System.currentTimeMillis();

            logger.info("Iniciando proceso de eliminar tarea: " + nombre);

            if (nombre == null || nombre.trim().isEmpty()) {
                logger.warning("Intento de eliminar tarea con nombre vacío");
                return false;
            }

            Iterator<Tarea> iterator = tareas.iterator();
            while (iterator.hasNext()) {
                Tarea tarea = iterator.next();
                if (tarea.getNombre().equals(nombre)) {
                    iterator.remove();
                    long fin = System.currentTimeMillis();
                    logger.info(String.format("Tarea '%s' eliminada exitosamente en %d ms",
                            nombre, (fin - inicio)));
                    logger.fine("Tarea eliminada: " + tarea);
                    return true;
                }
            }

            long fin = System.currentTimeMillis();
            logger.warning(String.format("Tarea '%s' no encontrada para eliminar (tiempo: %d ms)",
                    nombre, (fin - inicio)));
            return false;
        }

        public void listarTareas() {
            long inicio = System.currentTimeMillis();

            logger.info("Iniciando listado de tareas");
            logger.finer("Número total de tareas: " + tareas.size());

            if (tareas.isEmpty()) {
                logger.info("No hay tareas para mostrar");
                System.out.println("No hay tareas registradas.");
                return;
            }

            System.out.println("=== Lista de Tareas ===");
            for (int i = 0; i < tareas.size(); i++) {
                Tarea tarea = tareas.get(i);
                System.out.printf("%d. %s - %s%n",
                        i + 1, tarea.getNombre(), tarea.getDescripcion());
                logger.finest("Mostrando tarea: " + tarea.getNombre());
            }

            long fin = System.currentTimeMillis();
            logger.info(String.format("Listado completado en %d ms (%d tareas mostradas)",
                    (fin - inicio), tareas.size()));
        }
    }

    public static void ejemplosNivelesLog() {
        System.out.println("=== Ejemplos de niveles de logging ===");

        // Configurar logger para mostrar todos los niveles
        logger.setLevel(Level.ALL);

        // Crear handler para ver todos los mensajes
        ConsoleHandler handler = new ConsoleHandler();
        handler.setLevel(Level.ALL);
        handler.setFormatter(new SimpleFormatter());
        logger.addHandler(handler);

        // Ejemplos de cada nivel
        logger.severe("SEVERE: Error crítico del sistema");
        logger.warning("WARNING: Situación que requiere atención");
        logger.info("INFO: Información general del proceso");
        logger.config("CONFIG: Información de configuración");
        logger.fine("FINE: Información detallada para debugging");
        logger.finer("FINER: Información más detallada para debugging");
        logger.finest("FINEST: Información muy detallada para debugging");
    }

    public static void main(String[] args) {
        // Ejemplos básicos de logging
        ejemplosNivelesLog();

        System.out.println("\n=== DIFICULTAD EXTRA: Gestor de Tareas ===");

        GestorTareas gestor = new GestorTareas();
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("\n--- Menú ---");
            System.out.println("1. Añadir tarea");
            System.out.println("2. Eliminar tarea");
            System.out.println("3. Listar tareas");
            System.out.println("4. Salir");
            System.out.print("Seleccione una opción: ");

            try {
                int opcion = scanner.nextInt();
                scanner.nextLine(); // Consumir el salto de línea

                switch (opcion) {
                    case 1:
                        System.out.print("Nombre de la tarea: ");
                        String nombre = scanner.nextLine();
                        System.out.print("Descripción: ");
                        String descripcion = scanner.nextLine();
                        try {
                            gestor.añadirTarea(nombre, descripcion);
                            System.out.println("Tarea añadida exitosamente.");
                        } catch (Exception e) {
                            System.out.println("Error: " + e.getMessage());
                        }
                        break;

                    case 2:
                        System.out.print("Nombre de la tarea a eliminar: ");
                        String nombreEliminar = scanner.nextLine();
                        boolean eliminada = gestor.eliminarTarea(nombreEliminar);
                        if (eliminada) {
                            System.out.println("Tarea eliminada exitosamente.");
                        } else {
                            System.out.println("Tarea no encontrada.");
                        }
                        break;

                    case 3:
                        gestor.listarTareas();
                        break;

                    case 4:
                        logger.info("Cerrando aplicación de gestión de tareas");
                        System.out.println("¡Hasta luego!");
                        scanner.close();
                        return;

                    default:
                        logger.warning("Opción inválida seleccionada: " + opcion);
                        System.out.println("Opción inválida.");
                }
            } catch (Exception e) {
                logger.severe("Error inesperado en el menú principal: " + e.getMessage());
                System.out.println("Error: Entrada inválida.");
                scanner.nextLine(); // Limpiar buffer
            }
        }
    }
}
