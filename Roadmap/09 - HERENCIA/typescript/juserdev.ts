/*
 * EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.
 */

namespace herencias {

    class Animals{
        animal: string
        nombre: string

        constructor(animal: string, nombre: string){
            this.animal = animal
            this.nombre = nombre
        }

        talk():string{
            return `Soy un ${this.animal} y me llamo ${this.nombre} y emite un sonido no determiando`
        }

    }

    class Perro extends Animals{
        sonido: string

        constructor(nombre: string, sonido: string){
            super("perro", nombre)
            this.sonido = sonido
        }

        talk():string{
            return `Soy un ${this.animal}, me llamo ${this.nombre} y ladro, ${this.sonido}!`
        }
    }

    class Gato extends Animals{
        sonido: string
        
        constructor(nombre: string, sonido: string){
            super("gato", nombre)
            this.sonido = sonido
        }

        talk():string{
            return `Soy un ${this.animal}, me llamo ${this.nombre} y maullo, ${this.sonido}!`
        }
    }

    const loro = new Animals("loro", "theo")
    const perro = new Perro("Max", "guau! guau!")
    const gato = new Gato("Michi", "miau miau!")

    const emitirSonido = (animal: Animals): string=>{
        return `${animal.talk()}`
    }

    console.log(emitirSonido(loro))
    console.log(emitirSonido(perro))
    console.log(emitirSonido(gato))

    //! EXTRA

    class Empleado {
        name: string
        id: number
        empleados: Empleado[]

        constructor(name: string, id: number) {
            this.name = name
            this.id = id
            this.empleados = []
        }

        print(){
            return `Soy un el empleado ${this.name} con id: ${this.id} sin cargo asignado`
        }
        
        add(empleado: Empleado){
            this.empleados.push(empleado)
        }

        imprimirEmpleados(){
            let empleados: string[] = []
            for (const empleado of this.empleados) {
                empleados.push(empleado.name)
            }
            return empleados
        }

    }


    class Gerente extends Empleado {
        gerenciar(){
            return `${this.name} esta coordinando todos los proyectos de la empresa`
        }

    }

    class GerenteDeProyectos extends Empleado {
        proyecto: string

        constructor(name: string, id: number, proyecto: string){
            super(name, id)
            this.proyecto = proyecto
        }

        gerenciarDeProyectos(){
            return `${this.name} esta coordinando su proyectos`
        }
        
    }

    class Programador extends Empleado {
        lenguage: string

        constructor(name: string, id: number, lenguage: string){
            super(name, id)
            this.lenguage = lenguage
        }

        programar(){
            return `${this.name} esta programando en ${this.lenguage}`
        }

        add(empleado: Empleado): string{
            return `Un programador no tinene empleados a cargo, ${empleado.name} no se añadira`
        }

    }

    const miGerente = new Gerente("Sebastian", 1)
    const miGerenteDeProyectos = new GerenteDeProyectos("Laura", 2, "Proyecto 1")
    const miGerenteDeProyectos2 = new GerenteDeProyectos("Daniela", 3, "Proyecto 2")
    const miProgramador = new Programador("Juan", 4, "JavaScript")
    const miProgramador2 = new Programador("JuanSe", 5, "TypeScript")
    const miProgramador3 = new Programador("Sebas", 6, "Pyton")
    const miProgramador4 = new Programador("Michael", 7, "Java")

    miGerente.add(miGerenteDeProyectos)
    miGerente.add(miGerenteDeProyectos2)

    miGerenteDeProyectos.add(miProgramador)
    miGerenteDeProyectos.add(miProgramador2)
    miGerenteDeProyectos2.add(miProgramador3)
    miGerenteDeProyectos2.add(miProgramador4)

    console.log(miProgramador.add(miProgramador2))
    console.log(miGerente.print())

    console.log(miProgramador.programar())
    console.log(miProgramador2.programar())
    console.log(miProgramador3.programar())
    console.log(miProgramador4.programar())
    console.log(miGerenteDeProyectos.gerenciarDeProyectos())
    console.log(miGerenteDeProyectos2.gerenciarDeProyectos())
    console.log(miGerente.gerenciar())

    console.log(miGerente.imprimirEmpleados())
    console.log(miGerenteDeProyectos.imprimirEmpleados())
    console.log(miGerenteDeProyectos2.imprimirEmpleados())
    console.log(miProgramador.imprimirEmpleados())
}