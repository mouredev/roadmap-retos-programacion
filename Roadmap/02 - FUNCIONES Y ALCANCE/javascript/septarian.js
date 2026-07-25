 // Funciones basicas
 function hola(){
    console.log("hola mundo")
 }
 hola()

 function suma(a, b){
   return a + b
 }
 let a = 3
 let b = 2
 console.log(suma(a,b))

 // Funciones dentro de funciones
 function nombre(name, last){
   console.log("mi nombre es: "+ name )
   //metodo con argumento por defecto
   function apehido(lastName = "Mora"){
      console.log(`mi apehido es: ${lastName}`)
   }
   apehido()
 }
 const names = "johnny"
 const last = "joestar"
 nombre(names, last)

 // Funciones con numero variable de argumentos
function variable(...names){
   for(let i of arguments){
      console.log("Hola " + i)
   }
}
variable("erick", "dany", "johnny", "gyro")

// Funciones del lenguaje
let cadena = "soy una cadena"
console.log(typeof cadena)

// Variable local y global
let varr = "hola"  //variable global, las variables locales estan dentro de funciones

// EXTRA
function numeros(a, b){
   let cont = 0

   for(let i = 0;i <= 100;i++){
      if(i % 3 === 0 && i % 5 === 0){
         console.log(a)
      }
      else if(i % 5 === 0){
         console.log(b)
      }
      else if(i % 3 === 0){
         console.log(`${a} ${b}  `)
      }
      else{
         console.log(i)
         cont++
      }
   }
   return cont
}
const parametro1 = "bizarre"
const parametro2 = "adventure"
console.log(numeros(parametro1, parametro2))