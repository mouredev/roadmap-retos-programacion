import java.lang.String;

import static java.lang.StringTemplate.STR;

public class frannmv {

    public static void main(String[] args) {
    /*  ***
        Operaciones con Cadenas de Caracteres
        ***
    */
        String cadena = "RoadMap 2024";

        char caracterEspecifico = cadena.charAt(0); // Acceso a Caracter Especifico
        System.out.println(caracterEspecifico);

        System.out.println(cadena.substring(8)); // Substring - Desde la posicion pasada por parametro hasta
                                                          // el final del String

        System.out.println(cadena.substring(0,7)); // Substring - Desde la posicion pasada en el pirmer parametro hasta
                                                  // la posicion del segundo parametro - 1

        System.out.println(cadena.length()); // Longitud de la Cadena

        System.out.println(cadena.concat(" Con Java").concat(" - OOP")); // Concatenacion

        System.out.println(cadena.repeat(2)); // Repetición - El String "cadena" se repite 2 veces

        System.out.println(cadena.toUpperCase()); // Conversion a mayuscula

        System.out.println(cadena.toLowerCase()); // Conversion a minuscula

        String reemplazarCaracter = cadena.replace('4','5');
        System.out.println(reemplazarCaracter); // Reemplazar Caracter

        String reemplazarCadena = cadena.replace("RoadMap", "MapRoad");
        System.out.println(reemplazarCadena); // Reemplazar Cadena

        String nuevaCadena = "Java-Object-Oriented-Programming";
        String[] palabras = nuevaCadena.split("-"); // División
        for(String palabra : palabras){
            System.out.println(palabra);
        }

        String cadenaConcatenada = cadena + nuevaCadena;
        System.out.println(cadenaConcatenada); // Union - Concatenacion

        nuevaCadena = "Java";
        String inter = STR."Estoy programando en \{nuevaCadena}";
        System.out.println(inter); // Interpolación

        inter = String.format("Estoy programando en %s", nuevaCadena);
        System.out.println(inter); // Interpolación

        System.out.println(nuevaCadena.equals(cadena)); // Verificacion

    }
}
