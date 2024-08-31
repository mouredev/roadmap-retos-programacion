def reg_expr(cadena)
    patron = /-?\d*\.?\d+/
    numeros = cadena.scan(patron)
  
    puts "Números encontrados:"
    numeros.each { |numero| puts numero }
    puts "\n"
end
  

def email_validation(email)
  patron = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/
  if email.match?(patron)
    puts "El email #{email} es válido."
  else
    puts "El email #{email} no es válido."
  end
end

def phone_validation(phone)
  patron = /^\+?(\d{2,3})?[-. ]?\d{9}$/
  if phone.match?(patron)
    puts "El teléfono #{phone} es válido."
  else
    puts "El teléfono #{phone} no es válido."
  end
end

def url_validation(url)
  patron = /^(http|https):\/\/[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}/
  if url.match?(patron)
    puts "La URL #{url} es válida."
  else
    puts "La URL #{url} no es válida."
  end
end

texto = "Este es un texto con números como 123, 45.6, -7 y 1000."
puts "Vamos a analizar el siguiente texto:"
puts "'#{texto}'\n\n"
reg_expr(texto)

texto = "123Erase una vez un número 1234567890 y otro 0987654321. Y para terminar456"
puts "Vamos a analizar el siguiente texto:"
puts "'#{texto}'\n\n"
reg_expr(texto)

email_validation("correo@correo.com")
email_validation("correo@correo")

phone_validation("+34 123456789")
phone_validation("123456789")

url_validation("http://www.google.com")
url_validation("www.google.com")
