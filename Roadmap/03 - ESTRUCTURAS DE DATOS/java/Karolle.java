import java.util.*;

public class Karolle {
  public static void main(String[] args) {

    // Ejemplo de Lista
    List<String> lista = new ArrayList<>();
    lista.add("Uno"); // Inserción
    lista.add("Dos");
    lista.remove(0); // Borrado
    lista.set(0, "Tres"); // Actualización
    Collections.sort(lista); // Ordenación
    System.out.println("Lista: " + lista);

    // Ejemplo de Set
    Set<String> conjunto = new HashSet<>();
    conjunto.add("Uno"); // Inserción
    conjunto.add("Dos");
    conjunto.remove("Uno"); // Borrado
    // En un Set no se puede actualizar un elemento específico, necesitas removerlo y luego agregar el nuevo
    conjunto.add("Tres"); // Actualización simulada
    List<String> listaParaOrdenar = new ArrayList<>(conjunto);
    Collections.sort(listaParaOrdenar); // Ordenación
    System.out.println("Conjunto: " + listaParaOrdenar);

    // Ejemplo de Mapa
    Map<String, String> mapa = new HashMap<>();
    mapa.put("clave1", "valor1"); // Inserción
    mapa.put("clave2", "valor2");
    mapa.remove("clave1"); // Borrado
    mapa.put("clave2", "valor3"); // Actualización
    List<Map.Entry<String, String>> listaDeEntradas = new ArrayList<>(mapa.entrySet());
    listaDeEntradas.sort(Map.Entry.comparingByKey()); // Ordenación
    System.out.println("Mapa: " + listaDeEntradas);

    // Ejemplo de Contacto, Agenda
    Agenda agenda = new Agenda();
    agenda.agregarContacto("Juan", "1234567890");
    agenda.agregarContacto("Maria", "0987654321");
    agenda.mostrarContactos();
    agenda.eliminarContacto("Juan");
    agenda.actualizarContacto("Maria", "1111111111");
    agenda.mostrarContactos();
}
}

class Contacto {
String nombre;
String numeroDeTelefono;

Contacto(String nombre, String numeroDeTelefono) {
    this.nombre = nombre;
    this.numeroDeTelefono = numeroDeTelefono;
}


public String toString() {
    return "Nombre: " + nombre + ", Número de Teléfono: " + numeroDeTelefono;
}
}

class Agenda {
List<Contacto> contactos = new ArrayList<>();

void agregarContacto(String nombre, String numeroDeTelefono) {
    contactos.add(new Contacto(nombre, numeroDeTelefono));
}

void eliminarContacto(String nombre) {
    contactos.removeIf(contacto -> contacto.nombre.equals(nombre));
}

void actualizarContacto(String nombre, String nuevoNumero) {
    for (Contacto contacto : contactos) {
        if (contacto.nombre.equals(nombre)) {
            contacto.numeroDeTelefono = nuevoNumero;
            break;
        }
    }
}

void mostrarContactos() {
    for (Contacto contacto : contactos) {
        System.out.println(contacto);
    }
}
}