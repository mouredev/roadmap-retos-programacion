function indice () {
    let myArray = ["a", "b", "c"];
    console.log(myArray[1]);
    try {
        console.log(myArray[3]);
        throw new Error ("El indice no existe")
    } catch (error) {
        console.error(error.message);
    } finally {
        console.log("Fin del programa")
    }

}
indice();

//EXTRA 
//Primero definir el error personalizado
class errorPersonalizado extends Error {
    constructor (message) {
        super (message);
        this.name = "Mi error"
    }
}

//Aquí la función
function numero (num) {
    try {
        if (typeof num !== "number") {
            throw new TypeError ("El dato debe ser un número");
        }
        if (num < 0) {
            throw new RangeError ("El dato debe ser mayor a 0");
        }
        if (num === 0) {
            throw new errorPersonalizado ("El dato no puede ser 0");
        }
        console.log("Dato procesado:", num);
        console.log("No se ha producido ningún error");
    }
    catch(error) {
        console.log("Tipo de error:", error.name, error.message);
    } finally {
        console.log("Programa finalizado")
    }
}
numero(-6);
numero(6);
numero(0);