// RETO 1: 
function calcularBatmanDay(anioInicio, anioFinal) {
    console.log("Fechas del Batman Day hasta su 100 aniversario:");
    for (let anio = anioInicio; anio <= anioFinal; anio++) {
        let tercerSabado = new Date(anio, 8, 1); // Septiembre es el mes 8 (0-index)
        tercerSabado.setDate(1 + (6 - tercerSabado.getDay() + 21) % 7); // Ajustar al tercer sábado
        console.log(`Batman Day en el año ${anio}: ${tercerSabado.toLocaleDateString()}`);
    }
}

// RETO 2: 
function activarSistemaSeguridad(sensores) {
    const tamanoMapa = 20;
    const umbralSeguridad = 20;
    let mejorSumaAmenazas = 0;
    let mejorCentro = null;

    for (let i = 0; i <= tamanoMapa - 3; i++) {
        for (let j = 0; j <= tamanoMapa - 3; j++) {
            let sumaAmenazas = 0;
            for (let x = i; x < i + 3; x++) {
                for (let y = j; y < j + 3; y++) {
                    sumaAmenazas += sensores[x][y];
                }
            }
            if (sumaAmenazas > mejorSumaAmenazas) {
                mejorSumaAmenazas = sumaAmenazas;
                mejorCentro = [i + 1, j + 1];
            }
        }
    }
    if (mejorCentro) {
        const distanciaABatcueva = Math.abs(mejorCentro[0]) + Math.abs(mejorCentro[1]);
        console.log(`\nÁrea más amenazada en coordenadas (${mejorCentro[0]}, ${mejorCentro[1]})`);
        console.log(`Suma de amenazas: ${mejorSumaAmenazas}`);
        console.log(`Distancia a la Batcueva: ${distanciaABatcueva}`);
        
        if (mejorSumaAmenazas > umbralSeguridad) {
            console.log("¡Protocolo de seguridad activado!");
        } else {
            console.log("Protocolo de seguridad NO activado.");
        }
    }
}

// Ejecutar el reto 1
const anioInicio = 2024;
const anioFinal = 2024 + (100 - 85);
calcularBatmanDay(anioInicio, anioFinal);

// Ejecutar el reto 2
let sensores = Array.from({ length: 20 }, () => Array.from({ length: 20 }, () => Math.floor(Math.random() * 11)));
activarSistemaSeguridad(sensores);
