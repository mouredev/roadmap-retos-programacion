/*
_____________________________________
https://github.com/kenysdev
2024 - JavaScript
_______________________________________
#05 VALOR Y REFERENCIA
---------------------------------------
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
*/

// ________________________________________________________
// 1. Asignación de variables "por valor":

// Inicialización:
let int1 = 111;
let boo1 = false;
let str1 = "Ben";

// Asignación:
let int2 = int1;
let boo2 = boo1;
let str2 = str1;

// Cambio:
int1 = 777;
boo1 = true;
str1 = "Bob";

// Las segundas variables no fueron afectadas.
console.log(int2, boo2, str2); // 111 false "Ben"

// Ejemplo en una función:
function fun_v(en_int, en_boo, en_str) {
    // Cambio:
    en_int = 333;
    en_boo = false;
    en_str = "Ken";
}

// Paso por valor
fun_v(int1, boo1, str1);

// No afectadas por los cambios en la función.
console.log(int1, boo1, str1); // 777 true "Bob"

// ________________________________________________________
// 2. Asignación de variables "por referencia":

// Inicialización:
let lis1 = [444, true, "Dan"];
let set1 = new Set([444, true, "Dan"]);
let dic1 = { name: "Dan" };

// Asignación:
let lis2 = lis1;
let set2 = set1;
let dic2 = dic1;

// Cambio:
lis1.splice(0, 3, 888, false, "Zoe");
set1.delete(444);
set1.delete("Dan");
dic1.name = "Zoe";

// Las variables fueron afectadas por el cambio.
console.log(lis2);
console.log([...set2]);
console.log(dic2);

// Ejemplo en una función:
function fun_r(en_lis, en_set, en_dic) {
    // Cambio:
    en_lis.splice(0, 3, 333, true, "Jay");
    en_set.add(333);
    en_set.add("Jay");
    en_dic.name = "Jay";
}

// Paso por referencia
fun_r(lis2, set2, dic2);

// Fueron afectadas por los cambios en la función.
console.log(lis2);
console.log([...set2]);
console.log(dic2);

// ________________________________________________________
// 3. DIFICULTAD EXTRA

let s1 = "Ben";
let s2 = "Zoe";
let l1 = [12, 21];
let l2 = ["Ben", "Zoe"];

console.log(`Pre-Intercambio:\n${s1} - ${s2}\n${l1} - ${l2}`);

function by_value(str1, str2) {
    let temp = str1;
    str1 = str2;
    str2 = temp;
    return [str1, str2];
}

function by_reference(list1, list2) {
    return [list2.slice(), list1.slice()];
}

const [new_s1, new_s2] = by_value(s1, s2);
const [new_l1, new_l2] = by_reference(l1, l2);

console.log(`Originales:\n${s1} - ${s2}\n${l1} - ${l2}`);
console.log(`Nuevas:\n${new_s1} - ${new_s2}\n${new_l1} - ${new_l2}`);
