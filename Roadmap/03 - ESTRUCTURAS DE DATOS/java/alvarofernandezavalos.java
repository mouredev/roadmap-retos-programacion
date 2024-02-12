import java.util.ArrayList;
import java.util.Scanner;

public class alvarofernandezavalos {

  public static class Contacto {
    public String nombre;
    public long telefono;

    public Contacto (String nombre, long telefono) {
      this.nombre = nombre;
      this.telefono = telefono;
    }

    public String getNombre() {
      return nombre;
    }

    public long getTelefono() {
      return telefono;
    }

    public void setNombre(String nombre) {
      this.nombre = nombre;
    }

    public void setTelefono(long telefono) {
      this.telefono = telefono;
    }

  }


  private static Scanner keyboard = new Scanner(System.in);
  private static ArrayList<Contacto> agenda;

  private static final int BUSCAR = 1;
  private static final int INSERTAR = 2;
  private static final int ACTUALIZAR = 3;
  private static final int ELIMNAR = 4;
  private static final int SALIR = 5;

  public static void main(String[] args) {
    agenda =  new ArrayList<Contacto>();
    while (true) {
      int num = menu();
      switch (num) {
        case BUSCAR:
          System.out.println("Buscar");
          mostrar(search());
          break;
        case INSERTAR:
          System.out.println("Insertar");
          insert();
          break;
        case ACTUALIZAR:
          System.out.println("Actualizar");
          update();
          break;
        case ELIMNAR:
          System.out.println("Eliminar");
          delete();
          break;
        case SALIR:
          System.out.println("BYE!");
          keyboard.close();
          System.exit(0);
          break;
      }
    }
  }

  private static void mostrar(Contacto search) {
    if (search != null) System.out.println("Nombre: "+search.getNombre() +" Telefono: "+search.getTelefono());
    else System.out.println("Contacto no encontrado en la agenda!");
  }

  private static int menu() {
    int opcion=0;
    do {
      System.out.println("*************************");
      System.out.println("1 - Buscar");
      System.out.println("2 - Insertar");
      System.out.println("3 - Actualizar");
      System.out.println("4 - Eliminar");
      System.out.println("5 - Salir");
      System.out.println("*************************");
      System.out.println("Opcion:");
      try {
        opcion = keyboard.nextInt();
      } catch (Exception e) {
        System.out.println("Inserta un Numero !");
      }
    } while (opcion>5 || 1>opcion);
    return opcion;
  }

  private static void delete() {
    Contacto delete = search();
    if (delete != null) {
      agenda.remove(delete);
      System.out.println("Contacto Borrado !");
    }
    else System.out.println("El contacto no esta en la agenda");
  }

  private static void update() {
    Contacto contactoViejo = search();
    if (contactoViejo != null) {
      if (insert()) {
        agenda.remove(contactoViejo);
        System.out.println("Contacto Modificado !");
      }
    }
    else System.out.println("El contacto no esta en la agenda");
  }

  private static Contacto search () {
    keyboard = new Scanner(System.in);
    System.out.println("Nombre:");
    String nombre = keyboard.nextLine();
    for (Contacto contacto : agenda) {
      if (contacto.getNombre().equals(nombre)) return contacto;
    }
    return null;
  }

  private static boolean insert () {
    try {
      keyboard = new Scanner(System.in);
      System.out.println("Nombre:");
      String nombre = keyboard.nextLine();
      int size = 0;
      long telefono = 0;
      do {
        keyboard = new Scanner(System.in);
        System.out.println("Teléfono (11 Dígitos y sin Letras)):");
        try {
          telefono = keyboard.nextLong();
        } catch (Exception e ) {
          System.out.println("Inserta un Teléfono valido !");
        }
        size = String.valueOf(telefono).length();
      } while (size!=11);
      agenda.add(new Contacto(nombre,telefono));
      return true;
    } catch (Exception e) {
      return false;
    }
  }

}
