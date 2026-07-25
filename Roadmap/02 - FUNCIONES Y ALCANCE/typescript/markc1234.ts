// EJERCICIO:

(() => {
    // Crea ejemplos de funciones básicas que representen las diferentes posibilidades del lenguaje:
    function funcion1():void {
        console.log("Funcion que no recibe parametros")
    }
    funcion1()

    // Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
    const funcion2 = (a:number,b:number):number => {
        console.log("Funcion que recibe dos parametros y retorna un numero")
        return a + b
    }
    
    // Comprueba si puedes crear funciones dentro de funciones.
    const funcion3 = () => {
        const funcion4Anidada = () => {
            console.log("Esta es una funcion interna")
        }
        funcion4Anidada()
    }
    funcion3()

    // Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
    function funcion5() {
        return funcion2(25, 25)
    }
    const suma = funcion5()
    console.log(suma)

    // Pon a prueba el concepto de variable LOCAL y GLOBAL.
    let varGlobal:string = "GLOBAL"
    const funcion6 = () => {
        let varLocal: string = "LOCAL"
        // Debes hacer print por consola del resultado de todos los ejemplos.
        console.log(varLocal)
        console.log(varGlobal)
    }
    // (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
    funcion6()
    
    // DIFICULTAD EXTRA (opcional):
    // Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
    function funcionExtra(p1:string, p2:string):number {
        let contador:number = 0

        // La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
        for (let i = 1; i <= 100; i++) {
            // Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
            if(i % 3 === 0 && i % 5 === 0) {
                console.log(p1 + " " + p2)
            }
            // Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
            else if(i % 3 === 0) {
                console.log(p1)
            } else if(i % 5 === 0) {
                // Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
                console.log(p2)
            }
            
            contador += 1
        }
        // La función retorna el número de veces que se ha impreso el número en lugar de los textos.
        
        return contador
    }
})()