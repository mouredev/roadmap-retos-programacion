let x   = 3;
let y = 2;
console.log("los numeros son x = 3 y y = 2");

//****OPERADORES ARITMETICOS****
//SUMA
console.log("SUMA = "  +(x+y));
//RESTA
console.log("RESTA = "  +(x-y));
//MULTIPLICACION
console.log("MULTIPLICACION = "  +(x*y));
//DIVISION
console.log("DIVISION = "  +(x/y));
//MODULAR
console.log("MODULAR = "  +(x%y));
//EXPONENCIAL
console.log("EXPONENCIAL = "  +(x**y));
//INCREMENTO  x++
console.log("INCREMENTO = " +(x++));//devuelve x=3 luego incrementa
//DECREMENTO  x--
console.log("DECREMENTO = " +(x--)); //devuelve x=4 luego decrementa
//INCREMENTO ++x
console.log("INCREMENTO = " +(++x));//incrementa luego devuelve el valor de x
//DECREMENTO   --x
console.log("DECREMENTO = " +(--x)); //decrementa luego devuelve el valor de x

//****OPERADORES DE ASIGNACION****
//ASIGNACION SIMPLE
console.log("ASIGNACION SIMPLE = " + (x=x));
//ASIGNACION CON SUMA
console.log("ASIGNACION CON SUMA = " + (x+=x));
//ASIGNACION CON RESTA
console.log("ASIGNACION CON RESTA = " + (y-=x));
//ASIGNACION CON MULTIPLICACION
console.log("ASIGNACION CON MULTIPLICACION = " + (x*=x));
//ASIGNACION CON DIVISION
console.log("ASIGNACION CON DIVISION = " + (x/=x));
//ASIGNACION CON MODULO
console.log("ASIGNACION CON MODULO = " + (x%=x));
//ASIGNACION CON EXPONENCIAL
console.log("ASIGNACION CON EXPONENCIAL = " + (x**=x));

//****OPERADORES DE COMPARACION****
//IGUALDAD
console.log("IGUALDAD = " + (x==y));//compara valores
//IGUALDAD ESTRICTA
console.log("IGUALDAD ESTRICTA= " + (x===y));//compara valores y tipos estrictamente iguales
//DESIGUALDAD
console.log("IGUALDAD ESTRICTA= " + (x!=y));//compara valores 
//DESIGUALDAD ESTRICTA
console.log("DESIGUALDAD ESTRICTA= " + (x!==y));//compara valores y tipos estrictamente desiguales
//MAYOR QUE 
console.log(x+" ES MAYOR QUE "+y+ "="+ (x>y));//devuelve valores true o false depende si x es mayor que y
//MAYOR QUE 
console.log(x+" ES MAYOR IGUAL QUE  "+y+ "="+ (x>=y));
//MENOR QUE 
console.log(x+" ES MENOR QUE "+y+ "="+ (x<y));//devuelve valores true o false depende si x es menor que y
//MENOR QUE 
console.log(x+" ES MENOR IGUAL QUE "+y+ "="+ (x<=y));

//****OPERADORES DE LOGICOS****
//AND LOGICO(Y)
console.log("OPERADOR x&&y = "+(x&&y));

//NOT LOGICO(NO)
console.log("OPERADOR x!y  SIGNIFICA NOT");

//****OPERADORES BIT A BIT****
//AND 
console.log("OPERADOR x&y = "+(x&y));
//OR 
console.log("OPERADOR x|y = "+(x|y));
//XOR OR EXCLUSIVO
console.log("OPERADOR x^y = "+(x^y));
//NOT A BIT
console.log("OPERADOR x~y ");
//DESPLAZAMIENTO A LA IZQUIERDA
console.log("DESPLAZAMIENTO A LA IZQUIERDA = " + (x<<1));
//DESPLAZAMIENTO A LA DERECHA
console.log("DESPLAZAMIENTO A LA DERECHA = " + (x>>2));
//DESPLAZAMIENTO A LA DERECHA SIN SIGNO
console.log("DESPLAZAMIENTO A LA DERECHA SIN SIGNO = " + (x>>>3));

//****OPERADORES TERNARIOS****
let w = true;
let z =false;
console.log(x<=y  ?  z : w);// devuelve el valor de z si la condicion es correcta, de lo contrario devuelve w

//****OPERADORES DE TIPOS****
//TIPO DE UNA VARIABLE
console.log("TIPEOF TIPO DE UNA VARIABLE  = " + (typeof(x)));
//INSTANCIA DE UNA CLASE
let color="blue"
console.log("INSTANCEOF TIPO DE UNA VARIABLE  = " + (color  instanceof  String));
let color2 = new String("red");
console.log("INSTANCEOF TIPO DE UNA VARIABLE  = " + (color2  instanceof  String));
//IN  : Verifica si una propiedad existe en un objeto
console.log(0 in color2);
let array ={persona:"hola", saludando:"como estas"};
console.log("persona" in array);

//****OPERADORES DE DESTRUCTURACION****
//EJEMPLO DE DESTRUCTURACION CON ARRAY
const frutas  = ['banana', 'melon', 'mango'];

const fruta=[fruta1, fruta2, fruta3] = frutas;

console.log(fruta1, fruta2, fruta3);

//EJEMPLO DE DESTRUCTURACION CON OBJETO
const objeto={
    nombre: "Juan",
    apellido: "Perez",
    edad: 30
}

const {nombre, apellido, edad} = objeto;

console.log(nombre, apellido, edad);

//EJEMPLO DE DESTRUCTURACION CON VALORES PREDETERMINADOS

const colores=[ 'rojo'];

const [color1, color5='azul'] = colores;

console.log(color1);
console.log(color5);

//EJEMPLO DE DESTRUCTURACION EN OBJETOS ANIDADOS

const persona = {
    nombre: "Juan",
    apellido: "Perez",
    edad: 30,
    direccion: {
        ciudad: "Madrid",
        pais: "España"
    }
}

const { direccion: {ciudad, pais} } = persona;

console.log(ciudad, pais);

//EJEMPLO DE DESTRUCTURACION CON ELEMENTO SPREAD

const [primero, ...resto] = [1,2,3,4,5];

console.log(primero);
console.log(resto);


//***ESTRUCTURAS DE CONTROL
//CONDICIONALES (if, else if, else)
/*if(condicion){
  si la primera condicion es verdadera
}else if(otra condicion){
 si la otra condicion es verdadera 
}else{
 si ninguna de las dos condiciones anteriores son verdaderas
}*/
let condicion = 10;
if(condicion > 5){
  console.log("La condicion es verdadera");
}else if(condicion<5){
    console.log("La segunda condicion es verdadera");
}
else{
  console.log("La condicion es falsa");
}

//CONDICIONAL TERNARIO
//condicion ? exp1 : exp2

const esMayorDeEdad = edad >= 18 ? "Sí" : "No";
console.log(esMayorDeEdad); // Sí

//SWITCH

let dia = 2;
switch(dia){
  case 1:
    console.log("Lunes");
    break;
  case 2:
    console.log("Martes");
    break;
  case 3:
    console.log("Miércoles");
    break;
  case 4:
    console.log("Jueves");
    break;
  case 5:
    console.log("Viernes");
    break;
  case 6:
    console.log("Sábado");
    break;
  case 7:
    console.log("Domingo");
    break;
  default:
    console.log("Día inválido");
}

//BUCLES FOR, WHILE, DO WHILE
//FOR

for(let i=0; i<5; i++){
  console.log(i);
}

//WHILE 

let j = 0;
while(j<5){
  console.log(j);
  j++;
}

//DO WHILE

let k = 0;
do{
  console.log(k);
  k++;
}while(k<5);

//BUCLES CON INTERRUPCIONES BREAK, CONTINUE
//BREAK

for(let i=0; i<5; i++){
  if(i===2){
    break;
  }
  console.log(i);
}

//CONTINUE

for(let i=0; i<5; i++){
  if(i===2){
    continue;
  }
  console.log(i);
}

//BUCLES CON ITERADORES FOR IN, FOR OFF
//FOR IN
let persona1 = {
  nombre: "Juan",
  apellido: "Perez",
  edad: 30
}

for(let propiedad in persona1){
  console.log(propiedad, persona1[propiedad]);
}

//FOR OFF

let numeros = [1, 2, 3, 4, 5];

for (const numero of numeros) {
    console.log(numero);
}

//***TRY CATCH FINALLY

try {
  //codigo que puede generar excepciones
  let numero = 10 / 0;
} catch (error) {
  //codigo que se ejecuta cuando se produce una excepcion
  console.error("Hubo un error: ", error);
} finally {
  //codigo que se ejecuta siempre, independientemente de si hubo excepcion o no
  console.log("Este codigo siempre se ejecuta");
}

//***FOR EACH

let numeros2 = [1, 2, 3, 4, 5];

numeros2.forEach(function(numero){
  console.log(numero);
});

//***MAP

let numeros3 = [1, 2, 3, 4, 5];

let numerosMultiplicados = numeros3.map(num=>num*2);

console.log(numerosMultiplicados);

//***FILTER

let caramelos=['rojos','azul','rojos', 'verde','rojos','verde'];

let caramelosRojos = caramelos.filter(caramelo=>caramelo==='rojos');

console.log(caramelosRojos);

//***FIND

let caramelosVerdes = caramelos.find(caramelo=>caramelo==='verde');

console.log(caramelosVerdes);


//***REDUCE

let numeros4 = [1, 2, 3, 4, 5];

let suma = numeros4.reduce((total, numero) => total + numero, 0);

console.log(suma);

//***SORT

let numeros5 = [5, 2, 8, 1, 3];

numeros5.sort((a, b) => a - b);

console.log(numeros5);


//***DIFICULTAD EXTRA****

for (let i = 10; i <= 55; i++) {
    if ((i % 2 == 0 || i===55)&& i !== 16 && i % 3 !== 0) {
      console.log(i);
    }
  }
  