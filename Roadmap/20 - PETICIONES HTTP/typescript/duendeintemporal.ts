// #20 PETICIONES HTPP
/*
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
 */
// I use GPT for reference information.

// Short for console.log
let log = console.log;

// Definimos una interfaz para el objeto Pokémon
interface Pokemon {
    name: string;
    id: number;
    weight: number;
    height: number;
    types: { type: { name: string } }[];
    game_indices: { version: { name: string } }[];
}

// Función para hacer una petición HTTP y obtener el contenido de una web
async function fetchContent(url: string): Promise<void> {
    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        log(data);
    } catch (error) {
        console.error('Error fetching content:', error);
    }
}

// Función para obtener texto Lorem Ipsum
async function getLoremIpsum(numberOfParagraphs: number): Promise<void> {
    try {
        const response = await fetch(`https://baconipsum.com/api/?type=meat-and-filler&paras=${numberOfParagraphs}`);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const loremIpsumTextArray = await response.json();
        updateResult(loremIpsumTextArray);
    } catch (error) {
        showError(error as Error);
    }
}

// Función para actualizar el resultado en el DOM
function updateResult(textArray: string[]): void {
    const resultElement = document.querySelector('.result') as HTMLElement;
    if (resultElement) {
        resultElement.classList.add('show');
        resultElement.style.display = '';
        resultElement.innerHTML = textArray.map(paragraph => `<p>${paragraph}</p>`).join('');
        addCopyButton(textArray.join(''));

        // Aplicar estilos a los párrafos
        const pElements = document.querySelectorAll('.result p') as NodeListOf<HTMLElement>;
        pElements.forEach(p => {
            p.style.color = '#fff';
            p.style.lineHeight = '16px';
            p.style.textAlign = 'justify';
        });
    }
}

// Función para mostrar errores
function showError(error: Error): void {
    const resultElement = document.querySelector('.result');
    if (resultElement) {
        resultElement.innerHTML = `<p class="error">${error.message}</p>`;
    }
}

// Función para añadir un botón de copiar
function addCopyButton(text: string): void {
    const resultElement = document.querySelector('.result');
    if (resultElement) {
        const copyBtn = document.createElement('button');
        copyBtn.textContent = 'Copy';
        copyBtn.classList.add('copy');
        copyBtn.onclick = () => {
            navigator.clipboard.writeText(text).then(() => {
                copyBtn.textContent = 'Copied!';
                setTimeout(() => {
                    copyBtn.textContent = 'Copy';
                }, 2000);
            });
        };
        resultElement.appendChild(copyBtn);
    }
}

// Función para obtener información de un Pokémon
async function getPokemon(id: string): Promise<void> {
    try {
        const response = await fetch(`https://pokeapi.co/api/v2/pokemon/${id}`);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data: Pokemon = await response.json();

        type PokemonInfo = {
            name: string;
            id: string;
            weight: string;
            height: string;
            type: string;
            games: string;
        };

        const pokemon: PokemonInfo = {
            name: `Name: ${data.name}`,
            id: `Id: ${data.id}`,
            weight: `Weight: ${data.weight}`,
            height: `Height: ${data.height}`,
            type: `Type: ${data.types.map(t => t.type.name).join(', ')}`,
            games: `Games: ${data.game_indices.map(g => g.version.name).join(', ')}`,
        };

        log(pokemon);

        if (typeof window !== 'undefined') {
            const modal1 = document.createElement('div');
            modal1.style.position = 'relative';
            modal1.style.top = '50%';
            modal1.style.color = '#fff';
            modal1.style.left = '50%';
            modal1.style.transform = 'translate(-50%, -72%)';
            modal1.style.background = 'rgba(0,0,0,0.9)';
            modal1.style.width = '100vw';
            modal1.style.height = '100vh';
            modal1.style.display = 'flex';
            modal1.style.justifyContent = 'center';
            modal1.style.alignItems = 'center';

            const modal2 = document.createElement('div');
            modal2.style.width = '80vw';
            modal2.style.height = '100vh';
            modal2.style.display = 'flex';
            modal2.style.justifyContent = 'space-around';
            modal2.style.alignItems = 'flex-start';
            modal2.style.flexDirection = 'column';

            const h1 = document.createElement('h1');
            h1.textContent = `POKEMON`;
            h1.style.alignSelf = 'center';
            h1.style.fontFamily = 'cursive';
            modal2.appendChild(h1);
            modal1.appendChild(modal2);
            document.body.appendChild(modal1);

            for (let key in pokemon) {
                if (pokemon.hasOwnProperty(key)) {
                    let p = document.createElement('p');
                    p.textContent = pokemon[key as keyof PokemonInfo]; // Type assertion aquí
                    p.style.color = 'yellow';
                    p.style.fontSize = '2vw';
                    p.style.fontWeight = '600';
                    p.style.fontFamily = 'cursive';
                    p.style.textAlign = 'justify';
                    modal2.appendChild(p);
                }
            }

            // Función para eliminar el modal
            const removeModal = () => {
                modal1.remove();
                document.removeEventListener('keydown', handleKeyDown);
            };

            // Añadir event listener para eliminar el modal al hacer clic
            modal2.addEventListener('click', removeModal);

            // Función para manejar eventos de teclado
            const handleKeyDown = (event: KeyboardEvent) => {
                if (event.key === "Escape") {
                    removeModal();
                }
            };

            // Añadir event listener para eventos de teclado
            document.addEventListener('keydown', handleKeyDown);
        }
    } catch (error) {
        console.error('Error fetching Pokémon:', error);
    }
}

// Verificamos si estamos en un entorno de navegador
if (typeof window !== 'undefined') {
    window.addEventListener('load', () => {
        const body = document.querySelector('body');
        const title = document.createElement('h1');

        body?.style.setProperty('background', '#000');
        body?.style.setProperty('text-align', 'center');

        title.textContent = 'Retosparaprogramadores #20.';
        title.style.setProperty('font-size', '3.5vmax');
        title.style.setProperty('color', '#fff');
        title.style.setProperty('line-height', '34vh');

        body?.appendChild(title);
        log('Retosparaprogramadores #20');

        // Crear modal para Lorem Ipsum
        const modal = document.createElement('div');
        modal.style.position = 'relative';
        modal.style.top = '50%';
        modal.style.left = '50%';
        modal.style.transform = 'translate(-50%, -20%)';
        modal.style.background = 'rgba(0,0,0,0.2)';
        modal.style.width = '400px';
        modal.style.minHeight = '200px';
        document.body.appendChild(modal);

        const loremIpsumContainer = document.createElement('div');
        loremIpsumContainer.style.fontFamily = 'sans-serif';
        loremIpsumContainer.style.margin = '1rem';
        modal.appendChild(loremIpsumContainer);

        const label = document.createElement('label');
        label.style.padding = '10px';
        label.style.color = '#fff';
        label.setAttribute('for', 'paragraphsCount');
        const strong = document.createElement('strong');
        strong.textContent = 'How many Paragraphs?';
        loremIpsumContainer.appendChild(label);
        label.appendChild(strong);

        const input = document.createElement('input');
        input.setAttribute('type', 'number');
        input.style.width = '4rem';
        input.setAttribute('min', '0');
        input.classList.add('paragraphsCount');
        loremIpsumContainer.appendChild(input);

        const button = document.createElement('button');
        button.style.background = '#ff8c00';
        button.style.color = '#f6f6f6';
        button.style.padding = '5px';
        button.style.borderRadius = '15px';
        button.style.textAlign = 'center';
        button.style.marginLeft = '10px';
        button.textContent = 'Generate';
        button.classList.add('getLoremIpsum');
        loremIpsumContainer.appendChild(button);

        const result = document.createElement('div');
        result.style.marginTop = '1rem';
        result.style.padding = '1rem';
        result.style.border = '1px dashed black';
        result.style.fontSize = '.75rem';
        result.style.position = 'absolute';
        result.style.left = '-25%';
        result.style.width = '58vw';
        result.style.display = 'none';
        result.classList.add('result');
        loremIpsumContainer.appendChild(result);

        // Añadir event listener para el botón de generar Lorem Ipsum
        setTimeout(() => {
            const getLoremIpsumElement = document.querySelector('.getLoremIpsum');
            const paragraphsCountElement = document.querySelector('.paragraphsCount') as HTMLInputElement;

            getLoremIpsumElement?.addEventListener('click', () => {
                const numberOfParagraphs = parseInt(paragraphsCountElement.value);
                if (!isNaN(numberOfParagraphs)) {
                    getLoremIpsum(numberOfParagraphs);
                    paragraphsCountElement.value = '';
                }
            });
        }, 1000);

        // Solicitar información de un Pokémon después de 2 segundos
        setTimeout(() => {
            const id = prompt('Please type a number id to get the pokemon data');
            if (id) {
                getPokemon(id);
            }
        }, 2000);
    });
} else {
    log('This code is designed to run in a browser environment. Skipping window-related code.');
    log('Retosparaprogramadores #20');
}