/**
 * Principio de sustitución de Liskov
 * puede definirse como: Cada clase que hereda de otra puede usarse como su padre sin necesidad de conocer las diferencias entre ellas.
 *
 * Fuente: https://es.wikipedia.org/wiki/Principio_de_sustituci%C3%B3n_de_Liskov
 */

// Tenemos una clase Cocinero que prepara los diferentes platillos de un restaurante,
// una clase Comida que sirve de base para todos los tipos de platillos,
// una clase Pizza y Sopa que heredan de la clase Comida

// INCORRECTA
class Comida{
    constructor(ingredientes){
        if(!Array.isArray(ingredientes)) throw new Error('ingredientes debe ser un arreglo de strings')

        this.ingredientes = ingredientes
    }
}

class Pizza extends Comida{
    hornear(){
        console.log('Horneando...');
        console.log('Horneado Terminado!')
    }
}

class Sopa extends Comida{
    hervir(){
        console.log('Hirviendo...');
        console.log('Hervido Terminado!')
    }
}

class Cocinero{
    hacerPlatillo(comida){
        // agregar ingredientes
        console.log(`Preparando ${comida.constructor.name}`);


        comida.ingredientes.forEach((ingrediente) => console.log(`añadir ${ingrediente}`))

        /**
         *  Al tener Pizza y Sopa métodos diferentes necesarios para su preparación
         *  tenemos que rompemos el LSP debido a que no podemos usarlas indistintamente sino
         *  que debemos diferenciarlas.
         */
        if(comida instanceof Pizza) comida.hornear()

        if(comida instanceof Sopa) comida.hervir()

        console.log('Platillo listo!!!');
    }
}

const cocinero = new Cocinero()

cocinero.hacerPlatillo(new Pizza(['harina', 'agua', 'queso', 'peperoni']))
cocinero.hacerPlatillo(new Sopa(['agua', 'papa', 'zanahoria', 'sal']))

CORRECTA
class Comida{
    constructor(ingredientes){
        if(!Array.isArray(ingredientes)) throw new Error('ingredientes debe ser un arreglo de strings')

        this.ingredientes = ingredientes
    }

    preparar(){ }
}

class Pizza extends Comida{
    preparar() {
        this.hornear()
    }

    hornear(){
        console.log('Horneando...');
        console.log('Horneado Terminado!')
    }
}

class Sopa extends Comida{
    preparar(){
        this.hervir()
    }

    hervir(){
        console.log('Hirviendo...');
        console.log('Hervido Terminado!')
    }
}

class Cocinero{
    cocinarPlatillo(comida){
        // agregar ingredientes
        console.log(`Preparando ${comida.constructor.name}`);


        comida.ingredientes.forEach((ingrediente) => console.log(`añadir ${ingrediente}`))

        /**
         *  Agregando el método preparar en la clase Comida y abstrayendo el cómo se prepara la comida
         *  podemos cumplir con el LSP, de modo de que no nos preocupamos por el tipo de la comida.
         */
        comida.preparar()

        console.log('Platillo listo!!!');
    }
}

const cocinero = new Cocinero()

cocinero.hacerPlatillo(new Pizza(['harina', 'agua', 'queso', 'peperoni']))
cocinero.hacerPlatillo(new Sopa(['agua', 'papa', 'zanahoria', 'sal']))


// EXTRA

class Vehiculo {
    constructor({maxVelocidad, unidadVelocidad}){
        if(typeof(maxVelocidad) !== 'number') throw new Error('maxVelocidad debe ser un number')
        if(typeof(unidadVelocidad) !== 'string') throw new Error('unidadVelocidad debe ser un string')

        this.maxVelocidad = maxVelocidad
        this.unidadVelocidad = unidadVelocidad
        this.velocidad = 0
    }

    acelerar(aumento){
        if(this.velocidad + aumento > this.maxVelocidad){
            console.log('Velocidad Maxima alcanzada no se puede acelerar más')
            return
        }
        
        this.velocidad += aumento
        console.log(`Velocidad actual ${this.velocidad} ${this.unidadVelocidad}`)
    }

    frenar(){
        this.velocidad = 0
        console.log('Frenado Exitoso')
    }
}

class NaveEspacial extends Vehiculo{
    constructor(props){
        super(props)
    }
    despegar(){
        console.log('Despegue')
    }
}

class Automovil extends Vehiculo{
    constructor(props){
        super(props)
    }
}

class Barco extends Vehiculo{
    constructor(props){
        super(props)
    }
    subirAncla(){
        console.log('Ancla subida')
    }
    bajarAncla(){
        console.log('Ancla bajada')
    }
}

const vehiculos = []

vehiculos.push(new NaveEspacial({
    maxVelocidad: 10,
    unidadVelocidad: 'años luz'
}))

vehiculos.push(new Automovil({
    maxVelocidad: 200,
    unidadVelocidad: 'kilomentos'
}))

vehiculos.push(new NaveEspacial({
    maxVelocidad: 100,
    unidadVelocidad: 'milla nautica'
}))

// Como se puede ver aunque cada subclase tiene suspropios metodos, todas pueden ser reemplazadas por su 
// clase base de ser necesario sin problemas.

vehiculos.forEach(vehiculo => {
    vehiculo.acelerar(10)
    vehiculo.frenar()
    vehiculo.acelerar(100)
})
