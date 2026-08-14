import 'dart:io';

// ////////////////// Clase eejercicio extra //////////////////

class Product {
  String name;
  int quantitySold;
  double price;
  // Unica lista que comparten todas las instancias.

  static final fileName = 'productos.txt';
  static final file = File(fileName);

  Product({
    required this.name,
    required this.quantitySold,
    required this.price,
  });

  /////////// MÉTODOS //////////////////////

  Future<void> createFile() {
    return file.create();
  }

  String? item;

  Future<String?> validateProduct(productName) async {
    final currentLines = await file.readAsLines();
    for (final line in currentLines) {
      if (line.split(',').first.trim() == productName) {
        item = line;
        break;
      }
    }
    return item;
  }

  Future<void> addProduct(productName, quantitySold, price) async {
    await file.writeAsString(
      '$productName, $quantitySold, ${price.toStringAsFixed(2)}\n',
      mode: FileMode.append,
    );

    await calculateTotal();
    print('Producto añadido');
  }

  Future<void> viewProduct(String viewProduct) async {
    // final currentLines = await file.readAsLines();
    // final item = currentLines.firstWhere(
    //   (line) => line.split(',').first.trim() == viewProduct,
    //   orElse: () => '',
    // );

    await validateProduct(viewProduct);

    if (item != null) {
      print('Producto encontrado:\n$item');
      item = null;
    } else {
      print('El producto no existe');
    }

    // if (item.isNotEmpty) {
    //   print('Producto: ${item.split(',').first.trim()}');
    //   print(item);
    // } else {
    //   print('El producto no existe');
    // }
  }

  Future<void> updateProduct(
    String productName,
    String newName,
    int newQuantity,
    double newPrice,
  ) async {
    final currentLines = await file.readAsLines();
    // ReadAsLinesSync devuelve una lista teniendo como valores cada línea del texto.

    final updatedLines = currentLines.map((line) {
      if (line.split(',').first.trim() == productName) {
        return '$newName, $newQuantity, ${newPrice.toStringAsFixed(2)}';
      }
      return line;
    }).toList();
    /*  "EL PODER DE MAPEAP"
        * Al aplicar map a lines, toma cada linea y la divide por la "," creando una lista con 3 valores. 
        * Se selecciona el primer valor de esta lista y se le quita posibles espacios
        * Se la compara con el valor pasado a productName. De ser iguales 
        * Se devuelve una linea en reemplazo con los valores ingresados por la terminal y el precio fijado en 2 decimales.
        * El map debido a que devuelve un iterable se lo convierte a lista.
        * A continuación se escribe nuevamente el archivo con la lista producto de las líneas ya modificada 
        * y reconvertida a String mediante la función join. Que une los valores por el criterio de salto de línea. 
      */

    if (updatedLines.isEmpty) {
      print('El producto que desea eliminar no existe');
    }
    await file.writeAsString('${updatedLines.join('\n')}\n');
    await calculateTotal();
    print('Producto actualizado');
  }

  Future<void> deleteProduct(productName) async {
    await validateProduct(productName);

    final currentLines = await file.readAsLines();
    final newLine = currentLines
        .where((line) => line.split(',').first.trim() != productName)
        .toList();
    // Para borrar el archivo se debe reescribir todas las lineas con excepción de la que se quiere borrar.

    if (item == null) {
      print('El producto que desea eliminar no existe');
    } else {
      // El siguiente if evita que se añadan productos a la misma línea luego de que se borra un producto.
      if (newLine.isEmpty) {
        await file.writeAsString(
          '',
        ); // Borra todo el archivo cuando no hay productos mas que el borrado.
      } else {
        await file.writeAsString(
          '${newLine.join('\n')}\n',
        ); // el último salto asegura que se cree una nueva linea
      }
      await calculateTotal(); // Se actualiza el total
      print('Se eliminó $productName');
    }
  }

  Future<String> calculateByProduct(productToCalculate) async {
    final currentLines = await file.readAsLines();
    final line = currentLines.where((line) {
      return line.split(',').first.trim() == productToCalculate;
    }).toList();

    List<String> items = line[0].split(',');
    double itemPrice = double.parse(items.last);
    int itemQuantitySale = int.parse(items[1]);
    return '\nEl total de $productToCalculate vendido es: ${itemPrice * itemQuantitySale}';
  }

  Future<String> calculateTotal() async {
    final lines = await file.readAsLines();
    double total = 0;
    for (final line in lines) {
      final parts = line.split(',');
      final quantity = int.parse(parts[1].trim());
      final price = double.parse(parts[2].trim());
      total += quantity * price;
    }

    return '\nEl total de ventas es $total';
  }

  Future<void> deleteFile() async {
    if (file.existsSync()) {
      file.delete();
    }
  }

  Future<String>? showProducts() async {
    print('\nNombre de producto | cantidad | precio');
    return file.readAsString();
  }
}

Future<void> main(List<String> arguments) async {
  stdout.write(
    '\n************************** Manejo de archivos *******************************\n',
  );
  void createAjecsText() {
    String help =
        'Crea el archivo Ajecs.txt con el comando "create". eliminalo con el comando "delete"\nej: "dart Ajecs.dart create"';

    final filename = 'Ajecs.txt';
    var file = File(filename);
    Future<void> createFile(List<String> args) async {
      // FileMode.append permite anexar las cadenas de texto.
      // ! Es imporrtante el uso de await. Ya que de lo contrario los datos se solapan.
      if (file.existsSync()) {
        await file.delete();
        print('El archivo $filename ya existe');
        // ! En Dart por defecto se concatena el valor. Y se repeetiría el proceso de impresión de datos.
        // Por eso se elimina el archivo anterior y añade nuevamente. 😐
      }

      // Sin el modo append se concatenaría (por defecto) cada vez que se ejecuta el valor pasado ("lenguaje ..")
      await file.writeAsString('Nombre: Nicolás\n', mode: FileMode.append);
      await file.writeAsString('Edad: 39\n', mode: FileMode.append);
      await file.writeAsString(
        'Lenguaje favorito: Dart\n\n',
        mode: FileMode.append,
      );
      print('Archivo $filename creado');
    }

    Future<void> deleteFile(List<String> args) async {
      if (file.existsSync() == false && args[0] == 'delete') {
        print('El archivo $filename no existe');
      } else {
        await file.delete();
        print('Archivo $filename borrado');
      }
    }

    if (arguments.isNotEmpty) {
      switch (arguments[0]) {
        case 'create':
          createFile(arguments);
          break;
        case 'delete':
          deleteFile(arguments);
          break;
        case 'help':
          print(help);
          break;
        default:
          print(help);
      }
    } else {
      print(help);
    }
  }

  // createAjecsText();

  stdout.write(
    '\n*************************** Ejercicio Extra *************************\n',
  );

  Future<void> salesManagement() async {
    // ///////////////////// VARIABLES GLOBALES ///////////////////////////////

    Product product = Product(name: '', quantitySold: 0, price: 0.0);
    bool goOn = true;

    // /////////////////// UTILIDADES ////////////////////////////////////

    Function formatInput = () =>
        (stdin.readLineSync() ?? '').toLowerCase().trim();

    await product.createFile();

    stdout.write('\n<< Gestión de ventas >>\n');

    while (goOn) {
      print('\nPresione 1 -> Añadir producto');
      print('Presione 2 -> Consultar producto');
      print('Presione 3 -> Actualizar producto');
      print('Presione 4 -> Eliminar producto');
      print('Presione 5 -> Calcular venta por producto');
      print('Presione 6 -> Calcular venta total');
      print('Presione 7 -> Mostrar todos los productos');
      print('Presione "exit" para salir');

      String option = stdin.readLineSync() ?? '';

      switch (option) {
        case '1':
          String productNameInput;
          int quantitySoldInput;
          double priceInput;
          print('Ingrese el nombre del producto: ');
          productNameInput = formatInput();
          print('Ingrese la cantidad vendida: ');
          quantitySoldInput = int.parse(formatInput());
          print('Ingrese el precio: ');
          priceInput = double.parse(formatInput());

          product = Product(
            name: productNameInput,
            quantitySold: quantitySoldInput,
            price: priceInput,
          );
          await product.addProduct(
            productNameInput,
            quantitySoldInput,
            priceInput,
          );
          break;

        case '2':
          print('Busca por el nombre del producto: ');
          String viewProductInput = formatInput();
          await product.viewProduct(viewProductInput);

        case '3':
          print('Ingresa el nombre del producto a actualizar: ');
          String productToUpdate = formatInput();

          await product.validateProduct(productToUpdate);

          if (product.item == null) {
            print('El producto no existe');
            break;
          }

          print('Ingresa el nuevo nombre: ');
          String newName = formatInput();

          print('Ingresa la nueva cantidad vendida: ');
          int newQuantity = int.parse(formatInput());

          print('Ingresa el nuevo precio: ');
          double newPrice = double.parse(formatInput());

          await product.updateProduct(
            productToUpdate,
            newName,
            newQuantity,
            newPrice,
          );
          break;

        case '4':
          print('Eimina por el nombre del producto: ');
          String deleteProductInput = formatInput();
          await product.deleteProduct(deleteProductInput);
        case '5':
          print('Ingresa el nombre del producto: ');
          String productToCalculate = formatInput();
          print(await product.calculateByProduct(productToCalculate));
        case '6':
          print(await product.calculateTotal());
        case '7':
          print(await product.showProducts());
        case 'exit':
          goOn = false;
          await product.deleteFile();
          print('Se ha salido del programa');
          break;
        default:
          print('Ingrese una opción válida');
      }
    }
  }

  salesManagement();
}
