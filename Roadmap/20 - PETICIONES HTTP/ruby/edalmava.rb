# Ruby tiene un cliente HTTP interno llamado 'net/http' que no logre configurar en Windows
# En su lugar use la gema httparty que se instala con: gem install httparty

require 'httparty'
response = HTTParty.get('https://pokeapi.co/api/v2/pokemon/pikachu')
if response.code == 200
    puts "Respuesta OK: "
    puts response.body
else 
    print 'Código de respuesta: ' 
    puts response.code
end
