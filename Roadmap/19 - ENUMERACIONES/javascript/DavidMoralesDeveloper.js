// Crea un Enum que represente los días de la semana del lunes
//  * al domingo, en ese orden. Con ese enumerado, crea una operación
//  * que muestre el nombre del día de la semana dependiendo del número entero
//  * utilizado (del 1 al 7).
// un objeto o  una clase lo averiguaremos.
// que me aproximo a mi respuesta
// https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Object/entries

const diasDelaSemana = {
  lunes: 1,
  martes: 2,
  miercoles: 3,
  jueves: 4,
  viernes: 5,
  sabado: 6,
  domingo: 7,
};

function diaEnNum(num) {
  const numeros = Object.entries(diasDelaSemana);
  const guardar = numeros.find(([key, value]) => value === 4); //desestructuro mi arr en dos
  return guardar[0]
}

console.log(diaEnNum(3))

// * DIFICULTAD EXTRA (opcional):
// * Crea un pequeño sistema de gestión del estado de pedidos.
// * Implementa una clase que defina un pedido con las siguientes características:
// * - El pedido tiene un identificador y un estado.
// * - El estado es un Enum con estos valores: PENDIENTE, ENVIADO, ENTREGADO y CANCELADO.
// * - Implementa las funciones que sirvan para modificar el estado:
// *   - Pedido enviado
// *   - Pedido cancelado
// *   - Pedido entregado
// *   (Establece una lógica, por ejemplo, no se puede entregar si no se ha enviado, etc...)
// * - Implementa una función para mostrar un texto descriptivo según el estado actual.
// * - Crea diferentes pedidos y muestra cómo se interactúa con ellos. 


class estadosDePedidos {

     estadosDelPedido = {
        PENDIENTE : 1,
        ENVIADO : 2,
        ENTREGADO : 3,
        CANCELADO : 4
     }
     numero =Object.entries(this.estadosDelPedido)
     stado = this.numero.find(([key, value]) => value === 1)
   
    constructor(id){
        this.id = id
        this.estado =  this.stado[0]
        
    }

    enviado () {
        if(this.estado === 'PENDIENTE'){
            this.stado = this.numero.find(([key, value]) => value === 2)
            this.estado = this.stado[0]
        }else{
            console.log('el pedido fue entregado o cancelado')
        }
        this.descStatus()
    }

    entregado () {
        if (this.estado === 'ENVIADO'){
            this.stado = this.numero.find(([key, value]) => value === 3)
            this.estado = this.stado[0]
        }else{
            console.log(`el estado debe ser enviado o fue cancelado`)
        }
        this.descStatus()
        // console.log('gracias por su compra vuelva pronto')
    }

    cancelado () {
        this.stado = this.numero.find(([key, value]) => value === 4)
        this.estado = this.stado[0]
        this.descStatus()
    }
 
    descStatus (){
        // Implementa una función para mostrar un texto descriptivo según el estado actual.
        console.log(`el estado actual de el pedido ${this.id} tiene un estado de ${this.estado}`)
    }    
       
}



let orden1 = new estadosDePedidos(1)
orden1.descStatus()
orden1.enviado()
orden1.entregado()

console.log('-----------------------------------------orden2')
let oreden2 = new estadosDePedidos(2)
oreden2.descStatus()
oreden2.entregado()
oreden2.cancelado()
oreden2.enviado()


