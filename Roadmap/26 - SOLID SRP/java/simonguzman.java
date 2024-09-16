
import java.io.FileWriter;

public class simonguzman {
    public static void main(String[] args) {
        //incorrectSrp();
        correctSrp();
    }
    /****************************** ejemplo con srp(Correcto) ******************************/
    public static void correctSrp() {
        InvoiceSrp invoice = new InvoiceSrp("Laptop",2,1200.00);

        InvoicePrinter printer = new InvoicePrinter();
        printer.printInvoice(invoice);

        InvoiceSaver saver = new InvoiceSaver();
        saver.saveToFile(invoice);
    }
    static class InvoiceSrp{
        private String product;
        private int quantity;
        private double price;

        public InvoiceSrp(){
            
        }

        public InvoiceSrp(String product, int quantity, double price){
            this.product = product;
            this.quantity = quantity;
            this.price = price;
        }

        public double calculateTotal(){
            return quantity * price;
        }

        public String getProduct() {
            return product;
        }

        public int getQuantity() {
            return quantity;
        }

        public double getPrice() {
            return price;
        }
    }

    static class InvoicePrinter {
        public void printInvoice(InvoiceSrp invoice){
            System.out.println("Producto: "+invoice.getProduct());
            System.out.println("Cantidad: "+invoice.getQuantity());
            System.out.println("Precio: "+invoice.getPrice());
            System.out.println("Total: "+invoice.calculateTotal());
        }
    }

    static class InvoiceSaver{
        public void saveToFile(InvoiceSrp invoice){
            try (FileWriter writer = new FileWriter("invoice.txt")){
                writer.write("Producto: " + invoice.getProduct() + "\n");
                writer.write("Cantidad: " + invoice.getQuantity() + "\n");
                writer.write("Precio unitario: " + invoice.getPrice() + "\n");
                writer.write("Total: " + invoice.calculateTotal() + "\n");
            } catch (Exception e) {
                System.out.println("ERROR: no se pudo generar la factura..."+e.getMessage());
            }
        }
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
