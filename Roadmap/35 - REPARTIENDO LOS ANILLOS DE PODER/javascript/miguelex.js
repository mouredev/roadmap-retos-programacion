function esPrimo(num) {
    if (num <= 1) return false;
    if (num === 2) return true;
    if (num % 2 === 0) return false;
    
    for (let i = 3; i <= Math.sqrt(num); i += 2) {
        if (num % i === 0) return false;
    }
    return true;
}

function repartirAnillos(totalAnillos) {
    if (totalAnillos < 4) {
        return "Error: No hay suficientes anillos para cumplir con los requisitos.";
    }

    let anillosSauron = 1;
    totalAnillos -= 1;
    
    let mejorDiferencia = Number.MAX_SAFE_INTEGER;
    let mejorReparto = null;
    
    for (let anillosElfos = 1; anillosElfos <= totalAnillos; anillosElfos += 2) {
        for (let anillosEnanos = 2; anillosEnanos <= totalAnillos; anillosEnanos++) {
            if (esPrimo(anillosEnanos)) {
                let anillosHombres = totalAnillos - anillosElfos - anillosEnanos;
                
                if (anillosHombres > 0 && anillosHombres % 2 === 0) {
                    let diferencia = Math.max(anillosElfos, anillosEnanos, anillosHombres) - Math.min(anillosElfos, anillosEnanos, anillosHombres);
                    
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

const totalAnillos = 25;
const resultado = repartirAnillos(totalAnillos);
console.log(resultado);
