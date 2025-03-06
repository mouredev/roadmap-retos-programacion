/* Stacks: LIFO. Least In First Out
   Queue:  FIFO. First In First Out
*/

let stack = [1, 2]
stack.push(3)
// console.log(stack)
stack.pop()
// console.log(stack)

let queue = [1, 2]
queue.push(3)
// console.log(queue)
queue.shift()
// console.log(queue)



/*
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás de un navegador web. 
 * - Crea un programa en el que puedas navegar a una página o indicarle que te quieres desplazar 
 *   adelante o atrás, mostrando en cada caso el nombre de la web.
 * - Las palabras "adelante", "atrás" desencadenan esta acción
 * - el resto se interpreta como el nombre de una nueva web.
 * 
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 * - La palabra "imprimir" imprime un elemento de la cola
 * - el resto de palabras se interpretan como nombres de documentos.
 */

const readline = require('readline')
const rl = readline.createInterface({
   input: process.stdin,
   output: process.stdout
})

let history = []
let currentWebsite = ''

function showMenu() {

   console.log('----------------------------------------------')
   console.log('- forward')
   console.log('- backward')
   console.log('- Type a new website to go')
   console.log('- exit')

   rl.question('Choose an option: ', (option) => {

      console.log('----------------------------------------------')

      switch (option) {

         case 'backward':
            if (history.length == 0) {
               console.log('The history is empty. Type a new website to go')
               showMenu()
            } else {

               const index = history.indexOf(currentWebsite);

               if (index > 0) {
                  currentWebsite = history[index - 1];
                  console.log(`Current website: ${currentWebsite}`);
                  showMenu()
               }
            }
            break

         case 'forward':
            if (history.length == 0) {
               console.log('The history is empty. Type a new website to go')
            } else {
               const index = history.indexOf(currentWebsite);

               if (index < history.length - 1 && index !== - 1) {
                  currentWebsite = history[index + 1];
                  console.log(`Current website: ${currentWebsite}`);
               } else {
                  console.log('There is no website to go. Try other option')
               }
            }
            showMenu()
            break

         case 'exit':
            console.log('Bye!')
            rl.close()
            break

         default:
            currentWebsite = option
            console.log('current', currentWebsite)

            history.push(currentWebsite)
            console.log(`Current website ${currentWebsite}`)
            showMenu()
      }
   })
}




showMenu()


/* 
OK:
 - Exit
 - Forward con algo adelante
 - Backward con algo atras
 - Entrar a un nuevo sitio web con el default
- Forward: Nada adelante del currentWebsite, historial no vacio

NO OK:
 - Backward: Nada atras del currentWebsite, historial no vacio
*/