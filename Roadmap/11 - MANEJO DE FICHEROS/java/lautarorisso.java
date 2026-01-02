import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardOpenOption;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.logging.Level;
import java.util.logging.Logger;

public class LogicaJava11 {
    
    public static void main(String[] args) {
        // 1.
        Path path = Path.of("lautarorisso.txt");
        try {
            Files.write(path, List.of(
                    "Lautaro Risso",
                    "21",
                    "Java"
            ));
        } catch (IOException ex) {
            Logger.getLogger(LogicaJava11.class.getName()).log(Level.SEVERE, null, ex);
        }

        List<String> linesPrueba;
        try {
            linesPrueba = Files.readAllLines(path);
            for (String linePrueba : linesPrueba) {
            System.out.println(linePrueba);
        }
        } catch (IOException ex) {
            Logger.getLogger(LogicaJava11.class.getName()).log(Level.SEVERE, null, ex);
        }
        
        try {
            Files.delete(path);
        } catch (IOException ex) {
            Logger.getLogger(LogicaJava11.class.getName()).log(Level.SEVERE, null, ex);
        }
        
        // EXTRA
        Scanner t = new Scanner (System.in);
        
        while (true) {
            try {
                System.out.println("1. Añadir Producto");
                System.out.println("2. Consultar Producto");
                System.out.println("3. Actualizar Producto");
                System.out.println("4. Borrar Producto");
                System.out.println("5. Mostrar todos los productos");
                System.out.println("6. Calcular venta total");
                System.out.println("7. Calcular venta por producto");
                System.out.println("8. Salir");
                
                String file_name = "ventas.txt";
                Path p = Path.of(file_name);
                
                System.out.print("Seleccione una opción: ");
                String option = t.nextLine();
                
                switch (option) {
                    case "1": {
                        System.out.print("Nombre: ");
                        String name = t.nextLine();
                        System.out.print("Cantidad: ");
                        String quantity = t.nextLine();
                        System.out.print("Precio: ");
                        String price = t.nextLine();
                        
                        String line = name + ", " + quantity + ", " + price + "\n";
                            Files.writeString(
                                    p,
                                    line,
                                    StandardOpenOption.CREATE,
                                    StandardOpenOption.APPEND
                            );
                    }
                        break;
                    case "2": {
                        System.out.print("Nombre: ");
                        String name = t.nextLine();
                        List<String> lines = Files.readAllLines(p);
                            for (String line : lines) {
                                if (line.split(", ")[0].equals(name)) {
                                    System.out.println(line);
                                }
                            }
                    }
                        break;
                    case "3": {
                        System.out.print("Nombre: ");
                        String name = t.nextLine(); 
                        System.out.print("Cantidad: ");
                        String quantity = t.nextLine();
                        System.out.print("Precio: ");
                        String price = t.nextLine();
                        
                        Path pat = Path.of(file_name);
                        
                        // leemos todo
                        List<String> lines = Files.readAllLines(p);
                        List<String> updatedLines = new ArrayList<>();
                        
                        for (String line : lines) {
                            
                            String[] parts = line.split(", ");
                            
                            if (parts[0].equals(name)) {
                                // producto actualizado
                                updatedLines.add(
                                        name + ", " + quantity + ", " + price
                                );
                            } else {
                                // producto intacto
                                updatedLines.add(line);
                            }
                        }
                        // sobrescribimos el archivo
                        Files.write(pat, updatedLines);
                    }
                        break;
                    case "4": {
                        System.out.print("Nombre: ");
                        String name = t.nextLine();
                        Path pat2 = Path.of(file_name);

                        List<String> lines = Files.readAllLines(pat2);
                        List<String> deleteLine = new ArrayList<>();

                        boolean deleted = false;

                        for (String line : lines) {

                            String[] parts = line.split(", ");

                            if (parts[0].equals(name)) {
                                deleted = true;      // no la agregamos → se borra
                            } else {
                                deleteLine.add(line);
                            }
                        }
                        // sobrescribimos el archivo
                        Files.write(pat2, deleteLine);
                        
                        if (deleted) {
                            System.out.println("Producto eliminado.");
                        } else {
                            System.out.println("Producto no encontrado.");
                        } 
                    }
                        break;
                    case "5": {
                        List<String>lines = Files.readAllLines(p);
                        for (String line : lines) {
                            System.out.println(line);
                        }
                    }
                        break;
                    case "6": {
                        double total = 0;
                        List<String >lines = Files.readAllLines(p);
                            for (String line : lines) {
                                String[] parts = line.split(", ");
                                int quantity = Integer.parseInt(parts[1]);
                                double price = Double.parseDouble(parts[2]);
                                total+= quantity*price;
                        }
                        System.out.println(total);
                    }
                        break;
                    case "7": {
                        System.out.print("Nombre: ");
                        String name = t.nextLine();
                        double total = 0;
                        List<String >lines = Files.readAllLines(p);
                            for (String line : lines) {
                                String[] parts = line.split(", ");
                                if (parts[0].equals(name)) {
                                    int quantity = Integer.parseInt(parts[1]);
                                    double price = Double.parseDouble(parts[2]);
                                    total+= quantity*price; 
                                }
                        }
                        System.out.println(total);
                    }
                        break;
                    case "8": {
                        Files.delete(p);
                    }
                        break;
                    default:
                        System.out.println("Opción inválida");
                        return;
                }
            } catch (IOException ex) {
                Logger.getLogger(LogicaJava11.class.getName()).log(Level.SEVERE, null, ex);
            }
        }
    }
}
