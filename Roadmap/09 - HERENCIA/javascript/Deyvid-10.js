class Animal
{
    constructor(sonido)
    {
        this.sonido = sonido
    }
}

class Perro extends Animal
{
    constructor(sonido, raza)
    {
        super(sonido)
        this.raza = raza
    }

    hablar() 
    {
        console.log(`El perro hace ${this.sonido}`);
    }

    razaPerro() 
    {
        console.log(`El perro es de raza ${this.raza}`);
    }
}

let miPerro = new Perro("Wao!")
miPerro.hablar()
miPerro.razaPerro()

class Gato extends Animal
{
    constructor(sonido)
    {
        super(sonido)
    }

    hablar() 
    {
        console.log(`El gato hace ${this.sonido}`);
    }
}

let miGato = new Gato("Firulais", "Miau!")

// DIFICULTAD EXTRA

class Empleado
{
    constructor(id, nombre)
    {
        this.id = id
        this.nombre = nombre
    }

    datos()
    {
        console.log(`Identificador: ${this.id}`);
        console.log(`Nombre: ${this.nombre}`);
    }
}

let miEmpleado = new Empleado("05", "Manuel")
miEmpleado.datos()

class Gerentes extends Empleado
{
    constructor(id, nombre)
    {
        super(id, nombre)
    }

    supervisioGeneral() 
    {
        console.log(`${this.nombre} se encarga de monitorear el desempeño de todos los departamentos.`);
    }

    gestionRecursos()
    {
        console.log(`${this.nombre} aprueba los presupuestos y controla los gastos.`);
    }
}

let miGerente = new Gerentes("06", "Alberto")
miGerente.datos()
miGerente.gestionRecursos()
miGerente.supervisioGeneral()

class GerentesProyectos extends Empleado
{
    constructor(id, nombre, proyecto)
    {
        super(id, nombre)
        this.proyecto = proyecto
    }

    planificacion() 
    {
        console.log(`${this.nombre} crea el cronograma del proyecto`);
    }

    gestionEquipos()
    {
        console.log(`${this.nombre} asigna tareas y responsabilidades a los miembros del equipo`);
    }

    comunicacion()
    {
        console.log(`${this.nombre} provee informes de estado del proyecto y realiza reuniones de actualización`)
    }
}

let miGerenteProyectos = new GerentesProyectos("07", "Garcia", "Web de negocios")
miGerenteProyectos.datos()
miGerenteProyectos.comunicacion()
miGerenteProyectos.gestionEquipos()
miGerenteProyectos.comunicacion()

class Programador extends Empleado
{
    constructor(id, nombre, tegnologia)
    {
        super(id, nombre)
        this.tegnologia = tegnologia
    }

    desarrollo() 
    {
        console.log(`${this.nombre} escribe y revisa código en el lenguaje ${this.tegnologia}.`);
    }
}

let miProgramador = new Programador("09", "Jaime", "JavaScript")
miProgramador.datos()
miProgramador.desarrollo()