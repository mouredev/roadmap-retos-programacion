// @Roni

import java.util.Arrays;
import java.util.Iterator;
import java.util.Set;
import java.util.TreeSet;
import java.util.stream.IntStream;
import java.util.stream.Stream;

public class CADENAS_DE_CARACTERES_04 {

	public static void main(String[] args) {
			
		//Crear una cadena de caracteres
		
		String ejemplo = "Hola Mundo";
		String ejemplo2; ejemplo2 = "Hello World"; // --> Otra manera de crear
		
		//Mostrar cracter por su posicion
		
		System.out.println(ejemplo.charAt(0)); // --> Mostrar el caracater en la posicion 0 de la cadena
		System.out.println(ejemplo.codePointAt(0)); // --> Mostrar el valor del caracter en la posicion 0 de la cadena en codigo Unicode
		System.out.println(ejemplo.codePointBefore(4)); // --> Mostrar el valor del caracter en la posicion (4-1) de la cadena en codigo Unicode 
		System.out.println(ejemplo.compareTo(ejemplo2)); // --> Comparamos dos cadenas de caracteres mediante el codigo Unicode para determinar 
																//cual es mayor
		System.out.println(ejemplo.compareToIgnoreCase(ejemplo2)); // --> Comparamos dos caracteres o cadenas de caracteres, sin tener encuenta
														      //las mayusculas/minusculas, mediante el codigo Unicodepara determinar cual es mayor
		System.out.println(ejemplo.concat(ejemplo2)); // --> Concatenamos dos cadenas de caracteres
		System.out.println(ejemplo.contains("Hola")); // --> Comprueba si dentro de la cadena de caracteres se encuentran los mismos caracteres
														//que en el parametro dado
		System.out.println(ejemplo.contentEquals(ejemplo2)); // --> Comprueba si dos cadenas de caracteres son exactamente iguales
		System.out.println(ejemplo.endsWith("Mundo")); // --> Comprueba si la cadena de caracteres termina igual que la cadena que le pasemos
		System.out.println(ejemplo.equals(ejemplo2)); // --> Comprueba que la cadenas de caracteres sea exactamente igual en contenido a 
															// un objeto de tipo string
		System.out.println(ejemplo.equalsIgnoreCase("HoLa mUnDo")); // --> Comprueba que la cadenas de caracteres sea exactamente igual en contenido 
																	// a un objeto de tipo string sin tener en cuenta las mayusculas/minusculas
		System.out.println(ejemplo.getBytes()); // --> Devuelve un array de bytes a partir de la cadena de caracteres
		System.out.println(ejemplo.hashCode()); // --> Devuelve el un codigo(hashCode) generado apartir de la cadena de caracteres
		System.out.println(ejemplo.indent(5)); // --> Devuelve la cadena de caracteres con espacios en blanco al principio que le indiquemos como parametro
		System.out.println(ejemplo.indexOf('o')); // --> Devuelve la primera posicion del caracter indicado dentro de la cadena de caracteres
		System.out.println(ejemplo.indexOf("la")); // --> Devuelve la primera posicion de la cadena de caracteres que coincida con la cadena de caracteres
													// del parametro
		System.out.println(ejemplo.indexOf('o', 3)); // --> Devuelve la primera posicion del caracter indicado apartir de la posicion indicada y que si se 
													// encuentra dentro de la cadena de caracteres
		System.out.println(ejemplo.indexOf("la", 6)); // --> Devuelve la primera posicion del la cadena de caracteres que coincida con la cadena de caracteres
													//del parametro apartir de la posicion indicada
		System.out.println(ejemplo.isBlank()); //Devuelve True si la cadena de caracteres esta compuesta de espacios en blanco, o si no contiene nada.
		System.out.println(ejemplo.isEmpty()); //Devuelve True si la cadena de caracteres no contiene nada (si ejemplo.length()==0).
		System.out.println(ejemplo.lastIndexOf('o')); // --> Devuelve la ultima posicion del caracter indicado dentro de la cadena de caracteres
		System.out.println(ejemplo.lastIndexOf("la")); // --> Devuelve la ultima posicion de la cadena de caracteres que coincida con la cadena de caracteres
													// del parametro
		System.out.println(ejemplo.lastIndexOf('o',3)); // --> Devuelve la primera posicion del caracter indicado apartir de la posicion indicada
														//(en orden inverso)y si se encuentra dentro de la cadena de caracteres
		System.out.println(ejemplo.lastIndexOf("la", 6)); // --> Devuelve la posicion del la cadena de caracteres que coincida con la cadena de caracteres
													//del parametro apartir de la posicion indicada en orden inverso
		System.out.println(ejemplo.length()); // --> Devuelve el tamaño de la cadena de caracteres
		System.out.println(ejemplo.matches("(.*)un(.*)")); // --> Busca dentro de la cadena de caracteres mediante Expresiones Regulares (RegEx)
		System.out.println(ejemplo.repeat(2)); // --> Devuelve la cadena de caracteres repetida tanta veces como le indiquemos
		System.out.println(ejemplo.replace('o','e')); // --> Reemplaza el primer caracter por el segundo en toda la cadena de caracteres
		System.out.println(ejemplo.replace(ejemplo, ejemplo2)); // --> Reemplaza la primera cadena de caracteres por la segunda
		System.out.println(ejemplo.replaceAll("un", "dos")); //  --> Reemplaza la primera cadena de caracteres por la segunda utilizando la busqueda RegEX
		System.out.println(ejemplo.replaceFirst("o", "i")); // --> Reemplaza la primera cadena de caracteres por la segunda en la primera coincidencia
		System.out.println(ejemplo.startsWith("Ho")); // --> Devuelve True si la cadena de caracteres empieza exactamente igual que la cadena de caracteres del parametro, 
														// si el paramero esta vacio, o es .equals() a la cadena de caracteres
		System.out.println(ejemplo.startsWith("la", 1)); // --> Devuelve True si la cadena de caracteres empieza exactamente igual que la cadena de caracteres del parametro 
														// y en el indice indicado, si el paramero esta vacio, o es .equals() a la cadena de caracteres
		System.out.println("		Ejemplo\s\s\s\s".strip()); // --> Devuelve la cadena de caracteres sin los espacios en blanco del principio y del final
		System.out.println("    Hola\n        Mundo\n    Adios".stripIndent()); // --> Devuelve la cadena de caracteres sin los espacios en blanco del principio de cada 
																				  //linea y que coincidan en tamaño.
		System.out.println("		Ejemplo".stripLeading()); // --> Devuelve la cadena de caracteres sin los espacios en blanco del principio.
		System.out.println("Ejemplo		".stripTrailing()); // --> Devuelve la cadena de caracteres sin los espacios en blanco del final.
		System.out.println(ejemplo.substring(4)); // --> Devuelve una cadena de cararacteres apartir del indice dado
		System.out.println(ejemplo.substring(1, 4)); // --> Devuelve una cadena de cararacteres apartir del primer indice hasta el segundo indice.
		System.out.println(ejemplo.toCharArray()); // --> Devuelve un array de caracteres (no asignable a un String/cadena de caracteres)
		System.out.println(ejemplo.toLowerCase()); // --> Devuelve una la cadena de caracteres en minuscula
		Integer num = 5;
		System.out.println(num.toString()); // --> Devuelve la representacion en cadena de caracteres de un objeto
		System.out.println(ejemplo.toUpperCase()); // --> Devuelve una la cadena de caracteres en mayuscula
		System.out.println(ejemplo.translateEscapes()); // --> Traduce los escapes de teclado ej:"\u005Cn"(salto de linea)
		System.out.println("		Ejemplo\s\s\s\s".trim()); // --> Devuelve la cadena de caracteres sin los espacios en blanco del principio y del final
		System.out.println(ejemplo.getClass()); // --> Devuelve la clase del objeto
		String [] split = ejemplo.split(" ");// --> Devuelve un array de cadenas de caracteres divididos por la cadena de caracteres que le indiquemos
		System.out.println("Primera posicion del array: "+split[0]+"\nSegunda posicion del array: "+split[1]);
		split = ejemplo.split("o",2);// --> Devuelve un array de cadenas de caracteres divididos por la cadena de caracteres que le indiquemos y 
									// con un indice del maximo de divisiones que queremos realizar
		System.out.println("Primera posicion del array: "+split[0]+"\nSegunda posicion del array: "+split[1]);
		System.out.println(ejemplo.subSequence(2, 8)); // --> Devuelve una cadena de cararacteres apartir del primer indice hasta el segundo indice.
		Stream<String> lines = "Hola\nNuevo\nMundo".lines(); // --> Devuelve un stream de líneas extraídas de la cadena de caracteres, separadas por terminadores de línea.
		lines.forEach(System.out::println);
		
		/* DIFICULTAD EXTRA (opcional):
		 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
		 * para descubrir si son:
		 * - Palíndromos
		 * - Anagramas
		 * - Isogramas
		 */
		Palindromo("Anilina");
		Anagrama("Roma","Ramo");
		Isograma("Acondicionar");
	}		
	public static void Palindromo(String a) {
		/* Palindromo: 
		 * Palabra o frase cuyas letras están dispuestas de tal manera que resulta la misma leída de izquierda a derecha que de derecha a izquierda.
		 * Por ejemplo: anilina
		 */
		String aux="";
		for(int i = a.length()-1; i>=0 ; i--) {
			aux += a.charAt(i);
		}
		if(aux.equalsIgnoreCase(a)) {
			System.out.println("\nSon Palabras Palindromas");
		}else {
			System.out.println("No son palabras Palindromas");
		}
	}
	public static void Anagrama(String a, String b) {
		/* Anagrama:
		 * Cambio en el orden de las letras de una palabra o frase que da lugar a otra palabra o frase distinta.
		 * Por ejemplo: Amor --> Roma
		 */
		char[] a1= a.toLowerCase().toCharArray();
		char[] b1= b.toLowerCase().toCharArray();
		Arrays.sort(a1);
		Arrays.sort(b1);
		String sortA="";
		String sortB="";
		for (int i = 0; i < a1.length; i++) {
			sortA += a1[i];
		}
		for (int i = 0; i < b1.length; i++) {
			sortB += b1[i];
		}
		if (a.length()!= b.length()) {
			System.out.println("No son anagramas");
		}
		else if (sortA.equals(sortB)) {
			System.out.println("Son anagramas");
		}
		else {
			System.out.println("No son anagramas");
		}
	}
	public static void Isograma(String a) {
		/* Un isograma es una palabra o frase en la que cada letra aparece el mismo número de veces.
		 * Si cada letra aparece solo una vez será un heterograma, si aparece dos, un isogroma de segundo orden y así sucesivamente.
		 * Por ejemplo:
		 * Heterogramas: yuxtaponer, centrifugado, luteranismo.
		 * Isogramas con una repetición o de segundo orden: acondicionar, escritura, intestinos.
		 */
		boolean flag= false;
		int count=0;
		TreeSet<Character> subA = new TreeSet<>();
		for (int i = 0; i < a.length(); i++) {
			subA.add(a.charAt(i));
		}
		for (Character character : subA) {
			for (int i = 0; i < a.length(); i++) {
				if (character.equals(a.charAt(i))) {
					count++;					
				}				
			}
			System.out.println("La letra: \""+character+"\" esta repetida: "+count+" veces.");
			if (count>1) {
				flag=true;
			}
			count=0;
		}
		if(flag) {
			System.out.println("Es un isograma");
		}else {
			System.out.println("Es un heterograma");
		}				
	}
}
