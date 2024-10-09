/**
 * TEORÍA: Conjuntos (Sets) en TypeScript
 * 
 * TypeScript utiliza la misma implementación de Set que JavaScript, pero añade
 * tipado estático y algunas mejoras en la sintaxis. Los Sets en TypeScript:
 * 
 * 1. Son colecciones de valores únicos
 * 2. Pueden contener cualquier tipo de valor
 * 3. Mantienen el orden de inserción
 * 4. Proporcionan operaciones eficientes para añadir, eliminar y verificar elementos
 * 
 * TypeScript añade la capacidad de tipar los Sets, por ejemplo:
 * let stringSet: Set<string> = new Set<string>();
 */

class SetOperations<T> {
    private conjunto: Set<T>;

    constructor() {
        this.conjunto = new Set<T>();
    }

    /**
     * Muestra el contenido actual del conjunto
     */
    private mostrarConjunto(mensaje: string): void {
        console.log(`${mensaje}: [${Array.from(this.conjunto).join(", ")}]`);
    }

    /**
     * 1. Añade un elemento al final
     */
    agregarAlFinal(elemento: T): void {
        this.conjunto.add(elemento);
        this.mostrarConjunto(`Después de añadir '${String(elemento)}' al final`);
    }

    /**
     * 2. Añade un elemento al "principio"
     * Nota: En realidad, en un Set no hay concepto de principio o final
     * Simulamos esto convirtiendo a array, modificando y volviendo a Set
     */
    agregarAlPrincipio(elemento: T): void {
        const tempArray = Array.from(this.conjunto);
        this.conjunto = new Set([elemento, ...tempArray]);
        this.mostrarConjunto(`Después de añadir '${String(elemento)}' al principio`);
    }

    /**
     * 3. Añade varios elementos en bloque al final
     */
    agregarVariosAlFinal(elementos: T[]): void {
        elementos.forEach(elemento => this.conjunto.add(elemento));
        this.mostrarConjunto("Después de añadir varios elementos al final");
    }

    /**
     * 4. Añade varios elementos en bloque en una posición concreta
     */
    agregarVariosEnPosicion(elementos: T[], posicion: number): void {
        const tempArray = Array.from(this.conjunto);
        tempArray.splice(posicion, 0, ...elementos);
        this.conjunto = new Set(tempArray);
        this.mostrarConjunto(`Después de añadir elementos en posición ${posicion}`);
    }

    /**
     * 5. Elimina un elemento en una posición concreta
     */
    eliminarEnPosicion(posicion: number): void {
        const tempArray = Array.from(this.conjunto);
        if (posicion >= 0 && posicion < tempArray.length) {
            tempArray.splice(posicion, 1);
            this.conjunto = new Set(tempArray);
            this.mostrarConjunto(`Después de eliminar elemento en posición ${posicion}`);
        }
    }

    /**
     * 6. Actualiza el valor de un elemento en una posición concreta
     */
    actualizarEnPosicion(posicion: number, nuevoValor: T): void {
        const tempArray = Array.from(this.conjunto);
        if (posicion >= 0 && posicion < tempArray.length) {
            tempArray[posicion] = nuevoValor;
            this.conjunto = new Set(tempArray);
            this.mostrarConjunto(`Después de actualizar elemento en posición ${posicion}`);
        }
    }

    /**
     * 7. Comprueba si un elemento está en el conjunto
     */
    contiene(elemento: T): boolean {
        const resultado = this.conjunto.has(elemento);
        console.log(`¿El conjunto contiene '${String(elemento)}'? ${resultado ? "Sí" : "No"}`);
        return resultado;
    }

    /**
     * 8. Elimina todo el contenido del conjunto
     */
    limpiar(): void {
        this.conjunto.clear();
        this.mostrarConjunto("Después de limpiar el conjunto");
    }

    /**
     * Obtiene el conjunto actual
     */
    obtenerConjunto(): Set<T> {
        return this.conjunto;
    }
}

/**
 * Clase estática para operaciones extra con conjuntos
 */
class OperacionesExtra {
    /**
     * Unión de dos conjuntos
     */
    static union<T>(conjunto1: Set<T>, conjunto2: Set<T>): Set<T> {
        return new Set([...conjunto1, ...conjunto2]);
    }

    /**
     * Intersección de dos conjuntos
     */
    static interseccion<T>(conjunto1: Set<T>, conjunto2: Set<T>): Set<T> {
        return new Set([...conjunto1].filter(x => conjunto2.has(x)));
    }

    /**
     * Diferencia de dos conjuntos
     */
    static diferencia<T>(conjunto1: Set<T>, conjunto2: Set<T>): Set<T> {
        return new Set([...conjunto1].filter(x => !conjunto2.has(x)));
    }

    /**
     * Diferencia simétrica de dos conjuntos
     */
    static diferenciaSimetrica<T>(conjunto1: Set<T>, conjunto2: Set<T>): Set<T> {
        const diferencia1 = OperacionesExtra.diferencia(conjunto1, conjunto2);
        const diferencia2 = OperacionesExtra.diferencia(conjunto2, conjunto1);
        return OperacionesExtra.union(diferencia1, diferencia2);
    }
}

// Función para mostrar un conjunto
function mostrarConjunto<T>(nombre: string, conjunto: Set<T>): void {
    console.log(`${nombre}: [${Array.from(conjunto).join(", ")}]`);
}

// Demostración de uso
function demostrarOperaciones(): void {
    console.log("PARTE 1: OPERACIONES BÁSICAS");
    const demo = new SetOperations<string>();

    demo.agregarAlFinal("Elemento1");
    demo.agregarAlPrincipio("Elemento2");
    demo.agregarVariosAlFinal(["Elemento3", "Elemento4", "Elemento5"]);
    demo.agregarVariosEnPosicion(["ElementoA", "ElementoB"], 2);
    demo.eliminarEnPosicion(3);
    demo.actualizarEnPosicion(1, "ElementoActualizado");
    demo.contiene("Elemento1");
    demo.limpiar();

    console.log("\nPARTE 2: OPERACIONES EXTRA");
    const conjunto1 = new Set([1, 2, 3, 4, 5]);
    const conjunto2 = new Set([4, 5, 6, 7, 8]);

    mostrarConjunto("Conjunto 1", conjunto1);
    mostrarConjunto("Conjunto 2", conjunto2);

    const union = OperacionesExtra.union(conjunto1, conjunto2);
    mostrarConjunto("Unión", union);

    const interseccion = OperacionesExtra.interseccion(conjunto1, conjunto2);
    mostrarConjunto("Intersección", interseccion);

    const diferencia = OperacionesExtra.diferencia(conjunto1, conjunto2);
    mostrarConjunto("Diferencia (conjunto1 - conjunto2)", diferencia);

    const diferenciaSimetrica = OperacionesExtra.diferenciaSimetrica(conjunto1, conjunto2);
    mostrarConjunto("Diferencia simétrica", diferenciaSimetrica);
}

// Ejecutar la demostración
demostrarOperaciones();