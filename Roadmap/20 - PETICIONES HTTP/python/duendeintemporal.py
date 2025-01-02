#20 { Retos para Programadores } PETICIONES HTTP

# Bibliography reference
# PokéAPI (https://pokeapi.co)
# Additionally, I use GPT as a reference and sometimes to correct or generate proper comments.

"""  
 * EJERCICIO:
 * Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
 * una petición a la web que tú quieras, verifica que dicha petición
 * fue exitosa y muestra por consola el contenido de la web.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la PokéAPI (https://pokeapi.co), crea un programa por
 * terminal al que le puedas solicitar información de un Pokémon concreto
 * utilizando su nombre o número.
 * - Muestra el nombre, id, peso, altura y tipo(s) del Pokémon
 * - Muestra el nombre de su cadena de evoluciones
 * - Muestra los juegos en los que aparece
 * - Controla posibles errores

"""

import requests
import time

# Function to simulate console.log
def log(*args):
    print(*args)

# Simulating the window load event
def on_load():
    log('Retosparaprogramadores #20')

    # Simulating the modal creation
    modal = {
        'title': 'How many Paragraphs?',
        'input': 0,
        'result': '',
    }

    # Simulating user input for paragraphs count
    modal['input'] = int(input("Enter number of paragraphs: "))
    get_lorem_ipsum(modal['input'])
    log()

# Function to get Lorem Ipsum text
def get_lorem_ipsum(number_of_paragraphs):
    try:
        response = requests.get(f'https://baconipsum.com/api/?type=meat-and-filler&paras={number_of_paragraphs}')
        response.raise_for_status()
        lorem_ipsum_text_array = response.json()
        update_result(lorem_ipsum_text_array)
    except Exception as error:
        show_error(error)

# Function to update the result
def update_result(text_array):
    result = '\n'.join(f'<p>{paragraph}</p>' for paragraph in text_array)
    log(result)
    log()
    add_copy_button('\n'.join(text_array))

# Function to show error
def show_error(error):
    log(f'Error: {error}')

# Function to add a copy button (simulated)
def add_copy_button(text):
    log('Copy button created. Text to copy:', text)
    log()

# Extra Difficulty Exercise
def get_pokemon(id):
    try:
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{id}')
        response.raise_for_status()
        data = response.json()
        pokemon = {
            'name': f'Name: {data["name"]}',
            'id': f'Id: {data["id"]}',
            'weight': f'Weight: {data["weight"]}',
            'height': f'Height: {data["height"]}',
            'type': f'Type: {", ".join(t["type"]["name"] for t in data["types"])}',
            'games': f'Games: {", ".join(g["version"]["name"] for g in data["game_indices"])}',
        }
        log(pokemon)
        log()

        # Simulating modal display for Pokémon data
        display_pokemon_modal(pokemon)
    except Exception as error:
        log('Error fetching Pokémon:', error)

# Function to display Pokémon modal (simulated)
def display_pokemon_modal(pokemon):
    log('Displaying Pokémon Modal:')
    for key, value in pokemon.items():
        log(value)

# Main execution
if __name__ == "__main__":
    on_load()
    time.sleep(2)  # Simulating delay for user input
    pokemon_id = input('Please type a number id to get the Pokémon data: ')
    get_pokemon(pokemon_id)

# Output Example:
"""  
Retosparaprogramadores #20
Enter number of paragraphs: 4
<p>Short ribs dolore incididunt dolore, ground round burgdoggen ut buffalo.  Shankle tempor ham hock ut ground round ad dolore esse.  Biltong shank sausage laborum dolore dolore landjaeger nisi.  Tenderloin reprehenderit jerky andouille tempor anim alcatra.</p>
<p>Proident consequat venison, cupidatat cow pancetta ipsum occaecat irure sirloin shank lorem aute.  Eiusmod rump velit, jowl cupidatat mollit short loin culpa ut.  Picanha t-bone id est chislic.  Ut chislic sint, minim filet mignon turkey turducken excepteur consectetur occaecat beef venison est non shoulder.  Qui aute ribeye cupidatat, jerky dolore proident mollit pork chop tri-tip.  Ground round enim short loin veniam magna picanha strip steak, elit ribeye.</p>
<p>Labore bacon frankfurter alcatra, minim ribeye cow non culpa id.  Pork loin lorem in, do commodo tempor rump in tri-tip tail ex shoulder.  Do tempor qui exercitation voluptate shankle capicola aute hamburger beef dolor.  Pork belly labore ex, alcatra andouille commodo ribeye leberkas reprehenderit shank ut do in jowl fatback.  Meatloaf ribeye deserunt, meatball ut irure id short ribs ea swine commodo tempor exercitation.  Tempor short loin t-bone ut tail chicken commodo shankle beef dolor.</p>
<p>Prosciutto cupim ham aliqua proident, rump veniam duis minim.  Mollit jerky ut, pork labore voluptate t-bone salami pastrami id et pork chop ea tempor.  In meatball flank lorem non buffalo.  Shankle velit bresaola corned beef shoulder frankfurter.  Quis andouille aliqua biltong meatball cow ex in nostrud chuck ham tail tenderloin tempor.  T-bone short ribs consectetur bresaola enim laborum short loin sirloin et consequat occaecat shank minim sausage capicola.  Meatloaf capicola do enim, occaecat salami nostrud in incididunt id aliqua jowl deserunt sausage.</p>

Copy button created. Text to copy: Short ribs dolore incididunt dolore, ground round burgdoggen ut buffalo.  Shankle tempor ham hock ut ground round ad dolore esse.  Biltong shank sausage laborum dolore dolore landjaeger nisi.  Tenderloin reprehenderit jerky andouille tempor anim alcatra.
Proident consequat venison, cupidatat cow pancetta ipsum occaecat irure sirloin shank lorem aute.  Eiusmod rump velit, jowl cupidatat mollit short loin culpa ut.  Picanha t-bone id est chislic.  Ut chislic sint, minim filet mignon turkey turducken excepteur consectetur occaecat beef venison est non shoulder.  Qui aute ribeye cupidatat, jerky dolore proident mollit pork chop tri-tip.  Ground round enim short loin veniam magna picanha strip steak, elit ribeye.
Labore bacon frankfurter alcatra, minim ribeye cow non culpa id.  Pork loin lorem in, do commodo tempor rump in tri-tip tail ex shoulder.  Do tempor qui exercitation voluptate shankle capicola aute hamburger beef dolor.  Pork belly labore ex, alcatra andouille commodo ribeye leberkas reprehenderit shank ut do in jowl fatback.  Meatloaf ribeye deserunt, meatball ut irure id short ribs ea swine commodo tempor exercitation.  Tempor short loin t-bone ut tail chicken commodo shankle beef dolor.
Prosciutto cupim ham aliqua proident, rump veniam duis minim.  Mollit jerky ut, pork labore voluptate t-bone salami pastrami id et pork chop ea tempor.  In meatball flank lorem non buffalo.  Shankle velit bresaola corned beef shoulder frankfurter.  Quis andouille aliqua biltong meatball cow ex in nostrud chuck ham tail tenderloin tempor.  T-bone short ribs consectetur bresaola enim laborum short loin sirloin et consequat occaecat shank minim sausage capicola.  Meatloaf capicola do enim, occaecat salami nostrud in incididunt id aliqua jowl deserunt sausage.

Please type a number id to get the Pokémon data: 32
{'name': 'Name: nidoran-m', 'id': 'Id: 32', 'weight': 'Weight: 90', 'height': 'Height: 5', 'type': 'Type: poison', 'games': 'Games: red, blue, yellow, gold, silver, crystal, ruby, sapphire, emerald, firered, leafgreen, diamond, pearl, platinum, heartgold, soulsilver, black, white, black-2, white-2'}

Displaying Pokémon Modal:
Name: nidoran-m
Id: 32
Weight: 90
Height: 5
Type: poison
Games: red, blue, yellow, gold, silver, crystal, ruby, sapphire, emerald, firered, leafgreen, diamond, pearl, platinum, heartgold, soulsilver, black, white, black-2, white-2

"""