// TEORÍA: Conjuntos (Sets) en JavaScript
/*
 * Un Set en JavaScript es una estructura de datos que permite almacenar valores únicos
 * de cualquier tipo. A diferencia de los arrays:
 * - Los elementos en un Set son únicos
 * - No hay índices numéricos para acceder a los elementos
 * - El orden de los elementos se mantiene según el orden de inserción
 *
 * Los Sets son útiles cuando necesitamos asegurarnos de que no hay duplicados
 * y cuando el orden de los elementos no es crucial.
 */

// Función principal que demuestra todas las operaciones
function demostracionSets() {
    console.log("PARTE 1: OPERACIONES BÁSICAS CON SETS");
    
    // Creación de un Set
    let conjunto = new Set();
    console.log("Conjunto inicial:", conjunto);

    // 1. Añadir un elemento al final
    conjunto.add("Elemento1");
    console.log("Después de añadir un elemento:", conjunto);

    // 2. Añadir un elemento al "principio"
    // NOTA: En realidad, en un Set no hay concepto de principio o final
    conjunto.add("Elemento2");
    console.log("Después de añadir otro elemento:", conjunto);

    // 3. Añadir varios elementos en bloque
    const nuevosElementos = ["Elemento3", "Elemento4", "Elemento5"];
    nuevosElementos.forEach(elemento => conjunto.add(elemento));
    console.log("Después de añadir varios elementos:", conjunto);

    // 4. Añadir elementos en una posición concreta
    // NOTA: Los Sets no permiten insertar en posiciones específicas
    // Podemos convertir a array, modificar y volver a Set
    let arrayTemporal = Array.from(conjunto);
    arrayTemporal.splice(2, 0, "ElementoA", "ElementoB");
    conjunto = new Set(arrayTemporal);
    console.log("Después de 'insertar' en posición específica:", conjunto);

    // 5. Eliminar un elemento
    conjunto.delete("Elemento3");
    console.log("Después de eliminar 'Elemento3':", conjunto);

    // 6. Actualizar un elemento
    // NOTA: No se pueden actualizar elementos directamente
    // Hay que eliminar el viejo y añadir el nuevo
    if (conjunto.delete("Elemento4")) {
        conjunto.add("Elemento4Actualizado");
    }
    console.log("Después de actualizar 'Elemento4':", conjunto);

    // 7. Comprobar si un elemento está en el conjunto
    const contiene = conjunto.has("Elemento1");
    console.log("¿Contiene 'Elemento1'?", contiene);

    // 8. Eliminar todo el contenido
    conjunto.clear();
    console.log("Después de limpiar el conjunto:", conjunto);

    console.log("\nPARTE 2: OPERACIONES EXTRA CON SETS");
    
    // Creamos dos conjuntos para las operaciones
    const conjunto1 = new Set([1, 2, 3, 4, 5]);
    const conjunto2 = new Set([4, 5, 6, 7, 8]);
    
    // 1. Unión
    const union = new Set([...conjunto1, ...conjunto2]);
    console.log("Unión:", union);
    
    // 2. Intersección
    const interseccion = new Set(
        [...conjunto1].filter(x => conjunto2.has(x))
    );
    console.log("Intersección:", interseccion);
    
    // 3. Diferencia
    const diferencia = new Set(
        [...conjunto1].filter(x => !conjunto2.has(x))
    );
    console.log("Diferencia (conjunto1 - conjunto2):", diferencia);
    
    // 4. Diferencia simétrica
    const diferenciaSimetrica = new Set(
        [...conjunto1].filter(x => !conjunto2.has(x))
        .concat([...conjunto2].filter(x => !conjunto1.has(x)))
    );
    console.log("Diferencia simétrica:", diferenciaSimetrica);
}

// Funciones auxiliares útiles para trabajar con Sets
const utilidadesSets = {
    // Unión de dos sets
    union: (setA, setB) => new Set([...setA, ...setB]),
    
    // Intersección de dos sets
    interseccion: (setA, setB) => 
        new Set([...setA].filter(x => setB.has(x))),
    
    // Diferencia de dos sets
    diferencia: (setA, setB) => 
        new Set([...setA].filter(x => !setB.has(x))),
    
    // Diferencia simétrica de dos sets
    diferenciaSimetrica: (setA, setB) => 
        new Set([...setA].filter(x => !setB.has(x))
                .concat([...setB].filter(x => !setA.has(x))))
};

// Ejecutar la demostración
demostracionSets();