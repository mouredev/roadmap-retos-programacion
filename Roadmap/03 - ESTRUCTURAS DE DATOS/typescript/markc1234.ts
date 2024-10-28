(() => {    
    // EJERCICIO:
    // Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
    // array
    const arr:number[] = [1,2,3,4]
    const arr2: Array<string> = ["a", "e", "i", "o", "u"]

    // tupla
    const tup1: [number, string, boolean] = [10, "cadena", true]

    // enum
    enum DiasSemana {
        "LUNES"= "lunes",
        "MARTES"= "martes",
        "MIERCOLES"= "miercoles",
        "JUEVES"= "jueves",
        "VIERNES"= "viernes",
        "SABADO"= "sabado",
        "DOMINGO"= "domingo",
    }

    // interface (objetos)
    interface Person {
        name: string;
        age: number;
    }
    let person: Person = { name: "Fabricio", age: 20 };
    
    // clases
    class Animal {
        name: string;
        constructor(name: string) {
            this.name = name;
        }
        move(distance: number = 0) {
            console.log(`${this.name} moved ${distance} meters.`);
        }
    }
    let dog = new Animal("Dog");
    dog.move(10);

    // genericos
    function identity<T>(arg: T): T {
        return arg;
    }
    let output = identity<string>("myString");
    
    // maps y sets
    let map = new Map<string, number>();
    map.set("one", 1);
    map.set("two", 2);

    let set = new Set<number>();
    set.add(1);
    set.add(2);

    // union types
    let union: string | number;
    union = "hello";
    union = 42;

    // intersection types
    interface Name {
        name: string;
    }
    interface Age {
        age: number;
    }
    type PersonType = Name & Age;
    let personIntersection: PersonType = { name: "Alice", age: 25 };

    // Utiliza operaciones de inserción, borrado, actualización y ordenación.
    arr2.push("A", "E", "I", "O", "U")
    arr.pop()

    
    // DIFICULTAD EXTRA (opcional):
    // Crea una agenda de contactos por terminal.
    // Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
    // Cada contacto debe tener un nombre y un número de teléfono.
    // El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación los datos necesarios para llevarla a cabo.
    // El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos. (o el número de dígitos que quieras)
    // También se debe proponer una operación de finalización del programa.
})()