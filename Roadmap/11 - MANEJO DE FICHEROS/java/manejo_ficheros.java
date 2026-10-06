import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardOpenOption;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class manejo_ficheros {
    public static void main(String[] args) {

        try{
        
        Path miArchivo = Path.of("P.Escrbano.txt");

        String informacion = "Nombre: Pablo\n" + "Edad: 35\n" + "Lenguaje favorito: Java";
        
        Files.writeString(miArchivo, informacion);
        System.out.println("Archivo creado correctamete.");

        System.out.println("--- Informacióon escrita en el archivo ---");
        System.out.println(Files.readString(miArchivo));

        Files.delete(miArchivo);
        System.out.println("¡Archivo borrado!");

        }catch(IOException e){
            System.out.println("Error con el archivo: " + e.toString());
        }

        /*
          *Ejercicio
          *Extra
        */
        Scanner teclado = new Scanner(System.in);

        Path archivoTienda = Path.of("PabloShop.txt");

        boolean finalPrograma = true;

        while (finalPrograma) {
            System.out.println("1. Añadir producto");
            System.out.println("2. Consultar producto");
            System.out.println("3. Actualizar producto");
            System.out.println("4. Borrar producto");
            System.out.println("5. Mostrar productos");
            System.out.println("6. Calcular venta total");
            System.out.println("7. Calcular venta por producto");
            System.out.println("8. Salir");

            System.out.println("Seleciona una oción: ");
            int option = teclado.nextInt();
            teclado.nextLine();

            switch (option) {
                case 1:
                    System.out.println("Nombre: ");
                    String nameProduct = teclado.nextLine();
                    System.out.println("Cantidad: ");
                    String quantity = teclado.nextLine();
                    System.out.println("Precio: ");
                    String price = teclado.nextLine();
                    String nuevoProduto = nameProduct + ", " +  quantity + ", " + price + "\n";
                    try {
                        Files.writeString(archivoTienda, nuevoProduto, StandardOpenOption.CREATE, StandardOpenOption.APPEND);
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                    break;
                case 2:
                    System.out.println("Introduce el nombre del producto que quieres consultar:");
                    String name = teclado.nextLine();
                    System.out.println("Nombre: " + name);

                    try {
                        List<String> lineas = Files.readAllLines(archivoTienda);
                        for(String linea: lineas){
                            if (linea.split(", ")[0].equalsIgnoreCase(name)) {
                                System.out.println(linea);
                                break;
                            }
                         }
                        }catch (IOException e){
                        e.printStackTrace();
                        }
                    break;
                case 3:
                    System.out.println("Nombre: ");
                    nameProduct = teclado.nextLine();
                    System.out.println("Cantidad: ");
                    quantity = teclado.nextLine();
                    System.out.println("Precio: ");
                    price = teclado.nextLine();

                    try {
                        List<String> lineas = Files.readAllLines(archivoTienda);
                        boolean modificado = false;
                        for(int i = 0; i < lineas.size(); i++){
                            String linea = lineas.get(i);
                            if (linea.split(", ")[0].equalsIgnoreCase(nameProduct)) {
                                nuevoProduto = nameProduct + ", " +  quantity + ", " + price;
                                lineas.set(i, nuevoProduto);
                                modificado = true;
                               break;
                            }
                        }
                         if (modificado) {
                            Files.write(archivoTienda, lineas);
                            System.out.println("Producto actualizado correctamente.");
                         }else{
                            System.out.println("No se encontro ningún producto con ese nombre.");
                         }
                        }catch (IOException e){
                        e.printStackTrace();
                        }
                    break;
                case 4:
                    System.out.println("Nombre: ");
                    nameProduct = teclado.nextLine();
                    
                    try {
                        List<String> lineas = Files.readAllLines(archivoTienda);
                        boolean borrado = false;

                        for(int i = 0; i < lineas.size(); i++){
                            String linea = lineas.get(i);

                            if (linea.split(", ")[0].equalsIgnoreCase(nameProduct)) {
                                lineas.remove(i);
                                borrado = true;
                                break;
                            }
                        }

                        if (borrado) {
                            Files.write(archivoTienda, lineas);
                            System.out.println("Producto borrado correctamente.");
                        }else{
                            System.out.println("No se encontro ningún producto con ese nombre.");
                         }

                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                    
                    break;
                case 5:
                    try {
                        System.out.println(Files.readString(archivoTienda));
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                    break;
                case 6:
                    double total = 0;

                    try {
                        List<String> lineas = Files.readAllLines(archivoTienda);

                        for(String linea: lineas){

                            String[] componetes = linea.split(", ");
                            int cantidad = Integer.parseInt(componetes[1]);
                            double precio = Double.parseDouble(componetes[2]);
                            
                            total = total + (cantidad * precio);
                        }

                        System.out.println("El valor total de todos los productos es: " + total + " €.");
                    } catch (IOException e) {
                        e.printStackTrace();
                    }catch(NumberFormatException e){
                        e.toString();
                    }
                    break;
                case 7:
                    System.out.println("Nombre: ");
                    nameProduct = teclado.nextLine();
                    double totalProducto = 0;

                    try {
                        List<String> lineas = Files.readAllLines(archivoTienda);

                        for(String linea: lineas){

                            String[] componetes = linea.split(", ");

                            if (componetes[0].equalsIgnoreCase(nameProduct)) {
                                
                            
                            int cantidad = Integer.parseInt(componetes[1]);
                            double precio = Double.parseDouble(componetes[2]);
                            
                            totalProducto = totalProducto + (cantidad * precio);
                            break;
                            }
                        }

                        System.out.println("El valor total de " + nameProduct+  " los productos es: " + totalProducto + " €.");
                    } catch (IOException e) {
                        e.printStackTrace();
                    }catch(NumberFormatException e){
                        e.toString();
                    }
                    break;
                case 8:
                    try {
                        Files.delete(archivoTienda);
                        System.out.println("Borrando archivo y saliendo8");
                    } catch (IOException e) {
                        // TODO Auto-generated catch block
                        e.printStackTrace();
                    }
                    finalPrograma=false; 
                    break;
            
                default:
                    System.out.println("Seleccione una de las opciones disponibles.");
                    break;
            }
        }

    }
}
