/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */

console.log(`
╔══════════════════════════════════════════════════════════════════════════════╗
║                                    EJERCICIO                                 ║
║ - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:     ║
║   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia,  ║
║   bits... (Ten en cuenta que cada lenguaje puede poseer unos diferentes)     ║
║ - Utilizando las operaciones con operadores que tú quieras, crea ejemplos    ║
║   que representen todos los tipos de estructuras de control que existan      ║
║   en tu lenguaje: Condicionales, iterativas, excepciones...                  ║
║ - Debes hacer print por consola del resultado de todos los ejemplos.         ║
║                                                                              ║
║ DIFICULTAD EXTRA (opcional):                                                 ║
║ Crea un programa que imprima por consola todos los números comprendidos      ║
║ entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.   ║
║ Seguro que al revisar detenidamente las posibilidades has descubierto algo   ║
║ nuevo.                                                                       ║
╚══════════════════════════════════════════════════════════════════════════════╝
`);

let lon = 8;

// Operadores de Asignación
let va = 'hola' // Asignación de valor a variable
let si = 3; let santes = 3; let sim = 7; si += sim; // Asignación de Adición (Suma)
let ri = 9; let rantes = 9; let rim = 4; ri -= rim; // Asignación de Sustracción (Resta)
let mi = 8; let mantes = 8; let mim = 5; mi *= mim; // Asignación de Multiplización
let dvi = 9; let dvantes = 9; let dvim = 4; dvi /= dvim; // Asignación de División
let rsi = 16; let rsantes = 16; let rsim = 2; rsi %= rsim; // Asignación de Módulo (Resíduo)
let poi = 16; let poantes = 16; let poim = 2; poi **= poim; // Asignación de Potencición

let ni = 17; let niantes = 17; let vdi = 5; ni <<= vdi; // Asignación de Desplazamiento a la Izquierda <<<=
let niantesc = niantes.toString(2).padStart(lon, '0'); let nic = ni.toString(2).padStart(lon, '0');

let nd = 17; let ndantes = 17; let vdd = 5; nd >>= vdd; // Asignación de Desplazamiento a la Derecha >>=
let ndantesc = ndantes.toString(2).padStart(lon, '0'); let ndc = nd.toString(2).padStart(lon, '0');
let ndd = 76; let nddantes = 76; let vddd = 1; ndd >>= vddd; // Asignación de Desplazamiento a la Derecha >>=
let nddantesc = nddantes.toString(2).padStart(lon, '0'); let nddc = ndd.toString(2).padStart(lon, '0');

// Asignación de Desplazamiento a la Izquierda Sin Signo <<<=  NO EXISTE EN JAVASCRIPT

let nds = 17; let ndsantes = 17; let vdds = 5; nds >>>= vdds; // Asignación de Desplazamiento a la Derecha Sin Signo <<<=
let ndsantesc = ndsantes.toString(2).padStart(lon, '0'); let ndsc = nds.toString(2).padStart(lon, '0');
let ndds = 76; let nddsantes = 76; let vddds = 1; ndds >>>= vddds; // Asignación de Desplazamiento a la Derecha >>=
let nddsantesc = nddsantes.toString(2).padStart(lon, '0'); let nddsc = ndds.toString(2).padStart(lon, '0');

console.log("\n\t\t\tOperadores de Asignación");
console.log("\t+---------------------------------------------------------------------------+");
console.log("\t| Operacion                             | Nro.1    | Nro.2 | Resultado\t    |");
console.log("\t|---------------------------------------|----------|-------|----------------|");
console.log(`\t| Asigna valor a Variable (=)           | ${va}     |   N/A | ${va}           |`);
console.log(`\t| Asignación de Adición (+=)            |  ${santes}       |   ${sim}   | ${si}             |`);
console.log(`\t| Asignación de Resta (+=)              |  ${rantes}       |   ${rim}   | ${ri}              |`);
console.log(`\t| Asignación de Multipl. (*=)           |  ${mantes}       |   ${mim}   | ${mi}             |`);
console.log(`\t| Asignación de Divisio. (/=)           |  ${dvantes}       |   ${dvim}   | ${dvi}           |`);
console.log(`\t| Asignación de Módulo (%=)             |  ${rsantes}      |   ${rsim}   | ${rsi}              |`);
console.log(`\t| Asignación de Potenc. (**=)           |  ${poantes}      |   ${poim}   | ${poi}            |`);
console.log(`\t| Asignación Desp. Izq. (<<=)           |  ${niantes}      |   ${vdi}   | ${ni}            |`);
console.log(`\t|                                       | ${niantesc} |       | ${nic}     |`);
console.log(`\t| Asignación Desp. Der. (>>=)           |  ${ndantes}      |   ${vdd}   | ${nd}              |`);
console.log(`\t|                                       | ${ndantesc} |       | ${ndc}       |`);
console.log(`\t|                                       |  ${nddantes}      |   ${vddd}   | ${ndd}             |`);
console.log(`\t|                                       | ${nddantesc} |       | ${nddc}       |`);
console.log(`\t| Asignación Desp. Izq. Sin Signo (<<<=)|      No Existe en JavaScript      |`);
console.log(`\t| Asignación Desp. Der. Sin Signo (>>>=)|  ${ndsantes}      |   ${vdds}   | ${nds}              |`);
console.log(`\t|                                       | ${ndsantesc} |       | ${ndsc}       |`);
console.log(`\t|                                       |  ${nddsantes}      |   ${vddds}   | ${ndds}             |`);
console.log(`\t|                                       | ${nddsantesc} |       | ${nddsc}       |`);
console.log("\t+---------------------------------------------------------------------------+");


// Operadores Aritméticos
let s1 = 4; let s2 = 3; let suma = s1 + s2; // Suma +
let r1 = 21; let r2 = 52; let resta = r1 - r2; // Resta -
let m1 = 568; let m2 = -421; let multiplicacion = m1 * m2; // Multiplicación *
let d1 = -55; let d2 = -7; let division = d1 / d2; // División /
let mo1 = 77; let mo2 = 6; let modulo = mo1 % mo2; // Módulo %
let p1 = 13; let p2 = 7; let potenciacion = p1 ** p2; // Potenciación **

console.log("\n\t\t\tOperadores Aritméticos");
console.log("\t+-----------------------------------------------------------------+");
console.log("\t| Operacion                   | Nro.1 | Nro.2 | Resultado\t  |");
console.log("\t|-----------------------------|-------|-------|-------------------|");
console.log(`\t| Suma (+)                    |   ${s1}   |   ${s2}   | ${suma}                 |`);
console.log(`\t| Resta (-)                   |   ${r1}  |   ${r2}  | ${resta}               |`);
console.log(`\t| Multiplicación (*)          |   ${m1} |  ${m2} | ${multiplicacion}           |`);
console.log(`\t| División (/)                |   ${d1} |  ${d2}   | ${division} |`);
console.log(`\t| Módulo (%)                  |   ${mo1}  |  ${mo2}    | ${modulo}                 |`);
console.log(`\t| Potenciación (**)           |   ${p1}  |  ${p2}    | ${potenciacion}          |`);
console.log("\t+-----------------------------------------------------------------+");

// Operadores Lógicos
let y1 = true; let y2 = false; let y = y1 && y2; // AND &&
let o1 = true; let o2 = false; let o = o1 || o2; // OR ||
let n1 = false; let n = !n1; // NOT !

console.log("\n\t\t\tOperadores Lógicos");
console.log("\t+-----------------------------------------------------------------+");
console.log("\t| Operacion                   | Nro.1 | Nro.2 | Resultado\t  |");
console.log("\t|-----------------------------|-------|-------|-------------------|");
console.log(`\t| AND Lógico (&&)             | ${y1}  | ${y2} | ${y}             |`);
console.log(`\t| OR Lógico (||)              | ${o1}  | ${o2} | ${o}              |`);
console.log(`\t| NOT Lógico (!)              | ${n1} | N/A   | ${n}              |`);
console.log("\t+-----------------------------------------------------------------+");

// Operadores de Comparación
let i1 = 7; let i2 = 7; let i = i1 == i2; // Igualdad ==
let i11 = 7; let i22 = '7'; let ii = i11 == i22; // Igualdad ==
let ie1 = 5; let ie2 = 5; let ie = ie1 === ie2; // Igualdad Estricta ===
let ie11 = 5; let ie22 = '5'; let iee = ie11 === ie22; // Igualdad Estricta ===

let ds1 = 1; let ds2 = 5; let ds = ds1 != ds2; // Desigualdad !=
let ds11 = 2; let ds22 = '2'; let dsd = ds11 != ds22; // Desigualdad !=
let dse1 = 3; let dse2 = 7; let dse = dse1 !== dse2; // Desigualdad Estricta !==
let dse11 = 4; let dse22 = '4'; let dsed = dse11 !== dse22; // Desigualdad Estricta !==

let my1 = 9; let my2 = 8; let my = my1 > my2 // Mayor que >
let my11 = 15; let my22 = 20; let mym = my11 > my22 // Mayor que >
let myi1 = 82; let myi2 = 82; let myi = myi1 >= myi2 // Mayor o Igual que >=

let mn1 = 9; let mn2 = 8; let mn = mn1 < mn2 // Menor que <
let mn11 = 15; let mn22 = 20; let mnm = mn11 < mn22 // Menor que <
let mni1 = 82; let mni2 = 82; let mni = mni1 <= mni2 // Menor o Igual que <=

console.log("\n\t\t\tOperadores de Comparación");
console.log("\t+-----------------------------------------------------------------+");
console.log("\t| Operacion                   | Nro.1 | Nro.2 | Resultado\t  |");
console.log("\t|-----------------------------|-------|-------|-------------------|");
console.log(`\t| Igualdad (==)               |   ${i1}   |   ${i2}   | ${i}              |`);
console.log(`\t|                             |   ${i11}   |  '${i22}'  | ${ii}              |`);
console.log(`\t| Igualdad Estricta (===)     |   ${ie1}   |   ${ie2}   | ${ie}              |`);
console.log(`\t|                             |   ${ie11}   |  '${ie22}'  | ${iee}             |`);
console.log(`\t| Desigualdad (!=)            |   ${ds1}   |   ${ds2}   | ${ds}              |`);
console.log(`\t|                             |   ${ds11}   |  '${ds22}'  | ${dsd}             |`);
console.log(`\t| Desigualdad Estricta (!===) |   ${dse1}   |   ${dse2}   | ${dse}              |`);
console.log(`\t|                             |   ${dse11}   |  '${dse22}'  | ${dsed}              |`);
console.log(`\t| Mayor que (>)               |   ${my1}   |   ${my2}   | ${my}              |`);
console.log(`\t|                             |   ${my11}  |   ${my22}  | ${mym}             |`);
console.log(`\t| Mayor o Igual que (>=)      |   ${myi1}  |   ${myi2}  | ${myi}              |`);
console.log(`\t| Menor que (<)               |   ${mn1}   |   ${mn2}   | ${mn}             |`);
console.log(`\t|                             |   ${mn11}  |   ${mn22}  | ${mnm}              |`);
console.log(`\t| Menor o Igual que (<=)      |   ${mni1}  |   ${mni2}  | ${mni}              |`);
console.log("\t+-----------------------------------------------------------------+");

// Operadores de Pertenencia
let matriz = [1, 2, 3, 4]; let pr = 2; let npr = 7;
let pertenencia = pr in matriz; // Pertenencia in
let noPertenencia = npr in matriz; // Pertenencia in

console.log("\n\t\t\tOperadores de Pertenencia");
console.log("\t+-----------------------------------------------------------------+");
console.log("\t| Operacion                   | Nro.1   | Nro.2 | Resultado\t  |");
console.log("\t|-----------------------------|---------|-------|-----------------|");
console.log(`\t| Pertenencia (in)            | ${matriz} |   ${pr}   | ${pertenencia}            |`);
console.log(`\t|                             | ${matriz} |   ${npr}   | ${noPertenencia}           |`);
console.log("\t+-----------------------------------------------------------------+");

// Operadores a nivel de Bits
let yb1 = 4; let yb2 = 2; let yb = yb1 & yb2; // AND a nivel de bits &
let yb1c = yb1.toString(2).padStart(lon, '0'); let yb2c = yb2.toString(2).padStart(lon, '0'); let ybc = yb.toString(2).padStart(lon, '0');
let yb11 = 18; let yb22 = 2; let yby = yb11 & yb22; // AND a nivel de bits &
let yb11c = yb11.toString(2).padStart(lon, '0'); let yb22c = yb22.toString(2).padStart(lon, '0'); let ybyc = yby.toString(2).padStart(lon, '0');

let ob1 = 4; let ob2 = 2; let ob = ob1 | ob2; // OR a nivel de bits |
let ob1c = ob1.toString(2).padStart(lon, '0'); let ob2c = ob2.toString(2).padStart(lon, '0'); let obc = ob.toString(2).padStart(lon, '0');
let ob11 = 18; let ob22 = 2; let obo = ob11 | ob22; // OR a nivel de bits |
let ob11c = ob11.toString(2).padStart(lon, '0'); let ob22c = ob22.toString(2).padStart(lon, '0'); let oboc = obo.toString(2).padStart(lon, '0');

let xb1 = 4; let xb2 = 2; let xb = xb1 | xb2; // XOR a nivel de bits |
let xb1c = ob1.toString(2).padStart(lon, '0'); let xb2c = ob2.toString(2).padStart(lon, '0'); let xbc = xb.toString(2).padStart(lon, '0');
let xb11 = 18; let xb22 = 2; let xbx = xb11 ^ xb22; // XOR a nivel de bits |
let xb11c = xb11.toString(2).padStart(lon, '0'); let xb22c = xb22.toString(2).padStart(lon, '0'); let xbxc = xbx.toString(2).padStart(lon, '0');

let di1 = 17; let di2 = 5; let di = di1 << di2; // Desplazamiento a la Izquierda <<
let di1c = di1.toString(2).padStart(lon, '0'); let dic = di.toString(2).padStart(lon, '0');

let dd1 = 17; let dd2 = 5; let dd = dd1 >> dd2; // Desplazamiento a la Derecha >>
let dd1c = dd1.toString(2).padStart(lon, '0'); let ddc = dd.toString(2).padStart(lon, '0');
let dd11 = 76; let dd22 = 1; let ddd = dd11 >> dd22; // Desplazamiento a la Derecha >>
let dd11c = dd11.toString(2).padStart(lon, '0'); let dddc = ddd.toString(2).padStart(lon, '0');

// Desplazamiento a la Izquierda Sin Signo <<<=  NO EXISTE EN JAVASCRIPT

let nds1 = 17; let ndsantes1 = 17; let vdds1 = 5; nds1 >>>= vdds1; // Asignación de Desplazamiento a la Derecha Sin Signo <<<=
let ndsantesc1 = ndsantes1.toString(2).padStart(lon, '0'); let ndsc1 = nds.toString(2).padStart(lon, '0');
let ndds2 = 76; let nddsantes2 = 76; let vddds2 = 1; ndds2 >>>= vddds2; // Asignación de Desplazamiento a la Derecha >>=
let nddsantesc2 = nddsantes2.toString(2).padStart(lon, '0'); let nddsc2 = ndds2.toString(2).padStart(lon, '0');


let nb1 = 5; let nb = ~nb1 // NOT a nivel de Bits
let nb1c = nb1.toString(2).padStart(lon, '0'); let nbc = (nb >>> 0).toString(2).slice(-lon).padStart(lon, '0');

console.log("\n\t\t\tOperadores a nivel de Bits");
console.log("\t+-----------------------------------------------------------------+");
console.log("\t| Operacion                   | Nro.1    | Nro.2    | Resultado\t  |");
console.log("\t|-----------------------------|----------|----------|-------------|");
console.log(`\t| AND a nivel de bits (&)     |    ${yb1}     |    ${yb2}     |    ${yb}        |`);
console.log(`\t|                             | ${yb1c} | ${yb2c} | ${ybc}    |`);
console.log(`\t|                             |    ${yb11}    |    ${yb22}     |    ${yby}        |`);
console.log(`\t|                             | ${yb11c} | ${yb22c} | ${ybyc}    |`);
console.log(`\t| OR a nivel de bits (|)      |    ${ob1}     |    ${ob2}     |    ${ob}        |`);
console.log(`\t|                             | ${ob1c} | ${ob2c} | ${obc}    |`);
console.log(`\t|                             |    ${ob11}    |    ${ob22}     |    ${obo}       |`);
console.log(`\t|                             | ${ob11c} | ${ob22c} | ${oboc}    |`);
console.log(`\t| XOR a nivel de bits (|)     |    ${xb1}     |    ${xb2}     |    ${xb}        |`);
console.log(`\t|                             | ${xb1c} | ${xb2c} | ${xbc}    |`);
console.log(`\t|                             |    ${xb11}    |    ${xb22}     |    ${xbx}       |`);
console.log(`\t|                             | ${xb11c} | ${xb22c} | ${xbxc}    |`);
console.log(`\t| Desplazamiento Izq. (<<)    |    ${di1}    |    ${di2}     |    ${di}      |`);
console.log(`\t|                             | ${di1c} |          | ${dic}  |`);
console.log(`\t| Desplazamiento Der. (>>)    |    ${dd1}    |    ${dd2}     |    ${dd}        |`);
console.log(`\t|                             | ${dd1c} |          | ${ddc}    |`);
console.log(`\t|                             |    ${dd11}    |    ${dd22}     |    ${ddd}       |`);
console.log(`\t|                             | ${dd11c} |          | ${dddc}    |`);

console.log(`\t| Desp. Izq. Sin Signo (<<<=) |      No Existe en JavaScript      |`);
console.log(`\t| Desp. Der. Sin Signo (>>>=) |  ${ndsantes1}      |    ${vdds1}     | ${nds1}           |`);
console.log(`\t|                             | ${ndsantesc1} |          | ${ndsc1}    |`);
console.log(`\t|                             |  ${nddsantes2}      |   ${vddds2}      | ${ndds2}          |`);
console.log(`\t|                             | ${nddsantesc2} |          | ${nddsc2}    |`);


console.log(`\t| NOT a nivel de Bits (~)     |    ${nb1}     |    N/A   |    ${nb}       |`);
console.log(`\t|                             | ${nb1c} |          | ${nbc}    |`);
console.log("\t+-----------------------------------------------------------------+");

// Estructuras de Control

// Condicional IF
let pisos = 7; let conf = 4; let impIf;
if(pisos >= conf){
    impIf = "Es edificio";
}
else{
    impIf = "No es edificio :(";
}

// Switch
let opcion = 3; let impSwitch
switch(opcion){
    case 1:
        impSwitch = "C#";
        break;
    case 2:
        impSwitch = "Pyton";
        break;
    case 3:
        impSwitch = "JavaScript";
        break;
    default:
        impSwitch = "Otro";
}

console.log("\n\t\t\tCondicionales");
console.log("\t+-------------------------------------------------------------------------------------+");
console.log("\t| Operador                    | Comparación                                           |");
console.log("\t|-----------------------------|-------------------------------------------------------|");
console.log(`\t| Condicional IF              | Si nro. de pisos ${pisos} >=  ${conf} entonces "${impIf}"       |`);
console.log(`\t| Condicional SWITCH          | Si la opcion = ${opcion} entonces es ${impSwitch}               |`);
console.log("\t+-------------------------------------------------------------------------------------+");

// Bucles

// Bucle FOR
let maxNum = 100; let divisor = 7; let modFor; let esDivisible = []; let j = 0;
for(i = 0; i <= maxNum; i++){
    modFor = i % divisor;
    if(modFor === 0){ esDivisible[j] = i; j++; }
}

// Bucle While
let = colorEncontrado = false; let colores = ["amarillo", "azul", "rojo", "verde", "violeta"]; i = 0; 
let colorBuscado = "rojo"; let mensajeColor;
while(!colorEncontrado){
    if(colorBuscado === colores[i]){
        mensajeColor = `Color "${colorBuscado}" encontrado en los colores: ${colores}`;
        colorEncontrado = true;
    }
    i++;
}

// Do-WHILE
let listaFrutas = ["Pera", "Manzana", "Plátano", "Papaya"]; let msgFruta;
let buscarFruta = "Autobus";
do{
    msgFruta = `Buscando la fruta "${buscarFruta}" en "${listaFrutas}" => "Se ejecuta 1 vez" :(`;
} while(listaFrutas[i] === buscarFruta)

console.log("\n\t\t\tBucles");
console.log("\t+--------------------------------------------------------------------------------------------------------+");
console.log("\t| Bulce           | Comparación                                                                          |");
console.log("\t|-----------------|--------------------------------------------------------------------------------------|");
console.log(`\t| Bucle FOR       | Num. divisibles para ${divisor} desde el 0 al ${maxNum}: ${esDivisible} |`);
console.log(`\t| Bucle WHILE     | ${mensajeColor}             |`);
console.log(`\t| Bucle DO-WHILE  | ${msgFruta}|`);
console.log("\t+--------------------------------------------------------------------------------------------------------+");

//Excepciones

console.log("\n\t\t\tExcepciones");
console.log("\t+--------------------------------------------------------------------------------------------------------+");
console.log("\t| Bloque            | Ejecución                                                                          |");
console.log("\t|-------------------|------------------------------------------------------------------------------------|");
try{
    console.log(`\t| TRY-CATCH-FINALLY | TRY     => Intenta hacer algo y se produce un error....                            |`);
    throw new Error("Este es un error personalizado !!!");
}
catch(error){
    console.error("\t|                   | CATCH   => Se captura el Error: ", error.message + "                |");
}
finally{
    console.log("\t|                   | FINALLY => Termina la ejecuciión independientemente del Error !!!                  |");
}
    
console.log("\t+--------------------------------------------------------------------------------------------------------+");

// Dificultad extra
console.log("\n\t\t\tDificultad Extra");
console.log("\t+-------------------------------------------------------------------+");
console.log("\t| Números entre 10 y 55 (incluidos), pares, no 16 ni múltiplos de 3 |");
console.log("\t|-------------------------------------------------------------------|");
for(let i = 10; i <= 55; i++){
    if((i % 2 === 0) && (i !== 16) && (i % 3 !== 0))
        console.log(`\t| ${i}                                                                |`);
};
console.log("\t+------------------------------------------------------------------ +");


