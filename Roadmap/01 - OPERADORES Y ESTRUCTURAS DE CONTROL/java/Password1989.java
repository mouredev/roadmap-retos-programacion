package org.roadmap.java.ejercicio.uno;

public class Password1989 {

	public static void dificultadExtra()
	{
		/*
		 * Crea un programa que imprima por consola todos los números comprendidos
		 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3
		 * 
		 */
		
		int min = 10;
		int max = 55;
		
		for (int i = 10; i <= max; i++)
		{
			if( (i%2==0) && (i!=16) && (i%3!= 0))
			{
				System.out.println(String.format("El numero %s cumple las condiciones",i));
			}
		}
	}
	public static void main(String[] args) {
		/*
		 * EJERCICIO:
		 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
		 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
		 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
		 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
		 *   que representen todos los tipos de estructuras de control que existan
		 *   en tu lenguaje:
		 *   Condicionales, iterativas, excepciones...
		 * - Debes hacer print por consola del resultado de todos los ejemplos.
		 *
		 * DIFICULTAD EXTRA (opcional):
		 * Crea un programa que imprima por consola todos los números comprendidos
		 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
		 *
		 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
		 */
		
		/*
		 * Operadores: 
		 * Aritmeticos: Suma, Resta, Division, Producto
		 */
		
		System.out.println(String.format("Suma 10+3= %s", 10+3));
		System.out.println(String.format("Resta 10-3= %s", 10-3));
		System.out.println(String.format("Division 10/3= %s", 10/3));
		System.out.println(String.format("Producto 10 x 3= %s", 10*3));
		System.out.println(String.format("Resto 10/3= %s", 10%3));
		//System.out.println(String.format("Exponente 10/3= %s", 10^3));
		
		/*
		 * Operadores: 
		 * Lógicos: disruptivos && || sin disrupción & | ^
		 * 
		 * && AND Logico
		 * || OR Logico
		 * Los operadores sin disrupción ejecutan todas las expresiones aun cuando el resultado sea claramente false o true.
		 * 
		 */
		
		/*
		 * Operadores: 
		 * Comparativos: < > <= >= == !=
		 * < menor			a < b
		 * > mayor			a > b
		 * <= menor igual	a <= b
		 * >= mayor igual	a >= b
		 * == igual			a == b
		 * != distinto		a != b
		 */
		
		/*
		 * Operadores: 
		 * Asignación: = --= += *= %= /= >= <=>>= <<= >>>= <<<=
		 * =	Asignación					a = b
		 * +=	Suma y asignación			a += b (a=a + b)
		 * -=	Resta y asignación			a -= b (a=a - b)
		 * *=	Multiplicación y asignación	a *= b (a=a * b)
		 * /=	División y asignación		a / b (a=a / b)
		 * %=	Módulo y asignación			a % b (a=a % b)
		 */
		
		int a = 5;
		int b = 8;
		
		int ejemploAsignacion = 0;
		
		ejemploAsignacion += a;
		
		System.out.println(String.format("Resultado ejemplo: %s",ejemploAsignacion));
		
		
		ejemploAsignacion -= b;
		
		System.out.println(String.format("Resultado ejemplo: %s",ejemploAsignacion));
		
		ejemploAsignacion *= a;
		
		System.out.println(String.format("Resultado ejemplo: %s",ejemploAsignacion));
		
		ejemploAsignacion /= b;
		
		System.out.println(String.format("Resultado ejemplo: %s",ejemploAsignacion));
		
		ejemploAsignacion %= a;
		
		System.out.println(String.format("Resultado ejemplo: %s",ejemploAsignacion));
		
		/*
		 * Operadores: 
		 * Incremento: a++ (postincremento) y ++a (preincremento)
		 * Decremento: a-- (postdecremento) y --a (predecremento)
		 * 
		 */
		
		int j = 0;
		
		System.out.println(String.format("EjemploIncremento: %s",j));

		System.out.println(String.format("J vale: %s, EjemploPOSTIncremento: %s",j,j++));
		System.out.println(String.format("J vale: %s, EjemploPREIncremento: %s",j,++j));
		System.out.println(String.format("J vale: %s, EjemploPOSTDecremento: %s",j,j--));
		System.out.println(String.format("J vale: %s, EjemploPREDecremento: %s",j,--j));
		
		/*
		 * Operadores: 
		 * Ternario: x == y ? x: y;
		 * 
		 * Si se cumple la primera parte, x valdrá x si no, valdrá y
		 */
		
		int x = 10;
		int y = 20;
		
		System.out.println(x == y ? x: y);
		
		/*
		 * Operadores: 
		 * Bit: ^ ! & ~ << >> <<< >>>
		 * 
		 */
		
		/*
		 * Estructuras de control: Condicionales, iterativas, excepciones
		 * IF:
		 * La sentencia if permite llevar a cabo la ejecución condicional de sentencias. 
		 * Se ejecutan las sentencias si al evaluar la expresión se obtiene un valor booleano true.
		 * 
		 */
		
		boolean condicion = true;
		if (condicion)
		{
			System.out.println("True");
		}
		else 
			System.out.println("False");
		
		/*
		 * SWITCH:
		 * La sentencia switch en la que se indican los posibles valores que puede tomar la variable y las sentencias que se tienen que ejecutar
		 * sí es que la variable coincide con alguno de dichos valores.
		 * Cada case ejecutará las sentencias correspondientes, con base en el valor de la variable, que deberá de evaluarse con valores de tipo byte, char, short o int.
		 * Si el valor de la variable no coincide con ningún valor, entonces se ejecutan las sentencias por default, sí es que las hay.
		 * La sentencia break al final de cada case transfiere el control al final de la sentencia switch; de esta manera, cada vez que se ejecuta un case todos los enunciados case restantes son ignorados y termina la operación del switch.
		 * 
		 *
		 */
		
		String cadena = "salir";
		
		switch (cadena)
		{
		case "salir":
			System.out.println(cadena);
			break;
		default:
			System.out.println("default");
			break;
		}
		
		/*
		 * FOR:
		 * 
		 */
		
		for (int iterador=0; iterador < 5; iterador++)
		{
			System.out.println(iterador);
		}
		
		/* 
		 * WHILE:
		 * 
		 */
		
		boolean condicionWhile = true;
		while (condicionWhile) {
			System.out.println(condicionWhile);
			condicionWhile = false;
		}
		
		/*
		 * DO WHILE:
		 * 
		 */
		
		do {
			System.out.println(condicionWhile);
			condicionWhile = false;
		} while (condicionWhile);
		
		/*
		 * BREAK; CONTINUE; RETURN;
		 * 
		 */
		
		//dificultadExtra();
	}

}
