import java.io.*;
import java.util.LinkedList;
import java.util.List;
import java.util.Objects;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) throws IOException {
        File file = new File("asjordi.txt");
        String contenido = "Jordi Ayala\n20\nJava\n";

        escribirArchivo(file, contenido, false);

        System.out.println("Contenido del archivo:\n" + leerArchivo(file));

        boolean isDelete = file.delete();
        System.out.println(isDelete ? "El archivo fue eliminado" : "El archivo no fue eliminado");

        ventas();
    }

    /**
     * DIFICULTAD EXTRA (opcional):
     * Desarrolla un programa de gestión de ventas que almacena sus datos en un archivo .txt.
     * - Cada producto se guarda en una línea del arhivo de la siguiente manera: [nombre_producto], [cantidad_vendida], [precio].
     * - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
     * actualizar, eliminar productos y salir.
     * - También debe poseer opciones para calcular la venta total y por producto.
     * - La opción salir borra el .txt.
     */

    static class Venta {
        String nombre;
        String cantidad;
        String precio;

        public String getNombre() {
            return nombre;
        }

        public void setNombre(String nombre) {
            this.nombre = nombre;
        }

        public String getCantidad() {
            return cantidad;
        }

        public void setCantidad(String cantidad) {
            this.cantidad = cantidad;
        }

        public String getPrecio() {
            return precio;
        }

        public void setPrecio(String precio) {
            this.precio = precio;
        }

        public String getInfo() {
            return nombre + ", " + cantidad + ", " + precio + "\n";
        }

        @Override
        public String toString() {
            return "Venta{" +
                    "nombre='" + nombre + '\'' +
                    ", cantidad='" + cantidad + '\'' +
                    ", precio='" + precio + '\'' +
                    '}';
        }
    }

    static void ventas() {
        File file = new File("ventas.txt");
        Scanner sc = new Scanner(System.in);
        String opcion = "";

        while (!opcion.equals("6")) {
            mostrarOpciones();
            opcion = sc.nextLine();

            switch (opcion) {
                case "1":
                    Venta v = new Venta();
                    System.out.print("Ingrese el nombre del producto: ");
                    v.setNombre(sc.nextLine());
                    System.out.print("Ingrese la cantidad: ");
                    v.setCantidad(sc.nextLine());
                    System.out.print("Ingrese el precio: ");
                    v.setPrecio(sc.nextLine());
                    escribirArchivo(file, v.getInfo(), true);
                    break;
                case "2":
                    System.out.println("Ventas registradas:");
                    System.out.println(obtenerVentas(file));
                    break;
                case "3":
                    System.out.println("Actualizar venta");
                    Venta venta = new Venta();
                    System.out.print("Ingrese el nombre del producto a actualizar: ");
                    venta.setNombre(sc.nextLine());
                    System.out.print("Ingrese la cantidad: ");
                    venta.setCantidad(sc.nextLine());
                    System.out.print("Ingrese el precio: ");
                    venta.setPrecio(sc.nextLine());
                    actualizarVenta(file, venta);
                    break;
                case "4":
                    System.out.println("Eliminar venta");
                    System.out.print("Ingrese el nombre del producto a eliminar: ");
                    eliminarVenta(file, sc.nextLine());
                    break;
                case "5":
                    calcularTotal(file);
                    break;
                case "6":
                    System.out.println("Saliendo del sistema de ventas...");
                    file.delete();
                    break;
                default:
                    System.out.println("Opción no válida");
                    break;
            }
        }
    }

    static void calcularTotal(File file) {
        List<Venta> ventas = obtenerVentas(file);
        double total = 0;

        for (Venta v : ventas) {
            total += Double.parseDouble(v.getCantidad()) * Double.parseDouble(v.getPrecio());
        }

        System.out.println("El total de ventas es: " + total);
    }

    static void eliminarVenta(File file, String nombre) {
        List<Venta> ventas = obtenerVentas(file);

        for (Venta v : ventas) {
            if (v.getNombre().equals(nombre)) {
                ventas.remove(v);
                System.out.println("Venta eliminada");
                break;
            }
        }

        file.delete();
        ventas.forEach(v -> escribirArchivo(file, v.getInfo(), true));
    }

    static void actualizarVenta(File file, Venta venta) {
        List<Venta> ventas = obtenerVentas(file);

        for (Venta v : ventas) {
            if (v.getNombre().equals(venta.getNombre())) {
                v.setNombre(venta.getNombre());
                v.setCantidad(venta.getCantidad());
                v.setPrecio(venta.getPrecio());
                System.out.println("Venta actualizada");
                break;
            }
        }

        file.delete();
        ventas.forEach(v -> escribirArchivo(file, v.getInfo(), true));
    }

    static void mostrarOpciones() {
        System.out.println("Bienvenido al sistema de ventas");
        System.out.println("Favor de seleccionar una opción:");
        System.out.println("1- Agregar venta");
        System.out.println("2- Mostrar ventas");
        System.out.println("3- Actualizar venta");
        System.out.println("4- Eliminar venta");
        System.out.println("5- Calcular total de ventas");
        System.out.println("6- Salir");
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

    static List<Venta> obtenerVentas(File file) {
        List<Venta> list = new LinkedList<>();

        try (Reader r = new FileReader(file);
             BufferedReader br = new BufferedReader(r))  {
            String linea;
            while ((linea = br.readLine()) != null) {
                String[] partes = linea.split(",");
                Venta v = new Venta();
                v.setNombre(partes[0].trim());
                v.setCantidad(partes[1].trim());
                v.setPrecio(partes[2].trim());
                list.add(v);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }

        return list;
    }

}
