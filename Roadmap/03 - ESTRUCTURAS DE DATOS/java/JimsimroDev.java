import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.TreeMap;

public class JimsimroDev {
  public static void main(String[] args) {
    // Estructuras de datos
    // Listas enlasadas
    List<String> miListaInmutable = List.of("JimsimroDev", "Thor", "Comedian");// Inmutable no se puede modificar
    System.out.println(miListaInmutable);

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

    Scanner in = new Scanner(System.in);
    Map<String, Integer> agenda = new HashMap<>();
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
          System.out.println("Ingresa el nombre del contacto");
          String nombre = in.nextLine();
          System.out.println("Ingresa el numero de telefono");
          Integer telefono = in.nextInt();
          in.nextLine();

          int longitud = String.valueOf(telefono).length();
          if (longitud >= 0 && longitud <= 11) {
            agenda.put(nombre, telefono);
            System.out.println(agenda);
            break;
          } else {
            System.out.println("Debes introducir un número valido");
          }
          break;

        case 2:
          System.out.println("Escribe el nombre del contacto a buscar");
          nombre = in.nextLine();
          if (agenda.containsKey(nombre)) {
            System.err.println("El telefono de " + nombre + " es " + agenda.get(nombre));
          } else {
            System.out.println("Contacto no encontrado");
          }
          break;

        case 3:
          System.out.println("Escribe el nombre del contacto que desea Actualizar");
          String contactoActualizar = in.nextLine();
          if (agenda.containsKey(contactoActualizar)) {
            System.out.println("Escribe el nuevo número para el contacto ");
            Integer nuevoNumero = in.nextInt();
            longitud = String.valueOf(nuevoNumero).length();

            if (longitud >= 0 && longitud <= 11) {
              agenda.put(contactoActualizar, nuevoNumero);
              System.out.println(agenda);
            }
          }

          break;
        case 4:
          System.out.println("Escribe el nombre del contacto a eliminar");
          String contactoAEliminar = in.nextLine();
          if (agenda.containsKey(contactoAEliminar)) {
            agenda.remove(contactoAEliminar);
            System.out.println("Contacto eliminado ");
          }
          break;
        case 5:
          System.out.println("Saliendo de la agenda 🙌");
          break;

        default:
          break;
      }
    }
  }
}
