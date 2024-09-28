
// @Roni
public class FUNCIONES_Y_ALCANCE_02 {
	

		// Diferenciaremos entre Funciones, Metodos y Procedimientos
		
		// Las funciones utilizan el modificador static
	
	//Funcion de suma
	/*
	 * Las funciones pueden no recibir ningun parametro o pueden recibir varios parametros
	 * Siempre tienen un valor de retorno (return) que se devuelve al invocar la funcion
	 */
	public static int Suma(int numA, int numB) {
		
		int result = numA + numB + a;
		
		return result;
	
	}
	public static int Resta(int a) {
		/*public static int SegundaResta(int b) {
			return 0;}
		Podemos comprobra al descomentar este codigo que no podemos crear funciones dentro de funciones	
		*/  
		return 0;
	}
	//Llamadas a funciones dentro de funciones
	public static int Resultsuma(int numA, int numB) {
		
		int result = numA + numB;
		Resultados(); // ---> Podemos realizar llamadas a funciones dentro otra
		return result;
	
	}
	static int a = 1; //Variable global es accesible a en todo el programa
	
	public static int AccesoVariables() {
		 int a = 0; // ---> Variable Local (Solo existe dentro de la funcion)
		return a;
	}
		//Los metodos se utilizan principalmente en objetos, y no llevan modificador
	
	public int Resta(int numA, int numB) {
		
		int result = numA - numB;
		
		return result;
	
	}
		//Los procedimientos no retornan ningun valor, llevan el tipo void.
	public static void Resultados() {
		System.out.println("El resultado de la suma es:"+Suma(2,3));
		
	}
	public static void main(String[] args) {
		
		//Llamadas a Funciones
		 
		System.out.println(Suma(2, 3));
		//System.out.println(Resta(2, 3)); --> No se puede llamar al metodo porque no esta asociado a ningun objeto
		Resultados();
		System.out.println(Resultsuma(2, 3));	
		
		//Llamadas a Funciones predefinidas de java
		
		System.out.println("2 elevado a la potencia de 3 = "+Math.pow(2, 3));
		System.out.println("Genero un numero aleatorio : "+Math.random());
		
		//Variables
		
		System.out.println("Accedemos a la variable local a con valor : "+ AccesoVariables());
		System.out.println("Comprobamos la variable global a : "+a);
		
		/* DIFICULTAD EXTRA (opcional):
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
		System.out.println("Se ha impreso un numero: "+X("Soy multiplo de 3", "Soy multiplo de 5")+" veces");
	}
	public static int X (String a, String b) {
		int contador = 0;
		for (int i = 1; i < 100; i++) {
			if ((i%5==0)&&(i%3==0)){
				System.out.println(a+" y tambien "+b);
			}else if (i%3==0) {
				System.out.println(a);
			}else if (i%5==0) {
				System.out.println(b);
			}else {
				System.out.println(i);
				contador++;
			}
						
		}
		return contador;
	}
}
