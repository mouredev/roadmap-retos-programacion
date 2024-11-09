import * as readline from 'readline';

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

class Casa {
    private nombre: string;
    private puntos: number;

    constructor(nombre: string) {
        this.nombre = nombre;
        this.puntos = 0;
    }

    public getNombre(): string {
        return this.nombre;
    }

    public agregarPuntos(puntos: number): void {
        this.puntos += puntos;
    }

    public getPuntos(): number {
        return this.puntos;
    }
}

class Alumno {
    private nombre: string;

    constructor(nombre: string) {
        this.nombre = nombre;
    }

    public getNombre(): string {
        return this.nombre;
    }
}

interface Opcion {
    texto: string;
    casa: string;
}

class Pregunta {
    private pregunta: string;
    private opciones: Opcion[];

    constructor(pregunta: string, opciones: Opcion[]) {
        this.pregunta = pregunta;
        this.opciones = opciones;
    }

    public mostrarPregunta(): void {
        console.log(this.pregunta);
        this.opciones.forEach((opcion, index) => {
            console.log(`${index + 1}: ${opcion.texto}`);
        });
    }

    public obtenerCasaSegunRespuesta(respuesta: number): string {
        return this.opciones[respuesta - 1].casa;
    }
}

class SombreroSeleccionador {
    private casas: Record<string, Casa>;
    private preguntas: Pregunta[];

    constructor(casas: Record<string, Casa>, preguntas: Pregunta[]) {
        this.casas = casas;
        this.preguntas = preguntas;
    }

    public async asignarCasa(alumno: Alumno): Promise<void> {
        const preguntasSeleccionadas = this.seleccionarPreguntas();
        for (const pregunta of preguntasSeleccionadas) {
            pregunta.mostrarPregunta();
            const respuesta = await this.leerRespuesta();
            const casa = pregunta.obtenerCasaSegunRespuesta(respuesta);
            this.casas[casa].agregarPuntos(1);
        }

        this.mostrarResultado(alumno);
        rl.close();
    }

    private seleccionarPreguntas(): Pregunta[] {
        const preguntasSeleccionadas: Pregunta[] = [];
        const indicesSeleccionados = new Set<number>();

        while (preguntasSeleccionadas.length < 10) {
            const indice = Math.floor(Math.random() * this.preguntas.length);
            if (!indicesSeleccionados.has(indice)) {
                indicesSeleccionados.add(indice);
                preguntasSeleccionadas.push(this.preguntas[indice]);
            }
        }

        return preguntasSeleccionadas;
    }

    private leerRespuesta(): Promise<number> {
        return new Promise((resolve) => {
            rl.question("Selecciona una opción (1-4): ", (respuesta) => {
                resolve(parseInt(respuesta));
            });
        });
    }

    private mostrarResultado(alumno: Alumno): void {
        const casasOrdenadas = Object.values(this.casas).sort((a, b) => b.getPuntos() - a.getPuntos());

        const maxPuntos = casasOrdenadas[0].getPuntos();
        const ganadoras = casasOrdenadas.filter(casa => casa.getPuntos() === maxPuntos);

        let ganadora: Casa;
        if (ganadoras.length > 1) {
            console.log("\n\nLa decisión fue difícil...");
            ganadora = ganadoras[Math.floor(Math.random() * ganadoras.length)];
        } else {
            ganadora = ganadoras[0];
        }

        console.log(`\n\n ${alumno.getNombre()}, el sombrero seleccionador te ha asignado a la casa ${ganadora.getNombre().toUpperCase()}!!!!\n`);
    }
}

const casas: Record<string, Casa> = {
    'frontend': new Casa('Frontend'),
    'backend': new Casa('Backend'),
    'mobile': new Casa('Mobile'),
    'data': new Casa('Data')
};

const preguntas = [
    new Pregunta("¿Qué prefieres?", [
        { texto: 'Diseñar interfaces', casa: 'frontend' },
        { texto: 'Crear APIs', casa: 'backend' },
        { texto: 'Desarrollar apps móviles', casa: 'mobile' },
        { texto: 'Analizar datos', casa: 'data' }
    ]),
    new Pregunta("¿Cuál es tu lenguaje de programación favorito?", [
        { texto: 'JavaScript', casa: 'frontend' },
        { texto: 'Python', casa: 'backend' },
        { texto: 'Kotlin', casa: 'mobile' },
        { texto: 'R', casa: 'data' }
    ]),
    new Pregunta("¿Qué herramienta utilizas más a menudo?", [
        { texto: 'Figma o Sketch', casa: 'frontend' },
        { texto: 'Docker o Kubernetes', casa: 'backend' },
        { texto: 'Android Studio o Xcode', casa: 'mobile' },
        { texto: 'Jupyter Notebooks o Excel', casa: 'data' }
    ]),
    new Pregunta("¿Qué te interesa más aprender?", [
        { texto: 'HTML/CSS y JavaScript avanzado', casa: 'frontend' },
        { texto: 'Patrones de diseño y arquitectura de software', casa: 'backend' },
        { texto: 'Programación nativa para dispositivos móviles', casa: 'mobile' },
        { texto: 'Estadística y Machine Learning', casa: 'data' }
    ]),
    new Pregunta("¿Qué tipo de proyecto te gustaría liderar?", [
        { texto: 'Un sitio web interactivo y atractivo', casa: 'frontend' },
        { texto: 'Una plataforma escalable con microservicios', casa: 'backend' },
        { texto: 'Una app móvil innovadora', casa: 'mobile' },
        { texto: 'Un sistema de recomendación basado en datos', casa: 'data' }
    ]),
    new Pregunta("¿Qué es lo más importante para ti en un proyecto?", [
        { texto: 'La experiencia de usuario', casa: 'frontend' },
        { texto: 'El rendimiento y la escalabilidad', casa: 'backend' },
        { texto: 'La adaptabilidad a diferentes dispositivos', casa: 'mobile' },
        { texto: 'La precisión de los análisis', casa: 'data' }
    ]),
    new Pregunta("¿Qué prefieres trabajar?", [
        {texto : 'En un entorno donde el diseño visual es clave', casa :'frontend'},
        {texto : 'En la lógica del negocio y la arquitectura', casa :'backend'},
        {texto : 'En apps móviles con buen rendimiento', casa :'mobile'},
        {texto : 'En el análisis y visualización de datos', casa :'data'}
    ]),
    new Pregunta("¿Qué framework te parece más interesante?", [
        {texto: 'React o Angular', casa :'frontend'},
        {texto : 'Spring o Django', casa :'backend'},
        {texto : 'Flutter o React Native', casa :'mobile'},
        {texto : 'TensorFlow o Pandas', casa :'data'}
    ]),
    new Pregunta("¿Qué tipo de reto disfrutas más?", [
        {texto : 'Hacer que un sitio web sea accesible y rápido', casa :'frontend'},
        {texto : 'Optimizar la comunicación entre servicios', casa :'backend'},
        {texto : 'Mejorar la experiencia del usuario en móviles', casa :'mobile'},
        {texto : 'Encontrar patrones ocultos en los datos', casa :'data'}
    ]),
    new Pregunta("¿Qué prefieres resolver?", [
        {texto : 'Problemas de diseño y maquetación', casa :'frontend'},
        {texto : 'Problemas de concurrencia y escalabilidad', casa :'backend'},
        {texto : 'Problemas de rendimiento en aplicaciones móviles', casa :'mobile'},
        {texto : 'Problemas de predicción y análisis de datos', casa :'data'}
    ]),
    new Pregunta("¿Qué es lo que más te emociona en tecnología?", [
        {texto : 'La evolución de las interfaces de usuario', casa :'frontend'},
        {texto : 'La innovación en la arquitectura de software', casa :'backend'},
        {texto : 'Las nuevas capacidades de los dispositivos móviles', casa :'mobile'},
        {texto : 'Los avances en inteligencia artificial y análisis de datos', casa : 'data'}
    ]),
    new Pregunta("¿Qué te gusta hacer en tu tiempo libre?", [
        {texto : 'Diseñar sitios web personales o interfaces', casa: 'frontend'},
        {texto : 'Hacer proyectos con servidores y APIs', casa: 'backend'},
        {texto : 'Crear apps móviles para resolver problemas cotidianos', casa: 'mobile'},
        {texto : 'Hacer análisis de datos para tomar decisiones mejor informadas', casa: 'data'}
    ]),
    new Pregunta("¿Qué te gustaría dominar?", [
        {texto : 'Animaciones y transiciones en la web', casa: 'frontend'},
        {texto : 'Arquitectura de microservicios', casa: 'backend'},
        {texto : 'Optimización de aplicaciones móviles', casa: 'mobile'},
        {texto : 'Modelos predictivos y análisis de datos', casa: 'data'}
    ]),
    new Pregunta("¿Qué tipo de problema prefieres resolver en un hackathon?", [
        {texto : 'Mejorar la interfaz de usuario de una aplicación', casa: 'frontend'},
        {texto : 'Optimizar el rendimiento de una API', casa: 'backend'},
        {texto : 'Crear una aplicación móvil desde cero', casa: 'mobile'},
        {texto : 'Generar insights a partir de grandes conjuntos de datos', casa: 'data'}
    ]),
    new Pregunta("¿Qué prefieres al trabajar en equipo?", [
        {texto : 'Encargarte de la parte visual y de interacción del usuario', casa: 'frontend'},
        {texto : 'Asegurarte de que la lógica y los datos fluyan correctamente', casa: 'backend'},
        {texto : 'Hacer que la app funcione bien en diferentes dispositivos', casa: 'mobile'},
        {texto : 'Proveer métricas y análisis para tomar mejores decisiones', casa: 'data'}
    ]),
    new Pregunta("¿Cuál es tu prioridad al optimizar código?", [
        {texto : 'Que la interfaz cargue rápido y sea amigable', casa: 'frontend'},
        {texto : 'Que los servicios backend sean escalables y eficientes', casa: 'backend'},
        {texto : 'Que la app móvil consuma pocos recursos y sea fluida', casa: 'mobile'},
        {texto : 'Que el procesamiento de datos sea rápido y preciso', casa: 'data'}
    ]),
    new Pregunta("¿Qué prefieres al probar una aplicación?", [
        {texto : 'Verificar que el diseño y la usabilidad sean impecables', casa: 'frontend'},
        {texto : 'Asegurar que las funcionalidades y la lógica sean correctas', casa :'backend'},
        {texto : 'Revisar que la app funcione correctamente en múltiples dispositivos', casa : 'mobile'},
        {texto : 'Validar que los resultados de los análisis sean exactos', casa : 'data'}
    ]),
    new Pregunta("¿Qué tipo de proyectos sigues en la industria?", [
        {texto : 'Proyectos de diseño web innovador y UX', casa : 'frontend'},
        {texto : 'Nuevas tecnologías de servidores y backends', casa : 'backend'},
        {texto : 'Aplicaciones móviles disruptivas y eficientes', casa : 'mobile'},
        {texto : 'Proyectos de inteligencia artificial y ciencia de datos', casa : 'data'}
    ]),
    new Pregunta("¿Qué harías para mejorar una plataforma existente?", [
        {texto : 'Mejorar la apariencia y usabilidad de la interfaz', casa : 'frontend'},
        {texto : 'Optimizar el rendimiento de las consultas y los servidores', casa : 'backend'},
        {texto : 'Hacer que la plataforma sea accesible desde dispositivos móviles', casa : 'mobile'},
        {texto : 'Incluir más análisis de datos para obtener mejor información', casa : 'data'}
    ]),
    new Pregunta("¿Qué aspecto del desarrollo de software te parece más retador?", [
        {texto : 'Hacer que una aplicación web sea visualmente atractiva', casa : 'frontend'},
        {texto : 'Crear sistemas backend que manejen millones de usuarios', casa : 'backend'},
        {texto : 'Optimizar la app móvil para diferentes sistemas operativos', casa : 'mobile'},
        {texto : 'Gestionar grandes volúmenes de datos y extraer conclusiones útiles', casa : 'data'}
    ]),
];


rl.question("Por favor, introduce tu nombre: ", (nombreAlumno) => {
    const alumno = new Alumno(nombreAlumno);
    const sombrero = new SombreroSeleccionador(casas, preguntas);
    sombrero.asignarCasa(alumno);
});
