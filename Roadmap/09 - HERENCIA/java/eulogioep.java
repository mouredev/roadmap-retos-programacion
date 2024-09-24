// Clase base o superclase
class Animal {
    protected String nombre;

    public Animal(String nombre) {
        this.nombre = nombre;
    }

    public String sonido() {
        return "No hay sonido por defecto para el animal";
    }
}

// Clase derivada o subclase de Animal
class Perro extends Animal {
    public Perro(String nombre) {
        super(nombre);
    }

    @Override
    public String sonido() {
        return "Guau";
    }
}

// Clase derivada o subclase de Animal
class Gato extends Animal {
    public Gato(String nombre) {
        super(nombre);
    }

    @Override
    public String sonido() {
        return "Miau";
    }
}

// Dificultad extra: Clase base para Empleados
class Empleado {
    protected int identificador;
    protected String nombre;

    public Empleado(int identificador, String nombre) {
        this.identificador = identificador;
        this.nombre = nombre;
    }

    public int getIdentificador() {
        return identificador;
    }

    public String getNombre() {
        return nombre;
    }
}

// Clase derivada de Empleado para Gerentes
class Gerente extends Empleado {
    private int cantidadEmpleados;

    public Gerente(int identificador, String nombre, int cantidadEmpleados) {
        super(identificador, nombre);
        this.cantidadEmpleados = cantidadEmpleados;
    }

    public void setCantidadEmpleados(int cantidadEmpleados) {
        this.cantidadEmpleados = cantidadEmpleados;
    }

    public int getCantidadEmpleados() {
        return cantidadEmpleados;
    }
}

// Clase derivada de Empleado para Gerentes de Proyectos
class GerenteDeProyecto extends Empleado {
    private String proyecto;

    public GerenteDeProyecto(int identificador, String nombre, String proyecto) {
        super(identificador, nombre);
        this.proyecto = proyecto;
    }

    public String getProyecto() {
        return proyecto;
    }
}

// Clase derivada de Empleado para Programadores
class Programador extends Empleado {
    private String lenguajeFavorito;

    public Programador(int identificador, String nombre, String lenguajeFavorito) {
        super(identificador, nombre);
        this.lenguajeFavorito = lenguajeFavorito;
    }

    public String getLenguajeFavorito() {
        return lenguajeFavorito;
    }
}

public class EulogioEP {
    public static void main(String[] args) {
        // Instancia de las subclases de Animal
        Perro perro = new Perro("Bobby");
        Gato gato = new Gato("Whiskers");

        // Llamado a la función sonido() en las instancias de las subclases
        System.out.println(perro.nombre + ": " + perro.sonido());
        System.out.println(gato.nombre + ": " + gato.sonido());

        // Instancia de las subclases de Empleado
        Gerente gerente = new Gerente(1001, "Juan Pérez", 10);
        GerenteDeProyecto gerenteProyecto = new GerenteDeProyecto(1002, "Luis Morales", "Proyecto X");
        Programador programador = new Programador(1003, "Maria García", "Java");

        // Llamado a las funciones específicas de cada subclase de Empleado
        System.out.println("Gerente: " + gerente.getNombre() + ", Cantidad de empleados: " + gerente.getCantidadEmpleados());
        System.out.println("Gerente de Proyecto: " + gerenteProyecto.getNombre() + ", Proyecto: " + gerenteProyecto.getProyecto());
        System.out.println("Programador: " + programador.getNombre() + ", Lenguaje favorito: " + programador.getLenguajeFavorito());
    }
}