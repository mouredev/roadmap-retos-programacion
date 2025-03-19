// 1º Ejercicio
    /**
     * Hay varios tipo de clases y que se pueden utilizar en clases
     * Herencia (Clases Extendidas), Abstractas, Interfaces, etc... 
    */

    // Vamos a empezar por las clases más básicas hasta la más complicada:
        // class
        class Persona{
            // Un constructor se encarga de inicializar las propiedades de la clase cuando se crea el objeto.
            constructor(private _nombre : string,
                private _edad : number, 
                private _profesion : string)
            {};
            /**
             * En este caso estamos utilizando public pero hay más, lo normal no es utilizarlo ahora veremos porqué.
             * public => Es la que vamos a utilizar en el ejemplo y significa que podemos usarlas desde cualquier lugar
             * no suele ser lo normal.
             * private => Se puede acceder solo a sus propiedades desde su misma clase. Para solventar esto hacemos los
             * famosos métodos, si un atributo es privado se utiliza el '_' delante.
             * protected => Se puede acceder a sus propiedades desde su clase y desde otra que herede esa clase.
             */

            // Los get se utilizan para pillar el valor de la propiedad
            get nombre() : string{
                return this._nombre;
            }

            //Los set se utilizan para establecer sus valores
            set nombre(nombre : string){
                this._nombre = nombre;
            }

            get edad() : number{
                return this._edad;
            }

            set edad(edad : number){
                this._edad = edad;
            }

            get profesion() : string{
                return this._profesion;
            }

            set profesion(profesion : string){
                this._profesion = profesion;
            }

            //Tambien podemos incluir métodos
            cumplirAnhos() : number{
                this.edad = this.edad + 1;
                return this.edad;
            }

            cambiarProfesion(profesion : string) : string{
                this.profesion = profesion;
                return this.profesion;
            }

            // Esta funión nos va a servir para mostrar la información de nuestra persona
            toString() : string{
                return `Mi nombre es: ${this.nombre} tengo ${this.edad} Años, mi profesion es ser un/a ${this.profesion}`;
            }
        }

        //Vamos a crear a una persona
        let persona = new Persona('Igledev', 19, 'Programador');    // Le ponemos datos por defecto.
        console.log(persona)
        /**
         * Si hacemos nos va a aparecer un objeto con nuestras propiedades pero podremos acceder a ellas porque
         * estan en 'private', si fuese 'public' no tendríamos problema. Para ello vamos a utilizar los conocidos
         * setters & getters
        */

        //Una vez hechos los setter & getters podremos acceder a las propiedades
        // console.log(persona.nombre + ' ' + persona.edad + ' ' + persona.profesion); // Nos saldrá IgleDev 19 Profesión.
        //En vez de utilizar todo esto, lo hacemos llamando a una función
        console.log(persona.toString());

        //Utilizamos los métodos que hemos puesto en la clase
        persona.cumplirAnhos();
        persona.cambiarProfesion('Desarrollador Web');
        console.log(persona.toString());
        // Nos saldrá que nuestra edad ahora es de 20 y que somos desarrolladores web

        // Herencia (clases extendidas)
        /**
         * Que tenga la palabra reservada 'extends' hace referencia a que vamos a tener que utilar los
         * parametros establecedidos en la clase Padre (en nuestro caso la clase Persona)
         */
        class Hijo extends Persona{
            constructor(nombre : string, 
            edad : number, 
            profesion : string, 
            private _escuela : string)
            {super(nombre, edad, profesion)}    // El super se utiliza para avisar de que las propiedades que estén entre los () son de la clase Padre
                
            //Hacemos lo setter & getters necesarios
            get escuela() : string{
                return this._escuela;
            }

            set escuela(escuela : string){
                this._escuela = escuela; 
            }
        
            toString(): string {
                return super.toString() + ' y mi escuela es: ' + this.escuela;  //Si utilizamos super más un método va a heredar tambien el contenido del método padre
            }
        }

        let hijo = new Hijo('Arrian', 14, 'Estudiante', 'Montecastelo');
        console.log(hijo.toString());

        //Abstracta
        /**
         * Una clase abstracta se utiliza cuando sabemso que nuncan la vamos a utilizar pero 
         * si sus propiedades y que estén en clases derivadas.
         * 
        */

        abstract class ProductoDatos{
            constructor(private _nombre : string, 
                private _desc : string, 
                private _creado_en : Date, 
                private _creado_por : number)
            {};

            getFullYear(){
                return this._creado_en.getFullYear();
            }
        
            getFullDesc(){
                return this._nombre + ' ' + this._desc;
            }

            //Tambien puede contener métodos abstractos que obviamente solo se pueden utilizar en ella
            abstract guardar() : void;  // No se utilizan {}.
        }

        //Ahora es cuando vamos a entender mejor esto:
        class Producto extends ProductoDatos{
            constructor(
                nombre : string,
                desc : string,
                creado_en : Date,
                creado_por : number,
                public stock : number,)
            {super(nombre, desc, creado_en, creado_por)};

            override guardar(): void {
                console.log('Se ha guardado');
            }

        }

        // let datos = new ProductoDatos(). Si hacemos esto nos va saltar un error, debido a que una clase abstracta NO se puede instanciar

        let producto1 = new Producto('iPhone','Movil',new Date(), 1, 100);
        producto1.guardar();    // Podremos acceder a sus métodos!


        //Interfaces
        /**
         * Se utilizan cuando NO vamos a compartir lógica pero si necesitamos la implementación de métodos y propiedades.
        */

        interface Animal{
            nombre : string, 
            caminar() : string;
            onomatopeya() : string;
        } // En una Interfaz se pueden declarar tanto propiedades como métodos.

        class Gato implements Animal{
            nombre: string = 'Zelda';

            caminar(): string {
                return 'va caminando...';
            }

            onomatopeya(): string {
                return 'meow';
            }
        }

        let gato1 = new Gato();
        console.log(`El nombre del gato es ${gato1.nombre} y ${gato1.caminar()} mientras dice ${gato1.onomatopeya()}`);

// Ejercicio Extra
class Nodo<T> {
    dato: T | null;
    siguiente: Nodo<T> | null;

    constructor(dato: T) {
        this.dato = dato;
        this.siguiente = null;
    }
}

class Pila<T> {
    tope: Nodo<T> | null;

    constructor() {
        this.tope = null;
    }

    isEmpty(): boolean {
        return this.tope === null;
    }

    push(dato: T): void {
        const nuevoNodo = new Nodo(dato);
        nuevoNodo.siguiente = this.tope;
        this.tope = nuevoNodo;
    }

    pop(): T | null {
        if (this.isEmpty()) {
            return null;
        }

        const datoEliminado = this.tope!.dato;
        this.tope = this.tope!.siguiente;

        return datoEliminado;
    }

    size(): number {
        let contador = 0;
        let actual = this.tope;

        while (actual !== null) {
            contador++;
            actual = actual.siguiente;
        }

        return contador;
    }

    print(): void {
        let actual = this.tope;

        while (actual !== null) {
            console.log(actual.dato);
            actual = actual.siguiente;
        }
    }
}

class Cola<T> {
    frente: Nodo<T> | null;
    fin: Nodo<T> | null;

    constructor() {
        this.frente = null;
        this.fin = null;
    }

    isEmpty(): boolean {
        return this.frente === null;
    }

    enqueue(dato: T): void {
        const nuevoNodo = new Nodo(dato);

        if (this.isEmpty()) {
            this.frente = nuevoNodo;
            this.fin = nuevoNodo;
        } else {
            this.fin!.siguiente = nuevoNodo;
            this.fin = nuevoNodo;
        }
    }

    dequeue(): T | null {
        if (this.isEmpty()) {
            return null;
        }

        const datoEliminado = this.frente!.dato;

        if (this.frente === this.fin) {
            // Último elemento en la cola
            this.frente = null;
            this.fin = null;
        } else {
            this.frente = this.frente!.siguiente;
        }

        return datoEliminado;
    }

    size(): number {
        let contador = 0;
        let actual = this.frente;

        while (actual !== null) {
            contador++;
            actual = actual.siguiente;
        }

        return contador;
    }

    print(): void {
        let actual = this.frente;

        while (actual !== null) {
            console.log(actual.dato);
            actual = actual.siguiente;
        }
    }
}

// Ejemplo de uso:

let pila = new Pila<number>();
pila.push(1);
pila.push(2);
pila.push(3);

console.log('Pila:');
pila.print();
console.log('Tamaño de la pila:', pila.size());

console.log('Elemento eliminado de la pila:', pila.pop());
console.log('Pila después de eliminar un elemento:');
pila.print();

let cola = new Cola<string>();
cola.enqueue('A');
cola.enqueue('B');
cola.enqueue('C');

console.log('\nCola:');
cola.print();
console.log('Tamaño de la cola:', cola.size());

console.log('Elemento eliminado de la cola:', cola.dequeue());
console.log('Cola después de eliminar un elemento:');
cola.print();