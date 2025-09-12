import java.util.Arrays;
import java.util.Scanner;

public class Gerthai08 {
    public static void main(String[] args) {

        //Motrar una cadena de texto
        System.out.println("=====Cadena de texto=====");
        String texto = "Hola, esto es una Cadena de texto";
        System.out.println(texto);

        //Concatenación
        System.out.println("=====Concatenación de textos=====");
        String concatenacion = " , estoy programando con java";
        System.out.println(texto + concatenacion);
        System.out.println(texto.concat(concatenacion)); //Método para concatenar

        //Longitud de una cadena
        System.out.println("=====Longitud de la cadena de texto=====");
        String txt = "abcdefghijklmnopq";
        System.out.println("La longitud del texto es de: " + txt.length());

        //Texto en mayúsculas y en minúsculas
        System.out.println("=====Texto en mayúsculas=====");
        System.out.println(txt.toUpperCase());
        System.out.println("=====Texto en minúsculas=====");
        System.out.println(txt.toLowerCase());

        //Encontrar la posición de la palabra que quiero buscar
        System.out.println("=====Buscar palabra por indice=====");
        System.out.println(texto.indexOf("Cadena")); //tiene que dar como resultado el índice donde empieza la palabra asignada

        //Caracteres especiales
        System.out.println("=====Asignar comillas dobles=====");
        System.out.println("Somos los llamados \"Vikingos\" del norte"); //la barra invertida se coloca antes para asignar la comilla doble
        System.out.println("=====Asignar comillas simples=====");
        System.out.println("Somos los llamados \'Vikingos\' del norte");
        System.out.println("=====Asignar comillas Barra invertida=====");
        System.out.println("Somos los llamados \\Vikingos\\ del norte");
        System.out.println("=====Asignar salto de linea=====");
        System.out.println("Aplicando salto de \nlinea");
        System.out.println("=====Asignar retorno de carro=====");
        System.out.println("Hola \rMundo"); //Tiene que retornar solamente la palabra "Mundo", ya que el cursor vuelve al inicio
        System.out.println("=====Asignar tabulador=====");
        System.out.println("Hola \tMundo");
        System.out.println("=====Borrar una letra=====");
        System.out.println("Hol\ba Mund\bo");
        System.out.println("=====Asignar salto de pagina=====");
        System.out.println("Hola \fMundo");

        //subcadenas
        System.out.println("=====Subcadena sin argumento \"FINAL\"=====");
        System.out.println(texto.substring(6));
        System.out.println("=====Subcadena con argumento \"FINAL\"=====");
        System.out.println(texto.substring(6, 24));

        //repetición
        System.out.println("=====Repetición de texto=====");
        System.out.println((texto + "\n").repeat(3));

        //acceso a un carácter desde una posición específica
        System.out.println("=====Traer carácter desde una posición especifica=====");
        System.out.println(texto.charAt(3));

        //Recorrido
        System.out.println("=====Recorrido de texto=====");
        for (int i = 0; i < txt.length(); i++) {
            System.out.println(txt.charAt(i));
        }

        //reemplazo+
        System.out.println("=====Reemplazando=====");
        System.out.println(texto.replace("Hola", "Bienvenidos"));

        //división
        String division = "rojo,verde,azul,amarillo";
        System.out.println("=====División por comas=====");
        String[] colores = division.split(",");
        for (String c : colores) {
            System.out.println(c);
        }

        System.out.println("=====División por espacios=====");
        String[] espacios = texto.split(" ");
        for (String p : espacios){
            System.out.println(p);
        }

        //union (join)
        System.out.println("=====Método de union=====");
        String join = String.join(" ", "Juan", "Pedro", "Homar");
        System.out.println(join);

        //Interpolación
        System.out.println("=====Implementando la interpolación=====");
        String interpolacion = "Hola %s! Estamos en el %,d";
        System.out.println(String.format(interpolacion,"Mundo",2025));

        //Verificación
        String texto1 = "Hola";
        String texto2 = "hola";
        String texto3 = " ";
        String texto4 = "Ejemplo de texto";

        System.out.println("=====Metodo de verificación \"equals\"=====");
        System.out.println("Equals: " + texto1.equals(texto2)); //false

        System.out.println("=====Metodo de verificación \"equalsIgnoreCase\"=====");
        System.out.println("EqualsIgnoreCase: " + texto1.equalsIgnoreCase(texto2)); //true

        System.out.println("=====Metodo de verificación \"contains\"=====");
        System.out.println("Contains: " + texto4.contains("tex")); //true

        System.out.println("=====Metodo de verificación \"startsWith\"=====");
        System.out.println("startsWith: " + texto4.startsWith("Eje")); //true

        System.out.println("=====Metodo de verificación \"isEmpty\"=====");
        System.out.println("isEmpty: " + "".isEmpty()); //true

        System.out.println("=====Metodo de verificación \"isBlank\"=====");
        System.out.println("isBlank: " + texto3.isBlank()); //true

        //Ejercicio opcional
        extra();

    }
    public static void extra(){
        Scanner scanner = new Scanner(System.in);
        boolean running = true;

        System.out.println("¡Bienvenidos al juego de las palabras!");

        while (running){
            System.out.println("\nElige como quieres analizar la palabra");
            System.out.println("1. Palíndromo");
            System.out.println("2. Anagrama");
            System.out.println("3. Isograma");
            System.out.println("4. Salir");
            System.out.println("Selecciona una opción: ");

            String option = scanner.nextLine().trim();

            switch (option){
                case "1":
                    isPalindrome(scanner);
                    break;
                case "2":
                    isAnagram(scanner);
                    break;
                case "3":
                    isIsogram(scanner);
                    break;
                case "4":
                    running = false;
                    System.out.println("¡Hasta la próxima!");
                    break;
                default:
                    System.out.println("Opción no valida, intentalo de nuevo.");
            }
        }
        scanner.close();
    }

    private static void isIsogram(Scanner scanner) {
        String palabra = pedirDato(scanner, "Ingrese la palabra a analizar: ").toLowerCase().replaceAll("\\s+", "");

        boolean Isogram = true;

        for (int i = 0; i < palabra.length(); i++) {
            char letra = palabra.charAt(i);
            //Si la letra a parece mas de una vez
            if(palabra.indexOf(letra) != palabra.lastIndexOf(letra)){
                Isogram = false;
                break;
            }
        }
        if (Isogram){
            System.out.println("La palabra analizada es un Isograma");
        }else{
            System.out.println("La palabra analizada no es un Isograma");
        }
    }

    private static void isAnagram(Scanner scanner) {
        //Pedimos las dos palabras
        String palabra1 = pedirDato(scanner,"Ingrese la primer palabra: ").toLowerCase().replaceAll("\\s+", "");
        String palabra2 = pedirDato(scanner,"Ingrese la segunda palabra: ").toLowerCase().replaceAll("\\s+", "");;

        //Convertimos a array de caracteres
        char[] array1 = palabra1.toCharArray();
        char[] array2 = palabra2.toCharArray();

        //Ordenamos los arrays
        Arrays.sort(array1);
        Arrays.sort(array2);

        //Comparamos
        if(Arrays.equals(array1,array2)){
            System.out.println("Las palabras que asignaste son Anagramas");
        }else{
            System.out.println("Las palabras que asignaste no son Anagramas");
        }
    }
    //Verificación de palíndromo
    private static void isPalindrome(Scanner scanner) {
        String palabra = pedirDato(scanner,"Ingrese la palabra a analizar: ");

        //Normalizar: minúsculas y sin espacios
        palabra = palabra.toLowerCase().replaceAll("\\s","");

        //Invertir la palabra
        String invertida = new StringBuilder(palabra).reverse().toString();

        if (palabra.equals(invertida)) {
            System.out.println("La palabra \""+ palabra +"\" es un palíndromo. ");
        }else{
            System.out.println("La palabra \""+ palabra +"\" no es un palíndromo. ");
        }
    }

    //Metodo para introducir texto informativo y asignar el nombre a la variable scanner
    private static String pedirDato(Scanner scanner, String mensaje){
        System.out.println(mensaje);
        return scanner.nextLine().trim();
    }

}
