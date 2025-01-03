import java.util.*;

public class MohamedElderkaoui{

    public static void main(String[] args) {
        ArbolGenealogico arbol = new ArbolGenealogico();

        // Añadimos personas
        arbol.añadirPersona("Alicia");
        arbol.añadirPersona("Roberto");
        arbol.añadirPersona("Carlos");

        // Obtenemos los IDs de las personas
        String idAlicia = arbol.getPersonas().values().stream()
                .filter(p -> p.getNombre().equals("Alicia")).findFirst().get().getId();
        String idRoberto = arbol.getPersonas().values().stream()
                .filter(p -> p.getNombre().equals("Roberto")).findFirst().get().getId();
        String idCarlos = arbol.getPersonas().values().stream()
                .filter(p -> p.getNombre().equals("Carlos")).findFirst().get().getId();

        // Modificamos relaciones
        arbol.modificarPareja(idAlicia, idRoberto);
        arbol.añadirHijo(idAlicia, idCarlos);

        // Imprimimos el árbol
        arbol.imprimirArbol();
    }
}


class Persona {
    private final String id;
    private String nombre;
    private Persona pareja;
    private final List<Persona> hijos;

    public Persona(String nombre) {
        this.id = UUID.randomUUID().toString(); // Genera un identificador único
        this.nombre = nombre;
        this.hijos = new ArrayList<>();
    }

    public String getId() {
        return id;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public Optional<Persona> getPareja() {
        return Optional.ofNullable(pareja);
    }

    public void setPareja(Persona pareja) {
        this.pareja = pareja;
    }

    public List<Persona> getHijos() {
        return hijos;
    }

    public void añadirHijo(Persona hijo) {
        if (!hijos.contains(hijo)) {
            hijos.add(hijo);
        }
    }

    public void eliminarHijo(Persona hijo) {
        hijos.remove(hijo);
    }

    @Override
    public String toString() {
        return "Persona{id='" + id + "', nombre='" + nombre + "'}";
    }
}

class ArbolGenealogico {
    private final Map<String, Persona> personas;

    public ArbolGenealogico() {
        this.personas = new HashMap<>();
    }

    public void añadirPersona(String nombre) {
        Persona nuevaPersona = new Persona(nombre);
        personas.put(nuevaPersona.getId(), nuevaPersona);
        System.out.println("Persona añadida: " + nuevaPersona);
    }

    public void eliminarPersona(String id) {
        Persona persona = personas.remove(id);
        if (persona != null) {
            System.out.println("Persona eliminada: " + persona);
        } else {
            System.out.println("Persona no encontrada.");
        }
    }

    public void modificarPareja(String idPersona, String idPareja) {
        Persona persona = personas.get(idPersona);
        Persona pareja = personas.get(idPareja);

        if (persona != null && pareja != null) {
            persona.setPareja(pareja);
            pareja.setPareja(persona); // Hacemos la relación bidireccional
            System.out.println(persona.getNombre() + " ahora está emparejado con " + pareja.getNombre());
        } else {
            System.out.println("Una o ambas personas no fueron encontradas.");
        }
    }

    public void añadirHijo(String idPadre, String idHijo) {
        Persona padre = personas.get(idPadre);
        Persona hijo = personas.get(idHijo);

        if (padre != null && hijo != null) {
            padre.añadirHijo(hijo);
            System.out.println(hijo.getNombre() + " ahora es hijo de " + padre.getNombre());
        } else {
            System.out.println("Padre o hijo no fueron encontrados.");
        }
    }

    public void imprimirArbol() {
        for (Persona persona : personas.values()) {
            System.out.println(persona.getNombre() + " (ID: " + persona.getId() + ")");
            persona.getPareja().ifPresent(p -> System.out.println("  Pareja: " + p.getNombre()));
            if (!persona.getHijos().isEmpty()) {
                System.out.println("  Hijos:");
                for (Persona hijo : persona.getHijos()) {
                    System.out.println("    - " + hijo.getNombre());
                }
            }
        }
    }

    public Map<String, Persona> getPersonas() {
        return personas;
    }
}

