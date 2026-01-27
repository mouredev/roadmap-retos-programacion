import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

/* --- CONCEPTOS BÁSICOS EN MANEJO DE FICHEROS ---
* 1. Crear un archivo; con la clase File
* 2. Escribir datos; con la clase FileWriter o Files.writeString
* 3. Leer datos; clase Scanner o Files.readAllLines
*  4. Borrar datos; función .delete();  
*/

// ------- EXTRA -------
public class RodrigoGit87 {
    void main(String[] args) {
        String seller = "RodrigoGit87";
        File user = new File(seller);

        // SEleccion de opciones del menu
        Scanner sc = new Scanner(System.in);
        int opcion = 0;

        while (opcion != 6) {
            System.out.println("\n--- GESTIÓN DE VENTAS ---");
            System.out.println("1 - Añadir producto");
            System.out.println("2 - Consultar producto");
            System.out.println("3 - Actualizar producto");
            System.out.println("4 - Eliminar productos");
            System.out.println("5 - Calcular venta total");
            System.out.println("6 - SALIR ");
            System.out.print("Seleccione una opción: ");

            opcion = sc.nextInt();
            sc.nextLine(); // Limpiar el buffer después de leer un número

            switch (opcion) {
                case 1: // lógica de añadir -> nombre_producto, cantidad_prods_vendida, precio
                    System.out.println("Nombre del producto: ");
                    String name = sc.nextLine();
                    System.out.println("Cantidad de productos vendida: ");
                    int amount = sc.nextInt();
                    System.out.println("Precio de venta: ");
                    double value = sc.nextDouble();
                    sc.nextLine(); // depurar buffer

                    try (FileWriter writer = new FileWriter(user, true)) { // necesitamos que el programa sea capaz de
                                                                           // "añadir"nuevos
                        // productos sin borrar los anteriores. La clase FileWriter tiene un constructor
                        // especial para esto:
                        // new FileWriter(instanciaDeFile, true);
                        writer.write(name + ", " + amount + ", " + value + "\n");
                        System.out.println(" datos añadidos");

                    } catch (IOException e) {
                        System.err.println(" error ocurrido: " + e);
                    }
                    break;

                // TODO cases 2,3,4,5,6
                case 6:
                    // Lógica para borrar archivo y salir
                    System.out.println("Saliendo...");
                    break;
                default:
                    System.out.println("Opción no válida.");
            }
        }

    }
}