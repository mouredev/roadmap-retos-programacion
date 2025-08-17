
let contador1 = 0;
let contador2 = 0;
let contador3 = 0;

function text(text1, text2) {
    for (let i = 0; i <= 100; i++) {
        switch (true) {
            case i % 3 === 0 && i % 5 === 0:
                contador3 +=1;
                console.log(text1 + " " + text2);
                break;
            case i % 3 === 0:
                contador2 +=1;
                console.log(text1);
                break;
            case i % 5 === 0:
                contador1 +=1;
                console.log(text2);
                break;
            default:
                console.log(i);
                break;
        }
    }
}

text("Hola", "Mundo");
console.log(`El numero de veces que se imprimio Hola es: ${contador1}`);
console.log(`El numero de veces que se imprimio Mundo es: ${contador2}`);
console.log(`El numero de veces que se imprimio Hola Mundo es: ${contador3}`);
