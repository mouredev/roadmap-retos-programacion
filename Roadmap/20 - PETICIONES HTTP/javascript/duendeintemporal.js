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

let log = console.log;

window.addEventListener('load', ()=>{
    const body = document.querySelector('body');
    const title = document.createElement('h1');
    
    body.style.setProperty('background', '#000');
    body.style.setProperty('text-align', 'center');
    
    title.textContent = 'Retosparaprogramadores #20.';
    title.style.setProperty('font-size', '3.5vmax');
    title.style.setProperty('color', '#fff');
    title.style.setProperty('line-height', '34vh');
    
    body.appendChild(title);
    log( 'Retosparaprogramadores #20'); 

    /* LoremIpsum Paragraph Maker Visual Modal */

    let modal = document.createElement('div');
    modal.style.setProperty('position', 'relative');
    modal.style.setProperty('top', '50%');
    modal.style.setProperty('left', '50%');
    modal.style.setProperty('transform', 'translate(-50%, -20%)');
    modal.style.setProperty('background', 'rgba(0,0,0,0.2)');
    modal.style.setProperty('width', '400px');
    modal.style.setProperty('min-height', '200px');
    // modal.style.setProperty('display', 'none');
    document.body.appendChild(modal);
    
    let loremIpsumContainer = document.createElement('div');
    loremIpsumContainer.style.setProperty('font-family', 'sans-serif');
    loremIpsumContainer.style.setProperty('margin', '1rem');
    modal.appendChild(loremIpsumContainer);

    let label = document.createElement('label');
    label.style.setProperty('padding', '10px');
    label.style.setProperty('color', '#fff');
    label.setAttribute('for', 'paragraphsCount');
    let strong = document.createElement('strong');
    strong.textContent = 'How many Paragraphs?';
    loremIpsumContainer.appendChild(label);
    label.appendChild(strong);
    
    let input = document.createElement('input');
    input.setAttribute('type', 'number')
    input.style.setProperty('width', '4rem');
    input.setAttribute('min', '0');
    input.classList.add('paragraphsCount');
    loremIpsumContainer.appendChild(input);

    let button = document.createElement('button');
    button.style.setProperty('background', '#ff8c00');
    button.style.setProperty('color', '#f6f6f6');
    button.style.setProperty('padding', '5px');
    button.style.setProperty('border-radius', '15px');
    button.style.setProperty('text-align', 'center');
    button.style.setProperty('margin-left', '10px');
    button.textContent = 'Generate';
    button.classList.add('getLoremIpsum');
    loremIpsumContainer.appendChild(button);

    let result = document.createElement('div');
    result.style.setProperty('margin-top', '1rem')
    result.style.setProperty('padding', '1rem');
    result.style.setProperty('border', '1px dashed black');
    result.style.setProperty('font-size', '.75rem');
    result.style.setProperty('position', 'absolute');
    result.style.setProperty('left', '-25%');
    result.style.setProperty('width', '58vw');
    result.style.setProperty('display', 'none');
    result.classList.add('result');
    loremIpsumContainer.appendChild(result);
});


/* LoremIpsum Paragraph Maker Funcionality */

function getLoremIpsum(numberOfParagraphs){
    fetch(`https://baconipsum.com/api/?type=meat-and-filler&paras=${numberOfParagraphs}`)
        .then(response => response.json())
        .then(loremIpsumTextArray => {
            updateResult(loremIpsumTextArray);
        })
        .catch(error => {
            showError(error);
        });
};

function updateResult(textArray) {
    const resultElement = document.querySelector('.result');
    resultElement.classList.add('show');
    resultElement.style.setProperty('display', '');
    resultElement.innerHTML = '';
    resultElement.innerHTML = textArray
        .map(paragraph => `<p>${paragraph}</p>`)
        .join('');
    addCopyButton(textArray.join(''));

    // Apply styles to the paragraphs immediately
    const p_elements = document.querySelectorAll('.result p');
    p_elements.forEach(p => {
        p.style.setProperty('color', '#fff');
        p.style.setProperty('line-height', '16px');
        p.style.setProperty('text-align', 'justify');
    });
}

function showError(error){
     const resultElement = document.querySelector('.result');
    resultElement.innerHTML = '';
    resultElement.innerHTML = `<p class="error">${error.message}</p>`
}

function addCopyButton(text){
    const resultElement = document.querySelector('.result');
    const copyBtn = document.createElement('button');

    copyBtn.textContent = 'Copy';
    copyBtn.classList.add('copy');
    copyBtn.onclick = () => {
        navigator.clipboard.writeText(text);
        copyBtn.textContent = 'Copied!';
        setTimeout(() => {
            copyBtn.textContent = 'Copy';
        }, 2000);
    }

    resultElement.appendChild(copyBtn);

    setTimeout(()=> getPokemon(id = prompt('Please type a number id to get the pokemon data')), 2000)
}

setTimeout(()=>{
    const getLoremIpsumElement = document.querySelector('.getLoremIpsum');
    const paragraphsCountElement = document.querySelector('.paragraphsCount');

    getLoremIpsumElement.addEventListener('click', () => {
        getLoremIpsum(parseInt(paragraphsCountElement.value));
        paragraphsCountElement.value = '';

    })
}, 1000);
    

// Extra Dificulty Exercise

let pokemon;
function getPokemon(id){
    fetch(`https://pokeapi.co/api/v2/pokemon/${id}`)
    .then((response)=> response.json())
    .then((data)=> {
        log(data);
      ;
        pokemon = {
				name: `Name: ${data.name}`,
				id: `Id: ${data.id}`,
				weight: `Weight: ${data.weight}`,
				height: `Height: ${data.height}`,
				type: `Type: ${data.types.map(t => t.type.name).join(', ')}`,
				games: `Games: ${data.game_indices.map(g => g.version.name).join(', ')}`,
        }
        log(pokemon);

        let modal1 = document.createElement('div');
        modal1.style.setProperty('position', 'relative');
        modal1.style.setProperty('top', '50%');
        modal1.style.setProperty('color', '#fff');
        modal1.style.setProperty('left', '50%');
        modal1.style.setProperty('transform', 'translate(-50%, -72%)');
        modal1.style.setProperty('background', 'rgba(0,0,0,0.9)');
        modal1.style.setProperty('width', '100vw');
        modal1.style.setProperty('height', '100vh');
        modal1.style.setProperty('display', 'flex');
        modal1.style.setProperty('justify-content', 'center');
        modal1.style.setProperty('align-items', 'center');
        let modal2 = document.createElement('div');
        modal2.style.setProperty('width', '80vw');
        modal2.style.setProperty('height', '100vh');
        modal2.style.setProperty('display', 'flex');
        modal2.style.setProperty('justify-content', 'space-arround');
        modal2.style.setProperty('align-items', 'flex-start');
        modal2.style.setProperty('flex-direction', 'column');
        let h1 = document.createElement('h1');
            h1.textContent = `POKEMON`;
            h1.style.setProperty('align-self', 'center');
            h1.style.setProperty('font-family', 'cursive');
            modal2.appendChild(h1);
            modal1.appendChild(modal2);
        document.body.appendChild(modal1);

        for(let key in pokemon){
            let p = document.createElement('p');
            p.textContent = `${pokemon[key]}`;
            p.style.setProperty('color', 'yellow');
            p.style.setProperty('font-size', '2vw');
            p.style.setProperty('font-weight', '600');
            p.style.setProperty('font-family', 'cursive');
            p.style.setProperty('text-align', 'justify');
            modal2.appendChild(p);
        }

                // Function to remove the modal
                const removeModal = () => {
                    modal1.remove(); 
                    document.removeEventListener('keydown', handleKeyDown); // Clean up the event listener
                };
        
                // Add event listener to remove the modal when clicked
                modal2.addEventListener('click', removeModal);
        
                // Function to handle keydown events
                const handleKeyDown = (event) => {
                    if (event.key === "Escape") { // Check if the pressed key is "Escape"
                        removeModal(); // Call the function to remove the modal
                    }
                };
        
                // Add event listener for keydown events
                document.addEventListener('keydown', handleKeyDown);
            })
            .catch((error) => console.error('Error fetching Pokémon:', error));
        }
        
//Note: is easy use a external css file an just add classes rather than adding prperty by property.
/* By using CSS classes, your JavaScript code becomes cleaner and easier to manage, while your styles are centralized in a dedicated CSS file. This approach is generally recommended for larger projects or when working in teams. */