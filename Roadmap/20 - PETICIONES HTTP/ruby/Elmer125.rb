#  * EJERCICIO:
#  * Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
#  * una petición a la web que tú quieras, verifica que dicha petición
#  * fue exitosa y muestra por consola el contenido de la web.
# Doc: https://github.com/ruby/net-http
require 'net/http'
require 'json'

Net::HTTP.start('www.google.com') do |http|
  response = http.get('/')
  if response.code == '200'
    puts "Request successful"
    puts response.body
  else
    puts "Request failed"
  end
end

#  * DIFICULTAD EXTRA (opcional):
#  * Utilizando la PokéAPI (https://pokeapi.co), crea un programa por
#  * terminal al que le puedas solicitar información de un Pokémon concreto
#  * utilizando su nombre o número.
#  * - Muestra el nombre, id, peso, altura y tipo(s) del Pokémon
#  * - Muestra el nombre de su cadena de evoluciones
#  * - Muestra los juegos en los que aparece
#  * - Controla posibles errores

pokemon_url = 'https://pokeapi.co/api/v2/pokemon/'

puts "Enter a Pokémon name or id:"
pokemon = gets.chomp
puts "Searching for Pokémon #{pokemon}..."
response = Net::HTTP.get_response(URI(pokemon_url + pokemon))
if response.code == '200'
  pokemon_data = JSON.parse(response.body)
  puts "Name: #{pokemon_data['name']}"
  puts "Id: #{pokemon_data['id']}"
  puts "Weight: #{pokemon_data['weight']}"
  puts "Height: #{pokemon_data['height']}"
  puts "Types: #{pokemon_data['types'].map { |type| type['type']['name'] }.join(', ')}"
  puts "Games: #{pokemon_data['game_indices'].map { |game| game['version']['name'] }.join(', ')}"

  pokemon_species_url = pokemon_data['species']['url']
  pokemon_species_response = Net::HTTP.get_response(URI(pokemon_species_url))

  if pokemon_species_response.code == '200'
    pokemon_species_data = JSON.parse(pokemon_species_response.body)
    evolution_chain_url = pokemon_species_data['evolution_chain']['url']
    evolution_chain_response = Net::HTTP.get_response(URI(evolution_chain_url))

    if evolution_chain_response.code == '200'
      evolution_chain_data = JSON.parse(evolution_chain_response.body)
      puts "Evolutions: #{evolution_chain_data['chain']['evolves_to'].map { |evolution| evolution['species']['name'] }.join(', ')}"
    else
      puts "Request failed, couldn't get Pokémon evolution chain"
    end
  else
    puts "Request failed, couldn't get Pokémon species"
  end
else
  puts "Request failed, Pokémon not found"
end