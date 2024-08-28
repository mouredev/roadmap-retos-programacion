function esPrimo(num: number): boolean {
    if (num <= 1) return false;
    if (num === 2) return true;
    if (num % 2 === 0) return false;
    
    for (let i = 3; i <= Math.sqrt(num); i += 2) {
        if (num % i === 0) return false;
    }
    return true;
}

function repartirAnillos(totalAnillos: number): string {
    if (totalAnillos < 4) {
        return "Error: No hay suficientes anillos para cumplir con los requisitos.";
    }

    const anillosSauron = 1;
    totalAnillos -= 1;
    
    let mejorDiferencia = Number.MAX_SAFE_INTEGER;
    let mejorReparto: { Elfos: number, Enanos: number, Hombres: number, Sauron: number } | null = null;
    
    for (let anillosElfos = 1; anillosElfos <= totalAnillos; anillosElfos += 2) {
        for (let anillosEnanos = 2; anillosEnanos <= totalAnillos; anillosEnanos++) {
            if (esPrimo(anillosEnanos)) {
                const anillosHombres = totalAnillos - anillosElfos - anillosEnanos;
                
                if (anillosHombres > 0 && anillosHombres % 2 === 0) {
                    const diferencia = Math.max(anillosElfos, anillosEnanos, anillosHombres) - Math.min(anillosElfos, anillosEnanos, anillosHombres);
                    
                    if (diferencia < mejorDiferencia) {
                        mejorDiferencia = diferencia;
                        mejorReparto = {
                            Elfos: anillosElfos,
                            Enanos: anillosEnanos,
                            Hombres: anillosHombres,
                            Sauron: anillosSauron
                        };
                    }
                }
            }
        }
    }
    
    if (mejorReparto) {
        return `Reparto exitoso: Elfos = ${mejorReparto.Elfos}, Enanos = ${mejorReparto.Enanos}, Hombres = ${mejorReparto.Hombres}, Sauron = ${mejorReparto.Sauron}`;
    } else {
        return "Error: No se encontró una combinación válida para repartir los anillos.";
    }
}

const totalAnillos: number = parseInt(prompt("Ingresa el número total de anillos: ") || "0", 10);
const resultado: string = repartirAnillos(totalAnillos);
console.log(resultado);
