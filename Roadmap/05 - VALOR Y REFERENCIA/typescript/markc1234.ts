(() => {
    //  EJERCICIO:
    //  Muestra ejemplos de asignación de variables "por valor" y "por referencia", según su tipo de dato.
    
    // asignacion de variables por valor (para tipos primiticos - string - number -boolean - null - undefined - symbol)
    const a = 10;

    // es una copia de a
    let b:number = a;
    b = 20;
    console.log(a); 
    console.log(b); 

    // assignacion de varibles por referencia (para tipos object, array, functions)
    const obj1 = { name: "Marcos" };

    // obj2 apunta al mismo objeto que obj1
    let obj2 = obj1; 
    obj2.name = "Fabricio";
    console.log(obj1.name);
    console.log(obj2.name);


    //  - Muestra ejemplos de funciones con variables que se les pasan "por valor" y "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
    // se pasa una copia del valor
    function incrementaPorValor(valor: number): void {
        valor += valor;
        console.log(`Dentro de la función: ${valor}`); 
    }
    
    let numero = 10;
    incrementaPorValor(numero);
    console.log(`Fuera de la función: ${numero}`);

    // se pasa una referencia al objeto en memoria
    function incrementaPorReferencia(obj: { valor: number }): void {
        obj.valor++;
        console.log(`Dentro de la función: ${obj.valor}`);
    }
    
    let obj3 = { valor: 10 };
    incrementaPorReferencia(obj3);
    console.log(`Fuera de la función: ${obj3.valor}`);

    //  (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)


    //  DIFICULTAD EXTRA (opcional):
    //  Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
    //  - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
    
    // Programa que recibe dos parámetros por valor
    function program1(param1:number, param2:number):[number, number] {
        let temp:number = param1
        param1 = param2
        param2 = temp
        return [param1, param2]
    }

    
    // Programa que recibe dos parámetros por referencia 
    function program2(param1: string[], param2: string[]): void { 
        for (let i = 0; i < param1.length; i++) { 
            let temp = param1[i] 
            param1[i] = param2[i]
            param2[i] = temp
        } 
    }

    //  Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
    //  Comprueba también que se ha conservado el valor original en las primeras.

    const var1 = 5
    const var2 = 10
    const [num1, num2] = program1(var1, var2)
    console.log(`Valores iniciales var1: ${var1}`)
    console.log(`Valores iniciales var2: ${var2}`)
    console.log(`Valores finales var2: ${num1}`)
    console.log(`Valores finales var2: ${num2}`)

    const var3 = ["Typescript", "Python", "Go"]
    const var4 = ["Java", "PHP", "C++"]
    console.log(`Valores iniciales var3: ${var3}`)
    console.log(`Valores iniciales var4: ${var4}`)

    program2(var3, var4)
    console.log(`Valores iniciales var4: ${var3}`)
    console.log(`Valores iniciales var4: ${var4}`)
    
})()