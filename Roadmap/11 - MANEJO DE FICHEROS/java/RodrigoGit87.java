import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;

/* --- CONCEPTOS BÁSICOS EN MANEJO DE FICHEROS ---
* 1. Crear un archivo; con la clase File
* 2. Escribir datos; con la clase FileWriter o Files.writeString
* 3. Leer datos; clase Scanner o Files.readAllLines
*  4. Borrar datos; función .delete();  
*/

/*------ EXTRA -------
 * Desarrolla un programa de gestión de ventas que almacena sus datos en un 
 * archivo .txt.
 * - Cada producto se guarda en una línea del archivo de la siguiente manera:
 *   [nombre_producto], [cantidad_vendida], [precio].
 * - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
 *   actualizar, eliminar productos y salir.
 * - También debe poseer opciones para calcular la venta total y por producto.
 * - La opción salir borra el .txt.
 */
public class RodrigoGit87 {
    public static void main(String[] args) {
        String seller = "RodrigoGit87";
        File user = new File(seller);

        // -----Selección de opciones del menu --------
        Scanner sc = new Scanner(System.in);
        int opcion = 0;

        while (opcion != 6) { // El programa no termina hasta pulsar el 6
            System.out.println("\n--- GESTIÓN DE VENTAS ---");
            System.out.println("1 - Añadir productos");
            System.out.println("2 - Consultar productos");
            System.out.println("3 - Actualizar productos"); // Nota: Check case 3 y 4; podrian mejorar la logica, para
                                                            // establecer todos los productos a .toLowerCase y luego
                                                            // .contains para que el usuario no tenga q poner el nombre
                                                            // exacto.
            System.out.println("4 - Eliminar productos");
            System.out.println("5 - Calcular venta total");
            System.out.println("6 - SALIR ");
            System.out.print("Seleccione una opción: ");

            opcion = sc.nextInt();
            sc.nextLine(); // Limpiar el buffer después de leer un número

            // -------- MENU ---------------
            switch (opcion) {
                case 1: // lógica de añadir -> nombre_producto, cantidad_prods_vendida, precio
                    System.out.println("Nombre del producto: ");
                    String name = sc.nextLine();
                    System.out.println("Cantidad de productos vendida: ");
                    int amount = sc.nextInt();
                    System.out.println("Precio de venta(unitario): ");
                    double value = sc.nextDouble();
                    sc.nextLine(); // depurar buffer

                    try (FileWriter writer = new FileWriter(user, true)) { // necesitamos que el programa sea capaz de
                                                                           // "añadir" nuevos
                        // productos sin borrar los anteriores. La clase FileWriter tiene un constructor
                        // especial para esto:
                        // new FileWriter(instanciaDeFile, true); <- en false, elimina y sobreescribe.
                        writer.write(name + ", " + amount + ", " + value + "\n");
                        System.out.println(" datos añadidos");

                    } catch (IOException e) {
                        System.err.println(" error ocurrido: " + e);
                    }
                    break;
                case 2:
                    System.out.println("\n Consulta de productos ");
                    // Usamos try-with-resources para que el Scanner se cierre solo
                    try (Scanner lector = new Scanner(user)) { // Scanner(user) leerá el objeto instanciado user. de la
                                                               // clase File
                        while (lector.hasNextLine()) {
                            String linea = lector.nextLine();
                            System.out.println(linea);
                        }
                    } catch (IOException e) {
                        System.out.println("No se pudo leer el archivo o aún no existe.");
                    }
                    break;

                // Para los cases 3 y 4, necesitamos una forma de pasar el archivo a una
                // lista. Usaremos ArrayList<String>
                case 3:
                    System.out.print("Nombre del producto a actualizar: ");
                    String productoAEditar = sc.nextLine();
                    ArrayList<String> listaEdicion = new ArrayList<>();
                    boolean is_Editado = false;

                    try (Scanner lectorEdicion = new Scanner(user)) {
                        while (lectorEdicion.hasNextLine()) {
                            String linea = lectorEdicion.nextLine();
                            String[] datos = linea.split(", ");

                            if (datos[0].equalsIgnoreCase(productoAEditar)) {
                                System.out.print("Nueva cantidad: ");
                                int nCant = sc.nextInt();
                                System.out.print("Nuevo precio: ");
                                double nPrec = sc.nextDouble();
                                sc.nextLine(); // Limpiar buffer

                                // Añadimos la línea con los datos nuevos
                                listaEdicion.add(datos[0] + ", " + nCant + ", " + nPrec);
                                is_Editado = true;
                            } else
                                listaEdicion.add(linea); // Mantenemos la línea original
                        }
                    } catch (IOException e) {
                        System.err.println(" error : " + e.getMessage());
                    }

                    // Guardar cambios (Sobrescritura)
                    if (is_Editado) {
                        try (FileWriter fw = new FileWriter(user, false)) { // Al ponerlo en false (o no poner nada), el
                                                                            // archivo se vacía por completo antes de
                                                                            // escribir las líneas de nuestra lista.
                            for (String l : listaEdicion) // for each elemento en el arrayList, escribir elemento +
                                                          // salto de linea
                                fw.write(l + "\n");
                            System.out.println(" Producto actualizado.");
                        } catch (IOException e) {
                            System.err.println("error al actualizar: " + e.getMessage());
                        }
                    }
                    break;

                case 4:
                    System.out.print("Nombre del producto a eliminar: ");
                    String productoAEliminar = sc.nextLine();
                    ArrayList<String> todasLasLineas = new ArrayList<>();
                    boolean is_productoEncontrado = false;
                    // Leer user y añadir a un arrayList lo que no queremos borrar
                    try (Scanner scan = new Scanner(user)) {
                        while (scan.hasNextLine()) {
                            String linea = scan.nextLine();
                            if (!linea.split(", ")[0].equalsIgnoreCase(productoAEliminar)) { // ! <-- por que solo
                                                                                             // queremos añadir al array
                                                                                             // lo que no coincide con
                                                                                             // productoAEliminar
                                todasLasLineas.add(linea);
                            } else
                                is_productoEncontrado = true;

                        }
                    } catch (IOException e) {
                        System.err.println(" Error al leer: " + e.getMessage());
                    }
                    // Ya tenemos 'salvaguardado' en el arrayList lo que no queremos borrar (lo que
                    // sí, está en String productoAEliminar )
                    // Ahora, sobreescribir el user con el arrayList

                    if (is_productoEncontrado) {
                        try (FileWriter fw = new FileWriter(user, false)) { // false para eliminar datos y escribir
                                                                            // desde 0
                            for (String l : todasLasLineas) {
                                fw.write(l + "\n");
                            }
                            System.out.println(" Producto eliminado.");
                        } catch (IOException e) {
                            System.out.println(" Error al guardar cambios.");
                        }
                    } else
                        System.out.println(" Producto no encontrado.");
                    break;

                case 5:
                    double totalGeneral = 0;
                    System.out.println(" Cálculo de Ventas ");
                    try (Scanner filelector = new Scanner(user)) {
                        if (!user.exists()) {
                            System.out.println("No hay ventas regsitradas");
                            break;
                        }
                        while (filelector.hasNextLine()) {
                            String line = filelector.nextLine();
                            String[] parts = line.split(", ");

                            if (parts.length == 3) {
                                String nombre = parts[0];
                                int cantidad = Integer.parseInt(parts[1]);
                                double precio = Double.parseDouble(parts[2]);

                                double subtotal = (cantidad * precio);
                                totalGeneral += subtotal;

                                System.out.println("Producto: " + nombre + " / Subtotal: " + subtotal);
                            }
                            System.out.println("----------------------------");
                            System.out.println("VENTA TOTAL GLOBAL: " + totalGeneral);
                        }
                    } catch (IOException e) {
                        System.err.println(" error ocurrido: " + e.getMessage());
                    }
                    break;

                case 6:
                    // Lógica para borrar archivo y salir
                    System.out.println("Archivo, " + user + " eliminado. Hasta la vista, baby !");
                    break;
                default:
                    System.out.println("Opción no válida.");
            }
        }

    }
}