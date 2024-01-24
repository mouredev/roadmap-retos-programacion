import java.lang.String;
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

        String nuevaCadena = " Con Java";
        String cadenaConcatenada = cadena + nuevaCadena;
        System.out.println(cadenaConcatenada); // Concatenacion

        System.out.println(cadena.concat(nuevaCadena).concat(" - OOP")); // Concatenacion

        System.out.println(cadena.repeat(2)); // Repetición - El String "cadena" se repite 2 veces

        System.out.println(cadena.toUpperCase()); // Conversion a mayuscula

        System.out.println(cadena.toLowerCase()); // Conversion a minuscula

        String reemplazarCaracter = cadena.replace('4','5');
        System.out.println(reemplazarCaracter); // Reemplazar Caracter

        String reemplazarCadena = cadena.replace("RoadMap", "MapRoad");
        System.out.println(reemplazarCadena); // Reemplazar Cadena

    }
}
