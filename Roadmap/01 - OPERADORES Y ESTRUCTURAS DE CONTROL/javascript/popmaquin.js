/*
*____________________________
*|                          |
 |        Operadores        |  
*|__________________________|
*/

/* Operadores Aritméticos*/
console.log("Suma de 5+5 es: " + (5+5));
console.log("Resta de 5-5 es: " + (5-5));
console.log("Multiplicación de 5*5 es: " + (5*5));
console.log("Divición de 5/5 es: " + (5/5));
console.log("Modulo de 5%5 es: " + (5%5));
console.log("Potencia de 2^5 es: " + (2**5)); //2**5 == (2x2x2x2x2)

/* Operadores lógicos*/
console.log("Operador AND: " + (true && true));
console.log("Operador OR: "  + (true || false));
console.log("Operador NOT: " + (!true));

/* Operadores de comparacion*/
console.log("Operador igualdad: " + (5==5));        //compara 
console.log("Operador igualdad triple: "+ (5===5)); //compara y comprueba dato
console.log("Operador menorque: " + (5<5));
console.log("Operador mayorque: " + (5>5));
console.log("Operador menor igual que: " + (5<=5));
console.log("Operador mayor igual que: " + (5>=5));
console.log("Operador desigualdad: " + (5!=5));
console.log("Operador desigualdad estricta: " + (5!==5));

/* Operadores de asignacion*/
let x, y; 
x=8; y=2; 
console.log("Asignacion de x=8: " + (x=8)); 
console.log("Asignacion de suma: x+=y " + (x+=y));
console.log("Asignacion de resta: x-=y " + (x-=y));
console.log("Asignacion de multiplicación: x*=y " + (x*=y));
console.log("Asignacion de division: x/=y " + (x/=y));
console.log("Asignacion de potencia: x**=y " + (x**=y));
console.log("Asignacion de residuos: x%=y " + (x%=y));
console.log("Asignacion de desplazamiento a la izquierda: x<<=y " + (x<<=y));
console.log("Asignacion de desplazamiento a la derecha sin signo: x>>>=y " + (x>>>=y));
console.log("Asignacion AND bit a bit: x&=y " + (x&=y)); // x & = y == x = x & y;
console.log("Asignacion AND bit a bit: x|=y " + (x|=y));

/* Operadores de unarios*/
let a=2;
console.log("Valor de a inicial: " +a);     //a=2
console.log("Incremento a++: "+ (a++));     //a=2
console.log("Valor de a ahora: " +a);       //a=3
console.log("Decremento a--: " + (a--));    //a=3
console.log("Valor de a ahora: " +a);       //a=2
console.log("Incremento previo ++a: "+ (++a)); //a=3
console.log("Valor de a ahora: " +a);          //a=3
console.log("Decremento previo --a: " + (--a));//a=2
console.log("Valor de a ahora: " +a);          //a=2
console.log("Resta unaria -a: " + (-a));       //a=-2 vuelve negativo el valor



/* Operadores de bit a bit*/
    console.log("AND=& Devuelve uno, si ambos son iguales a uno: " + (14 & 13) );   // [ 1110 & 1101 ] Salida:1100= 12 
    console.log("OR=| Devuelve cero, si ambos son iguales a cero: " + (14 | 13) ); // [ 1110 & 1101 ] Salida:1111= 15 
    console.log("XOR=^ Devuelve cero, si ambos son iguales a uno y uno si son diferentes: " + (14 ^ 13) ); // [ 1110 & 1101 ] Salida:0011= 3 
    console.log("NOT=~  Invierte los bits: " + (~14) ); // [ 1110 ] Salida: 1111= -15

/* Operadores de cadena*/
    console.log("Mi" + " país" + " Guatemala"); //salida: "Mi país Guatemala"

/*___________________________
*|                          |
 |   Estructura de control  |  
*|__________________________|
*/

/*** tipos de estructuras de control ***/

/*condicional if*/
let edad=2 //Puede cambiar los valores de edad.
    if (edad<0) {
        console.log("Es numero negativo, ingrese una edad valida"); 
    } else if (edad===0) {
        console.log("Recien nacido ");          
    
    } else if (edad>=18) {
        console.log("Eres mayor de edad ");          
    } 
    else{
        console.log("Eres menor de edad")
    }

/*condicional switch*/
let opcion=prompt("Ingres uno de los dias de la semana: ");

switch (opcion) {
    case "lunes":
        console.log("Feliz semana, Desarrolla el éxito a partir de los fracasos.");
        break;
    case "martes":
        console.log("Hoy puede ser un día difícil, pero recuerda que cada desafío superado te hace más fuerte.");
        break;
    case "miercoles":
        console.log("Las tormentas no duran para siempre.");
        break;
    case "jueves":
        console.log("La acción es la clave fundamental de todo éxito.");
        break;
    case "viernes":
        console.log("No importa cuántas veces caigas, lo importante es cuántas veces te levantes.");
        break;
    case "sabado":
        console.log("Cada día es una nueva oportunidad para empezar de nuevo y hacerlo mejor.");
        break;
    case "domingo":
        console.log("No esperes a que las oportunidades lleguen, créalas tú mismo.");
        break;
    default:
        console.log("Ingrese los nombres de los dias validos.");
        break;
}

/*Iterativas.*/ //for 
for (let index = 0; index < 5; index++) {
    console.log("mensaje "+ index);  
    //imprime la palabra mensaje 5 veces.   
}

//for in
let array = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
for (i in array) {
    console.log(array[i]);
}

//do while
let tecla = '';
do{
    tecla = prompt("Adivina!!!..¿Qué cosa es que cuanto más le quitas más grande es?:");
}while (tecla != 'el agujero');
alert("Has acertado");

//while
let i=0;
while (i<5) {
    console.log("Hola!");
    i++;
}
// try catch

try {
    const prueba = 7
    console.log(prueba);
    prueba = 10;
} catch (error) {
    console.log(error); //TypeError: Assignment to constant variable. at <anonymous>
    console.log("Error de sintaxis, imposible reasignar valor variable constante."); 
} finally{
    console.log ("Saliendo del try catch");
}       
    console.log ("Fuera del try catch");

/*___________________________
*|                          |
 |   Extra Opcional         |  
*|__________________________|
*/
for(numero=10; numero<=55; numero++){
    if(numero%2==0 && (numero%3!=0) && (numero!=16)){
    console.log(numero);
    }
}
/*Salida: 10, 14, 20, 22, 26, 28, 32, 34, 38, 40, 44, 46, 50, 52*/ 