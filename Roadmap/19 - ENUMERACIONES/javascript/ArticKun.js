
//⚡ Enumeraciones

/*

Empleando tu lenguaje, explora la definición del tipo de dato
    - que sirva para definir enumeraciones (Enum).
    - Crea un Enum que represente los días de la semana del lunes
    - al domingo, en ese orden. Con ese enumerado, crea una operación
    - que muestre el nombre del día de la semana dependiendo del número entero
    - utilizado (del 1 al 7).



1.Object.freeze Para asegurarte de que la enumeración no se modifique 
accidentalmente

2. Uso de Symbol para valores únicos
Symbol para asegurarse de que cada valor de la enumeración sea único

*/

const Semana = Object.freeze({
    LUNES     : Symbol('lunes'),
    MARTES    : Symbol('martes'),
    MIERCOLES : Symbol('miércoles'), 
    JUEVES    : Symbol('jueves'),
    VIERNES   : Symbol('viernes'),
    SABADO    : Symbol('sábado'), 
    DOMINGO   : Symbol('domingo'),
});

// Función para obtener el nombre del día de la semana dependiendo del número entero
const getDia = (numeroDia) => {

    switch (numeroDia) {
        case 1:
            return Semana.LUNES;
        case 2: 
            return Semana.MARTES;
        case 3:
            return Semana.MIERCOLES;
        case 4:
            return Semana.JUEVES;
        case 5:
            return Semana.VIERNES;
        case 6:
            return Semana.SABADO;
        case 7:
            return Semana.DOMINGO;
        default:
            return "No existe ese día de la semana";
    }
};

console.log( getDia(7) );
