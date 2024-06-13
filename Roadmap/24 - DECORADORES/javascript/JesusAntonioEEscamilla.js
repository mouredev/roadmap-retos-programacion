/** #24 - JavaScript ->Jesus Antonio Escamilla */

/**
 * Los decoradores en JavaScript son funciones que permiten agregar nuevas funcionalidades a clases, métodos o propiedades sin cambiar su código original.
 * Funcionan envolviendo el elemento original con una nueva función que añade o modifica su comportamiento.
 * Esto es útil porque permite extender las capacidades de un objeto de manera flexible y reutilizable, siguiendo el patrón de diseño.
 * Decorator que consiste en añadir funcionalidades adicionales a un objeto colocándolo dentro de otro objeto especial que contiene estas funcionalidades.
*/

//---EJERCIÓ---
/*Decorador de Validación y Registro Cambiando*/
// Decorador
function loginUserAction(service) {
    return {
        createUser(user){
            //Validación
            if (!user.name || !user.email) {
                throw new Error('Datos dek usuario no validos');
            }
            console.log(`Intentando crear usuario: ${JSON.stringify(user)}`);

            // Llamando a la función original
            const result = service.createUser(user);

            console.log(`Resultado: ${result}`);
            return result;
        }
    }
}

// Clase Original
class UserService{
    createUser(user){
        return `Usuario ${user.name} ha sido creado con éxito.`;
    }
}

// Creando ña instancia de Clase y aplicando el decorador
let userService = new UserService();
userService = loginUserAction(userService);

// Usar la clase del decorador
const user = { name: "Jesus", email: "JesusAEE@outlook.com" };
    try {
        console.log(userService.createUser(user));
    } catch (error) {
        console.error(error.message);
    }



/**-----DIFICULTAD EXTRA-----*/

/*Decorador Contabilizar */
//  Decorador
function contadorLlamadas(func) {
    let count = 0;

    function decorador(...args) {
        count++;
        console.log(`La función ${func.name} ha sido llamada ${count} veces`);
        return func(...args);
    }
    return decorador;
}

//  Función de suma
function suma(a, b) {
    return a + b;
}

//  Aplicamos el decorador
const sumaDecorador = contadorLlamadas(suma);

//  Probamos la función decorador
console.log(sumaDecorador(2, 4));
console.log(sumaDecorador(7, 1));
console.log(sumaDecorador(5, 6));

/**-----DIFICULTAD EXTRA-----*/