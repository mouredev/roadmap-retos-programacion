public class Main {
    public static void main(String[] args) {

        File file = new File("src/data.txt");
        FileWriter writer;
        Scanner reader;

        try {
            //Creamos el fichero
            file.createNewFile();

            //Escribimos los datos
            writer = new FileWriter(file);

            writer.append("Nombre: Abel\n");
            writer.append("Edad: 30\n");
            writer.append("Lenguaje de programación: Java\n");

            writer.close();

            //Leemos el contenido
            reader = new Scanner(file);

            System.out.println("Contenido del fichero: ");

            while (reader.hasNext()) {
                String line = reader.nextLine();
                System.out.println(line);
            }

            reader.close();

            //Borramos el fichero
            file.delete();

        } catch (IOException e) {
            System.out.println("Error con el archivo");
        }

        System.out.println("\n-------DIFICULTAD EXTRA------\n");

        boolean exit = false;
        Scanner scanner = new Scanner(System.in);
        File venta = new File("src/venta.txt");
        try {
            if (!venta.exists()) {
                venta.createNewFile();
            }
        } catch (IOException e) {
            System.out.println("Error al crear el archivo\n");
        }
        do {
            System.out.println("Bienvenido al programa de ventas!\n");
            System.out.println("¿Qué deseas hacer?");
            System.out.println("1- Añadir un producto");
            System.out.println("2- Eliminar un producto");
            System.out.println("3- Buscar un producto");
            System.out.println("4- Actualizar un producto");
            System.out.println("5- Calcular precio de un producto");
            System.out.println("6- Calcular precio de venta total");
            System.out.println("7- Salir\n");

            System.out.print("Introduzca una opcion: ");
            int option = scanner.nextInt();
            scanner.nextLine();
            System.out.println();

            switch (option) {
                case 1:
                    try {
                        System.out.println("Vamos a añadir un producto!\n");
                        System.out.print("Introduce el nombre: ");
                        String name = scanner.nextLine();

                        System.out.print("Introduce la cantidad vendida: ");
                        int amount = scanner.nextInt();
                        scanner.nextLine();

                        System.out.print("Introduce el precio: ");
                        double precio = scanner.nextDouble();
                        scanner.nextLine();

                        FileWriter writerVenta = new FileWriter(venta, true);
                        writerVenta.append(name + ", " + amount + ", " + precio + "\n");
                        writerVenta.close();
                    } catch (IOException e) {
                        System.out.println("Error al escribir el archivo\n");
                    }
                    break;
                case 2:
                    System.out.println("Vamos a eliminar un producto!\n");

                    System.out.print("Introduce el nombre: ");
                    String nameDelete = scanner.nextLine();

                    ArrayList<String> products = new ArrayList<>();
                    try {
                        boolean exist = false;
                        Scanner readerVenta = new Scanner(venta);

                        while (readerVenta.hasNext()) {
                            String product = readerVenta.nextLine();
                            products.add(product);
                            if (product.contains(nameDelete)) {
                                exist = true;
                            }
                        }

                        if (exist) {
                            //Eliminamos el producto de la lista
                            for (int i = 0; i < products.size(); i++) {
                                if (products.get(i).contains(nameDelete)) {
                                    products.remove(i);
                                }
                            }
                        } else {
                            System.out.println("No existe el producto");
                        }

                        readerVenta.close();
                    } catch (FileNotFoundException e) {
                        System.out.println("Error al leer el archivo\n");
                    }

                    try {
                        FileWriter writeProducts = new FileWriter(venta, false);
                        for (String product : products) {
                            writeProducts.append(product + "\n");
                        }
                        writeProducts.close();
                    } catch (IOException e) {
                        System.out.println("Error al escribir el archivo\n");
                    }
                    break;
                case 3:
                    System.out.println("Vamos a buscar un producto!\n");

                    System.out.print("Introduce el nombre: ");
                    String name = scanner.nextLine();

                    try {
                        boolean exist = false;
                        Scanner readerVenta = new Scanner(venta);
                        String line = null;
                        while (readerVenta.hasNext() && !exist) {
                            line = readerVenta.nextLine();
                            if (line.contains(name)) {
                                exist = true;
                            }
                        }

                        if (exist) {
                            System.out.println("\nEstos son los datos del producto: ");
                            System.out.println(line + "\n");
                        } else {
                            System.out.println("No existe el producto\n");
                        }
                        readerVenta.close();
                    } catch (FileNotFoundException e) {
                        System.out.println("Error al leer el archivo\n");
                    }
                    break;
                case 4:
                    System.out.println("Vamos a actualizar un producto!\n");

                    System.out.print("Introduce el nombre (original): ");
                    String lastName = scanner.nextLine();

                    ArrayList<String> productsUpdate = new ArrayList<>();
                    try {
                        boolean exist = false;
                        Scanner readerVenta = new Scanner(venta);

                        while (readerVenta.hasNext()) {
                            String product = readerVenta.nextLine();
                            productsUpdate.add(product);
                            if (product.contains(lastName)) {
                                exist = true;
                            }
                        }

                        if (exist) {
                            System.out.print("Introduce el nombre (nuevo): ");
                            String nameUpdate = scanner.nextLine();

                            System.out.print("Introduce la cantidad (nueva): ");
                            int amountUpdate = scanner.nextInt();
                            scanner.nextLine();

                            System.out.print("Introduce el nuevo precio (nuevo): ");
                            double priceUpdate = scanner.nextDouble();
                            scanner.nextLine();

                            //Actualizamos el producto de la lista
                            for (int i = 0; i < productsUpdate.size(); i++) {
                                if (productsUpdate.get(i).contains(lastName)) {
                                    productsUpdate.set(i,nameUpdate+", "+amountUpdate+", "+priceUpdate);
                                }
                            }
                        } else {
                            System.out.println("No existe el producto");
                        }

                        readerVenta.close();
                    } catch (FileNotFoundException e) {
                        System.out.println("Error al leer el archivo\n");
                    }

                    try {
                        FileWriter writeProducts = new FileWriter(venta, false);
                        for (String product : productsUpdate) {
                            writeProducts.append(product + "\n");
                        }
                        writeProducts.close();
                    } catch (IOException e) {
                        System.out.println("Error al escribir el archivo\n");
                    }
                    break;
                case 5:
                    System.out.println("Vamos a calcular el precio de un producto!\n");

                    System.out.print("Introduce el nombre: ");
                    String nameProductPrice = scanner.nextLine();

                    Scanner readProduct = null;
                    try {
                        readProduct = new Scanner(venta);
                    } catch (FileNotFoundException e) {
                        System.out.println("Error al leer el archivo\n");
                    }
                    String product = "";
                    boolean exist = false;
                    while (readProduct.hasNext() && !exist) {
                        product = readProduct.nextLine();
                        if (product.contains(nameProductPrice)) {
                            exist = true;
                        }
                    }

                    int amountProduct = Integer.parseInt(product.substring((product.indexOf(',')+2),product.lastIndexOf(',')));
                    Double priceProduct = Double.valueOf(product.substring(product.lastIndexOf(",")+2));
                    System.out.println("\nEl precio total del producto es: " + (priceProduct*amountProduct)+"\n");

                    break;
                case 6:
                    System.out.println("Vamos a calcular el precio total!\n");

                    Scanner readProductPrice = null;
                    try {
                        readProductPrice = new Scanner(venta);
                    } catch (FileNotFoundException e) {
                        System.out.println("Error al leer el archivo\n");
                    }

                    int sum = 0;
                    while (readProductPrice.hasNext()) {
                        String prod = readProductPrice.nextLine();
                        int amount = Integer.parseInt(prod.substring((prod.indexOf(',')+2),prod.lastIndexOf(',')));
                        Double price = Double.valueOf(prod.substring(prod.lastIndexOf(",")+2));
                        sum += amount*price;
                    }

                    System.out.println("El precio total de la venta es: " + sum +"\n");

                    readProductPrice.close();
                    break;
                case 7:
                    if (venta.exists()) {
                        venta.delete();
                    }
                    exit = true;
                    break;
                default:
                    System.out.println("Opcion no valida!\n");
            }
        } while (!exit);

    }
}
