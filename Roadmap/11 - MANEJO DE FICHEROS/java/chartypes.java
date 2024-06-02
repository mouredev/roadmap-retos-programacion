
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.NoSuchFileException;
import java.nio.file.Path;
import java.nio.file.StandardOpenOption;
import java.util.List;
import java.util.Scanner;

public class FileManager {
  public static void main(String[] args) {
    try {
      exercise();
      extra();
    } catch (IOException e) {
      e.getMessage();
      e.printStackTrace();
    }

  }

  private static void exercise() throws IOException {
    Path path = Path.of("chartypes.txt");
    if (!Files.exists(path))
      Files.createFile(path);

    String content = """
        Name                        :      Carlos.
        Age                         :      22.
        Fav Programming Lenguague   :      Python.
        """;
    Files.writeString(path, content);
    List<String> data = Files.readAllLines(path);
    data.forEach(System.out::println);
    Files.delete(path);

  }

  private static void extra() throws IOException {
    Path path = Path.of("sales.txt");
    SalesManager salesManager = new SalesManager(path);
    salesManager.start();

  }
}

class SalesManager {
  private Path path;
  private Scanner scanner;

  public SalesManager(Path path) {
    try {
      this.path = path;
      scanner = new Scanner(System.in);
      Files.writeString(path, "");
    } catch (IOException e) {
      System.out.println(e);
    }
  }

  public void start() {
    int option = 0;
    while (true) {
      System.out.println("----------MENU----------");
      System.out.println("1 - Show all products");
      System.out.println("2 - Add product");
      System.out.println("3 - Check product");
      System.out.println("4 - Update product");
      System.out.println("5 - Delete product");
      System.out.println("6 - Calculate Total Sales");
      System.out.println("7 - Calculate Total Sales per product");
      System.out.println("8 - Exit");
      System.out.print("\nPick an option: ");

      if (scanner.hasNextInt())
        option = scanner.nextInt();

      switch (option) {
        case 1:
          readFile();
          break;
        case 2:
          StringBuffer line = new StringBuffer();
          System.out.println("Product name: ");
          line.append(scanner.next()).append(",");
          System.out.println("Quantity: ");
          line.append(scanner.next()).append(",");
          System.out.println("Price: ");
          line.append(scanner.next());
          addProduct(line.toString());
          break;
        case 3:
          System.out.println("Product name to look for: ");
          try {
            String name = scanner.next();
            searchProduct(name);
          } catch (Exception e) {
            System.out.println(e);
            System.out.println("You must insert a valid name");
          }
          break;
        case 4:
          StringBuilder newLine = new StringBuilder();
          System.out.println("Product name: ");
          String productName = scanner.next();
          newLine.append(productName).append(",");
          System.out.println("Quantity: ");
          newLine.append(scanner.next()).append(",");
          System.out.println("Price: ");
          newLine.append(scanner.next());
          updateProduct(productName, newLine.toString());
          break;
        case 5:
          System.out.println("Product name to delete: ");
          String name = scanner.next();
          deleteProduct(name);
          break;
        case 6:
          totalSales();
          break;
        case 7:
          salesPerProduct();
          break;
        case 8:
          deleteFile();
          return;
        default:
          System.out.println("You have to pick a valid option.");
          break;
      }

    }
  }

  private void readFile() {
    try (Scanner reader = new Scanner(path)) {
      while (reader.hasNext())
        System.out.println(reader.next());
    } catch (Exception e) {
      System.out.println(e);
      System.out.println("There was an error trying to read the file");
    }
  }

  private void addProduct(String product) {
    if (!Services.validateProduct(product)) {
      System.out.println("Please insert the correct values");
      return;
    }
    try {
      Files.writeString(path, product + "\n", StandardOpenOption.APPEND);
      System.out.println("Product added successfully");
    } catch (IOException e) {
      System.out.println(e);
      System.out.println("Error trying to insert the product");
    }

  }

  private void searchProduct(String productName) {
    boolean found = false;
    try (Scanner reader = new Scanner(path)) {
      reader.useDelimiter("\n");
      while (reader.hasNext()) {
        String product = reader.next();
        String[] parts = product.split(",");
        if (parts[0].equalsIgnoreCase(productName))
          found = true;
        if (found)
          System.out.println("Product found -> " + product);
        else {
          System.out.println("Product not found");
        }

      }
    } catch (Exception e) {
      System.out.println(e);
      System.out.println("Error trying to find the product");
    }
  }

  private void updateProduct(String productName, String newLine) {
    StringBuilder content = new StringBuilder();
    try (Scanner reader = new Scanner(path)) {
      reader.useDelimiter("\n");
      while (reader.hasNext()) {
        String next = reader.next();
        String[] parts = next.split(",");
        if (parts[0].equalsIgnoreCase(productName))
          content.append(newLine).append("\n");
        else {
          content.append(next).append("\n");
        }
      }
      Files.writeString(path, content);
      System.out.println("Product updated successfully");

    } catch (Exception e) {
      System.out.println(e);
      System.out.println("We found some issues trying to update your product");
    }
  }

  private void totalSales() {
    double total = 0;
    try (Scanner reader = new Scanner(path)) {
      reader.useDelimiter("\n");
      while (reader.hasNext()) {
        String[] line = reader.next().split(",");
        int quantity = Integer.parseInt(line[1]);
        double price = Double.parseDouble(line[2]);
        total = total + (quantity * price);
      }
      System.out.println("Total sales: " + total);

    } catch (Exception e) {
      System.out.println(e);
      System.out.println("We found some issues trying to get the total sales");
    }

  }

  private void salesPerProduct() {
    try (Scanner reader = new Scanner(path)) {
      reader.useDelimiter("\n");
      while (reader.hasNext()) {
        String[] line = reader.next().split(",");
        String productName = line[0];
        int quantity = Integer.parseInt(line[1]);
        double price = Double.parseDouble(line[2]);
        double total = price * quantity;

        System.out.println(
            "Product: " + productName + " quantity: " + quantity + " price: " + price + " Total Sales: " + total);
      }
    } catch (Exception e) {
      System.out.println(e);
      System.out.println("We found some issues trying to get the total sales of your products");
    }
  }

  private void deleteProduct(String productName) {
    StringBuilder content = new StringBuilder();
    try (Scanner reader = new Scanner(path)) {
      reader.useDelimiter("\n");
      while (reader.hasNext()) {
        String next = reader.next();
        String[] parts = next.split(",");
        if (!parts[0].equalsIgnoreCase(productName))
          content.append(next).append("\n");
      }
      Files.writeString(path, content.toString());
      System.out.println("Product deleted successfully");
    } catch (Exception e) {
      System.out.println(e);
      System.out.println("We found some issues trying to delete your product");
    }
  }

  private void deleteFile() {
    try {
      Files.delete(path);
    } catch (IOException e) {
      e.printStackTrace();
    }
  }

}

class Services {
  public static String formatingProduct(String productName, int quantity, double price) {
    String product = String.format("%s , %s , %s", productName, quantity, price);
    return product;
  }

  public static boolean validateProduct(String product) {
    try {
      String[] parts = product.split(",");
      String productName = parts[0];
      int quantity = Integer.parseInt(parts[1]);
      double price = Double.parseDouble(parts[2]);
    } catch (ArrayIndexOutOfBoundsException | NumberFormatException e) {
      System.out.println(e);
      return false;
    }
    return true;

  }
}
