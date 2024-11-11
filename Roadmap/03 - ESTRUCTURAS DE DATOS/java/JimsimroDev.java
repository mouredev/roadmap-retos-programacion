import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.Set;
import java.util.Stack;
import java.util.TreeMap;

public class JimsimroDev {
  private Scanner in = new Scanner(System.in);
  private Map<String, Long> agenda = new HashMap<>();
  private String nombre;
  private Long telefono;

  private void crearContacto() {
    System.out.println("Ingresa el nombre del contacto");
    nombre = in.nextLine();
    System.out.println("Ingresa el numero de telefono");
    telefono = in.nextLong();
    in.nextLine();
    validacion(nombre, telefono);
  }

  private void buscarContacto() {
    System.out.println("Escribe el nombre del contacto a buscar");
    nombre = in.nextLine();
    if (agenda.containsKey(nombre)) {
      System.err.println("El telefono de " + nombre + " es " + agenda.get(nombre));
    } else {
      System.out.println("Contacto no encontrado");
    }
  }

  private void actualizarContacto() {
    System.out.println("Escribe el nombre del contacto que desea Actualizar");
    String contactoActualizar = in.nextLine();
    if (agenda.containsKey(contactoActualizar)) {
      System.out.println("Escribe el nuevo número para el contacto ");
      Long nuevoNumero = in.nextLong();
      validacion(contactoActualizar, nuevoNumero);
    }
  }

  private void eliminarContacto() {
    System.out.println("Escribe el nombre del contacto a eliminar");
    String contactoAEliminar = in.nextLine();
    if (agenda.containsKey(contactoAEliminar)) {
      agenda.remove(contactoAEliminar);
      System.out.println("Contacto eliminado ");
    } else {
      System.out.println("Ese contacto no existe");
    }
  }

  public void run() {
    String menu = """
        Menu
        + 1. Crear contacto nuevo
        + 2. Buscar contacto
        + 3. Actualizar contacto
        + 4. Elimnar contacto
        + 5. Salir
        """;
    int opcion = 0;
    while (opcion != 5) {
      System.out.println(menu);
      System.out.print("Seleciona una opcion -> ");
      opcion = in.nextInt();
      in.nextLine();

      switch (opcion) {
        case 1:
          crearContacto();
          break;
        case 2:
          buscarContacto();
          break;
        case 3:
          actualizarContacto();
          break;
        case 4:
          eliminarContacto();
          break;
        case 5:
          System.out.println("Saliendo de la agenda");
          break;
        default:
          break;
      }
    }
  }

  private static boolean isDigit(Long telefono) {
    Integer longitud = String.valueOf(telefono).length();
    if (telefono >= 0 && longitud >= 10) {
      return true;
    }
    return false;
  }

  private void validacion(String nombre, Long telefono) {
    if (isDigit(telefono)) {
      agenda.put(nombre, telefono);
      System.out.println("Contacto Guardado " + agenda);
    } else {
      System.out.println("Debes introducir un número de telefono valido de 10 digitos");
    }
  }

  public static void main(String[] args) {
    JimsimroDev ejecutar = new JimsimroDev();
    String divLine = "::::::::::::::::::::::::::::::::::::::";
    // Estructuras de datos
    // Listas enlasadas
    //
    System.out.println(divLine);
    List<String> miListaInmutable = List.of("JimsimroDev", "Thor", "Comedian");// Inmutable no se puede modificar
    System.out.println(miListaInmutable);
    System.out.println(divLine);

    List<String> miLista = new ArrayList<>(Arrays.asList("JimsimroDev", "Thor", "Comedian"));
    System.out.println(miLista);
    miLista.add("Wanda");// Insercción
    System.out.println(miLista);

    miLista.remove("Wanda");// Eliminación
    System.out.println(miLista);

    System.out.println(miLista.get(1)); // Acceso
    miLista.set(1, "Wanda"); // Actualizaacion
    System.out.println(miLista);

    // Ordena la Listas
    Collections.sort(miLista);
    System.out.println(miLista);

    System.out.println(divLine);
    LinkedList<String> lista = new LinkedList<>() {
      {
        add("Phyton");
        add("Java");
        add("PHP");
        add("Rust");
      }
    };
    System.out.println(lista);

    lista.add("Cobol");// Insercción
    System.out.println(lista);

    lista.remove("PHP");// eliminacion
    System.out.println(lista);

    System.out.println(lista.get(3));// Acceso

    lista.set(3, "Perl");
    System.out.println(lista);

    System.out.println(divLine);
    Set<String> conjunto = new HashSet<>() {
      {
        add("Spring");
        add("Laravel");
        add("Angular");
        add("Angular");// No se agrega por que Set no permite elemento duplicados
      }
    };
    System.out.println(conjunto);

    conjunto.add("React");// Insercción
    System.out.println(conjunto);

    conjunto.remove("Laravel");// Eliminación
    System.out.println(conjunto);

    // no permite acceder a los elementos en un indice especifico ya que este los
    // guardan sin un ordenación y no permite tampoco duplicados
    // lo que podemos hacer es validar si existe un elemento con contains
    System.out.println("El framework Spring existe en el cojunto? " + conjunto.contains("Spring"));// Devuelve tru si
                                                                                                   // esta en el
                                                                                                   // conjunto
    System.out.println(divLine);
    Stack<String> pila = new Stack<>() {
      {
        push("Elemento 1");
        push("Elemento 2");
        push("Elemento 3");
      }
    };
    System.out.println(pila);

    pila.push("Elemento 4");// Insercción
    System.out.println(pila);

    pila.pop();// Elimina el ultimo elemento de la lista ya que no permite eliminar elementos
               // intermedios
    System.out.println(pila);
    System.out.println(pila.get(2));// Acceso al elementos por indice

    System.out.println(divLine);
    // Diccionario o mapas
    Map<String, String> map = new HashMap<>();
    map.put("nombre", "JimsimroDev");
    map.put("apellidos", "Simanca");
    map.put("edad", "28");
    System.out.println(map);

    map.put("telefono", "321343534");// Insercción
    System.out.println(map);

    map.remove("apellidos");// Eliminación
    System.out.println(map);

    System.out.println(map.get("nombre")); // Acceso

    map.put("edad", "29"); // Actualización
    System.out.println(map);

    Map<String, String> ordenacionPorClave = new TreeMap<>(map);
    System.out.println(ordenacionPorClave);// ordenación por la clave

    System.out.println(divLine);
    // Extra
    ejecutar.run();
  }
}
