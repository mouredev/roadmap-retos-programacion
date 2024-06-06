/*
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:                                                                ✓
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...                     ✓
 * - Comprueba si puedes crear funciones dentro de funciones.                                   ✓
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.                              ✓
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.                                       ✓
 * - Debes hacer print por consola del resultado de todos los ejemplos.                         ✓
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */


// Declaración de función simple o "DECLARADA"
function hola() {
    console.log("Hola a toda la comunidad");
}
hola();

// Funcion "EXPRESADA"
const comida = function () {
    console.log("Salsa de chile seco");
}
comida();

// Función con return
function colores() {
    return ("Arcoiris")
}
console.log(colores());

// Funcion que recibe un solo parametro
function consolaVideo(consola) {
    console.log(`Mi consola favorita es ${consola}`);
}
consolaVideo("XBOX");

// Función que recibe más de un parametro
function edad(a, b) {
    console.log(a * b);
}
edad(6, 29);

//Funcion que recibe parametros pero con parametros por defecto
function persona(nombre = "Nombre desconocido", apellido = "Apellido desconocido", edad = 0) {
    console.log(`Mi nombre completo es ${nombre} ${apellido} y tengo ${edad} años de edad`);
}

persona("Daniel", "Martinez", 27);
persona();

//Closures o Funciones anidadas
function miFuncion() {
    let contador = 0;

    function incrementar() {
        contador++;
        return contador;
    }

    return incrementar;
}

const incremento = miFuncion();

console.log(incremento()); // 1
console.log(incremento()); // 2


//Funciones anidadas
const formula1 = function () {
    let equipo = "RedBull";

    function escuderia(equipo, motor) {
        console.log(`La escudería ${equipo} utiliza motores ${motor}`);

        function piloto(equipo, nombre, edad) {
            console.log(`La escuderia ${equipo}, cuenta con el piloto ${nombre} el cual tiene la edad de ${edad}`)
        }
        piloto(equipo, "Sergio Perez", 38);
    }
    escuderia(equipo, "mercedes");
}
formula1();

// Funciones existentes
let piloto = "Lewis Hamilton";
console.log(piloto.substring(6, undefined));
// console.log(piloto.substring(6,9));

// Variable local
let team = "Liverpool";

function futbol() {
    function ligaMx() {
        let team = "Monterrey";
        console.log(team);
    }
    ligaMx(); //imprime el valor de la variable local : Monterrey
}
futbol(); //No imprime nada en consola

// Variable Global
let escuderia = "Mclaren";

function escuderiaF1() {
    console.log(`Lando Norris corre para la escudería ${escuderia}`);
}
escuderiaF1();


// DIFUCULTAD EXRA
function numeros(palabrauno, palabrados) {
    let contador = 0;
    for (let i = 1; i <= 100; i++) {
        if (i % 3 == 0 && i % 5 == 0) {
            console.log(palabrauno + " " + palabrados);
        } else if (i % 5 == 0) {
            console.log(palabrados);
        } else if (i % 3 == 0) {
            console.log(palabrauno);
        } else {
            console.log(i);
            contador++;
        }
    }
    console.log(`Las condiciones NO se cumplieron ${contador} veces`);;
}
numeros("hola", "adios");