public class AndrewCodev {
	//Variables Globales de la clase
	int num1;
    int num2;
    int num3;

    public void suma(){
    	this.num1 = 2;
    	this.num2 = 7;
    	this.num3 = 1;
    	
    	int resultado = this.num1 + this.num2 + this.num3;
        System.out.println("Resultado de la suma en un método sin argumentos y sin retorno");
        System.out.println(this.num1+" + "+this.num2+" + "+this.num3+" = "+ resultado);
    }
    
    /*las variables creadas como parametros son variable locales del método
     * al igual que las variables creadas dentro de este sin el operador this.
     * como ejemplola variable resultado.
     */
    public void sumaConParametros(int num1, int num2, int num3) {
    	//Variable Local llamando a la función Suma con Retorno
    	int resultado = sumaConRetorno(num1, num2, num3);
        System.out.println(this.num1+" + "+this.num2+" + "+this.num3+" = "+ resultado);
    }
    
    public int sumaConRetorno(int num1, int num2, int num3) {
    	this.num1 = num1;
    	this.num2 = num2;
    	this.num3 = num3;
    	int resultado = this.num1 + this.num2 + this.num3;
        return resultado;
    }
    
    //DIFICULTAD EXTRA
    public int contadorNumerico(String cadena1, String cadena2) {
    	//Variable local de método
    	int contador = 0;
    	
    	for (int i = 1; i <= 100; i++) {
    		
    		if(i % 3 == 0 && i % 2 == 0) {
    			System.err.println(i+": "+cadena1+" "+cadena2);
    		}else if(i % 2 == 0) {
    			System.err.println(i+": "+cadena2);
    		}else if(i % 3 == 0) {
    			System.err.println(i+": "+cadena1);
    		}
    		else {
    			System.err.println(i+" ");
    			contador++;
    		}			
		}
    	
    	return contador;
    }
    
    public static void main(String[] args) {
		AndrewCodev andrewCodev = new AndrewCodev();
		andrewCodev.suma();
		System.out.println("\nResultado de la suma en un método con argumentos y sin retorno");
		andrewCodev.sumaConParametros(5, 5, 10);
		

    	System.out.println("\nResultado de la suma en un método con argumentos y con retorno\n");
		int sumaConRetorno = andrewCodev.sumaConRetorno(6, 4, 5);
		System.out.println(sumaConRetorno);
		
		System.out.println("DIFICULTAD EXTRA");
		int contador = andrewCodev.contadorNumerico("Hola Mundo", "Adios Mundo");
		System.err.println("Total numeros no multiplos de 2 ni de 3: "+contador);
    }

}