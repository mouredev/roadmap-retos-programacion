/*
 * EJERCICIO:
 * Explora el "Principio SOLID de Segregación de Interfaces (Interface Segregation Principle, ISP)" 
 * y crea un ejemplo simple donde se muestre su funcionamiento de forma correcta e incorrecta.
*/


/* class Animal { // Ejemplo Incorrecto
    andar(especie) {
        console.log(`EL ${especie} anda.`)
    }

    volar(especie) {
        console.log(`EL ${especie} vuela`)
    }
}

class Pato extends Animal {

}

class Perro extends Animal {
    // Un perro no puede volar
}

const pato1 = new Pato()

pato1.andar("Pato")
pato1.volar("Pato")

const perro1 = new Perro()

perro1.andar("Perro")
// Pero no tiene sentido, porque logicamente los perros no vuelan.
perro1.volar("Perro") */





// Forma correcta
/* class AnimalAereo {
    andar(especie) {
        console.log(`EL ${especie} anda.`)
    }

    volar(especie) {
        console.log(`EL ${especie} vuela`)
    }
}

class AnimalTerrestre {
    andar(especie) {
        console.log(`EL ${especie} anda.`)
    }

    trotar(especie) {
        console.log(`EL ${especie} trota`)
    }
}

class Pato extends AnimalAereo {
    
}

class Perro extends AnimalTerrestre {
    
}
const pato2 = new Pato()

pato2.andar("Pato")
pato2.volar("Pato")

const perro2 = new Perro()

perro2.andar("Perro")
perro2.trotar("Perro") */


/*
 * DIFICULTAD EXTRA (opcional):
 * Crea un gestor de impresoras.
 * Requisitos:
 * 1. Algunas impresoras sólo imprimen en blanco y negro.
 * 2. Otras sólo a color.
 * 3. Otras son multifunción, pueden imprimir, escanear y enviar fax.
 * Instrucciones:
 * 1. Implementa el sistema, con los diferentes tipos de impresoras y funciones.
 * 2. Aplica el ISP a la implementación.
 * 3. Desarrolla un código que compruebe que se cumple el principio.
*/

class ImpresoraBlancoNegro {
    imprimirBlancoNegro(documento) {
        console.log(`EL documento de tipo ${documento} se imprimió en blanco y negro.`)
    }
}

class ImpresoraColor {
    imprimirColor(documento) {
        console.log(`EL documento de tipo ${documento} se imprimió en Color.`)
    }
}

class ImpresoraMultifuncion {
    imprimir(documento) {
        console.log(`EL documento de tipo ${documento} se imprimió.`)
    }

    escanear(documento) {
        console.log(`El documento de tipo ${documento} se ha escaneado.`)
    }
    fax(documento) {
        console.log(`EL documento de tipo ${documento} se envió por fax.`)
    }

}

class ImpresoraEnBlancoNegro extends ImpresoraBlancoNegro {
    
}

class ImpresoraEnColor extends ImpresoraColor {
    
}

class Multifuncion extends ImpresoraMultifuncion {
    
}

const imprimirEnBlancoNegro = new ImpresoraEnBlancoNegro()
imprimirEnBlancoNegro.imprimirBlancoNegro("Factura")

const imprimirA_Color = new ImpresoraEnColor()
imprimirA_Color.imprimirColor("Temario")

const imprimirMultifuncion = new Multifuncion()
imprimirMultifuncion.imprimir("Revista")
imprimirMultifuncion.escanear("Recibo")
imprimirMultifuncion.fax("Contrato")

console.log("\n--- COMPROBACIÓN ISP ---")

console.log(`ImpresoraEnBlancoNegro tiene imprimir color? ${typeof imprimirEnBlancoNegro.imprimirColor === "function"}`)
console.log(`ImpresoraEnColor tiene imprimir en blanco y negro? ${typeof imprimirA_Color.imprimirBlancoNegro === "function"}`)

console.log(`¿Multifunción puede imprimir? ${typeof imprimirMultifuncion.imprimir === "function"}`)
console.log(`¿Mulifunción puede escanear? ${typeof imprimirMultifuncion.escanear === "function"}`)
console.log(`¿Multifunción puede enviar un fax? ${typeof imprimirMultifuncion.fax === "function"}`)