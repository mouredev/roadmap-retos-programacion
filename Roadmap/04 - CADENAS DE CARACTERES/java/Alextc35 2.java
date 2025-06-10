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

import java.util.Arrays;

public class Alextc35 {
        public static void main(String[] args) {
                // Acceso a caracteres específicos
                System.out.println("\n--- Caracteres específicos ----");
                String texto = "Hola Mundo"; // String con 10 caracteres
                char caracter = texto.charAt(5); // Índice [0-9]
                System.out.println("Texto completo: " + texto);
                System.out.println("- Caracter en el índice 5: " + caracter); // M
                System.out.println("-------------------------------\n");

                // Subcadenas
                System.out.println("--------- Subcadenas ----------");
                System.out.println("Texto completo: " + texto);
                String subcadena1 = texto.substring(0, 4); // Hola
                String subcadena2 = texto.substring(5); // Mundo
                System.out.println("- Primera subcadena: " + subcadena1
                                + "\n- Segunda subcadena: " + subcadena2);
                System.out.println("-------------------------------\n");

                // Longitud
                System.out.println("---------- Longitud -----------");
                System.out.println("Texto completo: " + texto);
                int longitud = texto.length(); // 10
                System.out.println("- Longitud de la cadena: " + longitud);
                System.out.println("-------------------------------\n");

                // Concatenación
                System.out.println("-------- Concatenación --------");
                System.out.println("Subcadena1: " + subcadena1
                                + "\nSubcadena2: " + subcadena2
                                + "\n- Subcadena1+Subcadena2: " + subcadena1 + subcadena2);
                System.out.println("-------------------------------\n");

                // Repetición
                System.out.println("--------- Repetición ----------");
                texto = "Hola ";
                System.out.println("Texto completo: " + texto);
                String repetido = texto.repeat(3); // Repite la cadena 3 veces
                System.out.println("- Cadena repetida: " + repetido);
                System.out.println("-------------------------------\n");

                // Recorrido
                System.out.println("---------- Recorrido ----------");
                texto = "Hola Mundo";
                System.out.println("Texto completo: " + texto);
                for (int i = 0; i < texto.length(); i++) {
                        System.out.println("- Caracter en el índice " + i + ": "
                                        + texto.charAt(i));
                }
                System.out.println("-------------------------------\n");

                // Conversión a mayúsculas y mínusculas
                System.out.println("--- Conversión a mayús y mínus ---");
                String mayusculas = texto.toUpperCase();
                String minusculas = texto.toLowerCase();
                System.out.println("Texto completo: " + texto);
                System.out.println("- Texto en mayúsculas: " + mayusculas
                                + "\n- Texto en minúsculas: " + minusculas);
                System.out.println(" ------------------------------\n");

                // Reemplazo
                System.out.println("---------- Reemplazo ----------");
                System.out.println("Texto completo: " + texto);
                String reemplazado = texto.replace("Mundo", "Java"); // Reemplaza "Mundo" por "Java"
                System.out.println("- Cadena después del reemplazo:\n" + reemplazado);
                System.out.println("-------------------------------\n");

                // División
                System.out.println("---------- División -----------");
                texto = "Hola,Mundo,Java";
                System.out.println("Texto completo: " + texto);
                String[] palabras = texto.split(","); // Divide la cadena por comas
                for (String palabra : palabras) {
                        System.out.println("- Palabra: " + palabra);
                }
                System.out.println("-------------------------------\n");

                // Unión
                System.out.println("------------ Unión ------------");
                StringBuilder builder = new StringBuilder();
                builder.append("Hola");
                builder.append(" ");
                builder.append("Mundo");
                String resultado = builder.toString();
                System.out.println("- Cadena unida: " + resultado);
                System.out.println("-------------------------------\n");

                // Interpolación
                System.out.println("-------- Interpolación --------");
                texto = "Mundo";
                int edad = 23;
                String mensaje = String.format("Hola %s, tienes %d años.", texto, edad);
                System.out.println(mensaje);
                System.out.println("-------------------------------\n");

                // Verificación
                System.out.println("-------- Verificación ---------");
                texto = "Hola Mundo";
                boolean contiene = texto.contains("Mundo"); // True
                boolean empiezaCon = texto.startsWith("Hola"); // True
                boolean terminaCon = texto.endsWith("Mundo"); // True
                System.out.println("- Contiene 'Mundo': " + contiene
                                + "\n- Empieza con 'Hola': " + empiezaCon
                                + "\n- Termina con 'Mundo': " + terminaCon);
                System.out.println("-------------------------------\n");

                // Opcional

                // Palíndromos
                System.out.println("--------- Palíndromo ----------");
                String oracion = "Anita lava la tina";
                System.out.println(oracion + "\n¿Es palíndromo?: "
                                + palindromo(oracion) + "\n");

                oracion = "Mi slim";
                System.out.println(oracion + "\n¿Es palíndromo?: "
                                + palindromo(oracion));
                System.out.println("-------------------------------\n");

                // Anagramas
                System.out.println("--------- Anagramas -----------");
                String palabra1 = "Amor";
                String palabra2 = "Roma";
                System.out.println("¿" + palabra1 + " y " + palabra2 + " son anagramas?: " +
                                anagrama(palabra1, palabra2) + "\n");

                palabra1 = "Robo";
                palabra2 = "Bolo";
                System.out.println("¿" + palabra1 + " y " + palabra2 + " son anagramas?: " +
                                anagrama(palabra1, palabra2));
                System.out.println("-------------------------------\n");

                // Isogramas
                System.out.println("--------- Isogramas -----------");
                String palabra = "Joven";
                System.out.println(palabra + "\n¿es un isograma?: " + isograma(palabra)
                                + "\n");

                palabra = "Carnaval";
                System.out.println(palabra + "\n¿es un isograma?: " + isograma(palabra));
                System.out.println("-------------------------------\n");
        }

        // Palíndromos
        public static boolean palindromo(String palabra) {
                // Pasamos a mínusculas y omitimos los espacios
                palabra = palabra.toLowerCase().replace(" ", ""); // Los " " se eliminan
                String palabraInversa = ""; // Inicializamos la palabraInversa
                for (int i = palabra.length() - 1; i >= 0; i--) { // Recorremos al revés la palabra
                        palabraInversa += palabra.charAt(i); // Guardamos cada carácter
                }
                if (palabra.equals(palabraInversa)) {
                        return true; // Si son iguales, true
                } else {
                        return false; // Si no, false
                }
        }

        // Anagramas
        public static boolean anagrama(String palabra1, String palabra2) {
                if (palabra1.length() != palabra2.length()) {
                        return false;
                } // Si no tienen la misma longitud, directamente false

                palabra1 = palabra1.toLowerCase(); // Palabra a mínusculas
                palabra2 = palabra2.toLowerCase(); // Palabra a mínusculas
                char[] charsPalabra1 = new char[palabra1.length()]; // Array de chars
                char[] charsPalabra2 = new char[palabra2.length()]; // Array de chars

                // Amor
                for (int i = 0; i < palabra1.length(); i++) {
                        charsPalabra1[i] = palabra1.charAt(i);
                }

                // Roma
                for (int i = 0; i < palabra2.length(); i++) {
                        charsPalabra2[i] = palabra2.charAt(i);
                }

                // Las ordenamos, y si son iguales, son anagramas
                Arrays.sort(charsPalabra1);
                Arrays.sort(charsPalabra2);

                if (Arrays.equals(charsPalabra1, charsPalabra2)) {
                        return true; // Si son iguales true
                } else {
                        return false; // Si no, false
                }
        }

        // Isogramas
        public static boolean isograma(String palabra) {
                palabra = palabra.toLowerCase(); // Transformamos la palabra a mínusculas
                char[] letras = new char[palabra.length()]; // Array de chars
                for (int i = 0; i < palabra.length(); i++) {
                        letras[i] = palabra.charAt(i); // Añadimos cada letra al Array
                }

                Arrays.sort(letras); // Ordenamos las letras en orden
                char buffer = ' '; // Creamos un buffer para ver la letra anterior

                for (char letra : letras) {
                        if (buffer == letra) { // Si dos letras son iguales,
                                return false; // devolver false
                        }
                        buffer = letra; // Añadimos la letra al buffer
                }
                return true; // Si ninguna es igual, devolver true
        }
}