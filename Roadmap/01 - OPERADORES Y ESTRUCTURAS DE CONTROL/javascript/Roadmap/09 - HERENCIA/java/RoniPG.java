import java.util.ArrayList;
import java.util.List;

// Roni
/*
 * EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.
 */
class Animal{ // --> Superclase
	protected void sonidoAnimal() {	
		System.out.println("Soy un animal que emite sonido");
	}
}
class Perro extends Animal{ // --> Subclase
	protected void sonidoAnimal() {	
		System.out.println("Soy un perro y ladro");
	}
}
class Gato extends Animal{ // --> Subclase
	protected void sonidoAnimal() {	
		System.out.println("Soy un gato y maúllo");
	}
}
public class HERENCIA_09{
	public static void main(String[] args) {
		// Instaciamos los objetos
		Animal an = new Animal();// --> Objeto Animal
		an.sonidoAnimal();// --> Llamamos a la función
		Perro perro = new Perro();// --> Objeto Perro
		perro.sonidoAnimal();// --> Llamamos a la función sobrescrita
		Gato gato = new Gato();// --> Objeto Gato
		gato.sonidoAnimal();// --> Llamamos a la función sobrescrita
		/* DIFICULTAD EXTRA (opcional):
		 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
		 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
		 * Cada empleado tiene un identificador y un nombre.
		 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
		 * actividad, y almacenan los empleados a su cargo.
		 */
		// Instaciamos los objetos
		Gerente ger1 =new Gerente(0, "A");// --> Objeto Gerente
		Gerente ger2 =new Gerente(1, "B");// --> Objeto Gerente
		Gerente_de_Proyecto gdp1 = new Gerente_de_Proyecto(3, "C");// --> Objeto Gerente de Proyecto
		Gerente_de_Proyecto gdp2 = new Gerente_de_Proyecto(4, "D");// --> Objeto Gerente de Proyecto
		Programador pgr1= new Programador(5, "E");// --> Objeto Programador
		Programador pgr2= new Programador(6, "F");// --> Objeto Programador
		// Le asignamos un empleado(Gerente de proyecto) al Gerente
		ger1.asignarEmpleado(gdp1);
		ger1.soy();// --> Llamamos a la función propia del Gerente
		// Le asignamos un Encargado(Gerente) al Gerente de proyecto
		gdp2.asignarEncargado(ger2);
		ger2.soy();// --> Llamamos a la función propia del Gerente
		// Le asignamos un empleado(Programador) al Gerente de proyecto		
		gdp1.asignarEmpleado(pgr1);
		gdp1.soy();// --> Llamamos a la función propia del Gerente de proyecto de proyecto sobrescrita
		// Le asignamos un Encargado(Gerente de proyecto) al Programador
		pgr2.asignarEncargado(gdp2);
		gdp2.soy();// --> Llamamos a la función propia del Gerente de proyecto de proyecto sobrescrita
		pgr1.soy();// --> Llamamos a la función propia del Programador de proyecto sobrescrita
		pgr2.soy();// --> Llamamos a la función propia del Programador de proyecto sobrescrita
	}
}
class Empleado{ // --> Superclase
	//Atributos heredables
	protected int identificador;
	protected String nombre;
	public Empleado(int identificador, String nombre) {
		this.identificador=identificador;
		this.nombre=nombre;
	}
	public int getIdentificador() {
		return identificador;
	}
	public void setIdentificador(int identificador) {
		this.identificador = identificador;
	}
	public String getNombre() {
		return nombre;
	}
	public void setNombre(String nombre) {
		this.nombre = nombre;
	}
}
class Gerente extends Empleado{ // --> Subclase
	//Atributos propios
	private String cargo;
	private List<Gerente_de_Proyecto> g_d_p;// --> Lista de empleados
	public Gerente(int identificador, String nombre) {
		super(identificador, nombre);
		this.g_d_p= new ArrayList<>();
		this.cargo="Gerente";
	}
	//Metodos propios
	public void asignarEmpleado(Gerente_de_Proyecto gdp) {
		this.g_d_p.add(gdp);
	}
	public void soy() {
		System.out.print("\nSoy: " +this.nombre+ "\nMi cargo es: "+ this.cargo + "\nTengo a cargo a: ");
		for(Gerente_de_Proyecto gdp : g_d_p) {
			System.out.print(" - "+gdp.nombre);
		}
	}
}
class Gerente_de_Proyecto extends Empleado{ // --> Subclase
	//Atributos propios
	private String cargo;
	private List<Programador> programadores;// --> Lista de empleados
	public Gerente_de_Proyecto(int identificador, String nombre) {
		super(identificador,nombre);
		this.programadores= new ArrayList<>();
		this.cargo="Gerente de Proyecto";
	}
	//Metodos propios
	public void asignarEncargado(Gerente ger) {
		ger.asignarEmpleado(this);;
	}
	public void asignarEmpleado(Programador pgr) {
		this.programadores.add(pgr);
	}
	public void soy() {
		System.out.print("\nSoy: " +this.nombre+ "\nMi cargo es: "+ this.cargo + "\nTengo a cargo a: ");
		for(Programador programador : programadores) {
			System.out.print( " - " + programador.nombre);
		}
	}
}
class Programador extends Empleado{ // --> Subclase
	//Atributos propios
	private String cargo;
	public Programador(int identificador, String nombre) {
		super(identificador,nombre);
		this.cargo="Programador";
	}
	//Metodos propios
	public void asignarEncargado(Gerente_de_Proyecto gdp) {
		gdp.asignarEmpleado(this);;
	}
	public void soy() {
		System.out.print("\nSoy: " +this.nombre+ "\nMi cargo es: "+ this.cargo);
	}
}
