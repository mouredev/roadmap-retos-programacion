// Ejercicio 1º

    // Interación por Bucle For
        for(let i : number = 1; i <= 10; i++){
            console.log(`Número ${i}`);
        }
    // Iteración por While
        let iWhile = 1
        while(iWhile <= 10){
            console.log(`Número ${iWhile}`);
            iWhile++;
        }
    // Iteración con doWhile
        let iDoWhile = 1
        do{
            console.log(`Número ${iDoWhile}`);
            iDoWhile++;
        }while(iDoWhile<= 10)

//Ejercicio Extra
    let numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
    // Iteración con For of
        for (let num of numeros) {
            console.log(num);
        }
    // Iteración con For each
        numeros.forEach(num => console.log(num));
    // Iteración con Map
        numeros.map(num => console.log(num));
    // Iteración con entries
        let numerosEntries = [...Array(10).keys()].map(x => x + 1);
        for (let [value] of numerosEntries.entries()) {
            console.log(value);
        }
    // Iteración con Recursión
        function printarNumeros(start: number, end: number) {
            if (start <= end) {
                console.log(start);
                printarNumeros(start + 1, end);
            }
        }
        printarNumeros(1, 10);
