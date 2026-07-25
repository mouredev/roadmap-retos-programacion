import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Scanner;

public class JimsimroDev {

  private final static String DIVLINE = "::::::::::::::::::::::::::::::::::::::::::::::::::::";

  private static void menu() {
    String menu = """
            1 ~ Create product
            2 ~ Consult product
            3 ~ Update product
            4 ~ Delete product
            5 ~ List products
            6 ~ Calculate total sales
            7 ~ Calculate product sales
            8 ~ Exit
        """;
    System.out.println(menu);
  }

  private static void actions() {
    Scanner in = new Scanner(System.in);
    int option = 0;
    while (option != 8) {
      menu();
      System.out.println("Choose an option: ");
      option = in.nextInt();
      in.nextLine();
      switch (option) {
        case 1:
          System.out.print("Name: ");
          String name = in.nextLine();
          System.out.print("Quantity: ");
          int quantity = in.nextInt();
          System.out.print("Price: ");
          int price = in.nextInt();
          try {
            createProduct(name, quantity, price);
          } catch (IOException e) {
            e.printStackTrace();
          }
          break;
        case 2:
          System.out.print("Name of the product to search: ");
          String nameToSearch = in.nextLine();
          consultProduct(nameToSearch);
          break;
        case 3:
          System.out.print("Name: ");
          String nameToUpdate = in.nextLine();
          System.out.print("Quantity: ");
          int quantityToUpdate = in.nextInt();
          System.out.print("Price: ");
          int priceToUpdate = in.nextInt();
          updateProduct(nameToUpdate, quantityToUpdate, priceToUpdate);
          break;
        case 4:
          System.out.print("Name of the product to delete: ");
          String nameToDelete = in.nextLine();
          deleteProduct(nameToDelete);
          break;
        case 5:
          listProducts();
          break;
        case 6:
          calculateTotalSales();
          break;
        case 7:
          System.out.print("Name of the product: ");
          String productName = in.nextLine();
          calculateProductSales(productName);
          break;
        case 8:
          deleteFile();
          break;
      }
    }
    in.close(); // Close the scanner to avoid resource leak
  }

  private static void createProduct(String name, int quantity, int price) throws IOException {
    File file = getFileBasedOnOs();

    try (PrintWriter printWriter = new PrintWriter(new FileWriter(file, true))) { // 'true' for appending to the file
      printWriter.print(name + ", ");
      printWriter.print(quantity + ", ");
      printWriter.println(price);
    } catch (IOException e) {
      e.printStackTrace();
    }
    System.out.println("Created successfully");
  }

  private static void consultProduct(String name) {
    File file = getFileBasedOnOs();

    try (BufferedReader bufferedReader = new BufferedReader(new FileReader(file))) {
      String line;
      System.out.println(DIVLINE);
      while ((line = bufferedReader.readLine()) != null) {
        if (line.contains(name)) {
          System.out.println(line);
          break;
        }
      }
      System.out.println(DIVLINE);
    } catch (IOException e) {
      e.printStackTrace();
    }
  }

  private static void updateProduct(String name, int quantity, int price) {
    File file = getFileBasedOnOs();
    File tempFile = new File(file.getAbsolutePath() + ".tmp");
    boolean productFound = false;

    try (BufferedReader bufferedReader = new BufferedReader(new FileReader(file));
        BufferedWriter bw = new BufferedWriter(new FileWriter(tempFile))) {

      String line;
      while ((line = bufferedReader.readLine()) != null) {
        if (!line.contains(name)) {
          bw.write(line);
          bw.newLine();
        } else {
          bw.write(name + ", ");
          bw.write(quantity + ", ");
          bw.write(price + "\n");
          System.out.println("Updated successfully");
          productFound = true;
        }
      }
    } catch (IOException e) {
      System.out.println(e.getClass().getName() + " Error processing the file " + e.getMessage());
      e.printStackTrace();
    }
    if (!productFound) {
      System.err.println("Product " + name + " does not exist in the file " + file.getName());
      tempFile.delete();
      return;
    }
    if (!file.delete()) {
      return;
    }
    if (!tempFile.renameTo(file)) {
      System.err.println(file.getName());
    }
  }

  private static void deleteProduct(String name) {
    File file = getFileBasedOnOs();
    File tempFile = new File(file.getAbsolutePath() + ".tmp");

    try (BufferedReader bufferedReader = new BufferedReader(new FileReader(file));
        BufferedWriter bw = new BufferedWriter(new FileWriter(tempFile))) {

      String line;
      while ((line = bufferedReader.readLine()) != null) {
        if (!line.contains(name)) {
          bw.write(line);
          bw.newLine();
        }
      }
    } catch (IOException e) {
      System.out.println(e.getClass().getName() + " Error processing the file " + e.getMessage());
      e.printStackTrace();
    }

    if (!file.delete()) {
      return;
    }
    if (!tempFile.renameTo(file)) {
      System.err.println(file.getName());
    }
  }

  private static void listProducts() {
    File file = getFileBasedOnOs();

    try (BufferedReader bufferedReader = new BufferedReader(new FileReader(file))) {
      String line;
      System.out.println(DIVLINE);
      while ((line = bufferedReader.readLine()) != null) {
        System.out.println(line);
      }
      System.out.println(DIVLINE);
    } catch (IOException e) {
      e.printStackTrace();
    }
  }

  private static void calculateTotalSales() {
    File file = getFileBasedOnOs();

    try (BufferedReader bufferedReader = new BufferedReader(new FileReader(file))) {
      String line;
      int totalSales = 0;
      System.out.println(DIVLINE);
      while ((line = bufferedReader.readLine()) != null) {
        String[] parts = line.split(", ");
        int quantity = Integer.parseInt(parts[1]);
        int price = Integer.parseInt(parts[2]);

        totalSales += (quantity * price);
      }
      System.out.printf("Total sales: %d\n", totalSales);
      System.out.println(DIVLINE);
    } catch (IOException e) {
      e.printStackTrace();
    }
  }

  private static void calculateProductSales(String name) {
    File file = getFileBasedOnOs();

    try (BufferedReader bufferedReader = new BufferedReader(new FileReader(file))) {
      String line;
      int totalSales = 0;
      System.out.println(DIVLINE);
      while ((line = bufferedReader.readLine()) != null) {
        if (line.contains(name)) {
          String[] parts = line.split(", ");
          int quantity = Integer.parseInt(parts[1]);
          int price = Integer.parseInt(parts[2]);
          totalSales += (quantity * price);
          break;
        }
      }
      System.out.printf("Total sales of %s = %d\n", name, totalSales);
      System.out.println(DIVLINE);
    } catch (IOException e) {
      e.printStackTrace();
    }
  }

  private static void deleteFile() {
    File file = getFileBasedOnOs();
    file.delete();
  }

  private static File getFileBasedOnOs() {
    String osName = System.getProperty("os.name").toLowerCase();
    File file;

    if (osName.contains("win")) {
      file = new File("J:\\JimsimroDev.txt");
    } else if (osName.contains("nix") || osName.contains("nux")) {
      file = new File("/mnt/j/JimsimroDev.txt");
    } else if (osName.contains("mac")) {
      file = new File("/mnt/j/JimsimroDev.txt");
    } else {
      file = new File("/mnt/j/JimsimroDev.txt"); // Operating system not recognized
    }
    return file;
  }

  public static void main(String[] args) throws IOException {
    actions();
  }
}
