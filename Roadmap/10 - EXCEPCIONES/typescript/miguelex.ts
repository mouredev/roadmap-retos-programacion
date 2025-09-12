
function division(a: number, b: number): string {
    try {
        if (b === 0) {
            throw new Error("No se puede dividir por cero");
        }
        return (a / b).toString();
    } catch (error) {
        return error.message;
    }
}

console.log(division(10, 0));
console.log(division(5, 3));

function outOfRange(lista: any[], indice: number): string {
    try {
        if (indice < 0 || indice >= lista.length) {
            throw new Error("Índice fuera de rango");
        }
        return lista[indice];
    } catch (error) {
        return error.message;
    }
}

console.log(outOfRange([1, 2, 3], 5));

class MiError extends Error {
    valor: any;

    constructor(valor: any) {
        super();
        this.valor = valor;
    }

    toString(): string {
        return "Error: " + this.valor;
    }
}

function extra(a: string, b: number, c: string): string {
    if (typeof a !== "string" || a.length === 0) {
        throw new Error("El primer parametro debe ser un string y no vacio");
    }
    if (typeof b !== "number" || b <= 0) {
        throw new Error("El segundo parametro debe ser un entero y mayor que 0");
    }
    if (typeof c !== "string") {
        throw new Error("El tercer parametro debe ser un string");
    }
    if (c === "Mouredev") {
        throw new MiError("El tercer parametro no puede ser Mouredev");
    }
    return `Solucion reto ${b} - ${a} del usuario ${c}`;
}

try {
    //console.log(extra("Swift", 10, "Mouredev"));
    console.log(extra("TypeScript", 10, "Miguelex"));
    //console.log(extra("PHP", -5, "Miguelex"));
    //console.log(extra("", 10, "Miguelex"));
} catch (error) {
    console.log(error instanceof MiError ? error.toString() : error.message);
} finally {
    console.log("Todo ha ido bien");
}
