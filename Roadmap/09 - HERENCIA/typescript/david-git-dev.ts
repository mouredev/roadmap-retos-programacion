/*
 * EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal
 */
class Animal {
  private _habitat: string;
  private _dieta: any[];
  constructor(habitat: string, dieta: any[]) {
    this._habitat = habitat;
    this._dieta = dieta;
  }
  sonido() {
    return "sonido caracteristico de un animal";
  }
}
class Perro extends Animal {
  private _nombre: string;
  private _especie: string;

  constructor(nombre: string, especie: string, habitat: string, dieta: any[]) {
    super(habitat, dieta);
    this._nombre = nombre;
    this._especie = especie;
  }
  sonido() {
    return "¡Guau guau!";
  }
}
class Gato extends Animal {
  private _nombre: string;
  private _especie: string;

  constructor(nombre: string, especie: string, habitat: string, dieta: any[]) {
    super(habitat, dieta);
    this._nombre = nombre;
    this._especie = especie;
  }
  sonido() {
    return "¡Miau Miau!";
  }
}
const chauchau = new Perro("canela", "canino", "casa", [
  "croquetas",
  "pollo",
  "hueso",
]);
chauchau.sonido();
const naranja = new Gato("sr.tims", "felino", "casa", [
  "croquetas",
  "pescado",
  "whiskas",
]);
naranja.sonido();
/*
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.
 */
class Empleado{
  private _identificador:BigInt
  private _nombre:string
  private _salario:BigInt
  private _fechaDeContratacion:Date
  constructor(identificador:BigInt,nombre:string,salario:BigInt){
    this._identificador = identificador
this._nombre = nombre
    this._salario = salario
  }
}
class Gerente extends Empleado{
  private _usuariosACargo: Array<Empleado>
  constructor(identificador:BigInt,nombre:string,salario:BigInt,subordinados:Array<Empleado>){
    super(identificador,nombre,salario)
    this._usuariosACargo = subordinados
  }
  visionEstrategica(){

  }
  gestionDeRecursos(){}
  tomaDeDecisiones(){}
  supervisionGeneral(){}
  relacionesExternas(){}
}
class GerenteDeProyecto extends Empleado{
  private _usuariosACargo: Array<Empleado>;
  private _proyectosAsignados:Array<Proyecto>
  constructor(identificador:BigInt,nombre:string,salario:BigInt,subordinados:Array<Empleado>,proyectos:Array<Proyecto>){
    super(identificador,nombre,salario)
    this._usuariosACargo = subordinados
    this._proyectosAsignados = proyectos
  }
  planificacionDeProyectos(){}
  gestionDeEquipos(){}
  controlDePresupuestos(){}
  seguimientoYReportes(){}
  resolucionDeProblemas(){}
}
class Programador extends Empleado{
  private _experiencia:number = 0;
  private _proyectosAsignados: Array<Proyecto>;
  constructor(identificador:BigInt,nombre:string,salario:BigInt,experiencia:number,proyectosAsignados:Proyecto[]){
    super(identificador,nombre,salario)
    this._experiencia = experiencia
    this._proyectosAsignados = proyectosAsignados
  }
  escribirCodigo(){}
  depurarCodigo(){}
  colaborarEnProyectos(){}
  actualizarConocimientos(){}
}

