package ejercicio09;

import java.util.ArrayList;
import java.util.List;

/*
* EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.
 */
public class JesusWay69 {

    public static void main(String[] args) {
        Perro perro = new Perro();
        Gato gato = new Gato();
        Vaca vaca = new Vaca();
        Gerente gerente = new Gerente();
        GerenteProyectos gerenteproyectos = new GerenteProyectos();
        Programador programador = new Programador();

        perro.print(perro.animal, perro.sonido);
        gato.print(gato.sonido, gato.animal);
        vaca.print(vaca.sonido, vaca.animal);
        System.out.println("");

        String[] nombres = {"Carlos", "Ana", "Francisco", "Paula", "Felipe", "Ainhoa", "Jesus", "Raquel", "Álvaro"};
        List<String> empleadosGerencia = new ArrayList<>();
        List<String> empleadosProyectos = new ArrayList<>();
        for (int i = 1; i <= nombres.length; i++) {
            if (i > 2 && i <= nombres.length) {
                empleadosGerencia.add(nombres[i - 1]);
            }
            if (i > 5 && i <= nombres.length) {
                empleadosProyectos.add(nombres[i - 1]);

            }
        }

        for (int i = 1; i <= nombres.length; i++) {
            if (i > 0 && i < 3) {
                gerente.print(i, nombres[i - 1], gerente.cargo);
                gerente.print(empleadosGerencia);
            } else if (i > 2 && i < 6) {
                gerenteproyectos.print(i, nombres[i - 1], gerenteproyectos.cargo);
                gerenteproyectos.print(empleadosProyectos);

            } else {
                programador.print(i, nombres[i - 1], programador.cargo);

            }

        }

    }

}

abstract class Animal {

    public String animal;
    public String sonido;
    private String articulo;

    public Animal() {

        articulo = "El";
    }

    protected void print(String sonido, String animal) {
        if (animal.charAt(animal.length() - 1) == 'a') {
            articulo = "La";
        }
        System.out.println(articulo + " " + animal + " " + sonido);

    }

}

class Perro extends Animal {

    public Perro() {
        this.animal = "perro";
        this.sonido = "ladra";
    }

    @Override
    public void print(String sonido, String animal) {
        super.print("ladra", "perro");
    }

}

class Gato extends Animal {

    public Gato() {
        this.animal = "gato";
        this.sonido = "maulla";
    }
}

class Vaca extends Animal {

    public Vaca() {
        this.animal = "vaca";
        this.sonido = "muge";
    }
}


/*
 * DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.
 */
abstract class Empleado {

    public String finanzas = "NO";
    public String compras = "NO";
    public String proyectos = "NO";
    public String organizacion = "NO";
    public String programacion = "NO";
    public String despliegue = "NO";
    public int id;
    public String nombre;
    public String cargo;

    public Empleado() {

    }

    protected Empleado(int id, String nombre) {
        this.id = id;
        this.nombre = nombre;
    }

    protected Empleado(int id, String nombre, String cargo) {
        this.id = id;
        this.nombre = nombre;
        this.cargo = cargo;
    }

    protected void print(int id, String nombre, String cargo) {
        System.out.println("\nID: " + id + "\nnombre: " + nombre + "\ncargo: " + cargo + "\nHace finanzas? " + finanzas
                + "\nHace compras? " + compras + "\nHace proyectos? " + proyectos + "\nOrganiza el trabajo? " + organizacion
                + "\nPica código? " + programacion + "\nDespliega programas? " + despliegue);
    }

    protected void print(List listaEmpleados) {

        System.out.print("Empleados a su cargo: ");
        for (int i = 0; i < listaEmpleados.size() - 1; ++i) {
            System.out.print(listaEmpleados.get(i) + ((i != listaEmpleados.size() - 2) ? " , " : " y "));
        }
        System.out.println(listaEmpleados.get(listaEmpleados.size() - 1));
    }

}

class Gerente extends Empleado {

    protected Gerente() {
        this.compras = "SI";
        this.finanzas = "SI";
        this.cargo = "Gerente";
    }

}

class GerenteProyectos extends Empleado {

    protected GerenteProyectos() {
        this.organizacion = "SI";
        this.proyectos = "SI";
        this.cargo = "Gerente de proyectos";
    }

}

class Programador extends Empleado {

    protected Programador() {
        this.programacion = "SI";
        this.despliegue = "SI";
        this.cargo = "Programador";
    }

}
