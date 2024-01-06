	//@Roni

public class SINTAXIS_VARIABLES_TIPOS_DE_DATOS_Y_HOLA_MUNDO_00 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//URL = https://www.java.com 
		// Comentario en una linea.
		/*
		 * Comentario de varias lineas.
		 */
		byte start, end; start= -128; end = 127 ;
		short sh = 0 ; // start= -32768; end = 32767 ;
		int in = 0; // start= -2^31; end = 2^31 ;
		long lo = 0; // start= -2^63; end = 2^63 ;
		float fl = 0.0f; // ---> numeros decimales simples.
		double dl = 0.0d; // ---> numeros decimales largos.
		boolean bo = false; // ---> valores true, false(por defecto).
		char ch = 'a'; //---> valor para una letra/caracter.
		String st = "Texto"; //---> variable no primitivo para almacenar una cadena de caracteres.
		
		//Para crear una constante se a├▒ade 'final' antes de indicar el tipo de variable.
		
		final int fi=0;
		
		System.out.println("Hola JAVA");
	}

}
