package ejercicio09;

import java.util.ArrayList;

public class AndrewCodev {
	public static void main(String[] args) {
		Perro perro = new Perro(null, null);
		perro.setNombre("Pluto");
		perro.setRaza("Labrador");
		perro.ladra();

		System.out.println(perro.getNombre() + " - " + perro.getRaza() + " - " + perro.ladra());
		Gato gato = new Gato(null, null);
		gato.setNombre("Tom");
		gato.setRaza("Persa");
		gato.maulla();

		System.out.println(gato.getNombre() + " - " + gato.getRaza() + " - " + gato.maulla());

		System.out.println("\n");

		// Instancio la clase Gerente
		// Gerente gerente = new Gerente(null, null, null);
		ArrayList<Gerente> gerentes = new ArrayList<>();
		gerentes.add(new Gerente(1L, "Andres", "Desarrollo"));
		gerentes.add(new Gerente(2L, "Laura", "Diseño Gráfico"));
		gerentes.add(new Gerente(3L, "Luis", "Contabilidad"));
		Gerente.listarGerentes(gerentes);

		ArrayList<GerenteDeProyecto> gerentePro = new ArrayList<>();
		gerentePro.add(new GerenteDeProyecto(1L, "Diego", "Curso Java Web"));
		gerentePro.add(new GerenteDeProyecto(2L, "Ana", "Diseño de interfeces de usuario"));
		gerentePro.add(new GerenteDeProyecto(3L, "Sara", "Automatización Nómina"));
		GerenteDeProyecto.listarGerentesProyecto(gerentePro);

		ArrayList<Programador> programadorer = new ArrayList<>();
		programadorer.add(new Programador(1L, "Julio Cesar", "Roma"));
		programadorer.add(new Programador(2L, "Alejandro","Grecia"));
		programadorer.add(new Programador(3L, "Willian", "Escocia"));
		Programador.listarProgramadores(programadorer);
	}
}

//Se crea la superclase Animal
class Animal {
	private String nombre;
	private String raza;

	public Animal(String nombre, String raza) {
		super();
		this.nombre = nombre;
		this.raza = raza;
	}

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public String getRaza() {
		return raza;
	}

	public void setRaza(String raza) {
		this.raza = raza;
	}
}

//Se crea la clase perro que hereda de la Clase Animal
class Perro extends Animal {

	public Perro(String nombre, String raza) {
		super(nombre, raza);
	}

	public String ladra() {
		return "guau, guau";
	}
}

//Se crea la clase Gato que hereda de la Clase Animal
class Gato extends Animal {
	public Gato(String nombre, String raza) {
		super(nombre, raza);
	}

	public String maulla() {
		return "miau, miau";
	}
}

//DIFICULTAD EXTRA

class Empleado {
	private Long idEmpleado;
	private String nombre;

	public Empleado(Long idEmpleado, String nombre) {
		super();
		this.idEmpleado = idEmpleado;
		this.nombre = nombre;
	}

	public Long getIdEmpleado() {
		return idEmpleado;
	}

	public void setIdEmpleado(Long idEmpleado) {
		this.idEmpleado = idEmpleado;
	}

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}
}

class Gerente extends Empleado {
	String area;

	public Gerente(Long idEmpleado, String nombre, String area) {
		super(idEmpleado, nombre);
		this.area = area;
	}

	public String getArea() {
		return area;
	}

	public void setArea(String area) {
		this.area = area;
	}

	public static void listarGerentes(ArrayList<Gerente> gerentes) {
		System.out.println("\nLISTA DE GERENTES DE LA EMPRESA");
		for (int i = 0; i < gerentes.size(); i++) {
			System.out.println("Área: " + gerentes.get(i).getArea() + " | Gerente: " + gerentes.get(i).getNombre());
		}
	}
	
	public static void contratarEmpleados() {
		System.out.println("Vas a contratar un nuevo empleado");
	}
	
	public static void nuevoProyecto() {
		System.out.println("Creando nuevo proyecto");
	}
}

class GerenteDeProyecto extends Empleado {
	String proyecto;

	public GerenteDeProyecto(Long idEmpleado, String nombre, String proyecto) {
		super(idEmpleado, nombre);
		this.proyecto = proyecto;
	}

	public String getProyecto() {
		return proyecto;
	}

	public void setProyecto(String proyecto) {
		this.proyecto = proyecto;
	}

	public static void listarGerentesProyecto(ArrayList<GerenteDeProyecto> gerentePro) {
		System.out.println("\nLISTA DE GERENTES DE PROYECTOS");
		for (int i = 0; i < gerentePro.size(); i++) {
			System.out.println(
					"Proyecto: " + gerentePro.get(i).getProyecto() + " | Gerente: " + gerentePro.get(i).getNombre());
		}
	}
	
	public static void asignarDesarrollador() {
		System.out.println("Asignando nuevo desarrollador al equipo y proyecto");
	}
}

class Programador extends Empleado {
	String equipoDeTrabajo;

	public Programador(Long idEmpleado, String nombre, String equipoDeTrabajo) {
		super(idEmpleado, nombre);
		this.equipoDeTrabajo = equipoDeTrabajo;
	}

	public String getEquipoDeTrabajo() {
		return equipoDeTrabajo;
	}

	public void setEquipoDeTrabajo(String equipoDeTrabajo) {
		this.equipoDeTrabajo = equipoDeTrabajo;
	}

	public static void listarProgramadores(ArrayList<Programador> programadores) {
		System.out.println("\nLISTA DE PROGRAMADORES");
		for (int i = 0; i < programadores.size(); i++) {
			System.out.println("Equipo de trabajo: " + programadores.get(i).getEquipoDeTrabajo() + " | Programador: "
					+ programadores.get(i).getNombre());
		}
	}
	
	public static void desarrollarAplicacion() {
		System.out.println("Iniciando el desarrollo de la app para el equipo");
	}
}
