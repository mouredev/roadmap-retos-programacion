/*
 * EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
 */

// Practicando: Clases:
class Player{
    
    constructor( name, hatColor, game ){
        this._name     = name;
        this._hatColor = hatColor;
        this._game     = game;
    }

    jump(){
        console.log("Cada vez que gano yo salto varias veces xD");
    }
    run(){
        console.log("En mis ratos libres salgo a correr");
    }
    walk(){
        console.log("Y cuando me canso salgo a caminar");
    }

    greets(){
        return `Hola soy el Jugador ${this._name} y soy sombrero ${this._hatColor} y me gusta jugar ${this._game}`
    }
}

let player1 = new Player("Omar","Negro","God of War");
let player2 = new Player("Juan","Gris", "Call of duty");

console.log(">>>", player1.greets() );
console.log(">>>", player2.greets() );

/*
 * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
 */

// Ejercicio aplicando Pila:
class Games{
    constructor( element ){
        this.element = [];
    }

    pushing( game ){
        return this.element.push( game );
    }
    poping(){
        this.size() === 0 ? 'La cola está vacía' : this.element.pop();
    }
    sizing(){
        return this.element.length;
    }
    printing(){
        this.element.forEach( (element) => { console.log(element) } );
    }
}

let myGames = new Games();
myGames.pushing("God of War")
myGames.pushing("PlantsVsZombies");
myGames.pushing("Mortal Kombat");
myGames.poping();
myGames.poping();
myGames.printing();


// Ejercicio aplicando Cola:
class Queue{
    constructor( cola ){
        this.cola = [];
    }

    //implementamos la función enqueue para meter datos en cola:
    enqueue( element ){
        return this.cola.push( element );
    }

    //Ahora implemenramos función para sacar elementos de la cola
    dequeue(){
        if( this.size() === 0){
            return 'No hay elementos en cola...'
        }  
        return this.cola.shift();
    }

    //Función para ver cantidad de elementos en cola
    size(){
        return this.cola.length;
    }   

    // función para ver los elementos de la cola
    print(){
        this.cola.forEach( (element) =>{
            console.log(element);
        });
    }
}

let myQueue = new Queue();
myQueue.enqueue("elemento_1");
myQueue.enqueue("elemento_2");
myQueue.enqueue("elemento_3");
myQueue.enqueue("elemento_4");
myQueue.dequeue();
myQueue.dequeue();
myQueue.dequeue();
myQueue.print();
//myQueue.size();