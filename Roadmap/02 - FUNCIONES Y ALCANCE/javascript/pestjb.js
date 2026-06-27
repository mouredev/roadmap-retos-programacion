
//funciones simples

function saludar(){
    console.log("Hola, soy una función")
}

saludar() //saludar es una función que imprime un mensaje en consola

//funciones con retorno

function sumar(a, b){
    return a + b //return es una palabra reservada que se utiliza para devolver un valor desde una función
}
console.log(sumar(780, 345)) //sumar es una función que recibe dos parámetros y devuelve su suma



//funciones con parámetros/argumentos

function saludar2(nombre){
    console.log(`Hola, ${nombre}`) //template literals es una forma de crear cadenas de texto utilizando comillas invertidas y ${} para insertar variables
}

saludar2("Luis Miguel") //saludar2 es una función que recibe un parámetro y lo utiliza para imprimir un mensaje en consola


// funciones con argumentos predeterminados

function saludar3(saludo, nombre){
    console.log(`${saludo}, ${nombre}`) 
}

saludar3("Hola", "Luis Miguel") 

function saludar4(nombre = "Mundo", saludo = "Hola") {
  console.log(`${saludo}, ${nombre}`)
}

saludar4("Juan")   
saludar4()         


//funciones con retorno de varios valores
 
function  return_func(saludo, nombre){
    return saludo + nombre
}
return_func("Hola", " Neymar") //return_func es una función que recibe dos parámetros y devuelve su concatenación


// funciones con un número variable de argumentos

function variable_arg_greet(...nombres){
    for(let nombre of nombres){
        console.log(`Hola, ${nombre}`)
    }   
}

variable_arg_greet("Python", "JavaScript", "Mundo")

// funciones con un número variable de argumentos con palabra clave

function crearUsuario({nombre, edad, activo = true }){
    console.log(nombre, edad, activo)
}

crearUsuario({nombre: "Juan", edad: 20 })// En Javascript no existe un equivalente directo a la forma en que se realiza esto en Python, pero se logra lo mismo usando objetos.

//Funciones dentro de funciones


function function_externa(){
    function function_interna(){
        console.log("Hola desde la función interna")
    }
    function_interna()
}

function_externa()

//funciones del lenguaje(built-in functions)

parseInt("10") // funcion para convertir una cadena de texto a un numero entero, resultado 10(en numero)
parseFloat("10.46")// funcion que transforma una cadena de texto a un numero decimal. 
isNaN("hola") // arroja true si el argumento que le pasas no es un numero, si lo es, arroja false.
isFinite(100) // un numero finito es aquel que no es infinito ni NaN, arroja true si el argumento que le pasas es un numero finito, si no lo es, arroja false.
setTimeout(function(){console.log("Hola desde setTimeout")}, 2000) // ejecuta una función después de un tiempo determinado, en este caso 2 segundos.
setInterval(function(){console.log("Hola desde setInterval")}, 2000) // ejecuta una función cada cierto tiempo, en este caso cada 2 segundos.
encodeURI("https://www.google.com/search?q=hola mundo") // codifica una URL, reemplazando los caracteres especiales por su equivalente en porcentaje.
decodeURI("https://www.google.com/search?q=hola%20mundo") // decodifica una URL, reemplazando los caracteres especiales por su equivalente en porcentaje.

//FUNCIONES BUILT-IN DENTRO DE OBJETOS NATIVOS

Math.max(1, 5, 76) //Funcion que devuelve el numero mas grande de un conjunto. 
Math.floor(3.9) // Funcion que devuelve el entero más grande menor que o igual a su argumento numerico.
Math.random()  // Funcion que devuelve un numero aleatorio dentro de un rango. 
Math.min(1, 3, 5) // Funcion que devuelve el numero mas pequeño de un conjunto. 

//String 

"hola".toUpperCase() //"HOLA", transforma cualquier texto en minusculas a mayusculas
"hola".includes("la") // true, devuelve true si el caracter o la cadena de texto ingresada es parte de la original.
"hola".length// devuelve la longitud de caracteres de la cadena de texto. 


//Arrays

[1, 2, 3].map(x => x * 2) // [2, 4, 6]
[1, 2, 3].filter(x => x > 1) // [2, 3]
[1, 2, 3].reduce((a, b) => a * b) // 6

//Object

Object.keys({a:1, b:2}) // ["a", "b"]
Object.values({a:1, b:2}) // [1, 2]

//Built-in para manejar erroes

throw new Error("ID no encontrado")


//Variables locales y globales

let global_var = "JavaScript"



function hello_javascript(){
    let local_var = "Hola"
    console.log(`${local_var}, ${global_var}`)
}

console.log(global_var)
//console.log(local_var) no se puede acceder desde fuera de la función. 

hello_javascript()


// EJERCICO EXTRA

function ejercicioExtra(text_1, text_2){
    
  let count = 0

  for(let i = 1; i < 101; i++){ 
  
    if(i % 3 == 0 && i % 5 == 0){
    console.log(text_1 + text_2)
  }
  else if(i % 3 == 0){
      console.log(text_1)
    }
    else if(i % 5 == 0){
      console.log(text_2)
    }
    else{
      console.log(i)
      count += 1
    }

  }
return count
}


console.log(ejercicioExtra("Fizz", "Buzz"))