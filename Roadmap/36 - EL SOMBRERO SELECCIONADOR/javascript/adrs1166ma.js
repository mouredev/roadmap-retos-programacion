/*
EJERCICIO:
Cada 1 de septiembre, el Hogwarts Express parte hacia la escuela
de programación de Hogwarts para magos y brujas del código.
En ella, su famoso sombrero seleccionador ayuda a los programadores
a encontrar su camino...
Desarrolla un programa que simule el comportamiento del sombrero.
Requisitos:
1. El sombrero realizará 10 preguntas para determinar la casa del alumno.
2. Deben existir 4 casas. Por ejemplo: Frontend, Backend, Mobile y Data.
   (Puedes elegir las que quieras)
Acciones:
1. Crea un programa que solicite el nombre del alumno y realice 10
   preguntas, con cuatro posibles respuestas cada una.
2. Cada respuesta asigna puntos a cada una de las casas (a tu elección).
3. Una vez finalizado, el sombrero indica el nombre del alumno 
   y a qué casa pertenecerá (resuelve el posible empate de manera aleatoria,
   pero indicándole al alumno que la decisión ha sido complicada).
 */
//  🔥 SIMULADOR: Sombrero Seleccionador de Hogwarts para Programadores 🔥

console.log("🎩 ¡Bienvenido al Sombrero Seleccionador de Hogwarts para Programadores! 🎩");

// Función principal del programa
function iniciarSombreroSeleccionador() {
    console.log("\n--- INICIO DEL SELECCIONAMIENTO ---");
    const nombre = prompt("Ingrese el nombre del alumno: ");
    if (!nombre) {
        console.log("❌ El nombre del alumno es obligatorio.");
        return;
    }

    // Preguntas y asignación de puntos
    const preguntas = [
        "1. ¿Qué prefieres hacer en tu tiempo libre?\n   a) Crear interfaces bonitas\n   b) Optimizar bases de datos\n   c) Desarrollar apps móviles\n   d) Analizar grandes volúmenes de datos",
        "2. ¿Qué herramienta usas más a menudo?\n   a) HTML/CSS\n   b) SQL\n   c) Flutter\n   d) Python",
        "3. ¿Qué tipo de proyecto te emociona más?\n   a) Un sitio web interactivo\n   b) Una API RESTful\n   c) Una app móvil\n   d) Un modelo de machine learning",
        "4. ¿Qué prefieres aprender?\n   a) Animaciones CSS\n   b) Arquitectura de microservicios\n   c) Kotlin\n   d) TensorFlow",
        "5. ¿Qué lenguaje prefieres?\n   a) JavaScript\n   b) Java\n   c) Swift\n   d) R",
        "6. ¿Qué problema disfrutas resolviendo?\n   a) Diseño visual\n   b) Escalabilidad\n   c) Interfaz móvil nativa\n   d) Predicción de datos",
        "7. ¿Qué te motiva más?\n   a) Hacer que las cosas se vean bien\n   b) Hacer que las cosas funcionen bien\n   c) Hacer que las cosas estén disponibles en todas partes\n   d) Hacer que las cosas sean inteligentes",
        "8. ¿Qué prefieres depurar?\n   a) Estilos visuales\n   b) Lógica del servidor\n   c) Compatibilidad de dispositivos\n   d) Errores en pipelines de datos",
        "9. ¿Qué prefieres diseñar?\n   a) Layouts responsivos\n   b) Esquemas de bases de datos\n   c) Interfaces móviles\n   d) Diagramas de flujo de datos",
        "10. ¿Qué prefieres optimizar?\n    a) Velocidad de carga\n    b) Consultas SQL\n    c) Uso de memoria en dispositivos móviles\n    d) Precisión de modelos"
    ];

    const casas = { Frontend: 0, Backend: 0, Mobile: 0, Data: 0 };

    // Realizar las preguntas
    for (const pregunta of preguntas) {
        console.log(pregunta);
        const respuesta = prompt("Seleccione una opción (a/b/c/d): ").toLowerCase();

        switch (respuesta) {
            case "a":
                casas.Frontend += 1;
                break;
            case "b":
                casas.Backend += 1;
                break;
            case "c":
                casas.Mobile += 1;
                break;
            case "d":
                casas.Data += 1;
                break;
            default:
                console.log("⚠️ Respuesta no válida. No se asignaron puntos.");
        }
    }

    // Determinar la casa ganadora
    const puntuaciones = Object.entries(casas);
    const maxPuntos = Math.max(...puntuaciones.map(([_, puntos]) => puntos));
    const casasGanadoras = puntuaciones.filter(([_, puntos]) => puntos === maxPuntos).map(([casa]) => casa);

    let casaFinal;
    if (casasGanadoras.length > 1) {
        console.log(`\n🤔 Decisión complicada... ${nombre}, has obtenido un empate entre: ${casasGanadoras.join(", ")}.`);
        casaFinal = casasGanadoras[Math.floor(Math.random() * casasGanadoras.length)];
        console.log(`🎩 Después de mucho pensar, el sombrero ha decidido: ¡${casaFinal} será tu casa!`);
    } else {
        casaFinal = casasGanadoras[0];
        console.log(`\n🎉 ¡Felicidades, ${nombre}! El sombrero ha decidido que perteneces a la casa de ${casaFinal}.`);
    }

    // Mostrar puntuaciones finales
    console.log("\n--- PUNTUACIONES FINALES ---");
    for (const [casa, puntos] of puntuaciones) {
        console.log(`${casa}: ${puntos} puntos`);
    }
}

iniciarSombreroSeleccionador();