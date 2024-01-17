    // Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
    /*
    Operadores de asignacion
asignacion 
    let x = 10
multiplicacion
    x *= 2
division
    x /= 2

    */

    /*
    Operadores de comparacion
igual
    ==
no es igual
    !=
estrictamente igual
    ===
desigualdad estricta
    !==
mayor que
    >
mayor o igual que
    >=
menor que
    <
menor o igual que
    <=
    */

    /*
    Aritmeticos
residuo
    %
incremento
    ++
decremento
    --
negacion unaria
    -
positivo unario
    +
exponenciacion
    **
    */

    /*
    Bit a bit
desplazamiento izquierda
    x <<= 2
desplazamiento derecha
    x >>= 2
desplazamiento derecha sin signo
    x >>>= 2
AND bit a bit
    x &= y
XOR bit a bit
    x ^= y
OR bit a bit
    x |= y
not bit 
    ~ x
     */

    /*
    Logicos
AND logico
    x &&= y
OR logico
    x ||= y
anulacion logico
    x ??= y
    */

   /*
Operador ternario
    condition ? val1 : val2
   */

    /*
    Utilizando las operaciones con operadores que tú quieras, crea ejemplos
    que representen todos los tipos de estructuras de control que existan
    en tu lenguaje:
    */
let num = 1
while(num<5){
    console.log(num)
    num ++
}

do{
    console.log(num)
    num ++
}while(num<5)

if(num == 1){
    console.log(true)
}else{
    console.log(false)
}

switch(num){
    case 1:
        console.log("odd")
        break
    case 2:
        console.log("pair")
        break
    case 3:
        console.log("odd")
        break
    case 4:
        console.log("pair")
        break
    case 5:
        console.log("odd")
        break
    default:
        console.log("invalid")
}
for(let i = 0; i <= 5; i++){
    console.log(i)
}
    // extra
for(let i = 10;i<=55;i++){
	if(i %3 ==0 ||i == 16){
		continue
	}else if(i % 2 == 0){
		console.log(i)
	}
}