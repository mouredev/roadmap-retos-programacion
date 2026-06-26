//Arrays/Arreglos -- Lista ordenada de elementos.

const arr = ["Messi", "Ronaldo", "Johan Cruyff", "Zinedine Zidane"]
console.log(arr)

arr.push("Ahmed Musa") //inserción
console.log(arr)

arr.pop() // borrado 
console.log(arr)

console.log(arr[2]) //acceso
arr[2] = "Maradona" //actualización
console.log(arr)

arr.sort();//Reordenar datos
console.log(arr)

//Objects -- Estructura clave–valor general.

const persona = {contacto: "Juan Andrés", edad: 25}
console.log(persona) 

persona.nacionalidad = "Venezolano" // inserción
console.log(persona)

console.log(persona.edad) // acceso

persona.edad = 30   //Actualización
persona["edad"] = 30

console.log(persona)

delete persona.nacionalidad //borrado

console.log(persona)



//Maps --- Diccionario ordenado con claves de cualquier tipo.

const mapa = new Map()

mapa.set("contacto", "Rodrigo") //inserción
console.log(mapa)

mapa.get("contacto") // Acceso
console.log(mapa.get("contacto"))

mapa.set("contacto", "PestJB") // Actualización
console.log(mapa)

mapa.delete("contacto") // Borrado
console.log(mapa)

mapa.set("contacto", "Humberto")
console.log(mapa)

//mapa Ordenado

let mapaOrdenado = [...mapa.values()].sort()
console.log(mapaOrdenado)

//Sets --- Colección sin duplicados.

const conjunto = new Set()

conjunto.add(1) //inserción
conjunto.add(500)
conjunto.add(500) //no se añade porque no acepta duplicados

console.log(conjunto.has(1)) //Acceso ------ no se puede acceder por índice, no existe .get() como en Map. devuelve True O False dependiendo de si el valor existe o no. 
console.log(conjunto.has(2))

console.log(conjunto.delete(500))// devuelve True si se borró y False si no existia

// EN LOS SETS NO PODEMOS ACTUALIZAR DATOS PORQUE NO HAY PARES CLAVE-VALOR, SI QUIERES "ACTUALIZAR" DEBES BORRAR UN VALOR CON DELETE Y AÑADIR UNO NUEVO.

conjunto.add(1000)

console.log(conjunto.has(1000))
console.log(conjunto)



//WeakMaps ---- Como Map, pero con dos diferencias clave ---- 1 las claves solo pueden ser objetos ---- 2 las claves no son fuertes, si el objeto clave deja de existir en memoria, el WM lo elimina automáticamente, esto es útil para: Guardar datos privados asociados a objetos y para evitar Memory Leaks.


const wm = new WeakMap() //creamos nuestro WeakMap
const ID = {} //creamos un objeto que actuará como nuestra CLAVE

wm.set(ID, "89840309Ñ") // inserción --- si intentas usar un STRING o NUMERO como clave dará ERROR.

console.log(wm.get(ID)) // acceso

wm.set(ID, "55555555K") //actualización 
console.log(wm.get(ID))

wm.delete(ID) //Borrado
console.log(wm.get(ID)) 


//WeakSets ---- Como Set, pero solo acepta objetos. WeakSet solo funciona si añades y consultas la misma referencia, no un objeto “parecido”.


const ws = new WeakSet()
let contacto = {contacto : "Juan"} //creamos un objeto y lo añadimos a la variable


console.log(ws.add(contacto)) // añadimos la variable al Weakset / Inserción

console.log(ws.has(contacto)) // arroja True si el weakset contiene la variable / Acceso

console.log(ws.delete(contacto)) //eliminamos la variable //Borrado

console.log(ws.has(contacto)) // arroja false ya que no existe mas la variable.

//para actualizar habría que borrar y volver a añadir.

//no puedes meter números, strings, booleanos. Solo Objetos.



//EJERCICIO EXTRA AGENDA POR TERMINAL

const agenda = new Map()

import readline from "node:readline"

const rl = readline.createInterface(
    {
       input: process.stdin,
       output: process.stdout 
    }
)


function mostrarMenu(){

    console.log("")
    console.log("1. Añadir Contacto")   
    console.log("2. Actualizar Contacto")
    console.log("3. Eliminar Contacto")
    console.log("4. Buscar Contacto")
    console.log("5. Salir del Menú")

rl.question("\nElige una opción: ", (opcion) => {
    switch(opcion){
        case "1":
            añadirContacto()
            break;
        case "2":
            actualizarContacto()
            break;
        case "3":
            eliminarContacto()
            break;
        case "4":
            buscarContacto()
            break;
        case "5":
            rl.close()
            console.log("Programa finalizado");
            return
        default:
            console.log("Debes ingresar una de las opciones válidas.")
    mostrarMenu()
    }       
})
 
}

function actualizarContacto(){
    rl.question("\n¿Que contacto deseas actualizar?: ", (contacto) =>{

        if(!agenda.has(contacto)){
            console.log("\nEl contacto que buscas no está agregado")
            return mostrarMenu()
        }

        console.log("")
        console.log("Actualizar contacto")
        console.log("Actualizar teléfono")
        console.log("")

        rl.question("Escoge una opción: ", (opcion) => {


            if(opcion === "1"){
                rl.question("\nIntroduce el nuevo nombre: ", (nuevoNombre) => {

                    if (nuevoNombre.trim() === ""){
                        console.log("\nDebes introducir un nombre válido")
                        return mostrarMenu()
                    }

                    const telefonoActual = agenda.get(contacto)
                    agenda.delete(contacto)
                    agenda.set(nuevoNombre, telefonoActual)

                    console.log("\nNombre actualizado correctamente.")
                    return mostrarMenu()
                })
            }

            
            else if(opcion === "2"){
                rl.question("\nIngresa un nuevo numero de teléfono:  ", (telefono) => {

                    if(telefono.trim() === "" || isNaN(telefono)){
                        console.log("\nDebes añadir un número de teléfono válido")
                        return mostrarMenu()
                    }

                    if(telefono.length > 11){
                        console.log("\nEl teléfono no puede tener más de 11 dígitos")
                        return mostrarMenu()
                    }

                    agenda.set(contacto, telefono)
                    console.log("\nTeléfono actualizado correctamente")
                    return mostrarMenu()
                })
            }
            else{
                console.log("\nOpción no válida")
                return mostrarMenu()
            }
        })
    })
}



function eliminarContacto(){
     rl.question("\n¿Que contacto deseas eliminar?: ", (contacto) =>{

     if(contacto.trim() === ""){
        console.log("\nDebes introducir un contacto")
        return mostrarMenu()  
       }

     if(agenda.has(contacto)){
       agenda.delete(contacto)
       console.log("\nel contacto has sido eliminado correctamente")
       return mostrarMenu()
     }  
    })
}

function buscarContacto(){
    rl.question("\nBusca un contacto: ", (contacto) =>{
    if (agenda.has(contacto)){
        const telefono = agenda.get(contacto)
        console.log(`\nel telefono de ${contacto} es: `, telefono)
    }else {
        console.log("\nEl contacto ingresado no se encuentra en tu lista de contactos.")
    }

    return mostrarMenu()   
    })
}


function añadirContacto(){
    rl.question("\nNombre: ", (contacto) => {

        if(contacto.trim() === ""){
        console.log("\nDebes introducir un contacto")
        return mostrarMenu()  
       }

       rl.question("\nTeléfono: ", (telefono) =>{

       if(telefono.trim() === "" || isNaN(telefono)){
        console.log("\nDebes añadir un número de teléfono válido")
        return mostrarMenu()
       }

       if(telefono.length > 11){
        console.log("\nEl teléfono no puede tener más de 11 dígitos")
       return mostrarMenu()
       }
       agenda.set(contacto, telefono)
       console.log("\nContacto añadido correctamente")
       return mostrarMenu()

    })
   })
}


mostrarMenu()