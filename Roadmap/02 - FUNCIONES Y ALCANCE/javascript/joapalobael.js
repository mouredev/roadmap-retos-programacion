//---------------------------------------- > 
function funcion_simple() {
    let varLocal = "función simple"
    console.log(`Esto es una ${varLocal} y sin parámetro utilizando una variable local`);
}
funcion_simple();
//---------------------------------------->
function funcion_simpleParametro(a, b) {
    return a + b;
}
console.log(`Esto es una función simple, con parámetro y retorno: ${funcion_simpleParametro(3, 4)}.`);
//---------------------------------------->
let funcion_flecha = () => console.log("Esto es una función flecha simple");
funcion_flecha();
//---------------------------------------->
let funcion_flechaParametro = (cant) => console.log(`Esto es una función flecha con parámetro: ${cant}.`)
funcion_flechaParametro(3);
//---------------------------------------->
const nombreCriatura = "Roberto"
function vivir() {
    let llamar = () => console.log(`Hola, me llamo ${nombreCriatura} y soy una función dentro de una función con variable global.`)
    let respirar = () => console.log("Respiro");
    let alimentar = () => console.log("Me alimento");
    let morir = () => console.log("Muero")
    return llamar(), respirar(), alimentar(), morir();
}
vivir();
//---------------------------------------->
console.log("Soy una función propia del lenguaje // Built-in")
console.log(("Soy la función lenght // Built-in").length);
//---------------------------------------->
// ABSTRACCIÓN EJERCICIO EXTRA
/* Inicio
        Crear una función ejercicioExtra que reciba 2 parámetros (a,b) {
            setear contador en 0
            Crear un bucle contador que vaya del 1 al 100 teniendo en cuenta que{
                SI (el número es multiplo de 3 Y de 5){
                muestre el texto a concatenado con el b}
                SI (el número del contador es multiplo de 3) {
                muestre el parametro a}
                SI (el número del contador es multiplo de 5) {
                muestre el parametro b}
                ELSE {
                Mostrar por consola el index
                Incrementar el contador
                }
            }
        Retornar el contador
        }

        Mostrar por consola el retorno de la función => console.log(ejercicioExtra(fizz, buzz));
Fin */

function ejercicioExtra(a, b) {
    let counter = 0;
    for (let i = 1; i <= 100; i++) {
        if (i % 3 === 0 && i % 5 === 0) {
            console.log(`${a} ${b}`)
        } else if (i % 3 === 0) {
            console.log(a)
        } else if (i % 5 === 0) {
            console.log(b)
        } else {
            console.log(i);
            counter++;
        }
    }
    console.log(`Se mostraron números ${counter} veces`);
    // Si no pongo retorno, da indefinida la función
    return counter;
}
ejercicioExtra('Fizz', 'Buzz');