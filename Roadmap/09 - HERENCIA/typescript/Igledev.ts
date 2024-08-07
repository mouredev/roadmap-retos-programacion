// 1º Ejercicio 
    // Hacemos un type del tipo de comida que hay
    type AlimentacionAnimal = 'CARNIVORO' | 'HERVIBORO' | 'OMNIVORO'

    // Creamos la clase Animal donde le incluimos la base de cada animal
    abstract class Animal{  // La hacemos abstracta para hacer el método que reproduzca el sonido del animal
        constructor(private _nombre : string,
        private _especie : string,
        private _alimentacion  : AlimentacionAnimal)
        {}

        public set setNombre(nombre : string){
            this._nombre = nombre;
        }

        public get getNombre() : string{
            return this._nombre;
        }

        public set setEspecie(especie : string){
            this._especie = especie;
        }

        public get getEspecie() : string{
            return this._especie;
        }

        public set setAlimentacion(alimentacionAnimal : AlimentacionAnimal){
            this._alimentacion = alimentacionAnimal;
        }

        public get getAlimentacion() : AlimentacionAnimal{
            return this._alimentacion;
        }

        abstract sonido() : string; // Hacemos que devuelva un string que va a ser el sonido 

        //Vamos a hacer el método toString()
        public toString() : string{
            return `El animal es un/a ${this._especie}, es ${this._alimentacion} y se llama ${this._nombre}`;
        }
    }

    // Creamos la clase Perro que extiende de Animal
    class Perro extends Animal{
        constructor(_nombre : string,
            _especie : string,
            _alimentacion : AlimentacionAnimal,
            private _raza : string)
        {super(_nombre, _especie, _alimentacion)}

        public set setRaza(raza : string){
            this._raza = raza;
        }

        public get getRaza(){
            return this._raza;
        }

        sonido(): string {
            return 'guau!';
        }

        public toString(): string {
            return super.toString() + `. Es un ${this._raza}`;
        }

    }

    // Creamos la clase Gato que extiende de Animal
    class Gato extends Animal{

        constructor(_nombre : string,
            _especie : string,
            _alimentacion : AlimentacionAnimal,
            private _color : string)
        {super(_nombre, _especie, _alimentacion)}

        public set setColor(color : string){
            this._color = color;
        }

        public get getColor(){
            return this._color;
        }

        sonido(): string {
            return 'meow!';
        }

        public toString(): string {
            return super.toString() + `. Es de color ${this._color}`;
        }

    }

    // Vamos a crear instancias
    let perrete = new Perro('Blas', 'Perro', 'OMNIVORO', 'Payeiro');
    console.log(perrete.toString() + '. Su sonido es: ' + perrete.sonido());
    let gatete = new Gato('Zelda', 'Gato', 'OMNIVORO', 'Negro');
    console.log(gatete.toString() + '. Su sonido es: ' + gatete.sonido());

// Ejercicio Extra
    //Creamos la clase común para todos
    type tipoEmpleado = 'GERENTE' | 'GERENTE DE PROYECTOS' | 'PROGRAMADORES' 
    abstract class Empleado{
        constructor(private readonly _id : number, 
            private _nombre : string,
            private _tipoEmpleado : tipoEmpleado)
        {}

        public set setNombre(nombre : string){
            this._nombre = nombre;
        }

        public get getNombre(){
            return this._nombre;
        }

        public set setEmpleado(empleado : tipoEmpleado){
            this._tipoEmpleado = empleado;
        }

        public get getEmpleado(){
            return this._tipoEmpleado;
        }

        public toString() : string{
            return `Hola, soy ${this._tipoEmpleado}, mi identificado es: ${this._id} y mi nombre es ${this._nombre}`;
        }
    }

    class Gerente extends Empleado{
        constructor(
            id : number,
            nombre : string,
            tipoEmpleado : tipoEmpleado,
            private _funciones : string,
            private _gerentesProyecto : GerentesProyecto[])
        {super(id, nombre, tipoEmpleado)}

        public set setGerentesProyecto(gerentesProyecto : GerentesProyecto[]){
            this._gerentesProyecto = gerentesProyecto;
        }

        public get getGerentesProyecto() : GerentesProyecto[]{
            return this._gerentesProyecto;
        }

        public set setFunciones(funciones : string){
            this._funciones = funciones;
        }

        public get getFunciones() : string{
            return this._funciones;
        }

        public anhadirGerentesProyecto(gerenteProyecto : GerentesProyecto) : void{
            this._gerentesProyecto.push(gerenteProyecto);
        }

        public toString(): string {
            return super.toString() + `. Mi función es ${this._funciones} y tengo a mi cargo ${this._gerentesProyecto.length} Gerentes de Proyecto`;
        }
    }

    class GerentesProyecto extends Empleado{
        constructor(
            id : number,
            nombre : string,
            tipoEmpleado : tipoEmpleado,
            private _proyectos : number,
            private _programadores : Programador[])
        {super(id, nombre, tipoEmpleado)}

        public anhadirProgramadores(programador : Programador) : void{
            this._programadores.push(programador);
        }

        public toString(): string {
            return super.toString() + `. Tengo ${this._proyectos} proyectos a mi cargo y ${this._programadores.length} progamadores detrás`;
        }
    }

    type Especialidad = 'FRONT-END' | 'BACK-END' | 'FULL-STACK'
    class Programador extends Empleado{
        constructor(
            id : number,
            nombre : string,
            tipoEmpleado : tipoEmpleado,
            private _especialidad : Especialidad)
        {super(id, nombre, tipoEmpleado)}

        public set setEspecialidad(especialidad : Especialidad){
            this._especialidad = especialidad;
        }

        public get getEspecialidad(){
            return this._especialidad;
        }

        public toString(): string {
            return super.toString() + `. Soy ${this._especialidad}`;
        }
    }

    // Vamos a declarar las instancias
    let gerenteLista : GerentesProyecto[] = [];
    let programadores : Programador[] = [];
    let gerente = new Gerente(1,'Adri','GERENTE','Administración', gerenteLista);
    let gerenteProyecto = new GerentesProyecto(2,'Claudia','GERENTE DE PROYECTOS',8, programadores);
    let programador1 = new Programador(3 , 'Igledev', 'PROGRAMADORES', 'FRONT-END')
    let programador2 = new Programador(4 , 'Adrián', 'PROGRAMADORES', 'BACK-END')
    let programador3 = new Programador(5 , 'Moure', 'PROGRAMADORES', 'FULL-STACK')

    //Añadimos los empleados a sus correspondientes arrays.
    gerenteProyecto.anhadirProgramadores(programador1);
    gerenteProyecto.anhadirProgramadores(programador2);
    gerenteProyecto.anhadirProgramadores(programador3);
    console.log(gerenteProyecto.toString());

    gerente.anhadirGerentesProyecto(gerenteProyecto);
    console.log(gerente.toString());