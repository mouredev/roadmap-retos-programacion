import java.util.*;

public class AndrewCodev {
	public static void main(String[] args) {

		AndrewCodev andrewCodev = new AndrewCodev();
		// CONCATENACIÓN con operador +
		String cadena1 = "Andrew";
		String cadena2 = "Codev";

		System.out.println("Concatenando: " + cadena1 + " + " + cadena2 + " = " + cadena1 + cadena2);

		// OBTENER LONGITUD con length()
		String cadena3 = cadena1 + cadena2;
		System.out.println("La palabra: " + cadena3 + " tiene " + (cadena1 + cadena2).length() + " caracteres");

		// Acceder a un caracter indivudual con charAt(0)
		System.out.println("La sexta letra de la palabra " + cadena3 + " es: " + cadena3.charAt(5) + "\n");

		// Comparar cadenas de caracteres.
		String str1 = "Prueba";
		String str2 = "prueba";
		boolean comparar = str1.equals(str2);

		String mensaje = comparar ? str1 + " y " + str2 + ": Son iguales"
				: str1 + " y " + str2
						+ ": Son diferentes, debido a que equeals() \nverifica que los caracteres sean exactamente iguales incluyendo las Mayusculas y las Minusculas";
		System.out.println(mensaje);

		System.out.println("\n");
		comparar = str1.equalsIgnoreCase(str2);
		mensaje = comparar ? str1 + " y " + str2
				+ ": Son iguales ya que equalsIgnoreCase() solo compara las palabras y omite las Mayusculas y Minusculas"
				: str1 + " y " + str2 + ": Son diferentes";
		System.out.println(mensaje);

		System.out.println("\n");
		int comparar2 = str1.compareTo(str2);
		mensaje = comparar2 == 0 ? str1 + " y " + str2 + ": Son iguales"
				: str1 + " y " + str2
						+ ": Son diferentes, debido a que compareTo() \nverifica que los caracteres sean exactamente iguales \nincluyendo las Mayusculas y las Minusculas y nos da como resultado un número negativo: "
						+ comparar2;
		System.out.println(mensaje);

		System.out.println("\n");
		comparar2 = str1.compareToIgnoreCase(str2);
		mensaje = comparar2 == 0 ? str1 + " y " + str2
				+ ": Son iguales ya que compareToIgnoreCase() solo compara las palabras y omite las Mayusculas y Minusculas"
				: str1 + " y " + str2 + ": Son diferentes";
		System.out.println(mensaje);

		// SUBCADENA
		str1 = "Hola mundo";
		String subcadena = str1.substring(5);
		System.out.println("La subcadena es: " + subcadena);

		String criterio = "mundo";

		// BUSQUEDA DE SUBCADENAS
		int indice = str1.indexOf(criterio); // indice será 5
		boolean contiene = str1.contains(criterio); // contiene será true

		System.out.println("\nEl indice es: " + indice + " y " + (contiene ? "Contiene la palabra buscada: " + criterio
				: "No contiene la palabra buscada: " + criterio));

		// MODIFICAR CADENA str1.replace(
		System.out.println("\nLa palabra: " + str1 + " se ha modificado por: " + str1.replace(str1, cadena3));

		// MAYUSCULAS Y MINISCULAS

		System.out.println("Todo en MAYUSCULAS: " + str1.toUpperCase());
		System.out.println("Todo en minusculas: " + str1.toLowerCase());

		// DIFICULTAD EXTRA
		System.out.println("\nDIFICULTAD EXTRA\n");

		// Verificando si las palabras son palindromos o no
		String palabra1 = "amor";
		System.out.println(andrewCodev.isPalindromo(palabra1));
		String palabra2 = "remar";
		System.out.println(andrewCodev.isPalindromo(palabra2));

		// Verificando si ambas palabras son Anagramas
		System.out.println(andrewCodev.sonAnagramas(palabra1, palabra2));

		// Verificando si es Isograma
		System.out.println(andrewCodev.isIsograma(palabra1));
		System.out.println(andrewCodev.isIsograma(palabra2));

	}

	public String isPalindromo(String palabra) {
		int contCaracteres = palabra.length();
		int posicionLetra = contCaracteres - 1;
		String mensaje = "";
		String compararPalabra = "";

		for (int j = 0; j < contCaracteres; j++) {
			compararPalabra = compararPalabra + palabra.charAt(posicionLetra);
			posicionLetra--;
		}

		// Comprobando si la palabra es un palindromo
		if (palabra.equalsIgnoreCase(compararPalabra)) {
			mensaje = "La palabra: " + palabra + " es un palindromo";
		} else {
			mensaje = "La palabra: " + palabra + " no es un palindromo";
		}

		return mensaje;
	}

	public String sonAnagramas(String palabra1, String palabra2) {
		String mensaje = "";
		// Convertimos las palabras en arrys de caracteres
		char[] arregloPalabra1 = palabra1.replaceAll("[\\s]", "").toLowerCase().toCharArray();
		char[] arregloPalabra2 = palabra2.replaceAll("[\\s]", "").toLowerCase().toCharArray();

		// ordenamos los arrays
		Arrays.sort(arregloPalabra1);
		Arrays.sort(arregloPalabra2);

		if (Arrays.equals(arregloPalabra1, arregloPalabra2)) {
			mensaje = palabra1 + " y " + palabra2 + " son anagramas.";
		} else {
			mensaje = palabra1 + " y " + palabra2 + " no son anagramas.";
		}
		return mensaje;
	}

	public String isIsograma(String palabra) {
		String mensaje = "";
		boolean isorama = true;
		Set<Character> caracteres = new HashSet<>();

		for (char c : palabra.toCharArray()) {
			if (!caracteres.add(c)) {
				isorama = false;
			}
		}

		if (isorama) {
			System.out.println("La palabra " + palabra + " es un Isorama");
		} else {
			System.out.println("La palabra " + palabra + " no es un Isorama");
		}

		return mensaje;
	}
}

/*
 * EJERCICIO: Muestra ejemplos de todas las operaciones que puedes realizar con
 * cadenas de caracteres en tu lenguaje. Algunas de esas operaciones podrían ser
 * (busca todas las que puedas): - Acceso a caracteres específicos, subcadenas,
 * longitud, concatenación, repetición, recorrido, conversión a mayúsculas y
 * minúsculas, reemplazo, división, unión, interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional): Crea un programa que analice dos palabras
 * diferentes y realice comprobaciones para descubrir si son: - Palíndromos -
 * Anagramas - Isogramas
 */