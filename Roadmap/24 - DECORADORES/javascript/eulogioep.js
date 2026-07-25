/*
 * TEORÍA DE DECORADORES EN JAVASCRIPT
 * 
 * Los decoradores son funciones especiales que pueden modificar el comportamiento
 * de clases, métodos y propiedades. En JavaScript, son una característica que
 * permite añadir funcionalidad adicional de manera declarativa.
 * 
 * Tipos principales de decoradores:
 * 1. Decoradores de clase
 * 2. Decoradores de método
 * 3. Decoradores de propiedad
 * 
 * Para usar decoradores necesitas:
 * 1. Un entorno que soporte la sintaxis de decoradores (Node.js moderno o Babel)
 * 2. Configurar el compilador para soportar decoradores
 */

// Ejemplo 1: Decorador de clase
function logClass(target) {
    // Este decorador registra cuando se crea una instancia de la clase
    console.log(`Clase creada: ${target.name}`);
    return target;
}

// Ejemplo 2: Decorador de método
function logMethod(target, key, descriptor) {
    // Guardamos la función original
    const originalMethod = descriptor.value;
    
    // Reemplazamos el método con una nueva función
    descriptor.value = function(...args) {
        console.log(`Llamando al método ${key}`);
        return originalMethod.apply(this, args);
    }
    
    return descriptor;
}

// Ejercicio Extra: Decorador contador de llamadas
function contadorLlamadas(target, key, descriptor) {
    // Creamos un mapa para almacenar los contadores de cada método
    if (!target.constructor._contadores) {
        target.constructor._contadores = new Map();
    }
    
    // Guardamos la función original
    const originalMethod = descriptor.value;
    
    // Reemplazamos el método con una nueva función que incluye el contador
    descriptor.value = function(...args) {
        // Obtenemos el contador actual o inicializamos en 0
        const contador = (target.constructor._contadores.get(key) || 0) + 1;
        target.constructor._contadores.set(key, contador);
        
        console.log(`La función ${key} ha sido llamada ${contador} veces`);
        
        // Llamamos a la función original
        return originalMethod.apply(this, args);
    }
    
    return descriptor;
}

// Aplicamos el decorador a una clase
@logClass
class Ejemplo {
    constructor() {
        console.log('Constructor de Ejemplo ejecutado');
    }
    
    @logMethod
    saludar(nombre) {
        return `¡Hola ${nombre}!`;
    }
}

// Clase con el decorador contador
class Calculadora {
    @contadorLlamadas
    sumar(a, b) {
        return a + b;
    }
    
    @contadorLlamadas
    multiplicar(a, b) {
        return a * b;
    }
}

// Código de prueba
console.log("=== Pruebas de los decoradores ===");

// Prueba del decorador de clase y método
const ejemplo = new Ejemplo();
console.log(ejemplo.saludar("JavaScript"));

// Prueba del decorador contador
const calc = new Calculadora();
console.log("Resultado suma:", calc.sumar(5, 3));        // Primera llamada a sumar
console.log("Resultado suma:", calc.sumar(2, 4));        // Segunda llamada a sumar
console.log("Resultado multiplicación:", calc.multiplicar(3, 4));   // Primera llamada a multiplicar
console.log("Resultado suma:", calc.sumar(1, 1));        // Tercera llamada a sumar

// Ejemplo de uso de decoradores con clases ES6 modernas
// Decorador que añade un método a la clase
function añadirMetodo(target) {
    target.prototype.nuevoMetodo = function() {
        return "Este es un método añadido por el decorador";
    }
    return target;
}

@añadirMetodo
class EjemploModerno {
    constructor() {
        console.log("Clase moderna creada");
    }
}

const ejemploModerno = new EjemploModerno();
console.log(ejemploModerno.nuevoMetodo());