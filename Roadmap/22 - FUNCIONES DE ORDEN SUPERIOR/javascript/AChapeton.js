var radios = [1, 2, 3];

var calcularArea = function (radio) {
    return Math.PI * (Math.pow(radio, 2));
};

var calcularDiametro = function (radio) {
    return 2 * radio;
};

var calcular = function (radios, funcion) {
    var resultados = [];
    for (var i = 0; i < radios.length; i++) {
        resultados.push(funcion(radios[i]));
    }
    return resultados;
};

console.log('Areas: ', calcular(radios, calcularArea));
console.log('Diametros: ', calcular(radios, calcularDiametro));
