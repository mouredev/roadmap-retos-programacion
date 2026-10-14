/*
 * EJERCICIO:
 * Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
 * una petición a la web que tú quieras, verifica que dicha petición
 * fue exitosa y muestra por consola el contenido de la web.
*/


// Consumiendo una API
/* async function obtenerDatos() {
    try {
        const respuesta = await fetch("https://jsonplaceholder.typicode.com/posts/1")

        if(!respuesta.ok) {
            throw new Error(`Error http: ${respuesta.status}`)
        }

        const datos = await respuesta.json()
        console.log(datos)
        console.log(datos.id) // Podemos obtener el id porque es un objeto.json si fuera .txt no se podría.
    }catch(error) {
        console.error("Se ha producido un error", error.message)
    }
}
obtenerDatos() */


// Obtener el HTML de una página web

/* async function obtenerWeb() {
    try {

        const respuesta = await fetch("https://httpbin.org/html")

        if(!respuesta.ok) {
            throw new Error("La petición falló.")
        }

        const html = await respuesta.text() 
        console.log(html)
    }catch(error) {
        console.log("Ha habido un error: ", error.message)
    }
}
obtenerWeb() */

/*
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la PokéAPI (https://pokeapi.co), crea un programa por
 * terminal al que le puedas solicitar información de un Pokémon concreto
 * utilizando su nombre o número.
 * - Muestra el nombre, id, peso, altura y tipo(s) del Pokémon
 * - Muestra el nombre de su cadena de evoluciones
 * - Muestra los juegos en los que aparece
 * - Controla posibles errores
*/


const readline = require("readline/promises");
const { stdin, stdout } = require("process");
const rl = readline.createInterface({
    input: stdin,
    output: stdout
});

const BASE_URL = "https://pokeapi.co/api/v2";

// Configuración de la terminal


// Función para preguntar datos al usuario. ¡¡¡ Forma ANTIGUA antes de estar await rl.question() !!!!!
/* function preguntar(texto) {
    return new Promise(resolve => {
        rl.question(texto, respuesta => {
            resolve(respuesta);
        });
    });
} */



/*
===============================
    PETICIONES A POKÉAPI
===============================
*/

// AQUI OBTENEMOS LOS DATOS MEDIANTE LLAMADAS A LA API Y LOS TRANSFORMAMOS CON .json A OBJETO JAVASCRIPT PARA DESPUÉS PODER ACCEDER A SUS PROPIEDADES.

async function obtenerPokemon(nombreOId) {

    const response = await fetch(
        `${BASE_URL}/pokemon/${nombreOId.toLowerCase()}`
    );

    if (!response.ok) {
        throw new Error("No existe ese Pokémon.");
    }

    return response.json();
}


async function obtenerCadenaEvolutiva(url) {

    const response = await fetch(url);

    if (!response.ok) {
        throw new Error("No se pudo obtener la cadena evolutiva.");
    }

    return response.json();
}


/*
===============================
    RECURSIVIDAD PARA EVOLUCIONES
===============================
*/

// USAMOS LA RECURSIVIDAD PORQUE ESTAMOS RECORRIENDO UN ARBOL DE DATOS QUE TIENE UN NODO DENTRO DE OTRO Y 
// CON UN FOR SOLO EXAMINARÍA EL PIRMER NODO PERO NO ENTRARÍA EN EL RESTO DE NODOS ANIDADOS
// EN ESTE CASO LA RECURSIVIDAD NO ES LA HABITUAL YA QUE ES DE TIPO Preorden → hago algo con el nodo, luego visito hijos (tu código).
// EL ARRAY LLAMADO evoluciones LE PERMITE IR GUARDANDO LOS RESULTADOS AL BAJAR LA PILA Y CREAR EL CONTEXTO, EN LUGAR DE AL SUBIR LA PILA QUE ES CUANDO RESUELVE LA LÓGICA. 
// EN LUGAR DE LA TÍPICA LLAMADA: Postorden → visito hijos, luego hago algo con el nodo (el estilo que tú tenías en mente).

function obtenerEvoluciones(chain) {

    const evoluciones = [];

    function recorrer(nodo) { // La función solo esta declarada pero no hace nada hasta que no se ejecute hasta que la llamen.

        evoluciones.push(nodo.species.name);

        for (const evolucion of nodo.evolves_to) {
            recorrer(evolucion);
        }
    }

    recorrer(chain); // Esta línea es la primera lína que se ejecuta ya que es la llamada a la función .

    return evoluciones;
}


/*
===============================
    MOSTRAR INFORMACIÓN POKÉMON
===============================
*/

// AQUI ACCEDEMOS A LAS PROPIEDADES EN ESTE CASO URLS Y ESOS DATOS TAMBIÉN LOS CONVERTIMOS EN OBJETOS JAVSCRIPT MEDIANTE  .json
// PARA PODER ACCEDER A LAS PROPIEDADES DEL OBJETO: .name , .id etc.... Y ASÍ PODER MOSTRAR LOS VALORES DE ESAS PROPIEDADES.

async function mostrarPokemon(nombreOId) {

    try {

        const pokemon = await obtenerPokemon(nombreOId);


        console.log("\n===== POKÉMON =====");

        console.log(`Nombre : ${pokemon.name}`);
        console.log(`ID     : ${pokemon.id}`);

        // La API devuelve peso en hectogramos
        console.log(`Peso   : ${pokemon.weight / 10} kg`);

        // La API devuelve altura en decímetros
        console.log(`Altura : ${pokemon.height / 10} m`);

        console.log(
            `Tipos  : ${pokemon.types
                .map(tipo => tipo.type.name)
                .join(", ")}`
        );


        // Obtener especie para acceder a la cadena evolutiva
        const especie = await fetch(pokemon.species.url) // AQUÍ SE ACCEDEN A LA URL DE ESPECIOS MEDIANTE LAS PORPIEDADES DE LOS OBJETOS QUE SE HAN TRANSFORMADO DESPUÉS DE LAS LLAMADAS DE: async function obtenerPokemon(nombreOId)
            .then(res => res.json());


        const evolucion = await obtenerCadenaEvolutiva( // AQUÍ IGUAL QUE LA ANTERIOR ACCEDE AL URL DE  evolution_chain.url Y MEDIANTE obtenerEvoluciones(chain) QUE ES LA QUE LE DEVUELVE LOS DATOS DE LA LLAMADA TRANSFORMADOS EN UN OBJETO JS.
            especie.evolution_chain.url
        );


        console.log("\n===== EVOLUCIONES =====");

        console.log(
            obtenerEvoluciones(evolucion.chain) // AQUI LE PASA LOS DATOS ACCEDIDIOS MEDIANTE LA PROPIEDAD DEL OBJETO LLAMADA chain, Y SE LO PASA A LA FUNCIÓN RECURSIVA LLAMADA obtenerEvoluciones() PARA OBTENER LOS DATOS,
                .join(" -> ")  // Y CON .join(" -> ") LO CONVIERTE EN UN ARRAY FORMATEADO CON UNA FLECHA.
        );


        console.log("\n===== JUEGOS =====");

        pokemon.game_indices.forEach(juego => { // MEDIANTE LA CONSTANTE pokemon QUE CONTINE EL POQUEMON PEDIDO POR EL USER Y MEDIANTE LAS PROPIEDADES DE DICHO OBJETO, ACCEDE A LOS NOMBRES DE LOS JUEGOS EN LOS QUE APAREZCA EL NOMBRE DEL POKEMON CON UN FOREACH.
            console.log(`- ${juego.version.name}`);

        });


    } catch (error) {

        console.error("\nError:", error.message);

    }
}


/*
===============================
    MENÚ PRINCIPAL
===============================
*/

async function menu() {

    let salir = false;


    while (!salir) {


        console.log(`
========================
      POKÉAPI
========================

1. Buscar Pokémon
2. Salir

        `);


        const opcion = await rl.question(
            "Selecciona una opción: "
        );

        switch (opcion) {

            case "1":

                const nombreOId = await rl.question(
                    "\nIntroduce nombre o número del Pokémon: "
                );

                await mostrarPokemon(nombreOId);

                break;


            case "2":

                console.log(
                    "\nCerrando programa..."
                );

                salir = true;

                rl.close();

                break;

            default:

                console.log(
                    "\nOpción no válida."
                );

        }

    }

}

/*
===============================
    INICIO DEL PROGRAMA
===============================
*/

menu();
