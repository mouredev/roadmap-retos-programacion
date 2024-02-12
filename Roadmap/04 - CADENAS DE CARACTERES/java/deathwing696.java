
import java.util.Arrays;
import java.util.Scanner;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/*
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 */

/**
 *
 * @author death
 */
public class deathwing696 {
    
    private Scanner lectura = new Scanner(System.in);
    
    public static void main(String[] args)
    {
        String palabra1 = "amor", palabra2 = "Roma";
        Boolean palindromo1, palindromo2, anagrama, isograma1, isograma2;
        
        palindromo1 = EsPalindromo(palabra1);
        palindromo2 = EsPalindromo(palabra2);
        anagrama = EsAnagrama(palabra1, palabra2);
        isograma1 = EsIsograma(palabra1);
        isograma2 = EsIsograma(palabra2);
        
        if (palindromo1 && isograma1)
            System.out.println("La palabra " + palabra1 + " es palíndromo e isograma");
        else if (palindromo1)
            System.out.println("La palabra " + palabra1 + " es palíndromo");
        else if (isograma2)
            System.out.println("La palabra " + palabra1 + " es un isograma");
        
        if (palindromo2 && isograma2)
            System.out.println("La palabra " + palabra2 + " es palíndromo e isograma");
        else if (palindromo2)
            System.out.println("La palabra " + palabra2 + " es palíndromo");
        else if (isograma2)
            System.out.println("La palabra " + palabra2 + " es un isograma");
        
        if (anagrama)
            System.out.println("Las palabras " + palabra1 + " y " + palabra2 + " son anagramas");
        
    }
    
    private static Boolean EsPalindromo(String palabra)
    {
        String palabraReves;
        
        palabra = palabra.replace("\\s", "").toLowerCase();
        
        palabraReves = new StringBuilder(palabra).reverse().toString();
        
        return palabra.equals(palabraReves);
    }
    
    private static Boolean EsAnagrama(String palabra1, String palabra2)
    {
        char [] array1, array2;
        
        palabra1 = palabra1.replace("\\s", "").toLowerCase();
        palabra2 = palabra2.replace("\\s", "").toLowerCase();
        array1 = palabra1.toCharArray();
        Arrays.sort(array1);
        array2 = palabra2.toCharArray();        
        Arrays.sort(array2);
        
        return Arrays.equals(array1, array2);
    }
    
    private static Boolean EsIsograma(String palabra)
    {
        for (int i = 0; i < palabra.length();  i++)
        {
            for (int j = i + 1; j < palabra.length(); j++)
            {
                if (palabra.charAt(i) == palabra.charAt(j))
                    return false;
            }
        }
        
        return true;
    }
}
