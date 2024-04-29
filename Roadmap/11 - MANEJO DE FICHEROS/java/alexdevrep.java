package _11_Manejo_de_ficheros_;
/*
 * IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
 *
 * EJERCICIO:
 * Desarrolla un programa capaz de crear un archivo que se llame como
 * tu usuario de GitHub y tenga la extensión .txt.
 * Añade varias líneas en ese fichero:
 * - Tu nombre.
 * - Edad.
 * - Lenguaje de programación favorito.
 * Imprime el contenido.
 * Borra el fichero.
 *
 * DIFICULTAD EXTRA (opcional):
 * Desarrolla un programa de gestión de ventas que almacena sus datos en un
 * archivo .txt.
 * - Cada producto se guarda en una línea del arhivo de la siguiente manera:
 *   [nombre_producto], [cantidad_vendida], [precio].
 * - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
 *   actualizar, eliminar productos y salir.
 * - También debe poseer opciones para calcular la venta total y por producto.
 * - La opción salir borra el .txt.
 */

//Importamos las librerías necesarias para el proyecto
import java.io.*;
import java.util.LinkedList;
import java.util.List;
import java.util.Objects;

public class _11_Manejo_de_ficheros {
    public static void main (String args[]){
        //Creamos el archivo txt
        File file = new File("alexdevrep.txt");
        String contenido ="Alejandro\n24\nJava\n";
        //Añadimos contenido al archivo
        escribirArchivo(file, contenido, false);
        //Leemos el archivo
        System.out.println("Contenido del archivo:\n" + leerArchivo(file));
        //Borramos el archivo
        boolean isDelete = file.delete();


    }

    static void escribirArchivo(File file, String content, boolean append) {
        if (!file.exists()) {
            try {
                file.createNewFile();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }

        try (Writer w = new FileWriter(file, append);
             BufferedWriter bw = new BufferedWriter(w)) {
            bw.write(content);
            bw.flush();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    static String leerArchivo(File file) {
        StringBuilder sb = new StringBuilder();

        try (Reader r = new FileReader(file);
             BufferedReader br = new BufferedReader(r))  {
            String linea;
            while ((linea = br.readLine()) != null) {
                sb.append(linea).append("\n");
            }
        } catch (Exception e) {
            e.printStackTrace();
        }

        return sb.toString();
    }

}
