// ----------------------------- ESTRUCTURAS DE DATOS -----------------------------
  // ARRAYS

  const frutas = new Array('Manzana', 'Pera', 'Banana')
  // OBJECTS

    const persona = new Object({nombre: 'Aang', edad: 112, profesion: 'Avatar'});
  // SETS

    const notasMusicales = new Set(['do', 're', 'mi', 'fa', 'sol', 'la']);
  // MAPS

  const capacidad = new Map([[0, "zero"], [1, 'one'], [2, 'two'], [3, 'tree'], [4, 'four']]);

// ----------------------------- OPERACIONES BASICAS -----------------------------
    // Inserción
      frutas.push('Naranja')  // Array
      persona.tribu = 'Nómadas del aire'  // Object
      notasMusicales.add('si')  // Set
      capacidad.set(5, 'five')  // Map

    // Borrado
      frutas.splice(1, 1) // Array 
      delete persona.edad  // Object
      notasMusicales.delete('fa')  // Set
      capacidad.delete(5) //Map

    // Actualización
      frutas[0] = 'Mango'  // Array
      persona.profesion = 'Maestro del aire'  // Object
      // Los Sets no permiten actualización directa
      capacidad.set(3, 'three')  // Map

    // Ordenación
      frutas.sort()  // Array
      // Los Objects no tienen funciones de ordenación directa
      // Los Sets no tienen funciones de ordenación directa
      // Los Maps no tienen funciones de ordenación directa

// ----------------------------- DIFICULTAD EXTRA -----------------------------
let agenda = new Object({
  3321904500: 'Erick',
  6598204500: 'Jaime',
  3321968740: 'Raul',
  3654928824: 'Mateo',
  1218322247: 'Laura',
  9633455572: 'Miguel',
  3321994421: 'Omar',
  2076589124: 'Oscar',
  4863465825: 'Jose',
  5739514862: 'Fernando',
  8134679852: 'Eloy',
  7159852456: 'Daniel',
  3322577770: 'Erick',
  3999994500: 'Erick',
})

function verificarInfo() {
  //Verifica si el nombre o número ingresado por el usuario esta en la agenda
  while (true) {
    let info = prompt("Ingrese el nombre o telefono")
    if (Object.hasOwn(agenda, parseInt(info))) {
      return {'tel': info}
    } else if (Object.values(agenda).includes(info)) {
      return {'name': info}
    }
    alert("Persona/Telefono NO agendado/a")
  }
}

function verificarTel() {
  //Verifica que el número de telefono ingresado tenga entre 8 y 11 digitos
  while (true) {
    let tel = parseInt(prompt("Ingrese el teléfono (debe tener entre 8 y 11 dígitos)"))
    if (!isNaN(tel) && tel.toString().length >= 8 && tel.toString().length <= 11) {
      return tel;
    }
    alert("Número de teléfono inválido. Debe tener entre 8 y 11 dígitos.")
  }
}

function updateNombre() {
  //Actualiza el nombre de un contacto
  let infoUpdate = verificarInfo()
  if (infoUpdate.name !== undefined) {
    // busca a los contactos por nombre si hay varios devuelve los numeros y si hay uno permite cambiar el nombre
    let tel = Object.keys(agenda).filter(key => agenda[key] === infoUpdate.name)
    if (tel.length !== 1){
      alert(`Tienes varios contactos con ese nombre, verifica y actualiza el contacto que quieres por alguno de estos números ${tel}`)
    } else {
      let newName = prompt('Ingrese el nuevo nombre')
      agenda[parseInt(tel)] = newName
      alert(`Se ha actualizado el nombre del número ${tel} por ${newName}`)
    }
  } else {
    // busca el contacto por el telefono y le cambia el nombre
    let newName = prompt('Ingrese el nuevo nombre')
    agenda[parseInt(infoUpdate.tel)] = newName
    alert(`Se ha actualizado el nombre del número ${infoUpdate.tel} por ${newName}`)
  }
}

function updateTelefono(tel) {
  // Actualiza el telefono de un contacto
  let infoUpdate = verificarInfo()
  if (infoUpdate.name !== undefined) {
    // busca a los contactos por nombre si hay varios devuelve los numeros y si hay uno permite cambiar el telefono
    let tel = Object.keys(agenda).filter(key => agenda[key] === infoUpdate.name)
    if (tel.length !== 1){
      alert(`Tienes varios contactos con ese nombre, verifica y actualiza el contacto que quieres por alguno de estos números ${tel}`)
    } else {
      let newTel = verificarTel()
      delete agenda[tel]
      agenda[newTel] = infoUpdate.name
      alert(`Se ha actualizado el número de ${infoUpdate.name} a ${newTel}`)
    }
  } else {
    // busca el contacto por el telefono y le cambia el telefono
    let newTel = verificarTel()
    let lastName = agenda[infoUpdate.tel]
    delete agenda[infoUpdate.tel]
    agenda[newTel] = lastName
    alert(`Se ha actualizado el número de ${lastName} a ${newTel}`)
  }
}

function search() { 
  // te permite buscar, insertar, actualizar y borrar un contacto
  // ademas te pregunta si queres hacer otra operacion
  let operation = prompt("Ingrese la operación a realizar: buscar, insercion, actualizar, borrar")
  switch (operation) {
    case "buscar":
      let infoSearch = verificarInfo()
      if (infoSearch.name !== undefined) {
        // busca los telefonos que coincidan con el nombre ingresado y devuelve todos
        let tel = Object.keys(agenda).filter(key => agenda[key] === infoSearch.name)
        if (tel.length !== 1){
          alert(`Tienes ${tel.length} contactos llamados ${infoSearch.name} con los números ${tel}`)
        } else{
          alert(`El telefono de ${agenda[tel]} es ${tel}`)
        }
      } else {
        // busca el nombre del número de telefono ingresado
        let name = agenda[infoSearch.tel]
        alert(`El dueño del telefono ${infoSearch.tel} es ${name}`)
      }
      break;

    case "insercion":
      let name = prompt("Ingrese el nombre")
      tel = verificarTel()
      agenda[tel] = name
      alert(`Se ha agendado a ${name} con el número ${tel}`)
      break;

    case "actualizar":
      let updateOption = alert('¿Que queres actualizar nombre o telefono?')
        while (updateOption !== 'nombre' && updateOption !== 'telefono') {
          (updateOption === 'nombre') ? updateNombre()
                                      : updateTelefono()
        }
      break;

    case "borrar":
      let infoRemove = verificarInfo()
      if (infoRemove.name !== undefined) {
        // busca todos los números que estan agendados con el mismo nombre
        let tel = Object.keys(agenda).filter(key => agenda[key] === infoRemove.name)
        if (tel.length !== 1){
          let aviso = prompt('Tienes varios contactos con ese nombre, ¿Deseas borrar todos? Y/N')
          while (aviso !== 'Y' && aviso !== 'N') {
            if (aviso === 'Y'){
              let telRemoved = [...tel]
              while (tel.length !== 0) {
                // va eliminando de un telefono a la vez desde el último hasta el primero
                let i = tel.length - 1
                delete agenda[parseInt(tel[i])]
                tel.pop()
              }
              alert(`Los contacto con nombre ${infoRemove.name} y números ${telRemoved} han sido borrado`)
              break;
            } else {
              alert(`Los números que tienes agendados como ${infoRemove.name} son ${tel}`)
              break;
            }
          }
        } else {
          delete agenda[tel]
          alert(`El contacto con nombre ${infoRemove.name} y número ${tel} ha sido borrado`)
        }
      } else {
        let nameRemoved = agenda[infoRemove.tel]
        delete agenda[infoRemove.tel]
        alert(`El contacto con nombre ${nameRemoved} y número ${infoRemove.tel} ha sido borrado`)
      }
      break;
    default:
      break;
  }
  let stop = prompt('Quieres hacer otra operación? Y/N')
  while (stop !== 'Y' && stop !== 'N') {
    if (stop === 'Y') {
      search()
    } break;
  }
}

search()