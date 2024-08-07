// Super clase
//primera forma encontrada en internet 
class Animales{
    type = 'animal'
    sonido = 'Sonido'
    color = 'color de tu perro'
    constructor(){
        
    }
    sound(){
        console.log(`mi animal es un ${this.type} y hace ${this.sonido}`)
    }  
    aColor(){
        console.log(`mi ${this.type} de color  ${this.color}`)
    }
    setColor(nuevoColor){
        this.color = nuevoColor
    } 
  
}
//sub clase
class Perro extends Animales {
    type='perro'
    sonido= 'Guau'
    color = 'negro'
    constructor(){
        super() //entiendo que hereda el nombre y la funcion sound
    }

}

const perro = new Perro()
console.log(perro)
perro.sound()
perro.aColor()
perro.setColor('amarillo')
perro.aColor()
// -----------------------------------------------
//segundaForma

class Animal2 {
    constructor(nombre, color){
        this.nombre= nombre
        this.color = color
        
    }
}

class Cat extends Animal2{
    //ya no ocupo el constructor por que lo hereda juntos a los strings
    sound(){
        console.log(`mi gato ${this.nombre} hace Miauuuuu y es color ${this.color}`)
    }
}

const gato = new Cat('Michis', 'blanco')
gato.sound()

// ---------------------------------------------------------------------------------

// Extra

class Empleados {
    constructor( id, nombre, empleadosACargo = []){
        this.id = id
        this.nombre = nombre
        this.empleadosACargo = empleadosACargo
    }

    addEmploye(ACargo){
        this.empleadosACargo.push(ACargo)

    }
    verEmplye(){
        if(this.empleadosACargo.length === 0){
            console.log('no tiene a nadie a carargo')
        }else{//chat gpt me ayudo con esto por que no me salia el for in
            const nombresEmpleados =this.empleadosACargo.map(empleado => empleado.nombre);
            console.log(this.nombre,'Empleados a cargo:', nombresEmpleados);
        }
    }
}


class Gerentes extends Empleados{
    coodinarProjectos(){
        console.log(`${this.nombre} esta coodinando projectos de la empresa`)
    }
}
class GerentesProject extends Empleados{
    constructor(id, nombre, projecto){
        super(id, nombre)
        this.projecto = projecto
    }
    coodinarUnProjecto(){
        console.log(`${this.nombre} esta coodinando ${this.projecto}`)
    }
}
class Programadores extends Empleados{
    constructor(id, nombre, lenguaje){
        super(id, nombre)
        this.lenguaje = lenguaje
    }

    programando(){
        console.log(`${this.nombre} esta programando en ${this.lenguaje}`)
    }

    addEmploye(ACargo){
        console.log(`el Programado no tiene empleados a cargo el ${ACargo} no se agrego` )

    }
}

console.log('Gerente------------------------------- solo hay 1')

const gerente = new Gerentes(1 , 'Dav.Dev')
gerente.coodinarProjectos()

console.log('Gerentes de los projectos --------------------- solo hay2')

const miGerenteDeProjecto = new GerentesProject(2, 'Juan', 'Projecto 1')
miGerenteDeProjecto.coodinarUnProjecto()
const miGerenteDeProjecto2 = new GerentesProject(3, 'Diego', 'Projecto 2')
miGerenteDeProjecto2.coodinarUnProjecto()

console.log('programadores-------------------------------- solo hay 4')

const miProgramador = new Programadores(4,'Dani', 'JavaScript')
miProgramador.programando()
const miProgramador2 = new Programadores(5,'Jowell', 'Python')
miProgramador2.programando()
const miProgramador3 = new Programadores(6,'Fer', 'Python')
miProgramador3.programando()
const miProgramador4 = new Programadores(7,'Santi', 'JavaScript')
miProgramador4.programando()

console.log('jerarquias de los empleados Dav.Dev ---------------------------- Gerente ')
gerente.addEmploye(miGerenteDeProjecto) //juan
gerente.addEmploye(miGerenteDeProjecto2) //Diego
gerente.verEmplye()

console.log('jerarquias de los empleados ---------------------------- Gerentes de projectos')
console.log('projecto1------------------ Juan')
miGerenteDeProjecto.addEmploye(miProgramador) //Dani
miGerenteDeProjecto.addEmploye(miProgramador4)//Santi
miGerenteDeProjecto.verEmplye()

console.log('projecto2------------------ Diego')
miGerenteDeProjecto2.addEmploye(miProgramador2) //Jowell
miGerenteDeProjecto2.addEmploye(miProgramador3)//fer
miGerenteDeProjecto2.verEmplye()

console.log('jerarquias de los empleados ---------------------------- Gerentes de projectos')
miProgramador.addEmploye(miProgramador2)


