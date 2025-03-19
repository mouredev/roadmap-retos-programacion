import java.util.Collection;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Vector;

public class Jeigar2 {
    /*
     * EJERCICIO:
     * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
     * atributos y una función que los imprima (teniendo en cuenta las posibilidades
     * de tu lenguaje).
     * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
     * utilizando su función.
     *
     * DIFICULTAD EXTRA (opcional):
     * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
     * en el ejercicio número 7 de la ruta de estudio)
     * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
     *   retornar el número de elementos e imprimir todo su contenido.
     */
    public static void main(String[] args) {
        Persona persona1 = new Persona();
        persona1.setNombre("Pedro");
        persona1.setApellido("Picapiedra");
        persona1.setEdad(65);
        System.out.println(persona1);

        Persona pablo = new Persona("Pablo", "Marmol", 61);
        System.out.println(pablo);

        LaPila<Persona> lista = new LaPila<>();
        lista.agregarElemento(persona1);
        lista.agregarElemento(pablo);
        System.out.println(lista);

        LaCola<Persona> lista2 = new LaCola<>();
        lista2.agregarElemento(persona1);
        lista2.agregarElemento(new Persona("Bilma", "Topacio", 60));
        lista2.agregarElemento(pablo);
        lista2.agregarElemento(new Persona("Maria", "Cuarzo", 59));
        System.out.println(lista2);
    }
}

class Persona {
    private final int MAYOR_EDAD = 18;

    private String nombre;
    private String apellido;
    private int edad;

    public Persona() {
        super();
    }

    public Persona(String nombre, String apellido, int edad) {
        this.nombre = nombre;
        this.apellido = apellido;
        this.edad = edad;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getApellido() {
        return apellido;
    }

    public void setApellido(String apellido) {
        this.apellido = apellido;
    }

    public int getEdad() {
        return edad;
    }

    public void setEdad(int edad) {
        this.edad = edad;
    }

    public boolean isMayorEdad() {
        return edad >= MAYOR_EDAD;
    }

    @Override
    public String toString() {
        return "Persona{" +
                "nombre='" + nombre + '\'' +
                ", apellido='" + apellido + '\'' +
                ", edad=" + edad +
                '}';
    }
}

class LaPila<T> {
    private HashMap<Integer, T> laPila;

    public LaPila() {
        this.laPila = new HashMap<>();
    }

    public int totalElementos() {
        return laPila.size();
    }

    public void agregarElemento(T o) {
        laPila.put(ultimo(), o);
    }

    private Integer ultimo() {
        return Integer.valueOf(laPila.size());
    }

    public T sacarElemento() {
        return laPila.remove(ultimo());
    }

    @Override
    public String toString() {
        return toString(false);
    }

    public String toString(boolean verbose) {
        String cadena = "";
        for (int item = laPila.size()-1; item >= 0; item--) {
            cadena = cadena.concat("\n\t- ");
            if(verbose) {
                cadena = cadena.concat(Integer.toString(item)).concat(": ");
            }
            cadena = cadena.concat(laPila.get(Integer.valueOf(item)).toString()).concat(",");
        }
        if (cadena.length() > 0) {
            cadena = cadena.substring(0, cadena.length() - 1).concat("\n");
        }
        return "LaPila=[" + cadena + "]";
    }
}

class LaCola<T> {
    private HashMap<Integer, T> laCola;

    public LaCola() {
        this.laCola = new HashMap<>();
    }

    public int totalElementos() {
        return laCola.size();
    }

    public void agregarElemento(T o) {
        laCola.put(ultimo(), o);
    }

    private Integer ultimo() {
        return Integer.valueOf(laCola.size());
    }

    public T sacarElemento() {
        return laCola.remove(ultimo());
    }

    @Override
    public String toString() {
        return toString(false);
    }

    public String toString(boolean verbose) {
        String cadena = "";
        for (int item = 0; item < laCola.size(); item++) {
            cadena = cadena.concat("\n\t- ");
            if(verbose) {
                cadena = cadena.concat(Integer.toString(item)).concat(": ");
            }
            cadena = cadena.concat(laCola.get(Integer.valueOf(item)).toString()).concat(",");
        }
        if (cadena.length() > 0) {
            cadena = cadena.substring(0, cadena.length() - 1).concat("\n");
        }
        return "LaCola=[".concat(cadena).concat("]");
    }
}

