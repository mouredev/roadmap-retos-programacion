package org.roadmap.java.ejercicio.dos;

public class Password1989 {
	public static void sinRetorno()
	{
		System.out.println("Sin retorno");
	}
	
	public static int devuelveEntero()
	{
		return 0;
	}
	
	public static void sinRetornoConParametro(String cadena1)
	{
		System.out.println("cadena1");
	}
	
	public static void funcion1()
	{
		/* ERROR
		public static int funcion2() {
			System.out.println("F2");
		}
		*/
	}
	
	public static int dificultadExtra(String cadena1, String cadena2)
	{
		/*
		 * DIFICULTAD EXTRA (opcional):
		 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
		 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
		 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
		 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
		 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
		 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
		 *
		 */
		int resultado = 0;
		
		try {
			for (int i = 1; i <= 100; i++)
			{
				if ((i%3==0) && (i%5==0))
				{
					System.out.println("i:" + i + "-Cadenas:" + cadena1+cadena2);
					resultado++;
				}
				else if(i%3==0)
				{
					System.out.println("i:" + i + "-Cadenas:" + cadena1);
					resultado++;
				}
				else if(i%5==0)
				{
					System.out.println("i:" + i + "-Cadenas:" + cadena2);
					resultado++;
				}
				
			}
		} catch (Exception e) {
			// TODO: handle exception
			e.printStackTrace();
		}
		return resultado;
	}
	public static void main(String[] args) {
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
		 * 
		 * 
		 * El título de la Pull Request también debe seguir este formato: "#[número] - [lenguaje_utilizado]". 
		 * En el ejemplo anterior sería "#00 - Python".
		 * 
		 * En mi caso seria: "#02 - Java"
		 */
		int nVeces;
		System.out.println(String.format("Se han escrito las cadenas %s veces", nVeces = dificultadExtra("cadena1", "cadena2")));
		
	}

}
