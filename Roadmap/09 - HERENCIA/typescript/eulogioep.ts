// Ejemplo de implementación del concepto de herencia en TypeScript

// Definición de la clase base (superclase) Animal
class Animal {
    protected especie: string;
    protected sonido: string;
  
    constructor(especie: string, sonido: string) {
      this.especie = especie;
      this.sonido = sonido;
    }
  
    // Método que muestra el sonido que hace el animal
    public hacerSonido(): string {
      return `El ${this.especie} hace: ${this.sonido}`;
    }
  }
  
  // Definición de la subclase Perro
  class Perro extends Animal {
    private nombre: string;
  
    constructor(nombre: string, especie: string, sonido: string) {
      super(especie, sonido); // Llamada al constructor de la superclase
      this.nombre = nombre;
    }
  
    // Método exclusivo de la subclase Perro
    public ladrar(): string {
      return `${this.nombre} lanza un ladrido`;
    }
  }
  
  // Definición de la subclase Gato
  class Gato extends Animal {
    private nombre: string;
  
    constructor(nombre: string, especie: string, sonido: string) {
      super(especie, sonido); // Llamada al constructor de la superclase
      this.nombre = nombre;
    }
  
    // Método exclusivo de la subclase Gato
    public maullar(): string {
      return `${this.nombre} emite un maullido`;
    }
  }
  
  // Ejemplo de implementación adicional (dificultad extra)
  // Definición de la clase base (superclase) Empleado
  class Empleado {
    protected id: number;
    protected nombre: string;
  
    constructor(id: number, nombre: string) {
      this.id = id;
      this.nombre = nombre;
    }
  }
  
  // Definición de la subclase Gerente que hereda de Empleado
  class Gerente extends Empleado {
    private subordinados: Empleado[];
  
    constructor(id: number, nombre: string, subordinados: Empleado[]) {
      super(id, nombre);
      this.subordinados = subordinados;
    }
  
    // Método exclusivo de la subclase Gerente
    public informarSobreSubordinados(): string {
      let informacion = `El gerente ${this.nombre} tiene a los siguientes subordinados: \n`;
      informacion += this.subordinados.map((subordinado) => ` - ${subordinado.nombre}\n`).join('');
      return informacion;
    }
  }
  
  // Definición de la subclase GerenteDeProyectos que hereda de Empleado
  class GerenteDeProyectos extends Empleado {
    private proyectos: string[];
  
    constructor(id: number, nombre: string, proyectos: string[]) {
      super(id, nombre);
      this.proyectos = proyectos;
    }
  
    // Método exclusivo de la subclase GerenteDeProyectos
    public informarSobreProyectos(): string {
      let informacion = `El gerente de proyectos ${this.nombre} tiene los siguientes proyectos: \n`;
      informacion += this.proyectos.map((proyecto) => ` - ${proyecto}\n`).join('');
      return informacion;
    }
  }
  
  // Definición de la subclase Programador que hereda de Empleado
  class Programador extends Empleado {
    private lenguajes: string[];
  
    constructor(id: number, nombre: string, lenguajes: string[]) {
      super(id, nombre);
      this.lenguajes = lenguajes;
    }
  
    // Método exclusivo de la subclase Programador
    public informarSobreLenguajes(): string {
      let informacion = `El programador ${this.nombre} domina los siguientes lenguajes: \n`;
      informacion += this.lenguajes.map((lenguaje) => ` - ${lenguaje}\n`).join('');
      return informacion;
    }
  }
  
  // Ejemplo de uso
  const perro = new Perro("Lucky", "Perro", "Gua");
  console.log(perro.hacerSonido()); // El Perro hace: Gua
  console.log(perro.ladrar()); // Lucky lanza un ladrido
  
  const gato = new Gato("Whiskers", "Gato", "Miau");
  console.log(gato.hacerSonido()); // El Gato hace: Miau
  console.log(gato.maullar()); // Whiskers emite un maullido
  
  const gerente = new Gerente(1, "Juan Perez", [new Programador(2, "Maria Rodriguez", ["JavaScript", "TypeScript"])]);
  console.log(gerente.informarSobreSubordinados());
  
  const gerenteProyectos = new GerenteDeProyectos(3, "Luis Martinez", ["Proyecto A", "Proyecto B"]);
  console.log(gerenteProyectos.informarSobreProyectos());
  
  const programador = new Programador(4, "Karla Sanchez", ["JavaScript", "TypeScript"]);
  console.log(programador.informarSobreLenguajes());