import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

// @Roni
/*
 * EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
 */
class Iguana{
	private String genero;
	private String endemico;
	private String especie;
	public Iguana(String genero, String endemico, String especie){
		this.genero=genero;
		this.endemico=endemico;
		this.especie=especie;
	}
	public Iguana(){
		this.genero="";
		this.endemico="";
		this.especie="";
	}
	public String getGenero() {
		return genero;
	}
	public void setGenero(String genero) {
		this.genero = genero;
	}
	public String getEndemico() {
		return endemico;
	}
	public void setEndemico(String endemico) {
		this.endemico = endemico;
	}
	public String getEspecie() {
		return especie;
	}
	public void setEspecie(String especie) {
		this.especie = especie;
	}
	public void print() {
		System.out.println("Genero: "+this.genero+ "\nEndemico: "+this.endemico+"\nEspecie :"+this.especie);
	}
}
public class CLASES_08{
	
	public static void main(String[] args) {
		
		Iguana ig1 = new Iguana(); // --> Instanciamos/Incicalizamos la clase
		/*Le asignamos los valores*/
		System.out.println("****IGUANA****");
		ig1.setGenero("Macho");
		ig1.setEndemico("Sudamerica");
		ig1.setEspecie("Iguana");
		ig1.print(); // --> Llamamos al método que nos devolvera los valores		
		System.out.println("****PILA****");
		Pila pila = new Pila(); // --> Instanciamos/Incicalizamos la clase
		/*Le asignamos los valores*/
		pila.añadirDatos(1);		pila.añadirDatos(2);		pila.añadirDatos(3);
		System.out.println("El número de elementos es: "+pila.numeroDeElementos()); // --> Imprimimos números de elementos
		System.out.print("Su contenido es:\n"); pila.print(); // --> Imprimimos todos los datos
		pila.elminarDatos(); // --> Eliminamos elemento de arriba de la pila
		System.out.println("El número de elementos despúes de pila.elminarDatos(): "+pila.numeroDeElementos());
		System.out.print("Su contenido despúes de pila.elminarDatos():\n"); pila.print();
		pila.elminarDatos();
		pila.elminarDatos();
		pila.elminarDatos(); // --> Salta el aviso
		System.out.println("****COLA****");
		Cola cola= new Cola(); // --> Instanciamos/Incicalizamos la clase
		/*Le asignamos los valores*/
		cola.añadirDatos("Elemento 0");		cola.añadirDatos("Elemento 1");		cola.añadirDatos("Elemento 2");
		System.out.println("El número de elementos es: "+cola.numeroDeElementos()); // --> Imprimimos números de elementos
		System.out.print("Su contenido es:\n"); cola.print(); // --> Imprimimos todos los datos
		cola.elminarDatos(); // --> Eliminamos elemento de la cabeza de la cola
		System.out.println("El número de elementos despúes de cola.elminarDatos(): "+cola.numeroDeElementos());
		System.out.print("Su contenido despúes de cola.elminarDatos():\n"); cola.print();
		cola.elminarDatos();
		cola.elminarDatos();
		cola.elminarDatos(); // --> Salta el aviso
	}
}
 /*
 * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola 
 * (estudiadas en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
 */
class Pila{
	private Stack<Integer> datos;
	public Pila() {
	 this.datos=new Stack<>();
	}
	public void añadirDatos(int dato) {
		this.datos.push(dato);
	}
	public void elminarDatos() {
		if (!datos.empty()) {
			this.datos.pop();
		}else {
			System.out.println("La pila esta vacía");
		}		
	}
	public int numeroDeElementos() {
		return datos.size();
	}
	public void print() {
		int i=0;
		for (Integer dato : datos) {
			i++;
			System.out.println("Dato "+i+"= "+dato);
		}
	}
}
class Cola{
	private Queue<String> datos;
	public Cola() {
	 this.datos=new LinkedList<>();	
	}
	public void añadirDatos(String dato) {
		this.datos.offer(dato); // --> También podríamos utilizar datos.add(dato);
	}
	public void elminarDatos() {
		if (!datos.isEmpty()) {
			this.datos.poll();
		}else {
			System.out.println("La pila esta vacía");
		}		
	}
	public int numeroDeElementos() {
		return datos.size();
	}
	public void print() {
		int i=0;
		for (String dato : datos) {
			i++;
			System.out.println("Dato "+i+"= "+dato);
		}
	}	
}
