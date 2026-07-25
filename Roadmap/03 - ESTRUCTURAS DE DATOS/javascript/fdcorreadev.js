/**
 * javascript tiene estructuras de datos como casi todos los lenguajes, arrays, y objetos 
 */

// objetos estan diseñados para tener clave valor
let object = { saludar: 'Hola', objeto: 'mundo' }

//funciones que se pueden hacer con los objetos
let myCar = new Object()

//opcion1
myCar.brand = "ford"
myCar.reference = "mustang"
myCar.modelo = 1968

//opcion2
myCar["brand"] = "chevrolet";
myCar["reference"] = "aveo";
myCar["modelo"] = 2010;

console.log(myCar)

// eliminar propiedades no de un object.

delete myCar.brand

console.log(myCar)

//objeto tipo map
const map1 = new Map()

console.log('objeto tipo map')
console.log(map1)

//para insertar valores 
map1.set('nombre', 'fabian')
map1.set('apellido', 'correa')
map1.set('edad', 26)

console.log(map1)
//objener valores

console.log(map1.get("nombre"))

//borrar un valor
console.log("borrar valores")
map1.delete("edad")
console.log(map1)

//arrays
let arrays = ['hola', 'mundo', 'cruel']

// insertar valores, ya sea uno o varios

console.log('agregar valores a un array push()')
arrays.push("parte", "uno")
console.log(arrays)

//agregar valores al inicio un array
console.log('agregar valores al inicio un array unshift()')
arrays.unshift("¡")
console.log(arrays)


//eliminar el ultimo valor del array
console.log('eliminar el ultimo valor del array pop()')
arrays.pop()
console.log(arrays)

//eliminar el valor por indice de un array
console.log('eliminar por el valor del indice de un array splice()')
arrays.splice(4)
console.log(arrays)

//actualizar por indice el valor de un array
console.log('actualizar por indice el valor de un array splice()')
arrays.splice(1, 1, "hello")
console.log(arrays)

//actualizar un array
console.log('actualizar por indice array[indice]')
arrays[3] = "bello"
console.log(arrays)

//Ordenar un array 
console.log('ordenar un array con sort()')
arrays.sort()
console.log(arrays)

console.log('nuevo ejemplo para ordenar un array')
let newArray = [45, 12, 47, 28, 1, 0, 34, 56, 13, 10]

console.log(newArray)
console.log('ordenar un array con sort()')
newArray.sort()
console.log(newArray)


//ejercicio Extra

const readline = require('readline')

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

let data = []

function validatePhone(valor) {
    const splitNumber = valor.split('')
    const validateLenght = true ? splitNumber.length === 10 : false
    let validateNumbers;
    if (Number(valor)) {
        validateNumbers = true
    } else {
        validateNumbers = false
    }
    return true ? validateLenght === true && validateNumbers === true : false
}

function mostrarMenu() {
    console.log(`---->> escriba el numero de la tarea que vas a realizar en la agenda <<----`)
    console.log(`0. salir`)
    console.log(`1. insercion`)
    console.log(`2. busqueda`)
    console.log(`3. actualizacion`)
    console.log(`4. eliminacion`)
    console.log(`9. mostrar base`)

    rl.question('Numero: ', (numeroTask) => {
        processTask(numeroTask)
    })

}

function processTask(numeroTask) {
    switch (numeroTask) {
        case '1':
            console.log()
            console.log()
            console.log(`vamos a realizar una insercion`)
            let contacto = { name: '', telefono: '' }
            rl.question('Nombre: ', (name) => {
                contacto.name = name
                rl.question('telefono: ', (telefono) => {
                    let longNumber = validatePhone(telefono)
                    if (longNumber) {
                        contacto.telefono = telefono
                        data.push(contacto)
                        mostrarMenu()
                    } else {
                        console.log(`verifica los valores ingresados 10 digitos y deben ser numericos`)
                        mostrarMenu()
                    }
                })
            })
            break;
        case '2':
            console.log()
            console.log(`vamos a realizar una busqueda, puedes hacerlo por telefono o nombre`)
            console.log()
            rl.question('Ingrese valor de busqueda: ', (dataSearch) => {
                const findName = data.filter(value => value.name.toLowerCase() === dataSearch.toLowerCase())
                const findPhone = data.filter(value => value.telefono.toLowerCase() === dataSearch.toLowerCase())
                if (findName.length > 0) {
                    findName.forEach(name => {
                        console.log(`el usuario es: ${name.name} con numero de telefono ${name.telefono}`)
                    })
                } else if (findPhone.length > 0) {
                    findPhone.forEach(phone => {
                        console.log(`el usuario es: ${phone.name} con numero de telefono ${phone.telefono}`)
                    })
                } else {
                    console.log()
                    console.log()
                    console.log(`Este datos no se registro en la agenda registralo`)
                    console.log()
                    console.log()
                }
                console.log()
                console.log()
                mostrarMenu()
            })
            break;
        case '3':
            console.log(`vamos a realizar una actualizacion`)
            rl.question('ingresa Valor a Actualizar: ', (dataSearch) => {
                rl.question('Por cual quieres actualizar: ', (dataReplace) => {
                    const index = data.findIndex(value => value.name.toLowerCase() === dataSearch.toLowerCase() || value.telefono.toLowerCase() === dataSearch.toLowerCase())
                    if (index !== -1) {
                        //Determinar si el valor es un nombre o un telefono
                        if (isNaN(dataSearch)) {
                            data[index].name = dataReplace;
                            console.log()
                            console.log(`El nombre ${dataSearch} fue actualizado por ${dataReplace} con exito`)
                            console.log()
                        } else {
                            data[index].telefono = dataReplace;
                            console.log()
                            console.log(`El telefono ${dataSearch} fue actualizado por ${dataReplace} con exito`)
                            console.log()

                        }
                    } else {
                        console.log()
                        console.log()
                        console.log(`Verifique si es usuario se encuentra`)
                        console.log()
                        console.log()
                    }
                    mostrarMenu()
                })
            })
            break;
        case '4':
            console.log()
            console.log(`vamos a realizar una eliminacion`)
            console.log()
            rl.question('ingresa Valor a eliminar: ', (dataSearch) => {
                const findName = data.filter(value => value.name.toLowerCase() === dataSearch.toLowerCase())
                const findPhone = data.filter(value => value.telefono.toLowerCase() === dataSearch.toLowerCase())
                if (data.includes(findName[0]) || data.includes(findPhone[0])) {
                    const index = data.indexOf(findName[0])
                    data.splice(index, 1)
                    console.log(`el usuario fue eliminado con exito`)
                } else {
                    console.log()
                    console.log()
                    console.log(`Verifique si es usuario se encuentra`)
                    console.log()
                    console.log()
                }
                mostrarMenu()
            })

            break;
        case '9':
            console.log()
            console.log()
            console.table(data)
            console.log()
            console.log()
            mostrarMenu()
            break;
        case '0':
            console.log(`!nos vemos pronto fue un placer¡`)
            rl.close()
            break;
        default:
            console.log("el valor que escribiste no esta en el menu")
            mostrarMenu()
            break;
    }
}

mostrarMenu()
// rl.question('Que desea hacer: ', (task) => {
//     const tasks = ["busqueda", "insercion", "actualizacion", "eliminacion"]
//     if(tasks.includes(task)){
//         console.log(task)
//     } else {
//         console.log(`recuerda que tienes 4 opciones: "busqueda", "insercion", "actualizacion", "eliminacion"`)
//     }
// })



