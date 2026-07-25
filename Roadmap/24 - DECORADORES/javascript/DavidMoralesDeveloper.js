// decora otra funcion, esto quiere decir que la funcion original no cambia, podemos añadir un comportamiento a una funcion
// Decoradores: Se crean objetos decoradores que "envuelven" el objeto base o a otros decoradores. como cebolla en capas
// PATRONES DECORATIVAS CON CLASS 
class Cafe {
   costo (){
    return 10
   }
}

class Leche {
    constructor(cafe){
        this.cafe = cafe
    }

    costo() {
        return this.cafe.costo() + 2
    }
}

class Azucar {
    constructor(cafe) {
        this.cafe = cafe
    }
    costo (){
        return this.cafe.costo() + 1
    }
}

const cafe = new Cafe()
const cafeConLeche = new Leche(cafe)
const cafeConAzucar = new Azucar(cafe)
const cafeConLecheYAzucar= new Azucar(cafeConLeche)
console.log(cafe.costo())
console.log(cafeConAzucar.costo())
console.log(cafeConLeche.costo())
console.log(cafeConLecheYAzucar.costo())

console.log("-------------------------TERMINA PATRONES DECORATIVOS")

console.log("-------------------------COMIENZAN FUNCIONES DECORATIVAS")

function logFunction(func) {
    return function(...args) {
        console.log(`🔍 Ejecutando función: ${func.name}`);
        const result = func.apply(this, args);
        console.log(`✅ Función ${func.name} completada`);
        return result;
    };
}

// Aplicar el decorador
const saludar = logFunction(function saludar(nombre) {
    return `¡Hola, ${nombre}!`;
});

const sumar = logFunction(function sumar(a, b) {
    return a + b;
});



// Usar las funciones decoradas
console.log(saludar("Juan"));
console.log(sumar(5, 3));

console.log('-------------------comienza ejercicio extra');

function contadorDeFunciones(func) {
  let contador = 0; // This 'contador' is in the outer scope and will persist across calls

  const decoradorFunciones = function (...args) {
    contador += 1; // Correctly increments the persistent 'contador'
    console.log(`La función ${func.name} se ha ejecutado ${contador} vez(es).`); // More accurate phrasing for single/plural

    const result = func.apply(this, args); // Execute the original function

    return result;
  };

  // Attach a method to the decorated function to get the current count
  decoradorFunciones.getCount = () => contador;

  return decoradorFunciones;
}

const saludare = (nombre) => {
  console.log(`Hola ${nombre}`);
};

const saludarContador = contadorDeFunciones(saludare); // Decorate 'saludare'

// --- IMPORTANT: Call the *decorated* function here ---
saludarContador("David");
saludarContador("Jhon");
saludarContador("Juan");

console.log(`Total de ejecuciones de 'saludar': ${saludarContador.getCount()} vez(es).`);

const multiplicar = (a, b) => { a*b}
multiplicarContador = contadorDeFunciones(multiplicar)
multiplicarContador(5,2)
multiplicarContador(5,5)
console.log(multiplicarContador.getCount()+ "veces se a usado la funcion multiplicar")


const countFunc = contadorDeFunciones(function miFuncion() {
    console.log('Ejecutando mi función...');
    return 'Resultado';
});

console.log(countFunc()); // Llamada #1
console.log(countFunc()); // Llamada #2


console.log('Total de llamadas en la funcion mi cuncion:', countFunc.getCount());