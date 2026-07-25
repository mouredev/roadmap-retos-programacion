function mostrarHola() : void {
    console.log("Hola como estas");
}

function greet ( name : string) : void {
    console.log(`Hello ${name}!`);
} 

function operacion_logica (P : boolean, Q : boolean) : boolean {
    function operacion_logica_2(P : boolean, Q : boolean) : boolean{
        return P && Q && (!P || Q);
    }

    return ! operacion_logica_2(P, Q);
}

let uno_1 = 1;
var dos_2 = 2;

function numerica_global() {
    console.log(uno_1 ?? "Perro hp");
    console.log(dos_2);
    let perro = "hp";
}

mostrarHola();
greet("Jesús");
console.log(operacion_logica(true, false));
greet("Putas karens".toUpperCase());
numerica_global();
// console.log(perro); da un error porquela variable no fue definida dentro del espacio.

function ejercicio_funciones_extra_dificultad(cadena_1 : string, cadena_2: string) : number {
    let acumulador : number = 0;
    for (let i = 1; i <= 100; i++) {
        console.log(acumulador++);
        if ((i % 5 == 0) && (i % 3 == 0)) {
            console.log(cadena_1, cadena_2);
        } else if ((i % 3 == 0)) {
            console.log(cadena_1);
        } else if ((i % 5 == 0)) {
            console.log(cadena_2);
        }
    }

    return acumulador;
}

console.log(ejercicio_funciones_extra_dificultad("Jesus", "Peraza"))
