#  * IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
#  *
#  * EJERCICIO:
#  * Desarrolla un programa capaz de crear un archivo que se llame como
#  * tu usuario de GitHub y tenga la extensión .txt.
#  * Añade varias líneas en ese fichero:
#  * - Tu nombre.
#  * - Edad.
#  * - Lenguaje de programación favorito.
#  * Imprime el contenido.
#  * Borra el fichero.

file_name = "Elmer125.txt"

File.open(file_name, "w") do |file|
  file.puts "Elmer"
  file.puts "28"
  file.puts "Ruby"
end

File.open(file_name, "r") do |file|
  file.each_line do |line|
    puts line
  end
end

File.delete(file_name)

#  * DIFICULTAD EXTRA (opcional):
#  * Desarrolla un programa de gestión de ventas que almacena sus datos en un
#  * archivo .txt.
#  * - Cada producto se guarda en una línea del archivo de la siguiente manera:
#  *   [nombre_producto], [cantidad_vendida], [precio].
#  * - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
#  *   actualizar, eliminar productos y salir.
#  * - También debe poseer opciones para calcular la venta total y por producto.
#  * - La opción salir borra el .txt.
#  */

shopping_file = "elmer125_shopping.txt"
option = ""

while option != "8"
  puts "Introduce una opción: "
  puts "1. Añadir producto"
  puts "2. Consultar producto"
  puts "3. Actualizar producto"
  puts "4. Eliminar producto"
  puts "5. Mostrar productos"
  puts "6. Calcular venta total"
  puts "7. Calcular venta por producto"
  puts "8. Salir"

  option = gets.chomp

  case option
  when "1"
    puts "Introduce el nombre del producto:"
    product = "Nombre: #{gets.chomp}"
    puts "Introduce la cantidad vendida:"
    quantity = "Cantidad: #{gets.chomp}"
    puts "Introduce el precio:"
    price = "Precio: #{gets.chomp}"

    File.open(shopping_file, "a") do |file|
      file.puts "#{product}, #{quantity}, #{price}"
    end
  when "2"
    puts "Introduce el nombre del producto a consultar:"
    product = "Nombre: #{gets.chomp}"
    File.open(shopping_file, "r") do |file|
      file.each_line do |line|
        puts line if line.split(", ")[0] == product
      end
    end
  when "3"
    puts "Introduce el nombre del producto a actualizar:"
    product = "Nombre: #{gets.chomp}"
    puts "Introduce la nueva cantidad vendida:"
    quantity = "Cantidad: #{gets.chomp}"
    puts "Introduce el nuevo precio:"
    price = "Precio: #{gets.chomp}"

    products = File.readlines(shopping_file)

    File.open(shopping_file, "w") do |file|
      products.each do |line|
        if line.split(", ")[0] == product
          file.puts "#{product}, #{quantity}, #{price}"
        else
          file.puts line
        end
      end
    end
  when "4"
    puts "Introduce el nombre del producto a eliminar:"
    product = "Nombre: #{gets.chomp}"

    products = File.readlines(shopping_file)

    File.open(shopping_file, "w") do |file|
      products.each do |line|
        file.puts line unless line.split(",")[0] == product
      end
    end
  when "5"
    puts "Productos:"
    products = File.readlines(shopping_file)
    products.each do |line|
      puts line
    end
  when "6"
    products = File.readlines(shopping_file)
    puts "Venta total: #{products.map { |line| line.split(", ")[1].split(": ")[1].to_i * line.split(", ")[2].split(": ")[1].to_f }.sum}"

  when "7"
    products = File.readlines(shopping_file)
    puts "Introduce el nombre del producto a consultar:"
    product = "Nombre: #{gets.chomp}"
    puts "Venta por producto: #{products.select { |line| line.split(", ")[0] == product }.map { |line| line.split(", ")[1].split(": ")[1].to_i * line.split(", ")[2].split(": ")[1].to_f }.sum}"
  when "8"
    File.delete(shopping_file)
  else
    puts "Opción no válida"
  end
end