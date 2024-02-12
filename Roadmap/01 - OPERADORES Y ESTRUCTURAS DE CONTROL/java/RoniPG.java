
// @Roni

public class OPERADORES_Y_ESTRUCTURAS_DE_CONTROL_01 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		System.out.println("Tipo de operadores.");
		
		System.out.println("Operadores Aritmeticos.");
		
		System.out.println("Suma +, Resta -, Division /, Multiplicacion *, Resto % (En la division inexacta = lo que sobra)"); 
		
		System.out.println("Ejemplos");
		
		int a = 2;
		int b = 3;
		
		int suma = a + b;
		System.out.println(a + " + " + b + " = " + suma);
		
		int resta = a - b;
		System.out.println(a + " - " + b + " = " + resta);
		
		int division = a / b;
		System.out.println(a + " / " + b + " = " + division);
		
		int multiplicacion = a * b;
		System.out.println(a + " * " + b + " = " + multiplicacion);
		
		int resto = a % b;
		System.out.println(a + " % " + b + " = " + resto);
		
		System.out.println("Operadores de Asignacion.");
		
		System.out.println(" = para asignar el valor sobrescirbiendolo");
		System.out.println("+= sumar a la variable el valor dedicidido");
		System.out.println("-= restar a la variable el valor dedicidido");
		System.out.println("*= mutilpicar a la variable el valor dedicidido");
		System.out.println("/= dividir a la variable el valor dedicidido");
		
		System.out.println("Ejemplos");
		
		System.out.println(a);
		System.out.println(a + " += 2 ");
		a += 2;
		System.out.println(a);
		System.out.println(a + " -= 2 ");
		a -= 2;
		System.out.println(a);
		System.out.println(a + " *= 2 ");
		a *= 2;
		System.out.println(a);
		System.out.println(a + " /= 2 ");
		a /= 2;
		System.out.println(a);
		
		System.out.println("Operadores de comparacion");
		
		System.out.println("== igual a (para objetos equals(), != difente de, < menor que,"); 
		System.out.println("<= menor o igual que, >= mayor o igual que, > mayor que."); 
		System.out.println("Todos estos valores devuelven un booleano true o false");
		
		System.out.println("Ejemplos");
		
		boolean comparacion;
		
		System.out.println(a + " | " + b);
		comparacion = a == b;
		System.out.println(a + " es igual a " + b + ": " + comparacion);
		comparacion = a != b;
		System.out.println(a + " no es igual a " + b + ": " + comparacion);
		comparacion = a < b;
		System.out.println(a + " es menor que " + b + ": " + comparacion);
		comparacion = a <= b;
		System.out.println(a + " es menor o igual que " + b + ": " + comparacion);
		comparacion = a >= b;
		System.out.println(a + " es mayor o igual que " + b + ": " + comparacion);
		comparacion = a > b;
		System.out.println(a + " es mayor que " + b + ": " + comparacion);
		
		System.out.println("Operadores logicos.");
		
		System.out.println("|| operador OR (devuelve true si una de las variables se cumple)");
		System.out.println("&& operador AND (devuelve true si todas las variables se cumplen)");
		System.out.println("! operador NOT (invierte el valor de la condici├│n, de true a false y viceversa)");
		
		System.out.println("Ejemplos");
		
		boolean logico= true;
		comparacion=false;
		
		System.out.println("Operador OR: " + comparacion + " || " + logico);
		if (comparacion || logico) {
			System.out.println(logico);
		}else {
			System.out.println(comparacion);
		}
		System.out.println("Operador AND: " + comparacion + " && " + logico);
		if (comparacion && logico) {
			System.out.println(logico);
		}else {
			System.out.println(comparacion);
		}
		System.out.println("Operador NOT: !" + comparacion);
		if (!comparacion) {
			System.out.println(logico);
		}else {
			System.out.println(comparacion);
		}
		
		System.out.println("Operadores de incremento y decremento.");
		
		System.out.println("++ Incrementa en uno la variable.");
		System.out.println("-- Incrementa en uno la variable.");
		
		System.out.println("Ejemplos");
		
		a = 2;
		System.out.println(a);
		System.out.println(" ++ " + a);
		a ++;
		System.out.println(a);
		System.out.println(" -- " + a);
		a --;
		System.out.println(a);
		
		System.out.println("Operadores ternarios");
		
		System.out.println("Tienen la forma condicion ? valor_si_verdadero : valor_si_falso.");
		
		System.out.println("Ejemplos");
		
		boolean ternario = false;
		
		ternario = (comparacion || logico) ? logico : comparacion;
		System.out.println("Operador OR en ternario: " + comparacion + " || " + logico + " ternario = " + ternario);
		ternario = (comparacion && logico) ? logico : comparacion;
		System.out.println("Operador AND en ternario: " + comparacion + " && " + logico + " ternario = " + ternario);
		ternario = (!comparacion) ? logico : comparacion;
		System.out.println("Operador NOT en ternario: !" + comparacion + " ternario = " + ternario);
		
		System.out.println("Operadores de concatenacion");
		
		System.out.println("+ Unir diferentes strings a uno solo.");
		
		System.out.println("Ejemplos");
		
		String texto1 = "Hola, ";
		System.out.println(texto1);
		String texto2 = "Java!";
		System.out.println(texto2);
		String textoFinal = texto1 + texto2;
		System.out.println(textoFinal);
		
		System.out.println("Operadores de conversion de tipo");
		
		System.out.println("Para covertir a numero (int), o tambien Integer.parseInt()");
		System.out.println("Para convertir a texto (String), o tambien String.valueOf()");
		System.out.println("Para convertir a float (float), o tambien Float.parseFloat()");
		
		System.out.println("Ejemplos");
		
		texto1 = "2";
		System.out.println("Dato en texto = " + texto1);
		a = Integer.parseInt(texto1);
		System.out.println("Dato convertido a entero = " + a);
		texto1 = String.valueOf(a);
		System.out.println("Dato convertido a texto = " + texto1);
		float ft;
		ft = Float.parseFloat(texto1);
		System.out.println("Dato convertido a flotante = " + ft);
		
		System.out.println("Tipo de estucturas.");
		
		System.out.println("Estructura if");
		
		System.out.println("Se ejecuta el bolque si se cumple la condicion.");
		
		System.out.println("Ejemplos");
		
		a = 2;
		b = 2;
		
		System.out.println("Si " + a + " = " + b);
		if (a == b) {
			System.out.println("Se ejecuta el bloque");
		}
		
		System.out.println("Estructura if-else");
		
		System.out.println("Se ejecuta el bloque if si se cumple la condicion, si no se cumple se ejecuta el else.");
		
		System.out.println("Ejemplos");
		
		System.out.println("Si " + a + " < (menor que) " + b);
		if (a < b) {
			System.out.println("Se ejecuta el bloque if");
		}
		else {
			System.out.println("Se ejecuta el bloque else");
		}
		
		System.out.println("Estructura if else-if else");
		
		System.out.println("Se ejecuta el bloque if si se cumple la condicion.");
		System.out.println("Si no se cumple se ejecuta la siguiente condicion else if(asi sucesivamente).");
		System.out.println("Si no se cumple niguna condicion se ejecuta el else.");
		
		System.out.println("Ejemplos");
		
		System.out.println("if " + a + " < (menor que) " + b + "\n" + 
						   "else if " + a + " = (igula a) " + b);
		if (a < b) {
			System.out.println("Se ejecuta el bloque if");
		}
		else if (a == b ) {
			System.out.println("Se ejecuta el bloque else if");
		}
		else {
			System.out.println("Se ejecuta el bloque else");
		}
		
		System.out.println("Estructura switch");
		
		System.out.println("Se pasa una variable para luego indicar los casos en los que se ejecutaria.");
		System.out.println("Dentro de cada caso se a├▒ade 'break;'(opcional), para salir del switch despues de ejecutar el bloque de codigo.");
		System.out.println("Tambien se puede a├▒adir 'default:' para ejecutar el codigo si no se cumple ningun case.");
		
		System.out.println("Ejemplos");
		
		a = 1;
		b = 2;
		int c = 3;
		
		System.out.println("Case 1 = " + a + ",caso 2 = " + b + ",caso 3 = " + c + ",si no = ");
		switch (a) {
		case 1:
			System.out.println("Se ejecuta el primer caso");
			break;
		case 2:
			System.out.println("Se ejecuta el segundo caso");
			break;
		case 3:
			System.out.println("Se ejecuta el tecero caso");
			break;
		default:
			System.out.println("No se ejecuta ningun caso");
			break;
		}
		
		System.out.println("Estructura de bucles");
		
		System.out.println("Bucle for");
				
		System.out.println("Se ejecuta un bloque de codigo mientras la condicion sea verdadera.");
		System.out.println("Esto se controla mediante un iterador que se ira modificando por cada ejecucion del bucle.");
				
		System.out.println("Ejemplos");
		
		for (int i = 0; i < c; i++) {
			System.out.println(i);
		}
		
		System.out.println("Bucle while");
		
		System.out.println("Se ejecuta un bloque de codigo mientras la condicion sea verdadera.");
		System.out.println("El bucle se ejecutara hasta que se modifique la condicion.");
				
		System.out.println("Ejemplos");
		
		System.out.println("Condicion: " + a + " distito de " + c);
		while (a != c) {
			System.out.println("La condicion es verdera");
			a++;
			System.out.println(a);
		}
		
		System.out.println("Bucle do-while");
		
		System.out.println("Primero se ejecuta un bloque de codigo, luego se comprueba que la condicion sea verdadera.");
		System.out.println("El bucle se ejecutara hasta que se modifique la condicion.");
				
		System.out.println("Ejemplos");
		
		a = 0;
		
		do {
			System.out.println("Condicion: " + a + "distinto " + c);
			System.out.println("La condicion es verdera");
			a++;
		} while (a != c);
		
		System.out.println("DIFICULTAD EXTRA (opcional):");
		System.out.println("Crea un programa que imprima por consola todos los n├║meros comprendidos");
		System.out.println("entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni m├║ltiplos de 3.");
		
		for (int i = 10; i <= 55; i++) {
			if( i%2 != 0){
				
			}else if ((i == 16) || (i%3 == 0)){
				
			}else {
			System.out.println(i);
			}
		}
	}

}
