/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.codesecretchristmas;

import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

/**
 *
 * @author JOHN
 * * EJERCICIO:
 * Papá Noel tiene que comenzar a repartir los regalos...
 * ¡Pero ha olvidado el código secreto de apertura del almacén!
 *
 * Crea un programa donde introducir códigos y obtener pistas.
 *
 * Código:
 * x El código es una combinación de letras y números aleatorios
 *   de longitud 4. (Letras: de la A a la C, Números: del 1 al 3)
 * x No hay repetidos.
 * x Se genera de manera aleatoria al iniciar el programa.
 *
 * Usuario:
 * x Dispone de 10 intentos para acertarlo.
 * x En cada turno deberá escribir un código de 4 caracteres, y
 *   el programa le indicará para cada uno lo siguiente:
 *   - Correcto: Si el caracter está en la posición correcta.
 *   - Presente: Si el caracter existe, pero esa no es su posición.
 *   - Incorrecto: Si el caracter no existe en el código secreto.
 * - Deben controlarse errores de longitud y caracteres soportados.
 *
 * Finalización:
 * - Papa Noel gana si descrifra el código antes de 10 intentos.
 * - Pierde si no lo logra, ya que no podría entregar los regalos.

 */

public class CodeSecretChristmas {
    static int attemps = 10;
    
    public static String[] getLetters(){
        String[] letters = {"A","B","C","1","2","3"};
        
        return letters;
    }
    
    public static String generatedKey(){
        Set<String> key = new HashSet<>();
        String[] ls = getLetters();
        
        while(key.size() < 4){
            int number = (int) (Math.random()* ls.length);
            key.add(ls[number]);
        }
        String s = String.join("", key);
        
        return s;
    }
    
    
    public static String validKey(String keyGenerated, char character, int index){
        String flap = "";
        if(keyGenerated.charAt(index) == character && keyGenerated.indexOf(""+character) == index){
            flap = "c";
        }else if(keyGenerated.contains(""+character)){
            flap = "p";
        }else{
            flap = "i";
        }
        return flap;
    }
    
    public static boolean isValid(String code){
        boolean f = false;
        for(int x=0; x < getLetters().length; x++){
            if(code.contains(getLetters()[x])){
                f = true;
            }else{
                f = false;
            }
        }
        
        return f;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String code;
        String keyGenerated = generatedKey();
        
        System.out.println("Almacen de Santa");
        
        while(attemps < 11){
            
            System.out.println("Ingresa codigo de seguridad: ");
            code = scanner.nextLine().toUpperCase();
            
            while(!isValid(code)){
                System.out.println("Ingresa codigo de seguridad (A,B,C y 1, 2, 3): ");
                code = scanner.nextLine().toUpperCase();
                System.out.println("Hay uno o mas caracter(es) que no son permitidos");
                System.out.printf("son permitidos: ");
                for(String k: getLetters()){
                    System.out.printf(k+", ");
                    
                }
                System.out.println("");
            }
            
            
            if(code.length() == 4){
               for(int i=0; i<4; i++){
                    switch(validKey(keyGenerated,code.charAt(i), i)){
                        case "c":
                            System.out.println("Correcto: "+code.charAt(i));
                            break;
                        case "p":
                            System.out.println("Presente: "+code.charAt(i));
                            break;
                        case "i":
                            System.out.println(code.charAt(i)+ " No concuerda con el codigo generado.");
                            break;
                    }
               } 
            }else{
                System.out.println("el codigo debe contener solo 4 caracteres");
                System.out.println("codigo: "+code.toLowerCase());
            }
            
            if(keyGenerated.equals(""+code)){
                System.out.println("Acceso concedido clave: "+keyGenerated);
            }else{
                attemps -= 1;
                System.out.println("Te quedan #"+attemps+" intentos");
            }
        }

    }
}
