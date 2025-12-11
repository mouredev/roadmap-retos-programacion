import java.util.HashSet;
import java.util.Set;
import java.util.logging.ConsoleHandler;
import java.util.logging.FileHandler;
import java.util.logging.Level;
import java.util.logging.Logger;
import java.util.logging.SimpleFormatter;

public class JimsimroDev {
  private static final Logger logger = Logger.getLogger(JimsimroDev.class.getName());

  static {
    try {
      FileHandler archivo = new FileHandler("miApp.log", true);
      archivo.setFormatter(new SimpleFormatter());
      logger.addHandler(archivo);
      logger.setLevel(Level.ALL);
    } catch (Exception e) {
      logger.severe(() -> "No se pudo crear el FileHandler: " + e.getMessage());
    }
  }

  public void usoLogger() {
    logger.setUseParentHandlers(false);

    ConsoleHandler handler = new ConsoleHandler();
    handler.setLevel(Level.ALL);
    logger.addHandler(handler);

    logger.config("Mensajes de Cofiguración");

    logger.info("información general");

    logger.fine("debug detallado");

    logger.finer("debug muy detallada");

    logger.finest(() -> "debug más detallado");

    logger.warning("Este es un logger de warning");

    logger.severe("Error critico");
  }

  interface TareaService {

    void mostrarTareas();

    void crearTarea(Tarea tarea);

    void eliminarTarea(String titulo);
  }

  static class TareaServiceImpl implements TareaService {
    static Set<Tarea> listaTareas = new HashSet<>();

    @Override
    public void mostrarTareas() {
      listaTareas.stream().forEach(System.out::println);
      logger.info(() -> "Mostrando lista de tarea \n" + listaTareas);
    }

    @Override
    public void crearTarea(Tarea tarea) {
      if (listaTareas.stream().anyMatch(t -> t.titulo.equals(tarea.titulo))) {
        logger.log(Level.SEVERE, String.format("La tarea %s ya existe ", tarea.titulo));
        return;
      }
      listaTareas.add(tarea);
      logger.info(() -> "tarea creada " + tarea.getTitulo());
    }

    @Override
    public void eliminarTarea(String titulo) {
      if (listaTareas.stream().anyMatch(t -> t.titulo.equals(titulo))) {
        listaTareas.removeIf(t -> t.titulo.toLowerCase().contains(titulo.toLowerCase()));
        logger.log(Level.INFO, String.format("La tarea %s se elimino", titulo));
        return;
      }
      logger.log(Level.SEVERE, String.format("La tarea %s no existe ", titulo));
    }
  }

  static class Tarea {
    private String titulo;
    private String descripcion;

    public Tarea() {
    }

    public String getTitulo() {
      return titulo;
    }

    public void setTitulo(String titulo) {
      this.titulo = titulo;
    }

    public String getDescripcion() {
      return descripcion;
    }

    public void setDescripcion(String descripcion) {
      this.descripcion = descripcion;
    }

    @Override
    public String toString() {
      return String.format(" Tarea - Título: %s | Descripción: %s%n", titulo, descripcion);
    }
  }

  // Patron de diseño builder, crea objetos de tarea
  static class TareaBuilder {
    private String titulo;
    private String descripcion;

    public TareaBuilder setTitulo(String titulo) {
      this.titulo = titulo;
      return this;
    }

    public TareaBuilder setDescripcion(String descripcion) {
      this.descripcion = descripcion;
      return this;
    }

    public Tarea build() {
      Tarea t = new Tarea();
      t.setTitulo(this.titulo);
      t.setDescripcion(this.descripcion);
      return t;
    }
  }

  public static void main(String[] args) {
    new JimsimroDev().usoLogger();

    var listaTarea = new TareaServiceImpl();

    Tarea tarea1 = new TareaBuilder()
        .setTitulo("Comprar alimentos")
        .setDescripcion("Ir al supermercado y comprar leche,pan,frutas")
        .build();
    listaTarea.crearTarea(tarea1);

    Tarea tarea2 = new TareaBuilder()
        .setTitulo("Lavar la ropa")
        .setDescripcion("Separar ropa blanca y de color, lavar y tender")
        .build();
    listaTarea.crearTarea(tarea2);

    Tarea tarea3 = new TareaBuilder()
        .setTitulo("Sacar la basura")
        .setDescripcion("Sacar los residuos orgánicos y reciclables")
        .build();
    listaTarea.crearTarea(tarea3);

    Tarea tarea4 = new TareaBuilder()
        .setTitulo("Pagar facturas")
        .setDescripcion("Pagar la luz, agua e internet antes del fin de semana")
        .build();
    listaTarea.crearTarea(tarea4);

    Tarea tarea5 = new TareaBuilder()
        .setTitulo("Pagar facturas")
        .setDescripcion("Agendar cita de revisión anual")
        .build();
    listaTarea.crearTarea(tarea5);

    listaTarea.mostrarTareas();
    listaTarea.eliminarTarea("Sacar la basura");
    listaTarea.mostrarTareas();
  }
}
