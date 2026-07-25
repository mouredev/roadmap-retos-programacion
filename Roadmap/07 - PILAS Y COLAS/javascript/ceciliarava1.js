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

               if (index > 0 && index !== - 1) {
                  currentWebsite = history[index - 1];
                  console.log(`Current website: ${currentWebsite}`);
               } else {
                  console.log('There is no website to go. Try other option')
               }
            }
            showMenu()
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

// showMenu()


let documents = []

function showNewMenu() {

   console.log('----------------------------------------------')
   console.log('- print')
   console.log('- Type a new document')
   console.log('- exit')

   rl.question('Choose an option: ', (option) => {

      console.log('----------------------------------------------')

      switch (option) {

         case 'print':
            if (documents.length == 0) {
               console.log('There is no documents to print. Add a document')
            } else {
               console.log(`Printing ${documents[0]}`)
               documents.shift()
            }
            showNewMenu()
            break

         case 'exit':
            console.log('Bye!')
            rl.close()
            break

         default:
            documents.push(option)
            console.log(`${option}  added`)
            showNewMenu()
      }
   })
}

// showNewMenu()