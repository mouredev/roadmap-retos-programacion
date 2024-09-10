import java.util.*;

class Casa {
    private String nombre;
    private int puntos;

    public Casa(String nombre) {
        this.nombre = nombre;
        this.puntos = 0;
    }

    public String getNombre() {
        return nombre;
    }

    public void agregarPuntos(int puntos) {
        this.puntos += puntos;
    }

    public int getPuntos() {
        return puntos;
    }
}

class Alumno {
    private String nombre;

    public Alumno(String nombre) {
        this.nombre = nombre;
    }

    public String getNombre() {
        return nombre;
    }
}

class Pregunta {
    private String pregunta;
    private List<Opcion> opciones;

    public Pregunta(String pregunta, List<Opcion> opciones) {
        this.pregunta = pregunta;
        this.opciones = opciones;
    }

    public void mostrarPregunta() {
        System.out.println(pregunta);
        for (int i = 0; i < opciones.size(); i++) {
            System.out.println((i + 1) + ": " + opciones.get(i).getTexto());
        }
    }

    public String obtenerCasaSegunRespuesta(int respuesta) {
        return opciones.get(respuesta - 1).getCasa();
    }
}

class Opcion {
    private String texto;
    private String casa;

    public Opcion(String texto, String casa) {
        this.texto = texto;
        this.casa = casa;
    }

    public String getTexto() {
        return texto;
    }

    public String getCasa() {
        return casa;
    }
}

class SombreroSeleccionador {
    private Map<String, Casa> casas;
    private List<Pregunta> preguntas;

    public SombreroSeleccionador(Map<String, Casa> casas, List<Pregunta> preguntas) {
        this.casas = casas;
        this.preguntas = preguntas;
    }

    public void asignarCasa(Alumno alumno) {
        List<Pregunta> preguntasSeleccionadas = seleccionarPreguntas();
        Scanner scanner = new Scanner(System.in);

        for (Pregunta pregunta : preguntasSeleccionadas) {
            pregunta.mostrarPregunta();
            int respuesta = leerRespuesta(scanner);
            String casa = pregunta.obtenerCasaSegunRespuesta(respuesta);
            casas.get(casa).agregarPuntos(1);
        }

        mostrarResultado(alumno);
        scanner.close();
    }

    private List<Pregunta> seleccionarPreguntas() {
        List<Pregunta> preguntasSeleccionadas = new ArrayList<>();
        Set<Integer> indicesSeleccionados = new HashSet<>();
        Random random = new Random();

        while (preguntasSeleccionadas.size() < 10) {
            int indice = random.nextInt(preguntas.size());
            if (!indicesSeleccionados.contains(indice)) {
                indicesSeleccionados.add(indice);
                preguntasSeleccionadas.add(preguntas.get(indice));
            }
        }

        return preguntasSeleccionadas;
    }

    private int leerRespuesta(Scanner scanner) {
        int respuesta = 0;
        while (respuesta < 1 || respuesta > 4) {
            System.out.print("Selecciona una opción (1-4): ");
            respuesta = scanner.nextInt();
        }
        return respuesta;
    }

    private void mostrarResultado(Alumno alumno) {
        List<Casa> casasOrdenadas = new ArrayList<>(casas.values());
        casasOrdenadas.sort(Comparator.comparingInt(Casa::getPuntos).reversed());

        int maxPuntos = casasOrdenadas.get(0).getPuntos();
        List<Casa> ganadoras = new ArrayList<>();
        for (Casa casa : casasOrdenadas) {
            if (casa.getPuntos() == maxPuntos) {
                ganadoras.add(casa);
            }
        }

        Casa ganadora;
        if (ganadoras.size() > 1) {
            System.out.println("\n\nLa decisión fue difícil...");
            Random random = new Random();
            ganadora = ganadoras.get(random.nextInt(ganadoras.size()));
        } else {
            ganadora = ganadoras.get(0);
        }

        System.out.println("\n\n" + alumno.getNombre() + ", el sombrero seleccionador te ha asignado a la casa " + ganadora.getNombre().toUpperCase() + "!!!!\n");
    }
}

public class miguelex {
    public static void main(String[] args) {
        Map<String, Casa> casas = new HashMap<>();
        casas.put("frontend", new Casa("Frontend"));
        casas.put("backend", new Casa("Backend"));
        casas.put("mobile", new Casa("Mobile"));
        casas.put("data", new Casa("Data"));

        List<Pregunta> preguntas = Arrays.asList(
            new Pregunta("¿Qué prefieres?", Arrays.asList(
                new Opcion("Diseñar interfaces", "frontend"),
                new Opcion("Crear APIs", "backend"),
                new Opcion("Desarrollar apps móviles", "mobile"),
                new Opcion("Analizar datos", "data")
            )),
            new Pregunta("¿Cuál es tu lenguaje de programación favorito?", Arrays.asList(
                new Opcion("JavaScript", "frontend"),
                new Opcion("Python", "backend"),
                new Opcion("Kotlin", "mobile"),
                new Opcion("R", "data")
            )),
            new Pregunta("¿Qué herramienta utilizas más a menudo?", Arrays.asList(
                new Opcion("Figma o Sketch", "frontend"),
                new Opcion("Docker o Kubernetes", "backend"),
                new Opcion("Android Studio o Xcode", "mobile"),
                new Opcion("Jupyter Notebooks o Excel", "data")
            )),
            new Pregunta("¿Qué te interesa más aprender?", Arrays.asList(
                new Opcion("HTML/CSS y JavaScript avanzado", "frontend"),
                new Opcion("Patrones de diseño y arquitectura de software", "backend"),
                new Opcion("Programación nativa para dispositivos móviles", "mobile"),
                new Opcion("Estadística y Machine Learning", "data")
            )),
            new Pregunta("¿Qué tipo de proyecto te gustaría liderar?", Arrays.asList(
                new Opcion("Un sitio web interactivo y atractivo", "frontend"),
                new Opcion("Una plataforma escalable con microservicios", "backend"),
                new Opcion("Una app móvil innovadora", "mobile"),
                new Opcion("Un sistema de recomendación basado en datos", "data")
            )),
            new Pregunta("¿Qué es lo más importante para ti en un proyecto?", Arrays.asList(
                new Opcion("La experiencia de usuario", "frontend"),
                new Opcion("El rendimiento y la escalabilidad", "backend"),
                new Opcion("La adaptabilidad a diferentes dispositivos", "mobile"),
                new Opcion("La precisión de los análisis", "data")
            )),
            new Pregunta("¿Qué prefieres trabajar?", Arrays.asList(
                new Opcion("En un entorno donde el diseño visual es clave", "frontend"),
                new Opcion("En la lógica del negocio y la arquitectura", "backend"),
                new Opcion("En apps móviles con buen rendimiento", "mobile"),
                new Opcion("En el análisis y visualización de datos", "data")
            )),
            new Pregunta("¿Qué framework te parece más interesante?", Arrays.asList(
                new Opcion("React o Angular", "frontend"),
                new Opcion("Spring o Django", "backend"),
                new Opcion("Flutter o React Native", "mobile"),
                new Opcion("TensorFlow o Pandas", "data")
            )),
            new Pregunta("¿Qué tipo de reto disfrutas más?", Arrays.asList(
                new Opcion("Hacer que un sitio web sea accesible y rápido", "frontend"),
                new Opcion("Optimizar la comunicación entre servicios", "backend"),
                new Opcion("Mejorar la experiencia del usuario en móviles", "mobile"),
                new Opcion("Encontrar patrones ocultos en los datos", "data")
            )),
            new Pregunta("¿Qué prefieres resolver?", Arrays.asList(
                new Opcion("Problemas de diseño y maquetación", "frontend"),
                new Opcion("Problemas de concurrencia y escalabilidad", "backend"),
                new Opcion("Problemas de rendimiento en aplicaciones móviles", "mobile"),
                new Opcion("Problemas de predicción y análisis de datos", "data")
            )),
            new Pregunta("¿Qué es lo que más te emociona en tecnología?", Arrays.asList(
                new Opcion("La evolución de las interfaces de usuario", "frontend"),
                new Opcion("La innovación en la arquitectura de software", "backend"),
                new Opcion("Las nuevas capacidades de los dispositivos móviles", "mobile"),
                new Opcion("Los avances en inteligencia artificial y análisis de datos", "data")
            )),
            new Pregunta("¿Qué te gusta hacer en tu tiempo libre?", Arrays.asList(
                new Opcion("Diseñar sitios web personales o interfaces", "frontend"),
                new Opcion("Hacer proyectos con servidores y APIs", "backend"),
                new Opcion("Crear apps móviles para resolver problemas cotidianos", "mobile"),
                new Opcion("Hacer análisis de datos para tomar decisiones mejor informadas", "data")
            )),
            new Pregunta("¿Qué te gustaría dominar?", Arrays.asList(
                new Opcion("Animaciones y transiciones en la web", "frontend"),
                new Opcion("Arquitectura de microservicios", "backend"),
                new Opcion("Optimización de aplicaciones móviles", "mobile"),
                new Opcion("Modelos predictivos y análisis de datos", "data")
            )),
            new Pregunta("¿Qué tipo de problema prefieres resolver en un hackathon?", Arrays.asList(
                new Opcion("Mejorar la interfaz de usuario de una aplicación", "frontend"),
                new Opcion("Optimizar el rendimiento de una API", "backend"),
                new Opcion("Crear una aplicación móvil desde cero", "mobile"),
                new Opcion("Generar insights a partir de grandes conjuntos de datos", "data")
            )),
            new Pregunta("¿Qué prefieres al trabajar en equipo?", Arrays.asList(
                new Opcion("Encargarte de la parte visual y de interacción del usuario", "frontend"),
                new Opcion("Asegurarte de que la lógica y los datos fluyan correctamente", "backend"),
                new Opcion("Hacer que la app funcione bien en diferentes dispositivos", "mobile"),
                new Opcion("Proveer métricas y análisis para tomar mejores decisiones", "data")
            )),
            new Pregunta("¿Cuál es tu prioridad al optimizar código?", Arrays.asList(
                new Opcion("Que la interfaz cargue rápido y sea amigable", "frontend"),
                new Opcion("Que los servicios backend sean escalables y eficientes", "backend"),
                new Opcion("Que la app móvil consuma pocos recursos y sea fluida", "mobile"),
                new Opcion("Que el procesamiento de datos sea rápido y preciso", "data")
            )),
            new Pregunta("¿Qué prefieres al probar una aplicación?", Arrays.asList(
                new Opcion("Verificar que el diseño y la usabilidad sean impecables", "frontend"),
                new Opcion("Asegurar que las funcionalidades y la lógica sean correctas", "backend"),
                new Opcion("Revisar que la app funcione correctamente en múltiples dispositivos", "mobile"),
                new Opcion("Validar que los resultados de los análisis sean exactos", "data")
            )),
            new Pregunta("¿Qué tipo de proyectos sigues en la industria?", Arrays.asList(
                new Opcion("Proyectos de diseño web innovador y UX", "frontend"),
                new Opcion("Nuevas tecnologías de servidores y backends", "backend"),
                new Opcion("Aplicaciones móviles disruptivas y eficientes", "mobile"),
                new Opcion("Proyectos de inteligencia artificial y ciencia de datos", "data")
            )),
            new Pregunta("¿Qué harías para mejorar una plataforma existente?", Arrays.asList(
                new Opcion("Mejorar la apariencia y usabilidad de la interfaz", "frontend"),
                new Opcion("Optimizar el rendimiento de las consultas y los servidores", "backend"),
                new Opcion("Hacer que la plataforma sea accesible desde dispositivos móviles", "mobile"),
                new Opcion("Incluir más análisis de datos para obtener mejor información", "data")
            )),
            new Pregunta("¿Qué aspecto del desarrollo de software te parece más retador?", Arrays.asList(
                new Opcion("Hacer que una aplicación web sea visualmente atractiva", "frontend"),
                new Opcion("Crear sistemas backend que manejen millones de usuarios", "backend"),
                new Opcion("Optimizar la app móvil para diferentes sistemas operativos", "mobile"),
                new Opcion("Gestionar grandes volúmenes de datos y extraer conclusiones útiles", "data")
            ))
        );

        Scanner scanner = new Scanner(System.in);
        System.out.print("Por favor, introduce tu nombre: ");
        String nombreAlumno = scanner.nextLine();
        Alumno alumno = new Alumno(nombreAlumno);

        SombreroSeleccionador sombrero = new SombreroSeleccionador(casas, preguntas);
        sombrero.asignarCasa(alumno);
    }
}
