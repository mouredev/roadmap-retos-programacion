package Cadena_de_Caracteres_04;
import java.util.ArrayList;
import java.util.Scanner;
import java.util.Dictionary;
import java.util.HashMap;
import java.util.Hashtable;


/*
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 */


public class Cadena_de_Caracteres {

	public static void main(String[]args) {
		
		//OPERACIONES BASICAS
		
		// Concatenar
		String string_1 = "cadena 1";
		String string_2 = "cadena 2";
		String string_3 = " segundo elemento";

		System.out.println(string_1 + " más " + string_2);
		System.out.println(string_1.concat(string_3)); // Método CONCAT
		
		//Indexar
		String string_4 = "elemento";
		System.out.println(string_4.indexOf("m"));//Por caracter
		
		
		
		// METODOS ESPECIALES
		
		String cadena_1 = "Hola mundo";
		String cadena_2 = "HELLO";
		String cadena_3 = "MINUSCULAS";
		String cadena_4 = "mayusculas";
		String cadena_5 = "Esta es una cadena";
		String cadena_6 = "Caracter";
		String cadena_7 = "Listado de caracteres";
		
		//Método charAt, retorna un carácter a partir de un indice
 		System.out.println("---- METODO CHAR AT ----");
		System.out.println(cadena_1.charAt(3));

		//Método Length cuenta la cantidad de caracteres de una string
 		System.out.println("---- METODO LENGTH ----");
		System.out.println(cadena_1.length());
		
		//Método Replace cuenta la cantidad de caracteres de una string
 		System.out.println("---- METODO REPLACE ----");
		System.out.println(cadena_2.replace("L", "R"));
		
		//Método ToLowerCase convierte los caracteres en mayusculas a minusculas
 		System.out.println("---- METODO LOWERCASE ----");
 		System.out.println(cadena_3.toLowerCase());

		//Método ToUperCase convierte los caracteres en minusculas a mayusculas
 		System.out.println("---- METODO UPPERCASE ----");
 		System.out.println(cadena_4.toUpperCase());
 		
 		//Método Split, convierte una cadena en unas serie de subcadenas en formato array
 		System.out.println("---- METODO SPLIT ----");
 		String [] split_1 = cadena_5.split(" "); //Creamos un array y dividimos la cadena a partir de un caracter espacio(" ")
 		String part_1 = split_1[1]; // Podemos guardar los valores del array en variables
 		
 		System.out.println(split_1[0]);
 		System.out.println(part_1);
 		System.out.println(split_1[2]);
 		System.out.println(split_1[3]);

 		//Metodo endsWith, nos permite saber si una cadena termina con uno o varios caracteres especificos, devuelve true o false
 		System.out.println("---- METODO ENDSWITH ----");
 		System.out.println(cadena_6.endsWith("Cara"));
 		System.out.println(cadena_6.endsWith("ter"));
 		System.out.println(cadena_6.endsWith("r"));
 		
 		//Metodo startsWith, a diferencia de endsWith nos permite saber si una cadena empieza con uno o varios caracteres especificos
 		System.out.println("---- METODO STARTSWITH ----");
 		System.out.println(cadena_6.startsWith("Car"));
 		System.out.println(cadena_6.startsWith("ter"));
 		System.out.println(cadena_6.startsWith("C"));
 		
 		//Metodo getChars, junta un grupo de caracteres en un array 
		char[] ch = new char[7]; //En la declaración del array especificamos la cantidad de caracteres si la string tiene más se muestran espacios en blanco
 		cadena_7.getChars(0, 7, ch, 0); // (caracte-inicial, caracter-final, array, desfase)
 		System.out.println(ch);
 		
 		
		// OPERACIONES
 		
 		//Reversa a una cadena, invertimos el orden de una cadena
 		System.out.println("-------- OPERACION REVERSA -------");
 		String cadenaOriginal = "Cadena al reves";
 		String cadenaReversa = "";
 		
 		for (int i = 0; i < cadenaOriginal.length(); i++) {
 			System.out.println(cadenaOriginal.charAt(i));
 			cadenaReversa = cadenaOriginal.charAt(i) + cadenaReversa;
 		}
 		System.out.println(cadenaReversa);
 		
 		
 		/*
 		* DIFICULTAD EXTRA (opcional):
 		* Crea un programa que analice dos palabras diferentes y realice comprobaciones
 		* para descubrir si son:
 		* - Palíndromos
 		* - Anagramas
 		* - Isogramas
 		*/
 		
 		// ---------- PALINDROMO ---------
 		Scanner palindromo = new Scanner(System.in);
 		System.out.println("Frase:");
 		String palindromo_1 = palindromo.nextLine();
 		String frase_reves = "";
 		String frase_sinEspacios = "";
 		
 		//Pasamos todas las letras a minusculas
 		String palindromo_op = palindromo_1.toLowerCase();
 		
 		//Invierte la frase
 		for (int l=0; l < palindromo_op.length(); l++) {
 			if (palindromo_1.charAt(l) == ' ') {
 				continue;
 			}else if (palindromo_op.charAt(l) != ' ') {
 				frase_reves = palindromo_op.charAt(l) + frase_reves;
 			}
 		}
 		
 		//Frase original sin espacios (invertimos la frase que ya habiamos invertido, esta vez sin espacios)
 		for (int s=0; s < frase_reves.length(); s++){
 			frase_sinEspacios = frase_reves.charAt(s) + frase_sinEspacios;
 		}
 		
 		
 		System.out.println(palindromo_op);
 		System.out.println(frase_sinEspacios);
 		System.out.println(frase_reves);
 		
		if (frase_sinEspacios.equals(frase_reves)) { //CUANDO QUEREMOS COMPARAR EL CONTENIDO DE 2 CADENAS DEBEMOS USAR EL METODO EQUALS()
 			System.out.println("La frase es un palindromo");
 		}else {
 			System.out.println("La frase no es un palindromo ");
 		}
		
		/* Si hacemos una comparación tradicional "if(cadena_1 == cadena_2)"
		 * lo que estamos haciendo es comparar si la instancia es la misma,
		 * sin embargo la instancia no es la misma
		 * 
		 * (instancia) String frase_reves es distinto a (instancia) String palindromo_1 
		 * 
		 * la forma correcta de evaluar si el contenido de 2 cadenas es el mismo es por medio del
		 * método equals()
		 * 
		 * */
				
 		// ---------- ANAGRAMA ---------
				
		//Entregar 2 palabras y ver si una es un anagrama de la otra
		
		//Entrada de palabras
		Scanner palabra_1 = new Scanner(System.in);
		System.out.println("Palabra 1: ");
		String word_1 = palabra_1.nextLine();
		
		Scanner palabra_2 = new Scanner(System.in);
		System.out.println("Palabra 2: ");
		String word_2 = palabra_2.nextLine();
		
		anagrama(word_1, word_2);

 		// ---------- ISOGRAMA ---------
		
		Scanner palabra_3 = new Scanner(System.in);
		System.out.println("Palabra 3: ");
		String word_3 = palabra_3.nextLine();
		
		
		System.out.println(isograma(word_3));
		
		
		Scanner palabra_4 = new Scanner(System.in);
		System.out.println("Palabra 4: ");
		String word_4 = palabra_4.nextLine();
		
		System.out.println(isograma_2(word_4));
		
	}
	
	public static String anagrama(String cadena_1, String cadena_2) {
		
		String cadena_1_toLow;
		String cadena_2_toLow;
		
		//Convertimos las cadenas originales a minusculas
		cadena_1_toLow = cadena_1.toLowerCase(); //Guardamos la primera cadena con todos los caracteres en  minusculas
		cadena_2_toLow = cadena_2.toLowerCase(); //Guardamos la segunda cadena con todos los caracteres en  minusculas

		//Obtenemos el largo de cada cadena
		int cadena_1len = cadena_1.length();
		int cadena_2len = cadena_2.length();
		int counter = 0;
		int charCounter = 0;
		
		ArrayList<Character> letra_cadena_1 = new ArrayList<Character>();
		ArrayList<Character> letra_cadena_2 = new ArrayList<Character>();
		
		for(int c=0; c < cadena_1len; c++) { //Para añadir caracteres de la primera palabra en una lista
			letra_cadena_1.add(cadena_1_toLow.charAt(c));
		}
		for(int d = 0; d < cadena_2len; d++) { //Para añadir caracteres de la segunda palabra en una lista
			letra_cadena_2.add(cadena_2_toLow.charAt(d));
		}
		
		//Recorremos la segunda cadena a partir de cada caracter de la primera cadena
		if(cadena_1len == cadena_2len){
			for(int e = 0; e < cadena_1len; e++) {
				charCounter = 0;
				for(int f = 0; f < cadena_2len; f++) {
					if(cadena_1_toLow.charAt(e) == cadena_2_toLow.charAt(f)) {
						//System.out.println("Element " + cadena_1_toLow.charAt(e) + " is in both strings");
						charCounter += 1;
						counter += 1;
						//Esta sección reduce en 1 el contador si se repite más de una vez //Resolver que no se repita la impresión del mismo caracater 2 veces
						if(charCounter > 1) {
							counter -= 1;
						}
						else {
							System.out.println("Element " + cadena_1_toLow.charAt(e) + " is in both strings");
						}
					}
					else {
						continue;
					}	
				}
				//System.out.println(charCounter);
			}
			
			//Establecemos que 2 palabras son anagramas si tienen los mismos caracteres
			
			if (counter == cadena_1len) {
				System.out.println("The strings are anagrams");
			}else {
				System.out.println("The strings are not anagramas");
			}
		}else {
			System.out.println("The strings are not anagramas");
		}
		
		System.out.println("Length of both strings: " + cadena_1len + " and " + cadena_2len); 
		System.out.println("Characters that coincide: " + cadena_1len + " and " + counter); //Counter difiere del largo de la primera cadena si hay caracteres repetidos

		
		return "La palabra es un anagrama";
	}
	
	
		// ---------- ISOGRAMA ---------

	//Entregar 1 palabra y ver si se repiten la misma cantidad de veces cada una de sus letras
	
	//Señalamos que el resultado a retornar es un Diccionario
	public static Dictionary isograma(String cadena_3) {
		String cadena_3_low;
		cadena_3_low = cadena_3.toLowerCase();
		
		Dictionary<Character, Integer> dictCaracteres = new Hashtable<>();
		
		for(int i=0; i < cadena_3_low.length(); i++) {
				dictCaracteres.put(cadena_3_low.charAt(i), 1);
		}
		
		return dictCaracteres;
	}
	
	
	//Señalamos que el resultado a retornar es un HashMap

	public static HashMap isograma_2(String cadena_3) {
		String cadena_4_low;
		cadena_4_low = cadena_3.toLowerCase();
		
		HashMap<Character, Integer> hashMapCaracteres = new HashMap<>();
		
		for(int i=0; i < cadena_4_low.length(); i++) {
			for(int e=0; e < cadena_4_low.length(); e++) {
				if(cadena_4_low.charAt(i) == hashMapCaracteres.get(e)) {
					hashMapCaracteres.put(cadena_4_low.charAt(i), 1);
				}else {
					hashMapCaracteres.put(cadena_4_low.charAt(i), 2);
				}
			}
			//hashMapCaracteres.put(cadena_4_low.charAt(i), 1);
//			if(cadena_4_low.charAt(i) == hashMapCaracteres.get(cadena_4_low.charAt(i))) { //Buscar método que verifique que un elemento está en el diccionario
//				hashMapCaracteres.put(cadena_4_low.charAt(i), 1);
//			}
		}
		
		return hashMapCaracteres;
	}
	
}
