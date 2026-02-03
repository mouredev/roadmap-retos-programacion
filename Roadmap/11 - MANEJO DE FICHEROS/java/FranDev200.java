import java.io.*;
import java.util.Scanner;

public class FranDev200 {

    static void main() {
        /*

            EJERCICIO:
            * Desarrolla un programa capaz de crear un archivo que se llame como
            * tu usuario de GitHub y tenga la extensión .txt.
            * Añade varias líneas en ese fichero:
            * - Tu nombre.
            * - Edad.
            * - Lenguaje de programación favorito.
            * Imprime el contenido.
            * Borra el fichero.

         */

        Scanner scan = new Scanner(System.in);

        String usuarioGithub;
        String nombre;
        int edad;
        String lenguajeFavorito;

        System.out.print("Introduce el nombre del usuario de Github: ");
        usuarioGithub = scan.nextLine();
        System.out.print("Ingrese su nombre: ");
        nombre = scan.nextLine();
        System.out.print("Ingrese su edad: ");
        edad = Integer.parseInt(scan.nextLine());
        System.out.print("Ingrese lenguaje de programacion favorito: ");
        lenguajeFavorito = scan.nextLine();

        String nombreFichero = usuarioGithub + ".txt";
        File fichero = new File(nombreFichero);

        System.out.println("\nCreando y escribiendo en el fichero...");

        try{
            FileWriter fw = new FileWriter(fichero);
            BufferedWriter bffw = new BufferedWriter(fw);
            bffw.write(" - " + nombre + "\n");
            bffw.write(" - " + edad + "\n");
            bffw.write(" - " + lenguajeFavorito);
            bffw.close();

        }catch (IOException e){
            System.out.println("ERROR: " +  e.getMessage());
        }

        System.out.println("Contenido del fichero:");
        System.out.println("======================");

        try{
            FileReader fr = new FileReader(fichero);
            BufferedReader bffr = new BufferedReader(fr);

            String linea;
            while ((linea = bffr.readLine()) != null) {
                System.out.println(linea);
            }

            bffr.close();

        }catch (IOException e){
            System.out.println("ERROR: " +  e.getMessage());
        }

        System.out.println("ENTER para eliminar el fichero: ");
        scan.nextLine();


        System.out.println("Eliminando el fichero...");
        fichero.delete();
    }


}
