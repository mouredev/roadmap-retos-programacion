/*
<-------------- Herencia -------------->
Básicamente la herencia de clases es una característica que nos permite reutilizar, simplificar y añadir nuevo código. EL funcionamiento
de la herencia parte de que una "clase hija" obtiene acceso a las propiedades y métodos de una "clase padre". Dicho acceso se establece
mediante la palabra clave "extends" y el método "super()" que se encarga de llamar o ejecutar el constructor de la clase padre cuando
se crea o instancia un objeto de la clase hija. El método super() que debe usarse antes de usar "this".
*/

class Animal {
  constructor(nombre, color) {
    this.nombre = nombre
    this.color = color
  }

  sonido(sonido) {
    return console.log(sonido)
  }

  correr(velocidad) {
    return console.log(`La velocidad de ${this.nombre} es de ${velocidad}km/h`)
  }
}

class Perro extends Animal {
  constructor(nombre, color, edad) {
    super(nombre, color)
    this.edad = edad
  }

  dormir() {
    return console.log(`Shhh, ${this.nombre} de color ${this.color} y edad ${this.edad} años está durmiendo`)
  }
}

class Gato extends Animal {
  constructor(nombre, color, comida) {
    super(nombre, color)
    this.comida = comida
  }

  comer() {
    return console.log(`${this.nombre} de color ${this.color} está comiendo ${this.comida}`)    
  }
}

console.log('<-- Perro:')

const perro = new Perro('Anubis', 'naranja', 4)
perro.dormir()         // Shhh, Anubis de color naranja y edad 4 años está durmiendo
perro.correr(45)       // La velocidad de Anubis es de 45km/h
perro.sonido('¡guau!') // ¡guau!

console.log('<-- Gato:')

const gato = new Gato('Dakota', 'amarillo', 'ratones')
gato.comer()         // Dakota de color amarillo está comiendo ratones
gato.correr(48)      // La velocidad de Dakota es de 48km/h
gato.sonido('¡miau') // ¡miau!


// <-------------- Extra -------------->

class Empleados {
  constructor(identificador, nombre) {
    this.identificador = identificador
    this.nombre = nombre
  }

  presentacion() {
    return console.log(`Me llamo ${this.nombre}, mi número de Id de emplead@ es: ${this.identificador}`)
  }
}

class Gerentes extends Empleados {
  constructor(identificador, nombre, gestion) {
    super(identificador, nombre)
    this.gestion = gestion
    this.empleadosACargo = []
  }

  planear() {
    return console.log(`Soy la encargada de toda la gestión ${this.gestion}`)
  }

  /*
  Con ayuda de la sintaxis "super.metodo()" sobreescribo el método "presentacion()" de la clase padre para que se
  llame a él primero, y luego llame al método "planear()" de la clase hija.
  */
  presentacion() {
    super.presentacion()
    this.planear()
  }
}

class GerentesDeProyectos extends Empleados {
  constructor(identificador, nombre, proyecto) {
    super(identificador, nombre)
    this.proyecto = proyecto
    this.empleadosACargo = []
  }

  dirigir() {
    return console.log(`Estoy dirigiendo la construcción de una ${this.proyecto}`)
  }

  presentacion() {
    super.presentacion()
    this.dirigir()
  }
}

class Programadores extends Empleados {
  constructor(identificador, nombre, lenguaje) {
    super(identificador, nombre)
    this.lenguaje = lenguaje
  }

  codificar() {
    return console.log(`Estoy codificando un sitio web con ${this.lenguaje}`)
  }

  presentacion() {
    super.presentacion()
    this.codificar()
  }
}

console.log('<-- Gerente:')

const gerente = new Gerentes(1, 'Margot', 'administrativa')
gerente.presentacion()


console.log('<-- Gerente de proyectos:')

const gerenteDeProyecto = new GerentesDeProyectos(2, 'Andy', 'página web')
gerenteDeProyecto.presentacion()


console.log('<-- Programadores:')

const programador = new Programadores(3, 'Robert', 'javascript')
const programador1 = new Programadores(4, 'Lucas', 'python')
programador.presentacion()
programador1.presentacion()


// Inserto el Gerente de proyectos en el array del Gerente
gerente.empleadosACargo.push(gerenteDeProyecto)

// Inserto los programadores en el array del Gerente de Proyectos
gerenteDeProyecto.empleadosACargo.push(programador) 
gerenteDeProyecto.empleadosACargo.push(programador1)


console.log('<-- Empleados a cargo del Gerente:')

gerente.empleadosACargo.map(empleado => console.log(`Id: ${empleado.identificador} - nombre: ${empleado.nombre} - proyecto actual: ${empleado.proyecto}`))

console.log('<-- Empleados a cargo del Gerente de proyectos:')

gerenteDeProyecto.empleadosACargo.map(empleado => console.log(`Id: ${empleado.identificador} - nombre: ${empleado.nombre} - lenguaje: ${empleado.lenguaje}`))