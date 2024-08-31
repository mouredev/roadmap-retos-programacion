/****************REFERENCIAS**************************************************************
*Referencia de JavaScript: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference
*Referencia de JavaScript Estandarizado (ECMAScript): 
*   https://www.ecma-international.org/
*   https://ecma-international.org/publications-and-standards/standards/ecma-262/
*******************************************************************************************/
//declaracion de variables
var primeraDeclaracion;           //estoy declarando una variable, pero no se inicializa, 
let segundaDeclaracion;           //su valor sera undefined
//inicializacion de variables
primeraDeclaracion = 0;           //aqui inicializo mis variables
segundaDeclaracion = 12;

/*******************************
 * TIPOS DE DATOS EN JAVASCRIPT*
 ******************************/

let myBool = Boolean();             //Boolean   -> valores pueden ser: true, false un boleano. Es un wrapper (funcion que se llama segun convenga)
let myNumber = Number();            //Number    -> en escencia es un flotante de (double-precision) de 64bits  esta definido segun IEEE 754
let myBigInt = BigInt(2393243);     //BigInt    -> trabaja segun el estandard de formato de precision arbitrario, esto significa que sus digitos estan limitados por el poder de la memoria disponible en el host
let myString = String("Muestra");   //String    -> es texto o cadena de caracteres, en escencia es tambien un wrapper (funcion que se llama segun convenga)
let mySymbol = Symbol("@");         //Symbol    -> regresan una primitiva de symbol y estan garantizados de retornar un symbol unico
                                //Object    ->
let soyNull = null;                 //null      -> valor primitivo de javascript, pero es en escencia un objeto
let noDefinido = undefined;         //undefined -> valor primitivo de javascript, se asignan automaticamente a variables no inicializadas
let noDefinido2;

console.log("myNumber: ",myBool);
console.log("myNumber: ",myNumber);
console.log("myBigInt: ",myBigInt);
console.log("myString: ",myString);
console.log("mySymbol: ",mySymbol);
console.log("soyNull: ",soyNull);
console.log("noDefinido: ",noDefinido);
console.log("noDefinido2: ",noDefinido2);

myNumber = Number(myBigInt);            //aqui convertimos de BigInt a Number
console.log("myNumber: ",myNumber);
/*********************************
*Las siguientes son constantes****
*********************************/
const Uno = 1;                                  //declaracion y asignasion en la misma linea, 
const Hola = "Hola";                            //constantes deben inicializarce en la misma linea en que son declaradas
   
//las constantes no se pueden re-declarar ni pueden cambiar valor por asignasion, pero
//pueden mutar
const credenciales = {nombre: "Simon", apellido: "Belmonth", clave: "MyVampireKillerShinesLikeADimond"};
console.log("clave original de Simon: ",credenciales.clave);
credenciales.clave="TuAmigoDracula";
console.log("clave hackeada de Simon: ", credenciales.clave);
credenciales["contacto"]= "1111111";
console.log(credenciales);
//el contenido de los arreglos tampoco estan protegidos y por tanto lo siguiente es permitido
const misJuegos = ["SILENT HILL 2","ELDEN RING","FFXVI","CHRONO TRIGGER"];
console.log("Juegos originales: ",misJuegos);
misJuegos.push("LUFIA FORTRESS OF DOOM");
console.log("Juegos actualizados: ",misJuegos);


/*********************************
*Las siguientes son variables****
*********************************/

let variableLocalMayor = "Fui declarada al inicio del codigo"; //Variables declaradas con let tienen alcance 
let variableLocal = 10;                                        //dentro del bloque y sus sub-bloques
var variableGlobal = 0.5;   //variables que usan var, pueden tener alcance global, modular o dentro de funcion


//formas de asignasion de variables
var miArray = [1,2,3,4,5];                      //declaracion y asignasion de array
var miObjeto = {A: "Si", B: "No", C: "Talvez"}; //declaracion y asignasion de objeto
var misDimensiones = {X: 22.4, Y: 83.1, Z: 10}; //otro objeto, pero con numeros


/*************************************************************************
*La siguiente forma de asignasion se conoce como destructuring assignment*
*************************************************************************/
const {A} = miObjeto; 
({X,Z} = misDimensiones);
[a,b,c,d,...others] = [1,2,3,4,5,6,7,8,9,0,10,20,30,40,50];//aqui utilizamos la propiedad rest (resto)
//rest property, quiere decir que tomamos algunas variables especificas como a,b,c y d, pero
//el resto de valores los almacenamos en others, esta variable debe ser la ultima y debe comenzar con ...(...others en este caso)
let {C, Y} = {...miObjeto, ...misDimensiones};     //esta asignasion se da por una fusion o merge y se toman los elementos C y Y por destructuring assignment
var union = {...miObjeto, ...misDimensiones};   //esta asignasion se da por una fusion de objetos (merge)

console.log("Hoisted variable: ",hoisted);// una traduccion es elevacion de variable, la variable es declarada en la siguiente linea, 
//pero ya existe, sin embargo no tiene asignado ningun valor, mostrara undefined
var hoisted = "Ya fui declarada";
console.log("Hoisted variable con valor: ",hoisted);// aca mostramos la variable global nuevamente, ya tiene un valor asignado



/*************************************************
 * HOISTING (IZAMIENTO O ELEVACION) EN FUNCIONES**
 ************************************************/
console.log(callMyName());//esta funcion es declarada hasta el final, pero por propiedad de hoisting javascript
//la define por completo desde iniciado el programa

let copiaFuncion = imprimeEsto; //podemos copiar la direccion de la funcion, 
                                //no se copia sino que se toma la referencia de la region de memoria
console.log("Aqui se copio una funcion, la funcion no se llama si no se usa (), en la siguiente linea se imprimira \
por medio de su copia");
copiaFuncion(); //Ahora se llama la funcion por medio de su referencia


/**********************************************************************************************
 * LOS SIGUIENTES BLOQUES DE CODIGO MUESTRAN EL USO BASICO DE LAS VARIABLES E IMPRIME ALGUNAS,* 
 * PERO NO ES ESCENCIAL PARA EL RETO, MAS QUE NADA DEMUESTRAN EL SCOPE DE LAS VARIABLES********
 * 
**********************************************************************************************/
console.log("constant A: ",A,"local variable C: ",C,"local variable Y: ",Y);
console.log("X: ",X,"Z: ",Z);
console.log("a: ", a, "b: ", b, "c: ", c, "d: ", d, "others: ", others);
console.log("union:", union);


{
    
    console.log("dentro de bloque 1 valor variable global: ",variableGlobal);
    console.log("dentro de bloque 1 valor variable local: ",variableLocal);
    {
        const Hola = "Hola 2";

        var variableGlobalPluss = "soy Global";//
        var variableGlobal = 0.1;
        let variableLocal = 5;             //Esta variableLocal tiene el mismo nombre que la variableLocal declarada en bloque anterior, pero su alcance es este bloque
        
        console.log("dentro de sub-bloque valor variable Global: ",variableGlobal); //se imprime 0.1
        console.log("dentro de sub-bloque valor variable local: ",variableLocal); //se imprime 5
        variableLocal += 20;
        console.log("dentro de sub-bloque valor variable local:: ",variableLocal);//se imprime 25
        
        console.log(Hola); 
        console.log(variableLocalMayor,", pero en este momento esta en un sub-bloque de codigo");//las variables 
        //locales viven dentro de todo su propio bloque y sus sub-bloques, 
        //pero solo tienen prioridad en el nivel de bloque en que son declaradas, 
        //y mueren al terminar todo el bloque
        variableLocalMayor+=" (modificada en sub-bloque)";
    }
    console.log(Hola); 
    console.log("dentro de sub-bloque valor variable local:: ",variableLocal);//se imprime 25
    console.log("dentro de sub-bloque valor variable Global: ",variableGlobal); //se imprime 0.1
    
    console.log("Las Variables globales se pueden usar fuera del bloque donde se declaran: ",variableGlobalPluss);

}
console.log(variableLocalMayor,", y en este momento esta al final del codigo");




function callMyName(){
    return "Athanasius";
}
function imprimeEsto(){
    console.log("Yes, Master, My Master!!");
}

