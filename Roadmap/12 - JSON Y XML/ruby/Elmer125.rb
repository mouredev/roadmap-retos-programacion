#  * IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
#  *
#  * EJERCICIO:
#  * Desarrolla un programa capaz de crear un archivo XML y JSON que guarde los
#  * siguientes datos (haciendo uso de la sintaxis correcta en cada caso):
#  * - Nombre
#  * - Edad
#  * - Fecha de nacimiento
#  * - Listado de lenguajes de programación
#  * Muestra el contenido de los archivos.
#  * Borra los archivos.
require 'nokogiri'
require 'json'

data = {
  name: "John Doe",
  age: 30,
  birth_date: "07-07-1994",
  languages: ["Ruby", "Kotlin", "JavaScript"]
}


class FileHandler
  def initialize(file)
    @file = file
  end

  def show_file_content
    puts File.read(@file)
  end

  def delete_file
    File.delete(@file)
  end
end

###XML file###
# def create_xml(file, data)
#   File.open(file, "w") do |file|
#     file.puts "<user>"
#     data.each do |key, value|
#       file.puts "  <#{key}>#{value}</#{key}>"
#     end
#     file.puts "</user>"
#   end
# end

# Using the Nokogiri gem
xml_file = "elmer125.xml"
def create_xml(file, data)
  builder = Nokogiri::XML::Builder.new do |xml|
    xml.user {
      xml.name data[:name]
      xml.age data[:age]
      xml.birth_date data[:birth_date]
      xml.languages {
        data[:languages].each do |language|
          xml.language language
        end
      }
    }
  end

  File.write(file, builder.to_xml)
end

create_xml(xml_file, data)
xml_handler = FileHandler.new(xml_file)
puts "XML file content:"
xml_handler.show_file_content
xml_handler.delete_file

###JSON file###
json_file = "elmer125.json"

# Create JSON file
def create_json(file, content)
  File.write(file, content)
end
json_content = data.to_json
create_json(json_file, json_content)
json_handler = FileHandler.new(json_file)
puts "JSON file content:"
json_handler.show_file_content
json_handler.delete_file


#  * DIFICULTAD EXTRA (opcional):
#  * Utilizando la lógica de creación de los archivos anteriores, crea un
#  * programa capaz de leer y transformar en una misma clase custom de tu
#  * lenguaje los datos almacenados en el XML y el JSON.
#  * Borra los archivos.
#  */


create_xml(xml_file, data)
create_json(json_file, data.to_json)

class Data
  attr_accessor :name, :age, :birth_date, :languages

  def initialize(name, age, birth_date, languages)
    @name = name
    @age = age
    @birth_date = birth_date
    @languages = languages
  end

  def self.xml_file(file)
    xml = Nokogiri::XML(File.read(file))
    name = xml.xpath("//name").text
    age = xml.xpath("//age").text.to_i
    birth_date = xml.xpath("//birth_date").text
    languages = xml.xpath("//languages/language").map(&:text)
    new(name, age, birth_date, languages)
  end

  def self.json_file(file)
    data = JSON.parse(File.read(file))
    new(data["name"], data["age"], data["birth_date"], data["languages"])
  end

  def delete_file(file)
    File.delete(file)
  end

  def show_data
    puts "#"*10
    puts "Name: #{@name}"
    puts "Age: #{@age}"
    puts "Birth date: #{@birth_date}"
    puts "Languages: #{@languages.join(", ")}"
  end
end

xml = Data.xml_file(xml_file)
json = Data.json_file(json_file)

xml.show_data
json.show_data

xml.delete_file(xml_file)
json.delete_file(json_file)

