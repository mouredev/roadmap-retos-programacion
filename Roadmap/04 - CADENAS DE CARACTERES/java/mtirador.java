import java.util.Arrays;
import java.util.Scanner;

public class mtirador {

 public static void main(String[] args) {

    /*Operaciones con caracteres */

    /*Recorrer */
    String cad="Hola Mundo";
    for(int i=0;i<cad.length();i++){
        char caracter=cad.charAt(i);
        System.out.println(i+"-----"+ caracter);
    }

    /*Acceso a caracteres específicos */

    char car=cad.charAt(3);
    System.out.println(car);

    /*Longitud */

    System.out.println("Logitud"+ cad.length());

    /*Repeticion */
    System.out.println("Repeticion: "+ cad.repeat(2));

    //Conversión a mayúsculas y minúsculas
    System.out.println("Minúsculas: "+ cad.toLowerCase());
    System.out.println("Mayúsculas: "+ cad.toUpperCase());

    //Reemplazo

    String cambio=cad.replace("Hola", "Hello");
    System.out.println("Reemplazado: "+ cambio);

    
    //División

     String[] div= cad.split(",");
     System.out.println("Division: " + Arrays.toString(div));

     // Unión

    String[] words = { "Hola", "mundo", "Java" };
    String union = String.join(" ", words);
    System.out.println("Union: " + union);

    //Interpolación
    String interpol = String.format("Saludo: %s, Lenguaje: %s", words[0], words[2]);
    System.out.println("Interpolación: " + interpol);

    // Verificación
    System.out.println("Vamos a verificar esta frase: "+ cad);
    boolean empieza = cad.startsWith("Hola");
    boolean termina = cad.endsWith("mundo!");
    System.out.println("Empieza con Hola: " + empieza);
    System.out.println("Termina con mundo: " + termina);


    /*Ejercicio */

    System.out.println("Ingrese una palabra:");
    Scanner ent=new Scanner(System.in);
    String palabra1 = ent.nextLine();
    System.out.println("Ingrese otra palabra:");
    String palabra2 = ent.nextLine();
    String palabraInvertida="";
    String palabraInvertida2="";


    Palindromo(palabra1, palabra2, palabraInvertida, palabraInvertida2);
    Anagrama(palabra1, palabra2);
    Heterograma(palabra1, palabra2);


    ent.close();
 }
 
/*Heterograma */
static void Heterograma(String palabra1, String palabra2) {
    boolean esHet1 = true;
    boolean esHet2= true;
    
        for (int i = 0; i < palabra1.length() - 1; i++) {
            for (int j = i + 1; j < palabra1.length(); j++) {
                if (palabra1.charAt(i) == palabra1.charAt(j)) {
                    esHet1 = false;
                    break;
                }
            }
            if (!esHet1) {
                break;
            }
        }
    
        if (esHet1) {
            System.out.println(palabra1 +"-->Es un heterograma");
        } else {
            System.out.println(palabra1+ "-->No es un heterograma");
        }
    
    
    for (int i = 0; i < palabra2.length() - 1; i++) {
            for (int j = i + 1; j < palabra2.length(); j++) {
                if (palabra2.charAt(i) == palabra2.charAt(j)) {
                    esHet2 = false;
                    break;
                }
            }
            if (!esHet2) {
                break;
            }
        }
    
       
        if (esHet2) {
            System.out.println(palabra2 +"-->Es un heterograma");
        } else {
            System.out.println(palabra2+ "-->No es un heterograma");
        }
}

/*Anagrama */
static void Anagrama(String palabra1, String palabra2) {
    char[] word1 = palabra1.toCharArray();
    char[] word2 = palabra2.toCharArray();
    Arrays.sort(word1);
    Arrays.sort(word2);
    
    boolean esAnagrama = Arrays.equals(word1, word2);
    
    if (esAnagrama) {
        System.out.println(palabra1+" y "+ palabra2+ "--> Son anagramas");
    } else {
        System.out.println(palabra1+" y "+ palabra2+ "--> No son anagramas");
      
    }
}

/*Palindromo */
static void Palindromo(String palabra1, String palabra2, String palabraInvertida, String palabraInvertida2) {
    for(int i=palabra1.length()-1;i>=0;i--){
        palabraInvertida+=palabra1.charAt(i);
    }
    for (int i = palabra2.length() - 1; i >= 0; i--) {
        palabraInvertida2 += palabra2.charAt(i);
    }
    
    if(palabra1.equalsIgnoreCase(palabraInvertida)){
        System.out.println("Es palindromo-->" + palabra1);
    
    }else{
        System.out.println(palabra1+ "--> No es palindromo");
    }
    
    if(palabra2.equalsIgnoreCase(palabraInvertida2)){
        System.out.println("Es palindromo-->" + palabra2);
    
    }else{
        System.out.println(palabra2 +"--> No es palindromo");
    }


}



}

    

