// ENUMS en JavaScript
/*
Los enums en JavaScript son una forma de crear un conjunto de constantes que pueden ser utilizadas en cualquier parte de nuestro código.
los enumeradores (enums) no existen como una característica nativa del lenguaje, pero podemos simularlos utilizando objetos o técnicas específicas.

¿Cómo crear un ENUM en JavaScript?
En JavaScript, los ENUM se pueden implementar de varias formas. Aquí te muestro las más comunes:

1. Usando un objeto:
La forma más sencilla de crear un ENUM es utilizando un objeto donde las claves son los nombres de las constantes y los valores son los valores asociados.
Por ejemplo:
*/
const DaysOfWeek = {
    MONDAY: 'Monday',
    TUESDAY: 'Tuesday',
    WEDNESDAY: 'Wednesday',
    THURSDAY: 'Thursday',
    FRIDAY: 'Friday',
    SATURDAY: 'Saturday',
    SUNDAY: 'Sunday',
  };
  
console.log(DaysOfWeek.MONDAY);
console.log(DaysOfWeek.TUESDAY);

/*
2. Usando Object.freeze():
Para evitar que el objeto sea modificado accidentalmente, puedes usar Object.freeze. Esto hace que el objeto sea inmutable.
*/
const DaysOfWeek2 = Object.freeze({
    MONDAY: 'Monday',
    TUESDAY: 'Tuesday',
    WEDNESDAY: 'Wednesday',
    THURSDAY: 'Thursday',
    FRIDAY: 'Friday',
    SATURDAY: 'Saturday',
    SUNDAY: 'Sunday',
    });
DaysOfWeek2.MONDAY = 'New Day'; // Esto no tendrá efecto
console.log(DaysOfWeek2.MONDAY); // Output: Monday
/*
3. Usando Symbol para mayor seguridad
Los símbolos son únicos y pueden ser útiles para evitar colisiones de nombres.
*/
const Colors = Object.freeze({
    RED: Symbol('red'),
    GREEN: Symbol('green'),
    BLUE: Symbol('blue'),
  });
  
console.log(Colors.RED);
console.log(Colors.RED.description); // Output: red

/*
4. Usando map:
Un Map permite asignar valores personalizados sin perder flexibilidad
*/
const UserRole = new Map([
    ["ADMIN", { level: 3, canEdit: true, canDelete: true }],
    ["EDITOR", { level: 2, canEdit: true, canDelete: false }],
    ["USER", { level: 1, canEdit: false, canDelete: false }]
  ]);
  
  // ✅ Uso del Enum
console.log(UserRole.get("EDITOR")); // { level: 2, canEdit: true, canDelete: false }
console.log(UserRole.get("USER").canEdit); // false


/*
 * EJERCICIO:
 * Empleando tu lenguaje, explora la definición del tipo de dato
 * que sirva para definir enumeraciones (Enum).
 * Crea un Enum que represente los días de la semana del lunes
 * al domingo, en ese orden. Con ese enumerado, crea una operación
 * que muestre el nombre del día de la semana dependiendo del número entero
 * utilizado (del 1 al 7).
 */

// Definimos un objeto con las constantes que necesitamos
const diasDeLaSemana = {
    LUNES: 1,
    MARTES: 2,
    MIERCOLES: 3,
    JUEVES: 4,
    VIERNES: 5,
    SABADO: 6,
    DOMINGO: 7
};

// Utilizamos las constantes en nuestro código, por ejemplo:

let dia = diasDeLaSemana.LUNES;
console.log(dia); // 1

// Podemos utilizar un switch para hacer algo diferente dependiendo del valor de la constante:
switch (dia) {
    case diasDeLaSemana.LUNES:
        console.log('Hoy es Lunes');
        break;
    case diasDeLaSemana.MARTES:
        console.log('Hoy es Martes');
        break;
    case diasDeLaSemana.MIERCOLES:
        console.log('Hoy es Miércoles');
        break;
    case diasDeLaSemana.JUEVES:
        console.log('Hoy es Jueves');
        break;
    case diasDeLaSemana.VIERNES:
        console.log('Hoy es Viernes');
        break;
    case diasDeLaSemana.SABADO:
        console.log('Hoy es Sábado');
        break;
    case diasDeLaSemana.DOMINGO:
        console.log('Hoy es Domingo');
        break;
    default:
        console.log('Día no válido');
}

// Podemos hacer un bucle para recorrer todas las constantes:
for (let dia in diasDeLaSemana) {
    console.log(diasDeLaSemana[dia]);
}

// Podemos obtener el nombre de la constante a partir de su valor:
function getDia(dia) {
    for (let d in diasDeLaSemana) {
        if (diasDeLaSemana[d] === dia) {
            return d;
        }
    }
    return null;
}

console.log(getDia(1)); // LUNES

function obtenerNombreDelDia(valor){
    const clave = Object.keys(diasDeLaSemana).find(key => diasDeLaSemana[key] === valor);
    
    return clave || 'No existe';
}

console.log(obtenerNombreDelDia(1)); // LUNES
console.log(obtenerNombreDelDia(8)); // No existe


/* DIFICULTAD EXTRA (opcional):
* Crea un pequeño sistema de gestión del estado de pedidos.
* Implementa una clase que defina un pedido con las siguientes características:
* - El pedido tiene un identificador y un estado.
* - El estado es un Enum con estos valores: PENDIENTE, ENVIADO, ENTREGADO y CANCELADO.
* - Implementa las funciones que sirvan para modificar el estado:
*   - Pedido enviado
*   - Pedido cancelado
*   - Pedido entregado
*   (Establece una lógica, por ejemplo, no se puede entregar si no se ha enviado, etc...)
* - Implementa una función para mostrar un texto descriptivo según el estado actual.
* - Crea diferentes pedidos y muestra cómo se interactúa con ellos. 
*/

const estadosPedido = {
    PENDIENTE: 1,
    ENVIADO: 2,
    ENTREGADO: 3,
    CANCELADO: 4
}

class Pedido {

    constructor(id){
        this.id = id;
        this.estado = estadosPedido.PENDIENTE;
    }

    pedidoEnviado(){
        if(this.estado === estadosPedido.PENDIENTE){
            this.estado = estadosPedido.ENVIADO;
        }
        else{
            console.log('El pedido no se puede enviar, ya ha sido enviado o cancelado');
        }
    }

    pedidoEntregado(){
        if(this.estado === estadosPedido.ENVIADO){
            this.estado = estadosPedido.ENTREGADO;
        }
        else{
            console.log('El pedido no se puede entregar, no ha sido enviado');
        }
    }

    pedidoCancelado(){
        if(this.estado != estadosPedido.ENTREGADO){
            this.estado = estadosPedido.CANCELADO;
        }
        else{
            console.log('El pedido no se puede cancelar ya se entrego');
        }
    }

    mostrarEstado(){
        let mensaje = '';
        switch (this.estado) {
            case estadosPedido.PENDIENTE:
                mensaje = `El pedido ${this.id} está pendiente`;
                break;
            case estadosPedido.ENVIADO:
                mensaje = `El pedido ${this.id} ha sido enviado`;
                break;
            case estadosPedido.ENTREGADO:
                mensaje = `El pedido ${this.id} ha sido entregado`;
                break;
            case estadosPedido.CANCELADO:
                mensaje = `El pedido ${this.id} ha sido cancelado`;
                break;
            default:
                mensaje = 'Estado no válido';
        }
        console.log(mensaje);
    }
}

const pedido1 = new Pedido(1);
pedido1.mostrarEstado();
pedido1.pedidoEnviado();
pedido1.mostrarEstado();
pedido1.pedidoCancelado();
pedido1.mostrarEstado();
pedido1.pedidoEntregado();
pedido1.mostrarEstado();
console.log('-------------------------');
const pedido2 = new Pedido(2);
pedido2.mostrarEstado();
pedido2.pedidoEntregado();
pedido2.mostrarEstado();
pedido2.pedidoCancelado();
pedido2.mostrarEstado();
pedido2.pedidoEnviado();
pedido2.mostrarEstado();
