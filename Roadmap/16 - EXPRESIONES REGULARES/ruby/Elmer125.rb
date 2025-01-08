#  * EJERCICIO:
#  * Utilizando tu lenguaje, explora el concepto de expresiones regulares,
#  * creando una que sea capaz de encontrar y extraer todos los números
#  * de un texto.
# DOC: https://www.rubyguides.com/2015/06/ruby-regex/

def get_numbers(text)
  text.scan(/\d+/)
end

puts get_numbers("Hola, mi número es 1234567890 y el tuyo?") # ["1234567890"]
puts get_numbers("Este es el ejercicio 16 publicado 15/04/2024.") # ["16", "15", "04", "2024"]

#  * DIFICULTAD EXTRA (opcional):
#  * Crea 3 expresiones regulares (a tu criterio) capaces de:
#  * - Validar un email.
#  * - Validar un número de teléfono.
#  * - Validar una url.

def email_valid?(email)
  email.match?(/\A[\w+\-.]+@[a-z\d\-.]+\.[a-z]+\z/i)
end

def phone_valid?(phone)
  phone.match?(/(^[3]([1-9]{2})([0-9]{7})$)/)
end

def url_valid?(url)
  url.match?(/\Ahttps?:\/\/[a-z\d\-.]+\.[a-z]+\z/i)
end

puts "Valid Emails"
puts "joeDoe@example.com #{email_valid?("joeDoe@example.com")}" # true
puts "joeDoe@example #{email_valid?("joeDoe@example")}" # false

puts "Valid Phones"
puts "3123456789 #{phone_valid?("3123456789")}" # true
puts "3120456781 #{phone_valid?("3021456781")}" # false

puts "Valid URLS"
puts "https://www.example.com #{url_valid?("https://www.example.com")}" # true
puts "http://example #{url_valid?("http://example")}" # false