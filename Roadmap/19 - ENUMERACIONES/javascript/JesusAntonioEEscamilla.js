/** #19 - JavaScript ->Jesus Antonio Escamilla */

/**
 * Aunque JavaScript no tiene un tipo de datos enum incorporado como algunos otros lenguajes de programación,
    se pueden simular mediante el uso de Objects o Constantes.
 * En general, los enums son un tipo que puede contener un número finito de valores definidos.
 * Los valores de los enums no son mutables.
 */

//---EJERCIÓ---
// Creamos una función que puede agregar y leer los objetos (Enum)
function Enum() {
    this.obj = {};
    this.add = function(key, value) {
        this[key] = value;
        this.obj[value] = key;
    };
    this.getName = function(value) {
        return this.obj[value];
    };
}

// Creamos el Enum como Objeto
const Semana_Enum = new Enum();
// Agregamos Valores
Semana_Enum.add("Lunes", 1);
Semana_Enum.add("Martes", 2);
Semana_Enum.add("Miércoles", 3);
Semana_Enum.add("Jueves", 4);
Semana_Enum.add("Viernes", 5);
Semana_Enum.add("Sábado", 6);
Semana_Enum.add("Domingo", 7);

// Retornamos el nombre del dia asignado
function nombreDia(numero) {
    return Semana_Enum.getName(numero);
}

// Lo llamamos en un consola
console.log(`El numero es 5 que es el dia ${nombreDia(5)}`);



/**-----DIFICULTAD EXTRA-----*/

// Pendientes

/**-----DIFICULTAD EXTRA-----*/