public class Juandgg {
    
    public static int suma(int n1 , int n2){
        return (n1+n2);
    }

    public static void saludo(String saludo){
        System.out.println("hola" + saludo);
    }

    public static void holaMundo(){
        System.out.println("hola mundo");
    }

    public static int  dificultadExtra(String cadena1,String cadena2){
    //     DIFICULTAD EXTRA (opcional):
    // * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
    // * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
    // *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
    // *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
    // *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
    // *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
    // *
        System.out.println("\n DIFICULTAD EXTRA \n");
        
        int maxNumeroVeses =0;

        for (int i = 1; i <=100; i++) {
            
            if(i % 3==0 && i % 5 ==0){
                System.out.println(cadena1.concat(cadena2));
            }

            else if(i % 3==0){
                System.out.println(cadena1);
            }

            else if(i % 5==0){
                System.out.println(cadena2);
            }

            else {
                System.out.println(i);
                maxNumeroVeses++;
            }
        }

        return maxNumeroVeses ;

        



        
        


    }

    /*
     * 
     * 
     */
    


    public static void main(String[] args) {


        
        System.out.println(Juandgg.suma(1, 2));
        Juandgg.saludo("hola");
        Juandgg.holaMundo();

        //DIFICULTAD EXTRA  
        System.out.println(Juandgg.dificultadExtra("cadena1","cadena2"));

    }
}
