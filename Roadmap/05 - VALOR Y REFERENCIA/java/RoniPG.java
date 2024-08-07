// @Roni

public class VALOR_Y_REFERENCIA_05 {

	public static void main(String[] args) {
		
		// Asignación de variables por valor
		/*
		 * Las variables por valor son las que no comparten la misma posicion en memoria.
		 * Los datos primitivos en la asginacion de datos o al pasarle otro dato primitivo crea una copia, del valor
		 * en otra posicion de memoria(no comparte el puntero a su posicion en memoria)
		 * Una excepion dentro de los datos primitivos es el String, que es un dato de tipo objeto pero actua como un
		 * dato primitivo al asignarle otro valor/dato.
		 */
		int a=5; 			int b=10;
		String a1="Hola";	String b1="Adios";
		System.out.println("Numero a: "+a+".\t\tNumero b: "+b+"\nCadena a1: "+a1+".\tCadena b1: "+b1);
		a=b;				b=5;		// --> Intercambiamos los valores numericos
		a1=b1;				b1="Hola";  // --> Intercambiamos los valores en la cadena
		System.out.println("Numero a: "+a+".\t\tNumero b: "+b+"\nCadena a1: "+a1+".\tCadena b1: "+b1);
		
		// Asignación de variables por referencia
		/*
		 * Java no permite la modificación de la referencia en sí misma.
		 * No puedes hacer que una referencia apunte a otro objeto dentro de un método y esperar que esa modificación se refleje fuera del método
		 */
		
		int numsA [] = {5,10};	int numsB [] = {15,20};
		numsA=numsB;				numsB[0]=5;numsB[1]=10;
		// Comprobamos que al asignarle numsB a numsA pasan a compartir el mismo espacio de memoria.
		// Todo lo que se modifique en una variable modificara automaticamente la otra. 
		for(int numero : numsA) {System.out.print(numero+"\t");	}
		for(int numero : numsB) {System.out.print(numero+"\t");	}
		
		a=5; b=10;
		porValor(a, b);
		System.out.println("Valor de la variable a: "+a+"\nValor de la variable b: "+b);
		int [] arrayA= {5,10};
		int [] arrayB= {15,20};
		porReferencia(arrayA, arrayB);
		System.out.println("Valor del arrayA: "+arrayA[0]+", "+arrayA[1]+"\nValor del arrayB: "+arrayB[0]+", "+arrayB[1]);
		
		/* DIFICULTAD EXTRA (opcional):
		 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
		 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
		 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
		 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
		 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
		 *   Comprueba también que se ha conservado el valor original en las primeras.
		 */
		System.out.println();
		int numA=5;	int numB=10;
		System.out.println("\nValor de numA: "+numA+".\tValor de numB: "+numB);
		int result[]=intercambioPorValor(numA, numB);
		int numC=result[0];	int numD=result[1];
		System.out.println("Valor de numA: "+numA+".\tValor de numB: "+numB);
		System.out.println("Valor de numC: "+numC+".\tValor de numD: "+numD+"\n");
		
		int [] numArray1= {5,10};	int [] numArray2= {15,20};
		System.out.println("\nValor del array numArray1: "+numArray1[0]+","+numArray1[1]+".\tValor de numArray2: "+numArray2[0]+","+numArray2[1]);
		int res[][]=intercambioPorReferencia(numArray1, numArray2);
		int [] numArray3=new int[res[0].length]; int [] numArray4=new int[res[1].length];
		for(int i=0; i<numArray3.length;i++) {numArray3[i]=res[0][i];}
		for(int i=0; i<numArray4.length;i++) {numArray4[i]=res[1][i];}
		System.out.println("Valor del array numArray1: "+numArray1[0]+","+numArray1[1]+".\tValor de numArray2: "+numArray2[0]+","+numArray2[1]);
		System.out.println("Valor del array numArray3: "+numArray3[0]+","+numArray3[1]+".\tValor de numArray4: "+numArray4[0]+","+numArray4[1]+"\n");
	}
	public static int[] intercambioPorValor(int a, int b) {
		System.out.println("Entramos en la funcion intercambioPorValor");
		int aux = a ;
		a = b;
		b = aux;
		int result[]={a,b}; //--> Lo devolvemos como un array para luego asignar los valores deseados
		System.out.println("Salimos de la funcion porValor");
		return result;
	}
	public static int [][] intercambioPorReferencia(int [] a, int [] b) {
		System.out.println("Entramos en la funcion intercambioPorReferencia");
		int [] auxA=new int[a.length];
		int [] auxB=new int[b.length];
		for(int i=0; i<auxA.length;i++) {auxA[i]=a[i];}
		for(int i=0; i<auxB.length;i++) {auxB[i]=b[i];}
		
		System.out.println("Salimos de la funcion porValor");
		return new int [][] {auxB,auxA};
	}
		//Funciones con variables por valor
	
	public static void porValor(int a, int b) {
		System.out.println("\nEntramos en la funcion porValor");
		a=45; b=95;
		System.out.println("Valor de la variable a: "+a+"\nValor de la variable b: "+b);
		System.out.println("Salimos de la funcion porValor\n");
	}
	//Funciones con variables por valor
	public static void porReferencia(int [] arrayA, int [] arrayB) {
		System.out.println("\nEntramos en la funcion porReferencia");
		arrayA[0]=25; arrayA[1]=30;
		arrayB[0]=35; arrayB[1]=40;
		System.out.println("Valor del arrayA: "+arrayA[0]+", "+arrayA[1]+"\nValor del arrayB: "+arrayB[0]+", "+arrayB[1]);
		System.out.println("Salimos de la funcion porReferencia\n");
	}
		
}
