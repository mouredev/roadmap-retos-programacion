// 1º Tipo de Funciones
    // Funciones con retorno
    function minumero() : number{
        return 5;
    }
    let num = minumero();
    console.log(num);

    function olamundo() : string{
        return 'Ola Mundo';
    }
    let ola = olamundo();
    console.log(ola);

    // Tambien podemos hacerlas como una función flecha
    const minombre : () => string = () => {
        return 'IgleDev';
    }
    let nombre = minombre();
    console.log(nombre);

    //Funciones sin retorno
    function sinretorno() : void{
        console.log('No retorno nada');
    }
    console.log(sinretorno());

    //Funciones con un parámetro
    function getNumero(num : number) : number{
        return num;
    }
    let num2 = getNumero(5);
    console.log(num2);

    //Funciones con varios parametros
    function sumar(a : number, b : number) : number{
        return a + b;
    }
    let suma = sumar(3,2);
    console.log(suma);

    //Funciones con parámetros pero que no sabemos cuantos
    function concatenar(...args : string[]) : string{
        return args.join(' ');
    }
    let frase = concatenar('Ola','Mundo','con', 'TypeScript');
    console.log(frase);

    // Funciones donde la pasamos un dato y devolvemos otro distinto
    function dametuNumero(num : number) : string{
        return 'Mi número es el: ' + num;
    }
    let tunumero = dametuNumero(5);
    console.log(tunumero);

    //Funciones que se utilizan para lanzar expeciones o errores
    function error() : never{
        throw new Error('Error');
    }

// 2º Función dentro de función
    function factorialFunction(): (num: number) => number {
        function calculateFactorial(num: number): number {
            if (num <= 1) {
                return 1; 
            } else {
                return num * calculateFactorial(num - 1); 
            }
        }

        return calculateFactorial;
    }

    let factorial = factorialFunction();
    console.log(factorial(5));

// 3º Funciones del propio lenguaje
    //Funciones de Identidad: Permite la creación genérica que puedan aceptar y devolver tipos específicos
    function identidad<T>(dni: T): T {
        return dni;
    }

    //Funciones de alta orden: Toman una o más funciones como argumentos o devuelven una función.
    function altaOrden(callback: (x: number) => number): number {
        return callback(10);
    }

// 4º LOCAL vs GLOBAL.
    let global: string = "Global";

    function variableLocal() : void{
        let local: string = "Local";
        console.log("Desde la función: " + global);
        console.log("Desde la función: " + local);
    }

    variableLocal();

    console.log("Fuera de la función:", global);

// 5º Ejercicio Extra
function ejercicio(cadena1 : string, cadena2 : string) : number{
    let cadenaxnumero = 0;
    for(let i = 1; i <= 100; i++){
        console.log(i);
        if(i % 3 == 0 && i % 5 == 0){
            cadenaxnumero++;
            console.log(cadena1 + cadena2);
            continue;
        }else if(i % 5 == 0){
            cadenaxnumero++;
            console.log(cadena2);
            continue;
        }else if(i % 3 == 0){
            cadenaxnumero++;
            console.log(cadena1)
            continue;
        }
    }
    return cadenaxnumero;
}

let numvecesrepetidas = ejercicio('ola','mundo');
console.log('Nº Veces:' + numvecesrepetidas);