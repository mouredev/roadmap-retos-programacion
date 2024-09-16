
import java.io.FileWriter;

public class simonguzman {
    public static void main(String[] args) {
        incorrectSrp();
    }

    /****************************** ejemplo sin srp(Incorrecto) ******************************/
    public static void incorrectSrp(){
        Invoice invoice = new Invoice("Laptop",2,1200.00);
        invoice.printInvoice();
        invoice.saveToFile();
    }

    static class Invoice{
        private String product;
        private int quantity;
        private double price;

        public Invoice(){

        }

        public Invoice(String product, int quantity, double price){
            this.product = product;
            this.quantity = quantity;
            this.price = price;
        }

        public double calculateTotal(){
            return quantity * price;
        }

        public void printInvoice(){
            System.out.println("Producto: "+product);
            System.out.println("Cantidad: "+quantity);
            System.out.println("Precio: "+price);
            System.out.println("Total: "+calculateTotal());
        }
        
        public void saveToFile(){
            try (FileWriter writer = new FileWriter("invoice.txt")){
                writer.write("Producto: " + product + "\n");
                writer.write("Cantidad: " + quantity + "\n");
                writer.write("Precio Unitario: " + price + "\n");
                writer.write("Total: " + calculateTotal() + "\n");
            } catch (Exception e) {
                System.out.println("Error al guardar la factura: "+e.getMessage());
            }
        }
    }
}
