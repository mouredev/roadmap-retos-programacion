enum DiasDeLaSemana {
    Lunes = 1,
    Martes,
    Miercoles,
    Jueves,
    Viernes,
    Sabado,
    Domingo
}

function obtenerNombreDelDia(dia: number): string {
    switch (dia) {
        case DiasDeLaSemana.Lunes:
            return "Lunes";
        case DiasDeLaSemana.Martes:
            return "Martes";
        case DiasDeLaSemana.Miercoles:
            return "Miércoles";
        case DiasDeLaSemana.Jueves:
            return "Jueves";
        case DiasDeLaSemana.Viernes:
            return "Viernes";
        case DiasDeLaSemana.Sabado:
            return "Sábado";
        case DiasDeLaSemana.Domingo:
            return "Domingo";
        default:
            return "Número de día inválido";
    }
}

// Prueba de la función
console.log(obtenerNombreDelDia(1)); // "Lunes"
console.log(obtenerNombreDelDia(5)); // "Viernes"
console.log(obtenerNombreDelDia(7)); // "Domingo"
console.log(obtenerNombreDelDia(8)); // "Número de día inválido"
