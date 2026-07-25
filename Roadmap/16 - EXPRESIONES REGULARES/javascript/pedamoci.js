let txt = 'En la excavación, el equipo encontró una cápsula del tiempo, sellada hacía exactamente 87 años. La tapa, de un metal grisáceo, tenía grabado el número 1938 en una caligrafía pulcra. Dentro, había tres objetos principales. El primero era un diario con 432 páginas, detallando una vida en la ciudad durante la Gran Depresión. La segunda pieza era una moneda de 25 centavos de dólar, y la tercera, la más intrigante, era una partitura musical con solo siete notas repetidas en un patrón rítmico. Se estimó que la temperatura interior se había mantenido constante a 18 grados Celsius. Tras un estudio preliminar, se anunció que casi 9 de cada 10 hallazgos de ese tipo son falsificaciones, pero este era 100% auténtico. El valor histórico de los 3 objetos era incalculable.'

let regexNumeros = /\d+/g
console.log(txt.match(regexNumeros))

// --------------------------------------------------------- DIFICULTAD EXTRA ---------------------------------------------------------

let regexMail = /^[^\W]+@[^\W]+\.[a-zA-Z]{2,63}(\.[a-zA-Z]{2,63})?$/
// ^ ---> iinicia el string
// [^\W]+ ---> tiene que haber mas de un caracter y no puede ser uno especial (. @ % ...)
// @ ---> tiene que tener un arroba
// [^\W]+
// \. ---> tiene que tener un punto
// [a-zA-Z]{2,63} ---> tiene que tener caracteres tipo letras, al menos tienen que ser 2 y como maximo 63
// (\.[a-zA-Z]{2,63})? ---> puede tener un punto y puede tener caracteres tipo letras, al menos tienen que ser 2 y como maximo 63
// $ ---> finaliza el string

let regexNumerosDeTelefonos = /^(\d+)?\s?\d{8}$/
// ^ 
// (\d{1,4})? ---> puede haber uno o hasta cuatro digitos 
// \s? ---> puede haber un espacio 
// \d{8} ---> tiene que tener ocho digitos
// $

let regexUrl = /^https:\/{2}[^\s]{2,}\.[a-zA-Z]{2,63}$/
// ^
// https: ---> tiene que tener 'https:' 
// \/{2} ---> tiene que tener '//' 
// [^\s]{2,} ---> tiene que tener al menos 2 caracteres y no puede tener espacios
// \.
// [a-zA-Z]{2,63}
// $

console.log((regexMail).test('asdasdasd@sada.com'))
console.log((regexNumerosDeTelefonos).test('159753624852'))
console.log((regexUrl).test('https://google.com'))