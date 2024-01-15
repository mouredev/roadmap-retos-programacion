/*
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
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



// FUNCIONES SIN PARAMETROS NI RETORNO
function Saludo() {
    console.log("Hola Usuario"); //Hola Usuario
}

console.log(Saludo()) //undefined
//las funciones que no tienen retorno regresan el valor "undefined"

// FUNCIONES CON PARAMETROS Y RETORNO 
function SaludarUsuario(nombre) {
    return 'Hola @'+ nombre
}

// CON VARIOS PARAMETROS
function EsMayorDeEdad(nombre, edad) {
    let mensaje = ''
    edad >= 18 ? mensaje = 'sos mayor de edad' : mensaje='no sos mayor de edad'
    return 'Hola @'+ nombre + ' tenes ' + edad + ', ' + mensaje
}
console.log(EsMayorDeEdad('Carlos',16))

// para llamar a esta funcion debemos pasarle el argumento 
console.log(SaludarUsuario("asaelz")) //Hola @asaelz

// FUNCTION EXPRESSION --> una funcion es asignada a una variable 
const suma = function (n1, n2) {
    return n1 + n2;
}

console.log(suma(55,1)) //56

//ARROW FUNCTION
//PARA EJEMPLIFICAR LAS ARROW FUNCTION UTILIZAREMOS NUESTRA FUNCION SALUDAR USUARIO 
const SaludarUsuario2 = (usuario) => 'Hola @' +usuario
console.log(SaludarUsuario2('asaelz')) //Hola @asaelz
/**
 * Como podemos observar tenemos el mismo resultado que una funcion regular, pero mas facil de entender 
 * una arrow function siempre es anonima (o sea que la funcion no tiene nombre) y es una function expression
 * en el caso del return como podemos ver lo tiene implicito, pero no pasaria nada si lo agregamos: 
 */
const SaludarUsuario3 = (usuario) => { return 'Hola @' +usuario}
console.log(SaludarUsuario3('asaelz')) //Hola @asaelz

/**
 * RECURSIVIDAD --> SE DA CUANDO UNA FUNCION SE LLAMA ASI MISMA, 
 * COMO UNA MANERA DE SIMULAR UN BUCLE, EJEMPLO: 
 */

for (let index = 0; index < 3; index++) {
    console.log('En ' +(index + 1))
    
}
// ahora vamos a ver como simular este ciclo con recursividad 
function conteo(num) {
    if (num==3) { return }
    console.log('En '+ (num + 1))
    conteo(num + 1)
}
// EN AMBOS CASOS OBTENEMOS EL MISMO RESULTADO 

/**
 * Ejemplos de funciones existentes en lenguaje 
 */

console.log('se utiliza para imprimir en consola');
console.log(Math.floor(3.65)) // 3 --> redondea un numero
console.log('       HOLA     '.trim()) //Hola --> remueve los espacios en blanco al inicio y final de un string

/**
 * FUNCIONES DENTRO DE FUNCIONES
 */
function suma1(a,b) {
    function validacion(a,b) {
        if (typeof(a)!= 'number' || typeof(b)!= 'number') {
            return 'Debe insertar solo numeros'
        } 
        else {
            return true
        }
    }
    return validacion(a,b)==true ? a + b : validacion(a,b)
}

console.log(suma1('a',1)) //Debe insertar solo numeros

/**
 * VARIABLES LOCALES Y GLOBALES 
 * Las variables globales son las que se definen fuera de cualquier funcion
 * por tanto podemos acceder a ellas dentro y fuera de las mismas, mientras las locales solo funcionan dentro
 */

let user = 'asaelz' // variable global
function cambiarUsuario(NuevoUsuario) {
    let OldUser = user //variable local
    user = '@'+NuevoUsuario
    return 'Su usuario @' +OldUser + ' fue cambiado a '+ user
}

console.log(cambiarUsuario('yanci'))

/**
 *  * DIFICULTAD EXTRA (opcional):
 */

function Prints(text1, text2) {
    let contador = 0;
    for (let num = 1; num <= 100; num++) {
        if (num%3==0 && num%5!= 0){
            console.log(text1)
        }else if(num%5==0 && num%3!= 0)  {
            console.log(text2)
        } else if (num%3==0 && num%5==0) {
            console.log(text1 + ' ' + text2)
        } else contador +=1
    }
    return 'Se han impreso ' +contador +' números.'
}

console.log(Prints('Brais','Moure'))