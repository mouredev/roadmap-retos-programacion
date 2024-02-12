public class Kine_jdf {
    public static final String STATIC_CONSTANT= "ESTATICA\n";
    public static void main(String args[]) {
    
sola();
cParams(STATIC_CONSTANT);
globalLocal();
yaCreada();
System.out.print("Funcion con retorno de un nro" +retorno());
funcConFunc();
  
     System.out.println("         -+-           |EJERCICIO EXTRA|          +-+");
    int prueba=  laCosa("Mandale","Cumbia");
  
    System.out.print("\n");
     System.out.println("\n     -- Se imprimio el numero un total de "+prueba+" veces--");
    }
     public static int laCosa(String cadena1, String cadena2) {
        int contador = 0;

        for (int numero = 1; numero <= 100; numero++) {
            if (numero % 15==0) {
                System.out.println("|"+cadena1.concat(cadena2)+"| ");
            } else if (numero % 3 == 0) {
                System.out.print("|"+cadena1+"| ");
            } else if (numero % 5 == 0) {
                System.out.print("|"+cadena2+"| ");
            } else {  //aca viene un if completamente innecesario para el funcionamiento, pero que me hace bien a la organizacion visual de la matriz en consola
                if(numero<9){
                System.out.print("(0"+numero+") ");}else {System.out.print("("+numero+") ");}
               contador++;
            }

           
        }

        return contador;
    }
   
   public static void sola(){
         System.out.print("\n Funcion sin retorno ni parametros \n");
   } 
  
  public static void cParams(String para)  {
        System.out.print("\n Sin retorno, con el parametro "+para);
  }
  public static int retorno() {
      
      return 10;
  }
  public static void globalLocal() {
      String STATIC_CONSTANT= "Galletitas de Chocolate|\n";
        System.out.print("\nvariable GLOBAL STATIC_CONSTANT :"+MyClass.STATIC_CONSTANT);
       System.out.println("\nvariable local STATIC_CONSTANT |"+STATIC_CONSTANT);
  }
  
  public static void yaCreada(){
      
      int num = (int)(Math.random()*10);
      
       System.out.println("Impresion de un numero al azar con funcion nativa del lenguaje: "+num);
  }
  
  public static void funcConFunc() {
      String test = "Prueba";
      
       System.out.print("Java no permite crear funciones dentro de otras, pero si llamarlas. ejemplo: ");
          
      test(test);
      
  }
   private static void test(String prueba){
           System.out.println(prueba+"\n");
          
      }
}
