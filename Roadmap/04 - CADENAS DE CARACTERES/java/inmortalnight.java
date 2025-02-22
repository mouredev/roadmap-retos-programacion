// 04 - CADENAS DE CARACTERES

import java.util.ArrayList;
import java.util.Scanner;

public class inmortalnight {
    public static void main(String[] args) {
        // Ejemplos de operaciones con cadenas de caracteres
        String cadena = "Hola Mundo";
        System.out.println("Cadena: " + cadena);
        System.out.println("Longitud: " + cadena.length());
        System.out.println("Caracter en la posición 4: " + cadena.charAt(4));
        System.out.println("Subcadena desde la posición 5: " + cadena.substring(5));
        System.out.println("Concatenación: " + cadena.concat(" desde Java"));
        System.out.println("Repetición: " + cadena.repeat(3));
        System.out.println("Recorrido: ");
        for (int i = 0; i < cadena.length(); i++) {
            System.out.println(cadena.charAt(i));
        }
        System.out.println("Mayúsculas: " + cadena.toUpperCase());
        System.out.println("Minúsculas: " + cadena.toLowerCase());
        System.out.println("Reemplazo: " + cadena.replace("Hola", "Adiós"));
        System.out.println("División: " + cadena.split(" ")[0]);
        System.out.println("Unión: " + String.join(" ", "Hola", "Mundo"));
        System.out.println("Interpolación: " + String.format("Hola %s", "Mundo"));
        System.out.println("Verificación: " + cadena.equals("Hola Mundo"));
        
        comprobar();
    }
    // EXTRA: Comprobaciones
    public static void comprobar() {
        System.out.println("------Comprobaciones-----");
        System.out.println("Nota: las comprobaciones dan prioridad a la primera palabra introducida");
        // Entrada de datos
        Scanner scanner = new Scanner(System.in);
        System.out.print("Introduce la primera palabra: ");
        String palabra1 = scanner.nextLine();
        System.out.print("Introduce la segunda palabra: ");
        String palabra2 = scanner.nextLine();
        // Comprobaciones
        System.out.println("Palíndromo: " + esPalindromo(palabra1));
        System.out.println("Anagrama: " + esAnagrama(palabra1, palabra2));
        System.out.println("Isograma: " + esIsograma(palabra1));
        scanner.close();
    }
    // Palindromo: es una palabra o frase que se lee igual de izquierda a derecha que de derecha a izquierda
    public static boolean esPalindromo(String palabra) {
        return palabra.equals(new StringBuilder(palabra).reverse().toString());
    }
    // Anagrama: es una palabra o frase que contiene las mismas letras que otra palabra o frase
    public static boolean esAnagrama(String palabra1, String palabra2) {
        ArrayList<Character> lista1 = new ArrayList<>();
        for (char c : palabra1.toCharArray()) {
            lista1.add(c);
        }
        ArrayList<Character> lista2 = new ArrayList<>();
        for (char c : palabra2.toCharArray()) {
            lista2.add(c);
        }
        lista1.sort(Character::compareTo);
        lista2.sort(Character::compareTo);
        return lista1.equals(lista2);
    }
    // Isograma: es una palabra o frase que no contiene letras repetidas
    public static boolean esIsograma(String palabra) {
        return palabra.chars().distinct().count() == palabra.length();
    }
}