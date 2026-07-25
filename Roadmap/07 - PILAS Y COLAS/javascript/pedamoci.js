// ------------------------------ MECANISMO DE INTRODUCCION Y RECUPERACION DE ELEMENTO ------------------------------
  // EN PILAS --> (Un elemento en ejecución (antes de que esta termine) llama a otro elemento y pausa su ejecución, una ves que este se termine de ejecutar renueva la ejecución del anterior)
    let pila = []

    pila.push("PRIMER elemento que se añade a la pila y llama al SEGUNDO")
    console.table(pila) // hay un unico elemento en la pila
    pila.push('SEGUNDO elemento que se añade a la pila llamado por el PRIMERO y llama al TERCERO')
    console.table(pila) // se le añade un segundo elemento a la pila
    pila.push('TERCER elemento que se añade a la pila llamado por el SEGUNDO')
    console.table(pila) // ya hay tres elementos en la pila

    console.log('Ejecución del ULTIMO elemento llamado a la pila: ' + pila[pila.length - 1]) // (pila.length - 1) --> para demostrar que se ejecuta el último elemento
    pila.pop() // El último elemento llamado a la pila por el segundo ya se ejecuto y finalizo por lo tanto se elimina de esta

    console.log('Ejecución del SEGUNDO elemento llamado a la pila: ' + pila[pila.length - 1])
    pila.pop() // El segundo elemento llamado a la pila por el primero ya se ejecuto y finalizo por lo tanto se elimina de esta

    console.log('Ejecución del PRIMER elemento llamado a la pila, última en este caso: ' + pila[pila.length - 1])
    pila.pop() // El primer elemento llamado a la pila ya se ejecuto y finalizo por lo tanto se elimina de esta quedando vacia

    console.table(pila) // ya no hay elementos en la pila

  // EN COLAS --> (Un elemento en ejecución llama a otro elemento, cuando la ejecución del primer elemento termina recien ahí arranca la ejecución del segundo elemento)
    let cola = []

    cola.push("PRIMER elemento que se ejecuta, llama un SEGUNDO y despues un TERCERO")
    console.table(cola) // hay un unico elemento en la cola
    cola.push('SEGUNDO elemento que se añade a la cola llamado por el PRIMERO')
    console.table(cola) // se le añade un segundo elemento a la cola
    cola.push('TERCER elemento que se añade a la cola llamado por el PRIMERO')
    console.table(cola) // ya hay tres elementos en la cola

    console.log('Ejecución del PRIMER elemento en la cola: ' + cola[0])
    cola.shift() // El primer elemento de la cola ya se ejecuto y finalizo por lo tanto se elimina de esta

    console.log('Ejecución del SEGUNDO elemento en la cola: ' + cola[0])
    cola.shift() // al finalizar la ejecución del primer elemento inicia la del segundo. Este se ejecuta y una vez finaliza se elimina de la cola

    console.log('Ejecución del TERCER elemento en la cola, última en este caso: ' + cola[0])
    cola.shift() // al finalizar la ejecución del segundo elemento inicia la del tercero. Este se ejecuta y una vez finaliza se elimina de la cola quedando esta vacia

    console.table(cola) // ya no hay elementos en la cola

// ---------------------------------- DIFICULTAD EXTRA ----------------------------------
function navegadorWeb() {
  let pagina = []
  let move = ''
  do {
    move = prompt((pagina.length === 0 ? " ".repeat(31) + `Bienvenidos a la página de incio` + " ".repeat(31)
                                          : " ".repeat(30) + `Bienvenidos a la página número ${pagina.length}` + " ".repeat(30))

                      + "\n" + " ".repeat(22) + "(esbribe exit/salir para terminar la ejecución)" + " ".repeat(21) + "\n".repeat(4) +
                      "<--(atras/back)" + " ".repeat(19) + "Desea ir hacia" + " ".repeat(19) + "(next/adelante)-->").toLowerCase()
    if (move === 'adelante' || move === 'next')  {
      pagina.push('new page')
    } else if ((move === 'atras' || move === 'back') && pagina.length !==0) {
      pagina.pop()
    }
  } while (move !== 'salir' && move !== 'exit');
}
navegadorWeb()

function impresora() {
  let colaDocumentos = []
  let documento = ''
  do {
    documento = prompt(" ".repeat(47) + "IMPRESORA" + " ".repeat(48) + "\n" +
                        " ".repeat(14) + "Escriba el nombre del documento que desea imprimir" + " ".repeat(14) + "\n" +
                        " ".repeat(34) + `(en cola hay ${colaDocumentos.length} documentos)` + " ".repeat(34) + "\n".repeat(4)  +
                        " ".repeat(19) + "Escriba 'imprimir' para imprimir un documento" + " ".repeat(20)).toLowerCase()
    if (documento === 'imprimir' && colaDocumentos.length !== 0)  {
      alert(" ".repeat(47) + "IMPRESORA" + " ".repeat(48) + "\n".repeat(3) +
            "Se ha impreso: " + colaDocumentos[0] + ".pdf")
            colaDocumentos.shift()
    } else if (documento !== 'imprimir') {
      colaDocumentos.push(documento)
      alert(" ".repeat(47) + "IMPRESORA" + " ".repeat(48) + "\n".repeat(3) +
            "Se ha agregado a la cola: " + documento + ".pdf")
    }
  } while (true);
}
impresora()