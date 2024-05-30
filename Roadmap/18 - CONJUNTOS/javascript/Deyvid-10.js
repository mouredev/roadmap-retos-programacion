// Conjuntos

function agregarInicio(set, valor)
{
    let nuevoConjunto = new Set()
    nuevoConjunto.add(valor)

    for (let s of set) {
        nuevoConjunto.add(s)
    }

    return nuevoConjunto
}

function agregarVariosFinal(set, valores)
{
    for (let v of valores) {
        set.add(v)
    }
}

function agregarVariosPosicion(set, posicion, valores)
{
    let cont = -1
    let nuevoConjunto = new Set()
    
    for (let s of set) {
        cont ++
        
        if(cont == posicion)
        {
            for (let v of valores) 
            {
                nuevoConjunto.add(v)
            }
        }

        nuevoConjunto.add(s)
    }

    if(posicion > cont)
    {
        console.log("Esta posicion no existe");
    }

    return nuevoConjunto
}

function eliminar(set, posicion)
{
    let cont = -1
    
    for (let s of set) {
        cont ++
        
        if(cont == posicion)
        {
            set.delete(s)
        }
    }
}

function actualizar(set, posicion, valor)
{
    let cont = -1
    let nuevoConjunto = new Set()

    for (let s of set) {
        cont ++
        
        if(cont == posicion)
        {
            nuevoConjunto.add(valor)
        }
        else
        {
            nuevoConjunto.add(s)
        }
    }

    if(posicion > cont)
    {
        console.log("Esta posicion no existe");
    }

    return nuevoConjunto
}

let conjunto = new Set() // Crear el conjunto

conjunto.add(1) // Agregar al final del conjunto
conjunto.add(2) // Agregar al final del conjunto
conjunto.add(3) // Agregar al final del conjunto
console.log(conjunto);

conjunto = agregarInicio(conjunto, 0) // Agregar al inicio del conjunto
console.log(conjunto);

agregarVariosFinal(conjunto, [5, 6, 7]) // Agregar varios elementos al final
console.log(conjunto);

conjunto = agregarVariosPosicion(conjunto, 2, [8, 9, 10]) // Agregar varios elementos en una posicion concreta
console.log(conjunto);

eliminar(conjunto, 2) // Eliminar un elemento en una posición concreta
console.log(conjunto);

conjunto = actualizar(conjunto, 2, 11) // Actualiza el valor de un elemento en una posición concreta
console.log(conjunto);

console.log(`La comprobacion del elemnto es: ${conjunto.has(2)}`); // Comprueba si un elemento está en un conjunto.

conjunto.clear() // Eliminar todos los elementos
console.log(conjunto);


// DIFICULTAD EXTRA

let conjuntoA = new Set([1, 2, 3, 10, 12])
let conjuntoB = new Set([4, 5, 6, 10, 12])

// Union
let unionConjunto = new Set([...conjuntoA, ...conjuntoB])
console.log(unionConjunto);

// Intersección
let intersecciónConjunto = new Set([...conjuntoA].filter(elemento => conjuntoB.has(elemento)))
console.log(intersecciónConjunto);

// Diferencia 
let diferenciaConjunto = new Set([...conjuntoA].filter(elemento => !(conjuntoB.has(elemento))))
console.log(diferenciaConjunto);

// Diferencia simétrica
let simetricaConjunto = new Set([...conjuntoA, ...conjuntoB].filter(elemento => !(conjuntoB.has(elemento)) || !(conjuntoA.has(elemento))))
console.log(simetricaConjunto);
