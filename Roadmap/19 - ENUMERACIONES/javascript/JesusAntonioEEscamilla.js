/** #19 - JavaScript ->Jesus Antonio Escamilla */

/**
 * Aunque JavaScript no tiene un tipo de datos enum incorporado como algunos otros lenguajes de programación,
    se pueden simular mediante el uso de Objects o Constantes.
 * En general, los enums son un tipo que puede contener un número finito de valores definidos.
 * Los valores de los enums no son mutables.
 */

//---EJERCIÓ---
// Creamos una función que puede agregar y leer los objetos (Enum)
function Enum() {
    this.obj = {};
    this.add = function(key, value) {
        this[key] = value;
        this.obj[value] = key;
    };
    this.getName = function(value) {
        return this.obj[value];
    };
}

// Creamos el Enum como Objeto
const Semana_Enum = new Enum();
// Agregamos Valores
Semana_Enum.add("Lunes", 1);
Semana_Enum.add("Martes", 2);
Semana_Enum.add("Miércoles", 3);
Semana_Enum.add("Jueves", 4);
Semana_Enum.add("Viernes", 5);
Semana_Enum.add("Sábado", 6);
Semana_Enum.add("Domingo", 7);

// Retornamos el nombre del dia asignado
function nombreDia(numero) {
    return Semana_Enum.getName(numero);
}

// Lo llamamos en un consola
console.log(`El numero es 5 que es el dia ${nombreDia(5)}`);



/**-----DIFICULTAD EXTRA-----*/

//  Creamos una función para el ENUM Estado
function StateRaques() {
    this.obj = [];
    this.add = function(key, value) {
        this[key] = value;
        this.obj[value] = key;
    };
    this.getName = function(value) {
        return this.obj[value];
    };
}

//  Creamos un Estado de Pedidos
const State = new StateRaques();
//  Aquí agregamos en ENUM
State.add("Pendiente", 0);
State.add("Enviado", 1);
State.add("Entregado", 2);
State.add("Cancelado", 3);

//  Clase Pedido
class Order {
    constructor(identificador){
        this.identificador = identificador;
        this.estado = State.Pendiente
    }

    SendOrder(){
        if (this.estado === State.Pendiente) {
            this.estado = State.Enviado;
            console.log(`Pedido ${this.identificador} enviado.`);
        } else {
            console.log(`El pedido "${this.identificador}", no se puede enviar porque no está pendiente.`);
        }
    }

    DeliverOrder(){
        if (this.estado === State.Enviado) {
            this.estado = State.Entregado;
            console.log(`Pedido ${this.identificador} entregado.`);
        } else {
            console.log(`El pedido "${this.identificador}", no se puede entregar porque no ha sido enviado.`);
        }
    }
    
    CancelOrder(){
        if (this.estado !== State.Entregado) {
            this.estado = State.Cancelado;
            console.log(`Pedido ${this.identificador} cancelado.`);
        } else {
            console.log(`El pedido "${this.identificador}" no se puede cancelar porque ya fue entregado.`);
        }
    }

    DescriptionOrder(){
        return `El estado del pedido ${this.identificador} es: ${State.getName(this.estado)}.`;
    }
}

//  Ejemplo de ENUM
const order1 = new Order("001");
order1.SendOrder();
order1.DeliverOrder();
console.log(order1.DescriptionOrder());

const order2 = new Order("002");
order2.SendOrder();
order2.CancelOrder();
console.log(order2.DescriptionOrder());

const order3 = new Order("003");
console.log(order3.DescriptionOrder());

/**-----DIFICULTAD EXTRA-----*/