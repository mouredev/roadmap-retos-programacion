import java.util.Arrays;
import java.util.HashMap;

public class Kine_jdf {
    public static void main(String[] args) {
        // Operaciones con Strings
    String str = "Esta es mi cadena";
    System.out.println("Longitud: " + str.length());
     System.out.println("Carácter específico: " + str.charAt(0));
    System.out.println("Subcadena: " + str.substring(0, 4));
     System.out.println("Concatenación: " + str.concat(" de Java"));
     System.out.println("Mayúsculas: " + str.toUpperCase());
     System.out.println("Minúsculas: " + str.toLowerCase());
    System.out.println("Reemplazo: " + str.replace('o', 'a'));
    String[] division = str.split(" ");
    System.out.println("División: " + Arrays.toString(division));
    String union = String.join("-", division);
    System.out.println("Unión: " + union);
        
         System.out.println("Palindromo Zorra - Arroz " + palindromo("Zorra", "Arroz")); //true
         System.out.println("No es palindromo Casa - Saco " + palindromo("Casa", "Saco")); //false

  System.out.println("Anagrama Lacteo Coleta: " + anagram("lacteo","coleta"));

  System.out.println("Isograma Musica: " + isograma("Musica"));  /true
System.out.println("Isograma Intestinos: " + isograma("Intestinos"));  //true
System.out.println("Isograma Entender: " + isograma("Entender"));  //false
    }

static boolean palindromo(String uno, String dos){
    boolean son=false;
    String aux="";
 if(uno.length()==dos.length()){
     
     for (int j= uno.length(); j>0;j--){
aux +=  uno.charAt((j-1)); }
     
      }
    
    if(aux.equalsIgnoreCase(dos)){son=true;}
    
    
    return son; }  //

static boolean  anagram (String uno, String dos){
         boolean son=false; 
         char[] aux;
          char[] aux2;
         if(uno.length()==dos.length()){
             
             aux = uno.toCharArray();
             aux2=dos.toCharArray();
            aux.sort();
            aux2.sort();
son = aux.toString().equalsIgnoreCase(aux2.toString());
     }       
               return son; }

//metodo que analiza tanto heterogramas (todas letras sin repetir) como isograma(cuando una letra se repite, que se repita un nro par)
 static boolean isograma(String palabra) {
        HashMap<Character, Integer> frecuencias = new HashMap<>();

        for (char letra : palabra.toCharArray()) {
            frecuencias.put(letra, frecuencias.getOrDefault(letra, 0) + 1);
        }

        for (int frecuencia : frecuencias.values()) {
            if (frecuencia > 1) {
                // Verificar si el número de apariciones es impar
                if (frecuencia % 2 != 0) {
                    return false;
                }
            }
        }
        return true;
    }
        

   

}
