/*
 * EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
 *
 */

class Usuario {
    constructor(name, password){
        this.name = name
        this.password = password
    }

    imprimir() {
        console.log(`Nombre: ${this.name}`)
        console.log(`Password: ${this.password}`)
    }
}

let usuario1 = new Usuario("Paco", "pao124124")
usuario1.imprimir()

usuario1.name = "Edelmiro"
usuario1.password = "34242osijo"
//usuario1.modificar("Manolo", "2443jljl34343")
usuario1.imprimir()


/*
 * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
 *
*/

// LIFO
/* const readline = require("node:readline/promises");
const { stdin, stdout } = require("node:process");

const rl = readline.createInterface({
    input: stdin,
    output: stdout
});

class ImpresoraLifo {
    constructor() {
        this.cola = []
    }

    añadir(documento){
        this.cola.push(documento)
    }

    imprimir() {
        if(this.cola.length === 0) {
            console.log("\n¡No hay documentos que imprimir!\n")
            return
        }
        const documentoImprimido = this.cola.pop()
        console.log(`\nImprimiendo: ${documentoImprimido}\n`)
    }

    mostrarCola() {
       return this.cola.join(", ")
    }

    contar() {
       return this.cola.length
    }


    async main() {
        let activo = true
        let opcion

        while(activo) {
            opcion = await rl.question(`
                1. Añadir
                2. Imprimir
                3. Salir

            Opción elegida: `)

            switch(opcion) {
                case "1": // Añadir
                    const documento = await rl.question(`\nNombre del documento: `)
                    this.añadir(documento)
                    break;
               case "2": // Imprimir
                    this.imprimir()
                    break;
                case "3": // Salir
                    activo = false
                    console.log("\n¡Fin del programa!\n")
                    break;
                default:
                    console.log("\n¡Datos introducidos Incorrectos!\n")
                    break;
            }
            if(this.cola.length <= 0) {
                console.log("\n¡La cola de impresión está vacia!\n")
            }else {
                console.log(`\nCola de impresión:  ${this.mostrarCola()}\n`)
            }
            console.log(`EL número de elementos es: ${this.contar()}`)
        }
        rl.close()
    }
}
const impresora1 = new ImpresoraLifo()
impresora1.main() */

// FIFO
const readline = require("node:readline/promises");
const { stdin, stdout } = require("node:process");

const rl = readline.createInterface({
    input: stdin,
    output: stdout
});

class ImpresoraFifo {
    constructor() {
        this.cola = []
    }

    añadir(documento) {
        this.cola.push(documento)
    }

    imprimir() {
        if(this.cola.length <= 0) {
            console.log("\n¡No hay documentos para imprimir!\n")
            return
        }
        const documentoImpreso = this.cola.shift()
        console.log(`\nImprimiendo: ${documentoImpreso}\n`)
    }

    mostrarCola() {
        return this.cola.join(", ")
    }

    contar() {
       return this.cola.length
    }

    async  main() {
        let activo = true
        let accion
        let documento
        while(activo) {

            const accion = await rl.question(`Elige entre añadir, imprimir o salir:
             =========================

                1. Añadir
                2. Imprimir
                3. Salir

                Opción elegida: `)

            switch(accion) {
                case "1": // Añadir
                    documento = await rl.question("Nombre del documento: ")
                    this.añadir(documento)
                    break;
                case "2": // Imprimir
                    this.imprimir()
                    break;
                case "3": // Salir
                    activo = false
                    console.log("\n¡Programa finalizado!\n")
                    break;
                default:
                console.log("\n¡Introduce datos válidos!\n")
                    break;
            }
            if(this.cola.length <= 0) {
                console.log("\nLa cola de impresión está vacía\n")
            }else {
                console.log(`\nCola de impresión: ${this.mostrarCola()}`)
            }
            console.log(`\nEl número de elementos es: ${this.contar()}\n`);
        }
        rl.close()
    }
}
const miImpresora = new ImpresoraFifo()
miImpresora.main()

