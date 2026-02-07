import java.io.*;
import java.util.Scanner;

public class FranDev200 {
    static File file = new File("Almacen.txt");

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

            fr.close();
            bffr.close();

        }catch (IOException e){
            System.out.println("ERROR: " +  e.getMessage());
        }

        System.out.println("ENTER para salir y eliminar el fichero: ");
        scan.nextLine();


        System.out.println("Eliminando el fichero...");
        fichero.delete();


/*
            DIFICULTAD EXTRA (opcional):
            * Desarrolla un programa de gestión de ventas que almacena sus datos en un archivo .txt.
            * - Cada producto se guarda en una línea del archivo de la siguiente manera:
            *   [nombre_producto], [cantidad_vendida], [precio].
            * - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
            *   actualizar, eliminar productos y salir.
            * - También debe poseer opciones para calcular la venta total y por producto.
            * - La opción salir borra el .txt.

         */

        int respuesta;

        while (true) {

            System.out.println("GESTIÓN DE VENTAS DEL ALMACEN");
            System.out.println("=============================");
            System.out.println("1 - Añadir producto.");
            System.out.println("2 - Consultar productos totales.");
            System.out.println("3 - Editar producto.");
            System.out.println("4 - Eliminar producto.");
            System.out.println("5 - Salir.");
            System.out.println("=============================");
            System.out.print("Respuesta: ");

            try {
                respuesta = Integer.parseInt(scan.nextLine());
            } catch (NumberFormatException e) {
                System.out.println("Entrada no válida.\n");
                continue;
            }

            switch (respuesta) {

                case 1:
                    aniadirProducto(scan);
                    break;

                case 2:

                    if (!file.exists()) {
                        System.out.println("El fichero no existe.\n");
                        break;
                    }

                    try(BufferedReader bufferedReader = new BufferedReader(new FileReader(file))){

                        if(bufferedReader.readLine() == null){
                            System.out.println("No hay productos guardados.\n");
                            break;
                        }
                    }catch (IOException e){
                        System.out.println("Error al leer el archivo.\n");
                    }

                    listarProductos();
                    break;

                case 3:

                    if (!file.exists()) {
                        System.out.println("El fichero no existe\n");
                        break;
                    }

                    try(BufferedReader bufferedReader = new BufferedReader(new FileReader(file))){
                        if(bufferedReader.readLine() == null){
                            System.out.println("No hay productos guardados.\n");
                            break;
                        }
                    }catch (IOException e){
                        System.out.println("Error al leer el archivo.\n");
                    }

                    listarProductos();

                    System.out.print("Número del producto a editar: ");
                    int idEditar = Integer.parseInt(scan.nextLine());
                    editarProducto(scan, idEditar);
                    break;

                case 4:

                    if (!file.exists()) {
                        System.out.println("El fichero no existe.\n");
                        break;
                    }

                    try(BufferedReader bufferedReader = new BufferedReader(new FileReader(file))){
                        if(bufferedReader.readLine() == null){
                            System.out.println("No hay productos guardados.\n");
                            break;
                        }
                    }catch (IOException e){
                        System.out.println("Error al leer el archivo.\n");
                    }

                    listarProductos();

                    System.out.print("Número del producto a eliminar: ");
                    try {
                        int idEliminar = Integer.parseInt(scan.nextLine());
                        eliminarProducto(idEliminar);
                    }catch (NumberFormatException e){
                        System.out.println(e.getMessage());
                    }
                    break;

                case 5:
                    scan.close();
                    file.delete();
                    System.out.println("Saliendo de la base de datos...");
                    System.exit(0);
            }
        }
    }

    // ============================
    // AÑADIR PRODUCTO
    // ============================
    private static void aniadirProducto(Scanner scan) {

        try (BufferedWriter bw = new BufferedWriter(new FileWriter(file, true))) {

            System.out.print("Nombre del producto: ");
            String nombre = scan.nextLine();

            System.out.print("Cantidad: ");
            int cantidad = Integer.parseInt(scan.nextLine());

            System.out.print("Precio: ");
            double precio = Double.parseDouble(scan.nextLine());

            bw.write(nombre + " [ " + cantidad + " ud ] --> " + precio + " €/ud");
            bw.newLine();

            System.out.println("Producto guardado correctamente.\n");

        } catch (IOException | NumberFormatException e) {
            System.out.println("Error al añadir producto.\n");
        }
    }

    // ============================
    // LISTAR PRODUCTOS
    // ============================
    private static void listarProductos() {

        try (BufferedReader br = new BufferedReader(new FileReader(file))) {

            String linea;
            int contador = 1;
            double ventaTotalProducto = 0;
            double ventaTotalTodosLosProductos = 0;

            System.out.println("\nLISTADO DE PRODUCTOS");
            System.out.println("====================");

            while ((linea = br.readLine()) != null) {

                int cantidad = Integer.parseInt(linea.split(" ")[2].trim());
                double precio = Double.parseDouble(linea.split(" ")[6].trim());

                ventaTotalProducto += cantidad * precio;
                ventaTotalTodosLosProductos += ventaTotalProducto;
                System.out.println(contador + " - " + linea + ". \nVENTA TOTAL: " + ventaTotalProducto + "€");
                contador++;
            }
            System.out.println("=======================");
            System.out.println("Precio total de todos los productos: " +  ventaTotalTodosLosProductos + "€");
            System.out.println();

            if (contador == 1) {
                System.out.println("No hay productos registrados.\n");
            }

        } catch (IOException e) {
            System.out.println("Error al leer el archivo.\n");
        }
    }

    // ============================
    // ELIMINAR PRODUCTO
    // ============================
    private static void eliminarProducto(int idEliminar) {

        File temp = new File("temp.txt");
        int contador = 1;

        try (
                BufferedReader br = new BufferedReader(new FileReader(file));
                BufferedWriter bw = new BufferedWriter(new FileWriter(temp))
        ) {

            String linea;
            while ((linea = br.readLine()) != null) {

                if (contador != idEliminar) {
                    bw.write(linea);
                    bw.newLine();
                }
                contador++;
            }

        } catch (IOException e) {
            System.out.println("Error al eliminar producto.\n");
            return;
        }

        file.delete();
        temp.renameTo(file);
        System.out.println("Producto eliminado correctamente.\n");
    }

    // ============================
    // EDITAR PRODUCTO
    // ============================
    private static void editarProducto(Scanner scan, int idEditar) {

        System.out.print("Cantidad: ");
        int cantidad = Integer.parseInt(scan.nextLine());

        System.out.print("Precio: ");
        double precio = Double.parseDouble(scan.nextLine());

        File temp = new File("temp.txt");
        int contador = 1;

        try (
                BufferedReader br = new BufferedReader(new FileReader(file));
                BufferedWriter bw = new BufferedWriter(new FileWriter(temp))
        ) {

            String linea;
            String nomProducto;
            while ((linea = br.readLine()) != null) {

                if (contador == idEditar) {

                    nomProducto = linea.toString().split(" ")[0].toString();
                    System.out.println("Nombre del producto: " + nomProducto);
                    linea = nomProducto + " [ " + cantidad + " ud ] --> " + precio + " €/ud";

                    bw.write(linea);
                    bw.newLine();
                }else{
                    bw.write(linea);
                    bw.newLine();
                }
                contador++;
            }

        } catch (IOException e) {
            System.out.println("Error al editar producto.\n");
            return;
        }

        file.delete();
        temp.renameTo(file);
        System.out.println("Producto editado correctamente.\n");

    }
}
