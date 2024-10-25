/*
 * TEORÍA DE DECORADORES EN TYPESCRIPT
 * 
 * Los decoradores son un patrón de diseño que nos permite añadir funcionalidad
 * adicional a clases, métodos, propiedades o parámetros de manera declarativa.
 * 
 * En TypeScript, un decorador es una función especial que puede ser adjuntada a:
 * - Declaraciones de clase
 * - Métodos
 * - Propiedades
 * - Parámetros
 * 
 * Para usar decoradores en TypeScript, necesitamos:
 * 1. Habilitar la opción "experimentalDecorators" en tsconfig.json
 * 2. Definir una función decoradora
 * 3. Aplicar el decorador usando el símbolo @ 
 */

// Ejemplo 1: Decorador simple para una clase
function logClass(target: any) {
    // Este decorador simplemente registra el nombre de la clase
    console.log(`Clase creada: ${target.name}`);
}

// Aplicamos el decorador a una clase
@logClass
class Ejemplo {
    constructor() {
        console.log('Constructor de Ejemplo ejecutado');
    }
}

// Ejemplo 2: Decorador de método que registra la ejecución
function logMethod(target: any, propertyKey: string, descriptor: PropertyDescriptor) {
    // Guardamos la función original
    const originalMethod = descriptor.value;

    // Reemplazamos el método con una nueva función
    descriptor.value = function(...args: any[]) {
        console.log(`Llamando al método ${propertyKey}`);
        return originalMethod.apply(this, args);
    }

    return descriptor;
}

class EjemploMetodo {
    @logMethod
    saludar(nombre: string) {
        return `¡Hola ${nombre}!`;
    }
}

// EJERCICIO EXTRA: Decorador contador de llamadas
function contadorLlamadas(target: any, propertyKey: string, descriptor: PropertyDescriptor) {
    // Variable para almacenar el contador
    let contador = 0;
    
    // Guardamos la función original
    const originalMethod = descriptor.value;
    
    // Reemplazamos el método con una nueva función que incluye el contador
    descriptor.value = function(...args: any[]) {
        contador++;
        console.log(`La función ${propertyKey} ha sido llamada ${contador} veces`);
        return originalMethod.apply(this, args);
    }
    
    return descriptor;
}

// Ejemplo de uso del decorador contador
class Calculadora {
    @contadorLlamadas
    sumar(a: number, b: number): number {
        return a + b;
    }

    @contadorLlamadas
    multiplicar(a: number, b: number): number {
        return a * b;
    }
}

// Código de prueba
console.log("=== Pruebas de los decoradores ===");

// Prueba del decorador de clase
const ejemplo = new Ejemplo();

// Prueba del decorador de método
const ejemploMetodo = new EjemploMetodo();
console.log(ejemploMetodo.saludar("TypeScript"));

// Prueba del decorador contador
const calc = new Calculadora();
console.log(calc.sumar(5, 3));        // Primera llamada a sumar
console.log(calc.sumar(2, 4));        // Segunda llamada a sumar
console.log(calc.multiplicar(3, 4));   // Primera llamada a multiplicar
console.log(calc.sumar(1, 1));        // Tercera llamada a sumar