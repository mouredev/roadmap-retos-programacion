package reto11_2024;

import java.io.*;
import java.util.*;

public class jmichael39 {
    static File file;
    static FileWriter fileWriter;
    static BufferedReader bufferedReader;
    static LinkedList<Producto> lista = new LinkedList<>();
    static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        basic();
        extra.init();
    }

    private static void basic() {
        try {
            file = new File("jmichael39.txt");
            fileWriter = new FileWriter(file);
            bufferedReader = new BufferedReader(new FileReader(file));

            fileWriter.write("Nombre: John Michael\n");
            fileWriter.write("Edad: 31\n");
            fileWriter.write("Lenguaje favorito: Java\n");
            fileWriter.close();

            String line;
            while ((line = bufferedReader.readLine()) != null) {
                System.out.println(line);
            }

            bufferedReader.close();
            System.out.println(file.delete() ? "The file was successfully deleted" : "The file doesn't exist");
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    static class extra {

        static File file;
        static FileWriter fileWriter;

        static {
            try {
                file = new File("ventas.txt");
                fileWriter = new FileWriter(file);
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        }

        static String nombre;
        static int cantidadVendida;
        static double precio;
        static int choice = 0;

        static void init() {
            while (true) {
                System.out.println("\n1 - Añadir producto");
                System.out.println("2 - Consultar productos");
                System.out.println("3 - Actualizar producto");
                System.out.println("4 - Eliminar producto");
                System.out.println("5 - Calcular venta total");
                System.out.println("6 - Calcular venta por producto");
                System.out.println("7 - Salir");
                System.out.print("\nElija la operación a realizar: ");

                if (scanner.hasNextInt()) {
                    choice = scanner.nextInt();
                }

                switch (choice) {
                    case 1:
                        System.out.println("Nombre del producto a dar de alta: ");
                        nombre = scanner.next();
                        System.out.println("Unidades vendidas: ");
                        cantidadVendida = scanner.nextInt();
                        System.out.println("Precio del producto: ");
                        precio = Double.parseDouble(scanner.next());
                        lista.add(new Producto(nombre, cantidadVendida, precio));

                        try {
                            fileWriter.write("Nuevo producto - ID: " + lista.get(Producto.nextId - 1).getId()
                                    + " Nombre: " + lista.get(Producto.nextId - 1).getNombre()
                                    + " Unidades vendidas: " + lista.get(Producto.nextId - 1).getCantidadVendida()
                                    + " Precio:" + lista.get(Producto.nextId - 1).getPrecio() + "\n");
                            fileWriter.flush();
                        } catch (IOException e) {
                            e.getCause();
                        }

                        break;
                    case 2:
                        checkProducts();
                        break;
                    case 3:
                        updateProducts();
                        break;
                    case 4:
                        System.out.print("Id del producto a eliminar: ");
                        int id = scanner.nextInt() - 1;
                        System.out.println("Se ha eliminado el producto: " + lista.get(id));
                        lista.remove(id);
                        break;
                    case 5:
                        double totalGlobal = 0;
                        for (Producto producto : lista) {
                            totalGlobal += producto.getCantidadVendida() * producto.getPrecio();
                        }
                        System.out.println("El importe total de las ventas es: " + totalGlobal + "$");
                        break;
                    case 6:
                        System.out.println("Seleccione un ID de producto para calcular el total de ventas de ese producto");
                        checkProducts();
                        int product = scanner.nextInt() - 1;
                        double totalPerProduct = lista.get(product).getCantidadVendida() * lista.get(product).getPrecio();
                        System.out.println("El importe de las ventas de " + lista.get(product) + " es: " + totalPerProduct + "$");
                        break;
                    case 7:
                        try {
                            fileWriter.close();
                        } catch (IOException e) {
                            throw new RuntimeException(e);
                        }
                        System.out.println(file.delete() ? "Archivo de ventas eliminado" : "Ha habido un problema borrando el archivo");
                        System.exit(0);
                        break;
                    default:
                        System.out.println("No se reconoce el comando, intentelo de nuevo");
                        init();
                }
            }
        }

        private static void checkProducts() {
            for (Producto producto : lista) {
                System.out.println("Id: " + producto.getId()
                        + " , Nombre del artículo: " + producto.getNombre()
                        + " , Precio: " + producto.getPrecio()
                        + " , Unidades vendidas: " + producto.getCantidadVendida());
            }
        }

        private static void updateProducts() {
            int productToUpdate;
            int fieldToUpdate;
            String nuevoNombre;
            double nuevoPrecio;
            int nuevaCantidadVendida;

            System.out.println("Seleccione el id del producto a actualizar: \n");
            checkProducts();

            while (!scanner.hasNextInt()) {
                System.out.println("Debe introducir un número");
                scanner.next();
            }
            productToUpdate = scanner.nextInt() - 1;

            System.out.println("¿Qué campo desea actualizar?");
            System.out.println("1 - Nombre");
            System.out.println("2 - Precio");
            System.out.println("3 - Cantidad vendida");

            while (!scanner.hasNextInt()) {
                System.out.println("Debe introducir un número");
                scanner.next();
            }
            fieldToUpdate = scanner.nextInt();

            switch (fieldToUpdate) {
                case 1:
                    System.out.print("Nuevo nombre del producto: ");
                    nuevoNombre = scanner.next();

                    try {
                        fileWriter.write("Se ha cambiado el nombre de: " + lista.get(productToUpdate) + "\n");
                        lista.get(productToUpdate).setNombre(nuevoNombre);
                        fileWriter.write("Nombre actualizado: " + lista.get(productToUpdate).getNombre() + "\n");
                        fileWriter.flush();
                    } catch (IOException e) {
                        throw new RuntimeException(e);
                    }
                    System.out.println("Se ha actualizado el producto: " + lista.get(productToUpdate));
                    break;
                case 2:
                    System.out.print("Nuevo precio para el producto: ");
                    nuevoPrecio = Double.parseDouble(scanner.next());

                    try {
                        fileWriter.write("Se ha cambiado el precio de: " + lista.get(productToUpdate) + "\n");
                        lista.get(productToUpdate).setPrecio(nuevoPrecio);
                        fileWriter.write("Precio actualizado: " + lista.get(productToUpdate).getPrecio() + "\n");
                        fileWriter.flush();
                    } catch (IOException e) {
                        throw new RuntimeException(e);
                    }

                    System.out.println("Se ha actualizado el producto: " + lista.get(productToUpdate));
                    break;
                case 3:
                    System.out.print("Nueva cantidad: ");
                    nuevaCantidadVendida = scanner.nextInt();

                    try {
                        fileWriter.write("Se han actualizado las ventas de: " + lista.get(productToUpdate) + "\n");
                        lista.get(productToUpdate).setCantidadVendida(nuevaCantidadVendida);
                        fileWriter.write("Ventas actualizadas: " + lista.get(productToUpdate).getCantidadVendida() + "\n");
                        fileWriter.flush();
                    } catch (IOException e) {
                        throw new RuntimeException(e);
                    }

                    lista.get(productToUpdate).setCantidadVendida(nuevaCantidadVendida);
                    System.out.println("Se ha actualizado el producto: " + lista.get(productToUpdate));
                    break;
                default:
                    System.out.println("Error");
            }
        }
    }

    static class Producto {
        static int nextId = 0;
        int id;
        String nombre;
        int cantidadVendida;
        double precio;

        public Producto(String nombre, int cantidadVendida, double precio) {
            this.id = ++nextId;
            this.nombre = nombre;
            this.cantidadVendida = cantidadVendida;
            this.precio = precio;
        }

        public int getId() {
            return id;
        }

        public void setNombre(String nombre) {
            this.nombre = nombre;
        }

        public String getNombre() {
            return nombre;
        }

        public int getCantidadVendida() {
            return cantidadVendida;
        }

        public void setCantidadVendida(int cantidadVendida) {
            this.cantidadVendida = cantidadVendida;
        }

        public double getPrecio() {
            return precio;
        }

        public void setPrecio(double precio) {
            this.precio = precio;
        }

        @Override
        public String toString() {
            return "Producto{" +
                    "id= " + id +
                    ", nombre='" + nombre + '\'' +
                    ", cantidadVendida=" + cantidadVendida +
                    ", precio=" + precio +
                    '}';
        }
    }
}
