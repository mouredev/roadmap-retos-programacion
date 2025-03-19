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
import java.io.*;
public class VolumiDev {

	public static void extra() {
		System.out.println();
		System.out.println("A continuacion mostramos el programa extra, que nos muestra los numeros pares, distintos de 16 y que no sean multiplos de 3");
		System.out.println();
		for(int i=10; i<=55; i++) {
			if(i%2==0 && i!=16) {
				if(i%3!=0) {
				System.out.print(i+"\t");
				}
			}
		}
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int a=48;
		int b=26;
		String cad1="cho";
		String cad2="co";
		String cad3="la";
		String cad4="te";
		int c, d;
		boolean andlog;
		boolean orlog;
		boolean notlog;
		boolean bitand;
		boolean bitor;
		boolean bitxor;
		boolean bitnot;
		
		//operadores de asignacion
		c=8;
		d=8;
		
		//operadores aritméticos
		System.out.println(a+b);	//suma 
		System.out.println(cad1+cad2+cad3+cad4);	//concatenación de cadenas
		System.out.println(a-b);	//resta
		System.out.println(a*b);	//multiplicación
		System.out.println(a/b);	//división
		System.out.println(a%b);	//resto de la división
		
		//operadores aritmeticos incrementales
		System.out.println("Primero 'a' vale "+a+" despues de incremetarlo en 1 vale "+a++);	//incrementador
		System.out.println("Primero 'b' vale "+b+" despues de decrementarlo en 1 vale "+b--);	//decrementador
		
		//operadores aritmeticos combinados aritmeticos y asignacion
		System.out.println("El resultado de a=a+b es: "+(a+=b));	//suma combinada -> a=a+b
		System.out.println("El resultado de a=a-b es: "+(a-=b));	//resta combinada -> a=a-b
		System.out.println("El resultado de a=a*b es: "+(a*=b));	//multiplicacion combianda -> a=a*b
		System.out.println("El resultado de a=a/b es: "+(a/=b));	//multiplicacion combinada -> a=a/b
		System.out.println("El resultado de a=a%b es: "+(a%=b));	//restos de division combianda -> a=a%b;
		
		//operadores de comparacion
		System.out.println("Igualdad, c es igual a d: "+(c==d));	//igualdad
		System.out.println("Distinto, a es destinto de b: "+(a!=b));	//distinto
		System.out.println("Mayor que, a es mayor que b: "+(a>b));	//mayor que
		System.out.println("Menor que, b es menor que a: "+(b<a));	//menor que 
		System.out.println("Mayor o igual, a es meyor o igual que c: "+(a>=c));	//mayor o igual
		System.out.println("Menor o igual, c es menor o igual que d: "+(c<=d));	//menor o igual
		
		//operadores logicos
		andlog=(c==8 && d==8);	//operador and
		System.out.println("Operador logico AND "+andlog);	
		orlog=(c==0 || d==11);	//operador or
		System.out.println("Operador logico OR "+orlog);
		notlog=!(andlog);	//operador not
		System.out.println("Lo contrario al operador logico AND "+notlog);
		
		//operadores ternarios
		System.out.println((a>b)?"'a' es mayor que 'b'":"'b' es mayor que 'a'");
		
		//operadores de bits para operaciones a nivel de bit en numeros enteros
		
		//desplazamientos
		System.out.println("Desplaza los bits de 45 a la izquierda 2 posiciones para combertirlo en: "+(a<<2));	//desplazamiento a la izq
		
		System.out.println("Desplaza los bits de 45 a la izquierda 2 posiciones para combertirlo en: "+(a>>2)); //desplazamiento a la der
		
			//logicos
		bitand=(c==8 & d==8);
		System.out.println("Operador logico a nivel de bit AND "+bitand);
		bitor=(c==8 | a==8);
		System.out.println("Operador logico a nivel de bit OR "+bitor);
		
		//operadores de conversion
		System.out.println("El numero a es un entero "+a+" y lo casteamos a real "+(double)a);
		
		extra();
	}

}
