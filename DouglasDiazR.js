/*Operadores Aritméticos */

//Suma +
var suma = 4 + 5;
console.log("suma: " + suma);

//Resta -
var resta = 5 - 2;
console.log("resta: " + resta);

// Multiplicación *
var multiplica = 5 * 5;
console.log("multiplicación: " + multiplica);

//División /
var divide = 10 / 2;
console.log("División: " + divide);

//Módulo o Resto
var resto = 20 % 2;
console.log("Resto: " + resto);

/*Operadores de Asignación */

//Asignación =
var variable = "VALOR ASIGNADO";
console.log("este es un " + variable);

//Asignación con Operación += , -= , *= , /= , %=
var a = 3;
a += 5; // ésto es igual a hacer a = a + 5. Igual para los otros operadores aritméticos
console.log(a);


/*Operadores de Comparación*/

//Igualdad Estricta ===
var igualdadEstricta = ( 3 === 3);//true

//igualdad 
var igualdad = (3 == "3"); //true

//Desigualdad Estricta !==
var desigualdadEstricta = (2 !== "2"); //true

//Desigualdad
var desigualdad = (4 != "4"); //false

//Mayor que >
var mayor = (5 > 3); //true

//Menor que <
var menor = (3 < 5); //true 

//Mayor o Igual que >=
var mayorIgual = (5 >= 5); //true

//Menor o ------igual que <=
var menorIgual = (3 <= 10); //true


/*Operadores Lógicos*/

//AND &&
var and = (true && false) //si todas las condiciones son true, devuelve true, si no retorna false

//OR ||
var or = (true && false) //si alguna de las condiciones son true, devuelve true, si no retorna false

//NOT !
var not = !true; //false


/*OPERADORES DE INCREMENTO Y DECREMENTO*/

//Incremento ++
var incremento = 5;
incremento++; // ésto es igual a hacer (incremento = incremento + 1)
console.log("incremento: " + incremento);

//Decremento --
var decremento = 5;
decremento --; //éstp es igual a hacer (decremento = decremento - 1)
console.log("decremento: " + decremento);

/*ESTRUCTURAS DE CONTROL CONDICIONALES*/

//if
var a = 5;
var b = 3;
if(a > b){
    console.log(a + " es mayor que " + b );
}

//if-else
var edad = 18;
if(edad >= 18){
    console.log("Es Mayor de Edad");
}
else{
    console.log("Es Menor de Edad");
}

//if-else if
var semaforo = "verd";
if(semaforo === "verde"){
    console.log("Siga");
}
else if(semaforo === "amarillo"){
    console.log("precaución");
}
else if(semaforo === "rojo"){
    console.log("Pare");
}
else{
    console.log("error");
}


//Switch
var numero = 5;
switch(numero){
    case numero % 2 == 0:
        console.log(numero + " Es un número par");
        break;
    case numero % 3 == 0:
        console.log(numero + " Es un multiplo de 3");
        break;
    default:
        console.log(numero + " No es multiplo de 2 ni de 3");
}


/*ESTRUCTURAS DE CONTROL ITERATIVAS */

//For
for(i = 0; i <= 10; i++){
    console.log("el valor de i es: " + i);
}

var numero = 2;
while( numero % 2 ===0 && numero < 10 ){
    console.log("número par: " + numero);
    numero += 2;
    }


//do-while  
var numero = 3;
do{
    console.log(numero + " Es Múltiplo de 3");
    numero += 3;
}
while( numero % 3 ===0 && numero < 10 );

//for in
var jugadores = {
    nombre: 'Juan',
    numero: 9,
    posicion: 'Delantero'
};

for (var jugador in jugadores) {
    console.log(jugador + ': ' + jugadores[jugador]);
}

//for of
var colores = ['rojo', 'verde', 'azul'];
for (var color of colores) {
    console.log(color);
}

//break
for(i = 0; i <= 10; i++){
    console.log(i);
    if(i === 5){
        break;
    }
}
    

//continue
numero = 0;
while(numero <= 20){
    numero ++;
    if(numero % 3 === 0){
        continue;
    }
    console.log(numero + " No es Múltiplo de 3");
}


/*DIFICULTAD EXTRA*/

for(i = 10; i < 55; i ++){
    if( i % 2 === 0 && i != 16 && i % 3 !== 0){
        console.log(i)
    }
}





