/* Tipos de operadores logicos */

// Valores iniciales
let dato1 = 15;
let dato2 = 30
//Operadores

let asg = dato1;

/*Problemas para Practicar Operadores de Asignación */

console.log(`**********Actualiza el precio de un producto aplicando impuestos dinámicos**********\n\n1- Tienes un producto con un precio base. El porcentaje de impuesto puede variar según la región.\nUsa el operador correcto para actualizar el precio del producto tras aplicar el impuesto.\n\nImpuesto: 19%\nPrecio de producto: $80.000\n`)
//datos de entrada
let precioProducto = 80000;
const impuestoRegion = 0.19; 

let precioTotal = precioProducto *= (1 + impuestoRegion);

console.log(`EL precio total del producto, incluyendo el impuesto es de $${precioTotal.toFixed(2)}\n\n`)


console.log(`**********Reduce el tiempo restante en un temporizador**********\n\n 2-Estás desarrollando una app de productividad.\n Tienes un temporizador que empieza en cierto número de minutos.\n Cada ciclo reduce el tiempo en 5 minutos.\n`)
let tiempoRestante = 30; // minutos
const duracionCiclo = 5; // minutos

tiempoRestante -= duracionCiclo

console.log(`El temporizador, tras el ciclo queda en ${tiempoRestante} minutos\n\n`)

console.log(`**********Escala un puntaje entre 0 y 100 a una escala de 0 a 10**********\n\n3-Un sistema devuelve puntajes del 0 al 100, pero necesitas convertirlos a una escala del 0 al 10 para mostrarlos en una interfaz amigable.\n`)
let puntajeOriginal = 75;
let puntajeConvertido = puntajeOriginal /= 10
console.log(`EL puntaje convertido es de ${puntajeConvertido}\n\n`)

console.log(`**********Convierte segundos totales en minutos**********\n\n4-Tienes una variable con la cantidad total de segundos transcurridos y necesitas convertirla a minutos.\n`)
let segundosTotales = 360;
let minutosTotales = segundosTotales /= 60

console.log(`Los ${segundosTotales} segundos son equivalentes a ${minutosTotales} minutos\n\n`)

console.log(`**********Alterna entre modos claro y oscuro usando XOR bit a bit**********\n\n5-En una aplicación de configuración, tienes una bandera (modoOscuro) que indica si está activado el modo oscuro.\n Usa el operador adecuado para alternar su valor entre true y false.\n`)
let modoOscuro = true;
modoOscuro ^= true 
console.log(`¿El modo oscuro esta activado?: ${modoOscuro}\n\n`)

console.log(`**********Calcula el crecimiento exponencial de usuarios**********\n\n6-Una startup tiene 1000 usuarios iniciales y experimenta un crecimiento del 20% mensual. Usa el operador correcto para calcular cuántos usuarios tendrán después de 6 meses.\n`)
let usuarios = 1000;
const tasaCrecimiento = 1.2;
const meses = 6
let usuariosFinales = usuarios *= Math.pow(tasaCrecimiento, meses);

console.log(`Los usuarios obtenidos despues de haber transcurrido 6 meses, la cifra es de ${usuariosFinales} usuarios\n`)


console.log(`**********Establece una configuración predeterminada solo si no está definida**********\n\n7-Tienes una variable que puede venir desde una API o no estar definida. Usa el operador lógico correcto para establecer un valor por defecto solo si es necesario.\n`)
let idiomaUsuario = undefined;
idiomaUsuario ??= 'Español'
console.log(`El idioma del usuario es: ${idiomaUsuario}\n`)

console.log(`**********Filtra permisos de usuario usando AND bit a bit**********\n\n8-Tienes un sistema de roles basado en máscaras de bits. Usa el operador correcto para verificar si el usuario tiene permiso de administrador.`)
const PERMISO_ADMIN = 4; // 100 en binario
let permisosUsuario = 5; // 101 en binario
let tienePermisoAdmin = (permisosUsuario & PERMISO_ADMIN) !== 0;
console.log(`¿El usuario cuenta con permiso de administrador?: ${permisosUsuario ? 'si' : 'no'}\n`)

console.log(`Combina colores RGB usando OR bit a bit**********\n\n9-Tienes tres variables que representan componentes de color rojo, verde y azul. Usa el operador correcto para combinarlos en un único valor entero que represente el color completo.`)
let rojo = 255 << 16;
let verde = 128 << 8;
let azul = 0;
let combinacion = rojo | verde | azul;
console.log(`El color representativo es: ${combinacion} \n`)

//Aritmeticos
const numero1=10
const numero2=55


console.log(`**********OPERADORES ARITMETICOS**********\n\n`)
let suma=numero1+numero2
console.log(`La suma de 10 + 55 = ${suma} `)
let resta=numero1-numero2
console.log(`La resta de 10 - 55 = ${resta}`)
let multiplicacion=numero1*numero2
console.log(`La multiplicacion de 10 * 55 =${multiplicacion}`)
let division=numero2/numero1
let modulo=numero2%numero1
console.log(`La division de 55 / 10 = ${division}\n y el residuo de esta division es: ${modulo}`)
let elevacion=numero1**numero2
console.log(`Eleva el numero 10 a 55 = ${elevacion}`)



console.log(`**********ESTRUCTURAS DE CONTROL**********\n\n`)

console.log(`1-Escribe un programa que determine si una persona puede votar. Para votar, debe ser mayor de edad (18 años o más) y estar registrada.`)
let edad = 20;
let registrada = true;
if (edad >= 18){
    console.log("Estas habilitado para votar, ya que cumples con la mayoria de edad")
}else{
    console.log("No puedes votar, no eres mayor de 18 años")
}

console.log(`Dado un puntaje entre 0 y 100, imprime la calificación equivalente:\n
90-100 → A\n
80-89 → B\n
70-79 → C\n
60-69 → D\n
Menos de 60 → F`)
let puntaje = "85";
if (puntaje >= 90 && puntaje <= 100){
    console.log("El resultado de la calificacion es: A")
}else if (puntaje >= 80 && puntaje <= 89){
    console.log("El resultado de la calificacion es: B")
}else if (puntaje >= 70 && puntaje <= 79){
    console.log("El resultado de la calificacion es: C")
}else if(puntaje >= 60 && puntaje <= 69){
    console.log("El resultado de la calificacion es: D")
}else if(puntaje <= 59 ){
    console.log("El resultado de la calificacion es: F")
}else{
    console.log("El puntaje a evaluar es invalido; No se encuentra entre el rango de 0 a 100")
}


console.log(`\n\nCrea un sistema que, dado un día de la semana (como número), muestre su nombre en español.`)

let dia = 3;
switch (dia) {
    case 1 :
        console.log("Lunes")
    break
    case 2 :
        console.log("Martes")
        break
    case 3 :
        console.log("Miercoles")
        break
    case 4 :
        console.log("Jueves")
        break
    case 5 :
        console.log("Viernes")
        break
    case 6 :
        console.log("Sabado")
        break
    case 7 :
        console.log("Domingo")
        break
    default:
        console.log("La opcion selecionada no es valida")
        break
}

console.log(`\n\nImprime los primeros 10 números dependiendo si se ingresa la palabra Par o Impar`)
let condicion="par"
if (condicion == "par"){
    for (let num = 0; num < 10; num += 2){
        console.log(`Los numeros son: ${num}`)
    }
}else{
    for (let num = 1; num < 10; num += 2 ){
        console.log(`los numeros son: ${num}`)
    }
}

console.log(`\n\nSimula un cajero automático que pregunta por una contraseña hasta que sea correcta (usa while para repetir)`)

import { access } from 'fs';
// Importar módulo readline
import { createInterface } from 'readline';

// Crear interfaz para entrada/salida
const rl = createInterface({
  input: process.stdin,
  output: process.stdout
});

const claveCorrecta = "1234";

function pedirClave() {
  rl.question("Ingrese su contraseña: ", (intento) => {
    if (intento === claveCorrecta) {
      console.log("¡Acceso permitido!");
      rl.close(); // Cierra la conexión
    } else {
      console.log("Contraseña incorrecta. Intente nuevamente.");
      pedirClave(); // Vuelve a preguntar
    }
  });
}

// Iniciar proceso
pedirClave();

//Comparacion

console.log(`**********OPERADORES COMPARACION**********\n\n`)

let Igual = dato1 == dato2
let NotIgual = dato1 != dato2
let IgualdaEstric = dato2 === dato2
let NotIgualdaEstric = dato1 !== dato1
let Mayor = dato1 > dato2
let MayorIgual= dato2 >= dato1
let Menor = dato1 < dato2
let MenorIgual= dato1 <= dato2

console.log(`/********OPERADORES DE COMPARACION********/`)
console.log(`Verifiquemos si el numero ${dato1} es igual(==) a el numero ${dato2}, el resultado es: ${Igual}.`)
console.log(`Verifiquemos si el numero ${dato1} no es igual(!=) al numero ${dato2} el resutado es: ${NotIgual}`)
console.log(`Verifiquemos si el numero ${dato2} es estrictamente igual(===) al numero ${dato2} el resutado es: ${IgualdaEstric}`);
console.log(`Verifiquemos si el numero ${dato1} no es estrictamente igual(!==) al numero ${dato1} el resutado es: ${NotIgualdaEstric}`)
console.log(`El numero ${dato1} es mayor que(>) el numero ${dato2} : ${Mayor}`)
console.log(`El numero ${dato2} es mayor que o igual(>=) el numero ${dato1} : ${MayorIgual}`)
console.log(`El numero ${dato1} es menor que(<) el numero ${dato2} :${Menor}`)
console.log(`El numero ${dato1} es menor que o igual(<=) el numero ${dato2} :${MenorIgual}`)