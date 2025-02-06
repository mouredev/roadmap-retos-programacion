/*
 EJERCICIO:
 - Crea ejemplos de funciones básicas que representen las diferentes
   posibilidades del lenguaje:
   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 - Comprueba si puedes crear funciones dentro de funciones.
 - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 - Debes hacer print por consola del resultado de todos los ejemplos.
   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)

 DIFICULTAD EXTRA (opcional):
 Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 
 Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */

 //Funciones básicas
 function sinP(){
    console.log("Esta es una función sin parámetros ni retorno");
 };

 sinP();

 function con1P(num1){
    console.log(`Esta es una función con ${num1} parámetro`);
 };

 con1P(1);

 function conMasP(num1, num2){
    console.log(`Esta es una función con ${num1} parámetros y ${num2} retornos`);
 };

 conMasP(2,0);
 
 function conR(num1) {
    return 1
 };

 console.log(`Esta es una función con ${conR()} retorno`);
 
 //Funciones dentro de funciones
 function calcularDescuento(precio) {
    const descuento = 15;

    function descontar(precio) {
        return (precio * descuento)/100;
    }
    
    const total = precio - descontar(precio);
    return total;
 };

 const totalDescuento = calcularDescuento(120);
 console.log(`El precio con el 15% de descuento es: ${totalDescuento}`);

 //Funciones ya creadas en el lenguaje

 function valNaN(x) {
    if (isNaN(x)) {
        console.log('!No es un número¡');
    } else {
        console.log(`El número es: ${x}`)
    };
 };

 valNaN(NaN);
 valNaN(900);

 function valFinite(x) {
    if (isFinite((1000 / x))) {
        console.log('No es un número infinito');
    } else {
        console.log('El número es inifinito');
    };
 };

 valFinite(0);
 valFinite(10);
