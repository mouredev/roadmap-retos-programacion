/*
 * IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
 *
 * EJERCICIO:
 * Desarrolla un programa capaz de crear un archivo que se llame como
 * tu usuario de GitHub y tenga la extensión .txt.
 * Añade varias líneas en ese fichero:
 * - Tu nombre.
 * - Edad.
 * - Lenguaje de programación favorito.
 * Imprime el contenido.
 * Borra el fichero.
 *
 * DIFICULTAD EXTRA (opcional):
 * Desarrolla un programa de gestión de ventas que almacena sus datos en un 
 * archivo .txt.
 * - Cada producto se guarda en una línea del archivo de la siguiente manera:
 *   [nombre_producto], [cantidad_vendida], [precio].
 * - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
 *   actualizar, eliminar productos y salir.
 * - También debe poseer opciones para calcular la venta total y por producto.
 * - La opción salir borra el .txt.
 */

import 'dart:io';

void main() async {
  //exercice11();
  salesManagment();
}

void exercice11() async {
  try {
    final userName = 'Teren91';
    final age = 32;
    final lenguage = 'Dart';

    final file = File('$userName.txt');

    await file.create();
    await file.writeAsString('''
    Nombre: $userName
    Edad: $age
    Lenguaje de programación favorito: $lenguage
    ''');

    final content = await file.readAsString();
    print(content);
    await file.delete();
  } catch (e) {
    print(e);
  }
}

void salesManagment() async {
  int? option;

  final file = File('Products.txt');

  ProductList productList = new ProductList(file);
  await productList.createProductsFile(file);

  SalesCalculator salesCalculator = new SalesCalculator();

  UserUI ui = new UserUI(productList, salesCalculator);

  try {
    do {
      ui.showMenu();
      option = int.tryParse(stdin.readLineSync()!);

      await ui.chooseOption(option!);
    } while (option != 8);
  } catch (e) {
    print(e);
  }
}

class UserUI {
  final ProductList productList;
  final SalesCalculator salesCalculator;

  UserUI(this.productList, this.salesCalculator);

  void showMenu() {
    print('''
      
      --------------------
        1. Añadir producto
        2. Buscar producto
        3. Ver todos los productos
        4. Actualizar producto      
        5. Eliminar producto
        6. Ver venta total
        7. Ver venta por producto
        8. Exit
      --------------------
      ''');
  }

  Future<void> chooseOption(int option) async {
    try {
      switch (option) {
        case 1:
          await _addProduct();
        case 2:
          await _searchProduct();
        case 3:
          await _getAllProducts();
         case 4:
          await _updateProduct();
        case 5:
          await _deleteProduct();
        case 6:
          await _calculateTotalSales();
        case 7:
          await _calculateProductSales();
        case 8:
          await _deleteFile();
        default:
          print('Program finished');
      }
    } catch (e) {
      print(e);
    }
  }

  Future<void> _addProduct() async {
    try {
      print('Introduzca los datos requeridos:');
      print('Nombre del producto:');
      final productName = stdin.readLineSync()!;

      print('Cantidad vendida:');
      final saleAmount = int.tryParse(stdin.readLineSync()!);

      print('Precio del producto:');
      final price = double.tryParse(stdin.readLineSync()!);

      Product product = new Product(productName, saleAmount!, price!);

      await productList.addProduct(product);

      print('Producto añadido correctamente');
    } catch (e) {
      print(e);
    }
  }

  Future<void> _getAllProducts() async {
    final products = await productList.getAllProducts();

    if(products.isNotEmpty)
      print(products);
  }

  Future<void> _searchProduct() async {
    print('Indica el nombre del producto:');
    final name = stdin.readLineSync();

    final product = await productList.searchProduct(name!);

    print(product);
  }

  Future<void> _deleteProduct() async {
    print('Indica el nombre del producto que deseas eliminar:');

    final name = stdin.readLineSync();

    await productList.deleteProduct(name!);

    print('Producto eliminado correctamente!.');
  }

  Future<void> _updateProduct() async
  {
    print('Indica el nombre del producto para actualizar:');
    final productName = stdin.readLineSync()!;

    print('Indica la nueva cantidad de venta:');
    final saleAmount = int.tryParse(stdin.readLineSync()!);

    print('Indica el nuevo precio:');
    final price = double.tryParse(stdin.readLineSync()!);

    Product product = new Product(productName, saleAmount!, price!);

    await productList.updateProduct(product);
  }

  Future<void> _deleteFile() async
  {
    await productList.deleteFile();
  }

  _calculateTotalSales() async
  {
    final products = await productList.getAllProducts();

    print(salesCalculator.totalSales(products));

  }

  _calculateProductSales() async
  {
    print('Introduzca el nombre del producto');
    final productName = stdin.readLineSync()!;

    final products = await productList.getAllProducts().then((products) => products);

    final sales = salesCalculator.productTotalSales(products, productName);
    

    print(sales);

  }


}

class Product {
  final String productName;
  final int saleAmount;
  final double price;

  Product(this.productName, this.saleAmount, this.price);

  @override
  String toString() {
    return '$productName, $saleAmount, $price';
  }
}

class ProductList {
  final File productsFile;

  ProductList(this.productsFile);

  Future<void> createProductsFile(File file) async {
  try {
    await file.create();
  } catch (e) {
    print(e);
  }
}

  Future<void> addProduct(Product product) async {
    try {
      final content = await productsFile.readAsString();
      final newContent = '$content\n${product.toString()}';

      await productsFile.writeAsString(newContent);
    } catch (e) {
      print(e);
    }
  }

  Future<Product> searchProduct(String name) async {
    final products = await getAllProducts();

    final product =
        products.firstWhere((element) => element.productName == name);

    return product;
  }

  Future<List<Product>> getAllProducts() async {
    List<Product> products = [];
    try {
      final content = await productsFile.readAsString();

      if(content.isEmpty)
      {
        print('No hay productos disponibles.');
        return products;
      }
      final lines = content.split('\n');

      for (final line in lines) {
        final parts = line.split(',');
        final product =
            Product(parts[0], int.parse(parts[1]), double.parse(parts[2]));
        products.add(product);
      }

      return products;
    } catch (e) {
      print(e);
    } finally {
      return products;
    }
  }

  Future<void> deleteProduct(String name) async {
    try {
      final products = await getAllProducts();

      products.removeWhere((element) => element.productName == name);
      await _saveProducts(products);

    } catch (e) {
      print(e);
    }
  }

  Future<void> updateProduct(Product product) async
  {
    final products = await getAllProducts();

    final index = products.indexWhere(
      (element) => element.productName == product.productName);
  
    products[index] = product;

    _saveProducts(products);
  }

  Future<void> _saveProducts(List<Product> products) async {
    try {
      final content = products.map((e) => e.toString()).join('\n');
      await productsFile.writeAsString(content);
    } catch (e) {
      print(e);
    }
  }

  Future<void> deleteFile() async
  {
    try {
      productsFile.delete();
    } catch (e) {
      print(e);
    }
  }

}

class SalesCalculator{
  
  double totalSales(List<Product> productList)
  {
    double total = 0;

    try {
      
      for (final product in productList)
      {
        total += product.price * product.saleAmount;
      }

     // return total;
      
    } catch (e) {
      print(e);
    }

    return total;
  }

  double productTotalSales(List<Product> productList, String productName)
  {
    try {

      final product = productList.firstWhere((element) => element.productName == productName);

       return product.saleAmount * product.price;
    } catch (e) {
      print(e);
    }

      return 0;

   
  }
}
