import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) {
        try {
            crearArchivo();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    /*
     * #11 MANEJO DE FICHEROS
     */

    public static void crearArchivo() throws IOException {
        String nombre = "cesar-ch";
        int edad = 4;
        String lenguajeFavorito = "JavaScript";
        String contenido = "Nombre: " + nombre + "\nEdad: " + edad + "\nLenguaje de programación favorito: "
                + lenguajeFavorito;
        FileWriter writer = new FileWriter(nombre + ".txt");
        writer.write(contenido);
        writer.close();
        System.out.println("1. Archivo " + nombre + ".txt creado exitosamente");
        System.out.println("2. Contenido añadido al archivo");
        leerArchivo(nombre);
    }

    public static void leerArchivo(String nombre) throws IOException {
        BufferedReader reader = new BufferedReader(new FileReader(nombre + ".txt"));
        System.out.println("3. Contenido leído del archivo");
        String line;
        while ((line = reader.readLine()) != null) {
            System.out.println(line);
        }
        reader.close();
        borrarArchivo(nombre);
    }

    public static void borrarArchivo(String nombre) {
        if (new java.io.File(nombre + ".txt").delete()) {
            System.out.println("4. Archivo eliminado exitosamente");
        } else {
            System.out.println("No se pudo eliminar el archivo");
        }
        menu();
    }

    /*
     * DIFICULTAD EXTRA
    */

    public static void menu() {
        System.out.println("\n=== Gestión de Ventas ===");
        System.out.println("1. Añadir producto");
        System.out.println("2. Consultar producto");
        System.out.println("3. Actualizar producto");
        System.out.println("4. Eliminar producto");
        System.out.println("5. Calcular venta total");
        System.out.println("6. Calcular venta por producto");
        System.out.println("7. Salir");
        System.out.println("===========================");
        seleccionarOpcion();
    }

    public static void seleccionarOpcion() {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        try {
            System.out.print("Seleccione una opción: ");
            String opcion = reader.readLine();
            switch (opcion) {
                case "1":
                    añadirProducto();
                    break;
                case "2":
                    consultarProducto();
                    break;
                case "3":
                    actualizarProducto();
                    break;
                case "4":
                    eliminarProducto();
                    break;
                case "5":
                    calcularVentaTotal();
                    break;
                case "6":
                    calcularVentaPorProducto();
                    break;
                case "7":
                    eliminarArchivo();
                    reader.close();
                    break;
                default:
                    seleccionarOpcion();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void añadirProducto() throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        System.out.print("Introduce el nombre del producto: ");
        String nombre = reader.readLine();
        System.out.print("Introduce la cantidad del producto: ");
        String cantidad = reader.readLine();
        System.out.print("Introduce el precio del producto: ");
        String precio = reader.readLine();
        String producto = nombre + "," + cantidad + "," + precio + "\n";
        FileWriter writer = new FileWriter("productos.txt", true);
        writer.write(producto);
        writer.close();
        System.out.println("Producto añadido correctamente");
        menu();
    }

    public static void consultarProducto() throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        System.out.print("Introduce el nombre del producto a consultar: ");
        String nombre = reader.readLine();
        BufferedReader fileReader = new BufferedReader(new FileReader("productos.txt"));
        String line;
        boolean encontrado = false;
        while ((line = fileReader.readLine()) != null) {
            String[] parts = line.split(",");
            if (parts[0].equals(nombre)) {
                System.out.println("Producto encontrado: " + line);
                encontrado = true;
                break;
            }
        }
        if (!encontrado) {
            System.out.println("Producto no encontrado");
        }
        fileReader.close();
        menu();
    }

    public static void actualizarProducto() throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        System.out.print("Introduce el nombre del producto a actualizar: ");
        String nombre = reader.readLine();
        System.out.print("Introduce la nueva cantidad del producto: ");
        String cantidad = reader.readLine();
        System.out.print("Introduce el nuevo precio del producto: ");
        String precio = reader.readLine();
        String nuevoProducto = nombre + "," + cantidad + "," + precio + "\n";
        BufferedReader fileReader = new BufferedReader(new FileReader("productos.txt"));
        StringBuilder fileContent = new StringBuilder();
        String line;
        boolean encontrado = false;
        while ((line = fileReader.readLine()) != null) {
            String[] parts = line.split(",");
            if (parts[0].equals(nombre)) {
                fileContent.append(nuevoProducto);
                encontrado = true;
            } else {
                fileContent.append(line).append("\n");
            }
        }
        fileReader.close();
        if (encontrado) {
            FileWriter writer = new FileWriter("productos.txt");
            writer.write(fileContent.toString());
            writer.close();
            System.out.println("Producto actualizado correctamente");
        } else {
            System.out.println("Producto no encontrado");
        }
        menu();
    }

    public static void eliminarProducto() throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        System.out.print("Introduce el nombre del producto a eliminar: ");
        String nombre = reader.readLine();
        BufferedReader fileReader = new BufferedReader(new FileReader("productos.txt"));
        StringBuilder fileContent = new StringBuilder();
        String line;
        boolean encontrado = false;
        while ((line = fileReader.readLine()) != null) {
            String[] parts = line.split(",");
            if (!parts[0].equals(nombre)) {
                fileContent.append(line).append("\n");
            } else {
                encontrado = true;
            }
        }
        fileReader.close();
        if (encontrado) {
            FileWriter writer = new FileWriter("productos.txt");
            writer.write(fileContent.toString());
            writer.close();
            System.out.println("Producto eliminado correctamente");
        } else {
            System.out.println("Producto no encontrado");
        }
        menu();
    }

    public static void calcularVentaTotal() throws IOException {
        BufferedReader fileReader = new BufferedReader(new FileReader("productos.txt"));
        String line;
        double total = 0;
        while ((line = fileReader.readLine()) != null) {
            String[] parts = line.split(",");
            total += Integer.parseInt(parts[1]) * Double.parseDouble(parts[2]);
        }
        fileReader.close();
        System.out.println("Venta total: " + total);
        menu();
    }

    public static void calcularVentaPorProducto() throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        System.out.print("Introduce el nombre del producto a consultar: ");
        String nombre = reader.readLine();
        BufferedReader fileReader = new BufferedReader(new FileReader("productos.txt"));
        String line;
        boolean encontrado = false;
        while ((line = fileReader.readLine()) != null) {
            String[] parts = line.split(",");
            if (parts[0].equals(nombre)) {
                double total = Integer.parseInt(parts[1]) * Double.parseDouble(parts[2]);
                System.out.println("Venta total: " + total);
                encontrado = true;
                break;
            }
        }
        if (!encontrado) {
            System.out.println("Producto no encontrado");
        }
        fileReader.close();
        menu();
    }

    public static void eliminarArchivo() {
        if (new java.io.File("productos.txt").delete()) {
            System.out.println("Archivo eliminado correctamente");
        } else {
            System.out.println("No se pudo eliminar el archivo");
        }
    }
}
