// Ejercicio 1º
    // Declaramos el conjunto de datos
        let idolos : Array<string> = ['Igledev', 'Messi'];
        console.log(`Mis idolos principales ${idolos}`);
    // Añadir elemento al final
        idolos.push('MoureDev');
        console.log(`Añdiendo un nuevo ídolo ${idolos}`);
    // Añadir elemento al principio
        idolos.unshift('Mi novia');
        console.log(`Actualizando mi primer ídolo ${idolos}`);
    // Añade varios elementos en bloque al final.
        let idolos2 : Array<string> = ['Yoshi', 'Ana Pontón'];
        idolos.push(...idolos2);
        console.log(`Añadiendo más ídolos ${idolos}`);
    // Añade varios elementos según la posición deseada
        let masIdolos : Array<string> = ['Lahm', 'Luis Suarez', 'Neymar'];
        idolos.splice(6, 0, ...masIdolos);
        console.log(`Añadiendo más ídolos pero con posición${idolos}`);
    // Actualiza el valor de un elemento en una posición concreta
        idolos[1] = 'Arrian';
        console.log(`Cambiando el ídolo${idolos}`);
    // Comprueba si un elemento está en un conjunto.
        let idoloEncontrado = idolos.find(idolo => idolo === 'Messi' ? true : false);
        console.log(`Esta el ídolo en la lista? ${idoloEncontrado}`);
    // Elimina todo el contenido del conjunto
        idolos.length = 0;
        console.log(`Eliminando todos los idolos: ${idolos}`);

// Ejercicio Extra
    let numeros1: Array<number> = [1, 2, 3, 4];
    let numeros2: Array<number> = [3, 4, 5, 6];
    let union: Set<number> = new Set();

    // Union
        numeros1.forEach(number => union.add(number));
        numeros2.forEach(number => union.add(number));
        console.log(`Unión de numeros: ${union}`);
    // Interseccion
        let interseccion: Set<number> = new Set();
        numeros1.forEach(n1 => {
            numeros2.forEach(n2 => {
                if(n1 === n2){
                  interseccion.add(n1);
                }
            })
        })
        console.log(`Interseccion de numeros: ${interseccion}`);
    // Diferencia
        let diferencia: Set<number> = new Set();
        numeros1.forEach(number => diferencia.add(number));
        numeros2.forEach(number => {
            if (diferencia.has(number)){
              diferencia.delete(number);
            }
        })
        console.log(`Diferencia de numeros: ${diferencia}`);
    // Diferencia simetrica
        let difSimetrica: Set<number> = new Set();
        numeros1.forEach(number => difSimetrica.add(number))
        numeros2.forEach(number => {
            if(difSimetrica.has(number)){
              difSimetrica.delete(number);
            }else{
              difSimetrica.add(number);
            }
        });
        console.log(`Diferencia SIMÉTRICA de números: ${difSimetrica}`)