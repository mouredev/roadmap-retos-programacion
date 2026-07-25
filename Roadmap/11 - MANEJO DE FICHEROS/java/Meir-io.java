import java.io.*;
import java.nio.file.*;
import java.util.Scanner;

public class Meir {
    public static void main(String[] args) {

        String fileName = "Meir.txt";

        try (BufferedWriter writer = new BufferedWriter(new FileWriter(fileName))) {
            writer.write("Nombre: Meir");
            writer.newLine();
            writer.write("Edad: 19");
            writer.newLine();
            writer.write("Lenguaje favorito: Java");
            System.out.println(" Archivo creado");
        } catch (IOException e) {
            System.out.println("Error al crear: " + e.getMessage());
        }

        try (BufferedReader reader = new BufferedReader(new FileReader(fileName))) {
            String linea;
            System.out.println("\n── Contenido ──");
            while ((linea = reader.readLine()) != null) {
                System.out.println(linea);
            }
        } catch (IOException e) {
            System.out.println("Error al leer: " + e.getMessage());
        }

        File file = new File(fileName);
        if (file.delete()) {
            System.out.println("\n Archivo borrado");
        } else {
            System.out.println(" No se pudo borrar");
        }

        // Extra



        String productos = "Productos.txt";

        while (true) {


            System.out.println("Bienvenido a la tienda de productos");
            System.out.println("1.- Añadir producto");
            System.out.println("2.- Ver productos");
            System.out.println("3.- Modificar producto");
            System.out.println("4.- Eliminar producto");
            System.out.println("5.- Calcular total");
            System.out.println("6.- Ventas de un producto");
            System.out.println("7.- Borrar archivo");
            System.out.println("8.- Salir");
            System.out.println("Elige una opcion: ");

            Scanner scanner = new Scanner(System.in);
            int opcion = scanner.nextInt();

            scanner.nextLine();
            switch (opcion) {
                case 1:
                    System.out.println("Escribe el nombre del producto: ");
                    String nombre = scanner.nextLine();
                    System.out.println("Escribe la cantidad vendida");
                    int cantidad = scanner.nextInt();
                    System.out.println("Escribe el precio del producto: ");
                    double precio = scanner.nextDouble();
                    try (BufferedWriter writer = new BufferedWriter(new FileWriter(productos,true))) {
                        writer.write("nombre_producto:" + nombre);
                        writer.newLine();
                        writer.write("cantidad_vendida:" + cantidad);
                        writer.newLine();
                        writer.write("precio: " + precio);
                        writer.newLine();
                        writer.newLine();
                    } catch (IOException e) {
                        System.out.println("Error al crear: " + e.getMessage());
                    }
                    break;
                case 2:
                    System.out.println("Productos: ");
                    try (BufferedReader reader = new BufferedReader(new FileReader(productos))) {
                        String linea;
                        while ((linea = reader.readLine()) != null) {
                            System.out.println(linea);
                        }
                    } catch (IOException e) {
                        System.out.println("Error al leer: " + e.getMessage());
                    }
                    break;
                case 3:
                    System.out.println("Indica el nombre del producto que quieres modificar: ");
                    String producto = scanner.nextLine();

                    try {
                        File archivoProductos = new File(productos);
                        StringBuilder contenido = new StringBuilder();
                        boolean encontrado = false;

                        try (BufferedReader reader = new BufferedReader(new FileReader(archivoProductos))) {
                            String linea;
                            while ((linea = reader.readLine()) != null) {
                                if (linea.equals("nombre_producto:" + producto)) {
                                    encontrado = true;
                                    System.out.println("Nueva cantidad vendida: ");
                                    int nuevaCantidad = scanner.nextInt();
                                    System.out.println("Nuevo precio: ");
                                    double nuevoPrecio = scanner.nextDouble();
                                    scanner.nextLine();

                                    contenido.append("nombre_producto:").append(producto).append("\n");
                                    contenido.append("cantidad_vendida:").append(nuevaCantidad).append("\n");
                                    contenido.append("precio: ").append(nuevoPrecio).append("\n");

                                    reader.readLine();
                                    reader.readLine();
                                } else {
                                    contenido.append(linea).append("\n");
                                }
                            }
                        }
                        if (!encontrado) {
                            System.out.println(" Producto no encontrado");
                            break;
                        }


                        try (BufferedWriter writer = new BufferedWriter(new FileWriter(archivoProductos))) {
                            writer.write(contenido.toString());
                        }

                        System.out.println(" Producto modificado");

                    } catch (IOException e) {
                        System.out.println("Error: " + e.getMessage());
                    }
                    break;
                case 4:
                    System.out.println("Indica el nombre del producto que quieres eliminar: ");
                    String productoEliminar = scanner.nextLine();

                    try {
                        File archivoEliminar = new File(productos);
                        StringBuilder contenidoEliminar = new StringBuilder();
                        boolean encontradoEliminar = false;

                        try (BufferedReader reader = new BufferedReader(new FileReader(archivoEliminar))) {
                            String linea;
                            while ((linea = reader.readLine()) != null) {
                                if (linea.equals("nombre_producto:" + productoEliminar)) {
                                    encontradoEliminar = true;
                                    reader.readLine(); // salta cantidad
                                    reader.readLine(); // salta precio
                                    reader.readLine(); // salta línea vacía
                                } else {
                                    contenidoEliminar.append(linea).append("\n");
                                }
                            }
                        }

                        if (!encontradoEliminar) {
                            System.out.println(" Producto no encontrado");
                            break;
                        }

                        try (BufferedWriter writer = new BufferedWriter(new FileWriter(archivoEliminar))) {
                            writer.write(contenidoEliminar.toString());
                        }
                        System.out.println(" Producto eliminado");

                    } catch (IOException e) {
                        System.out.println("Error: " + e.getMessage());
                    }
                    break;

                case 5:
                    System.out.println("── Total de ventas ──");
                    double total = 0;

                    try (BufferedReader reader = new BufferedReader(new FileReader(productos))) {
                        String linea;
                        int cantidadTotal = 0;
                        double precioTotal = 0;

                        while ((linea = reader.readLine()) != null) {
                            if (linea.startsWith("cantidad_vendida:")) {
                                cantidadTotal = Integer.parseInt(linea.split(":")[1].trim());
                            } else if (linea.startsWith("precio:")) {
                                precioTotal = Double.parseDouble(linea.split(":")[1].trim());
                                total += cantidadTotal * precioTotal;
                            }
                        }
                        System.out.println("Total: $" + total);

                    } catch (IOException e) {
                        System.out.println("Error: " + e.getMessage());
                    }
                    break;

                case 6:
                    System.out.println("Indica el nombre del producto: ");
                    String productoVentas = scanner.nextLine();

                    try (BufferedReader reader = new BufferedReader(new FileReader(productos))) {
                        String linea;
                        boolean encontradoVentas = false;

                        while ((linea = reader.readLine()) != null) {
                            if (linea.equals("nombre_producto:" + productoVentas)) {
                                encontradoVentas = true;
                                String cantidadLinea = reader.readLine();
                                String precioLinea = reader.readLine();

                                int cantidadVentas = Integer.parseInt(cantidadLinea.split(":")[1].trim());
                                double precioVentas = Double.parseDouble(precioLinea.split(":")[1].trim());

                                System.out.println("Producto: " + productoVentas);
                                System.out.println("Cantidad vendida: " + cantidadVentas);
                                System.out.println("Precio unitario: $" + precioVentas);
                                System.out.println("Total ventas: $" + (cantidadVentas * precioVentas));
                                break;
                            }
                        }

                        if (!encontradoVentas) System.out.println("Producto no encontrado");

                    } catch (IOException e) {
                        System.out.println("Error: " + e.getMessage());
                    }
                    break;

                case 7:
                    File archivoborrar = new File(productos);
                    if (archivoborrar.delete()) {
                        System.out.println(" Archivo borrado");
                    } else {
                        System.out.println(" No se pudo borrar");
                    }
                    break;

                case 8:
                    System.out.println("Hasta luego!");
                    scanner.close();
                    return;

                default:
                    System.out.println(" Opción no válida");

            }


        }
    }
}
