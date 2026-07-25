public class RodrigoGit87 {

    // Superclase
    public static class Animal {
        protected String nombre, genero;

        // Constructor
        public Animal(String nombre, String genero) {
            this.nombre = nombre;
            this.genero = genero;
        }

        // Metodo
        public void emitirSonido() {
        }
    }

    // Subclase
    public static class Perro extends Animal {
        String tamaño;

        // Constructor
        public Perro(String nombre, String genero) {
            super(nombre, genero);
        }

        // Metodo sobreescrito
        @Override
        public void emitirSonido() {
            System.out.println("Guau guau");
        }

        public String getTamaño() {
            return tamaño;
        }

        public void setTamaño(String tamaño) {
            this.tamaño = tamaño;
        }
    }

    // Subclase
    public static class Gato extends Animal {
        String pelaje;

        // Constructor
        public Gato(String nombre, String genero, String pelaje) {
            super(nombre, genero);
            this.pelaje = pelaje;
        }

        // Metodo sobreescrito
        @Override
        public void emitirSonido() {
            System.out.println("Miau miau");
        }
    }

    // ----------------- EXTRA ------------------
    // Superclase
    public static class Empleado { // Empleado podría ser una clase abstracta, de la cual crear las subclases con
                                   // sus respectivos constructores y metodos sobreescritos y/o propios. para el
                                   // ejercicio, es una clase normal
        protected String nombre;
        protected String apellidos;
        protected String dni;
        protected int edad;

        // Constructor
        public Empleado(String nombre, String apellidos, String dni, int edad) {
            this.nombre = nombre;
            this.apellidos = apellidos;
            this.dni = dni;
            this.edad = edad;
        }

        // metodo
        public String trabajar() {
            return "";
        }

        // Subclase Gerente
        public static class Gerente extends Empleado {
            private String zona;

            public Gerente(String nombre, String apellidos, String dni, int edad, String zona) {
                super(nombre, apellidos, dni, edad);
                this.zona = zona;
            }

            @Override
            public String trabajar() {
                return "El gerente " + nombre + " " + apellidos + "\nSupervisa a programadores de la zona " + zona;
            }

        }

        // Subclase Programadores
        public static class Programadores extends Empleado {
            protected String cargo, lenguaje;
            protected int horasTrabajadas;

            // constructor
            public Programadores(String nombre, String apellidos, String dni, int edad, String cargo, String lenguaje) {
                super(nombre, apellidos, dni, edad);
                this.cargo = cargo;
                this.lenguaje = lenguaje;
            }

            public int getHoras() {

                return horasTrabajadas;
            }

            public void setHoras(int horas) {
                this.horasTrabajadas = horas;
            }

            // metodo sobreescrito
            @Override
            public String trabajar() {
                return " El programador " + nombre + " " + apellidos + " trabaja con el lenguaje, " + lenguaje
                        + ", tiene el puesto de: "
                        + cargo + ".\n Lleva " + horasTrabajadas + " horas trabajadas";
            }

        }

    }

    // ----------- main ----------------
    public static void main(String[] args) {
        var perro = new Perro("Fido", "macho");
        perro.setTamaño(" mediano ");
        IO.println("El perro es de tamaño" + perro.getTamaño());

        var gato = new Gato("Garfield", " macho", " naranja");

        perro.emitirSonido();
        gato.emitirSonido();

        // ------------------ extra ------------------
        var gerente = new Empleado.Gerente("Bruce", "Wayne", "12345678A", 30, "Sur");
        var programador = new Empleado.Programadores("Peter", "Parker", "87654321B", 25, "Junior", "Java");

        IO.println(gerente.trabajar());
        System.out.println("----------------");
        programador.setHoras(10);
        IO.println(programador.trabajar());

    }

}
