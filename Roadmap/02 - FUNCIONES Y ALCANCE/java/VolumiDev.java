/*
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */
import java.io.*;
public class VolumiDev {
	public static BufferedReader leer=new BufferedReader(new InputStreamReader(System.in));
	
	//metodo sin retorno ni parametros
	public static void HolaJava() {
		
		System.out.println("Hola Java.");
	}
	
	//Metodo con retorno de un entero y sin parametros y publico
	public static int pedirnum(String cad) throws NumberFormatException, IOException {
		int num;
		System.out.println(cad);
		num=Integer.parseInt(leer.readLine());
		return num;
	}
	
	//Metodo con retorno de un double y 3 parametros
	private static double pedirn2(String cad, int l1, int l2) throws NumberFormatException, IOException {
		double n;
		do {
			System.out.println(cad+l1+" y "+l2);
			n=Double.parseDouble(leer.readLine());
		} while (n<l1 || n>l2);
		return n;
	}
	
	//metodo que retorna un String;
	public static String pedircad() throws IOException {
		System.out.println("Introduce una cadena de caracteres");
		return leer.readLine();
	}
	
	//metodo que no retorna nada y al que le pasamos 2 parametros
	private static void mostrarcad(String cad, int n) {
		for(int i=0; i<n; i++) {
			System.out.println(cad);
		}
	}

	
	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub
		String cad;
		HolaJava();
		
		System.out.println(pedirnum("Introducen un numero entero"));

		System.out.println(pedirn2("Introduce un numero real entre ", 5, 10));
		
		mostrarcad(pedircad(), pedirnum("Introduce el numero de veces que quieres que se repita la cadena que acabas de introducir"));
		
		System.out.println("NO SE PUEDE GENERAR METODOS DENTRO DE UN METODO, PUEDES LLAMAR A UN METODO DENTRO DE OTRA, PERO NO CREARLOS.");
		
		// Con la funcion .length de la clase string podemos saber la longitud de la cadena de caracteres.
		
		cad=pedircad();
				System.out.println("La palabra "+cad+" tiene "+cad.length()+" caracteres");
	}

}
