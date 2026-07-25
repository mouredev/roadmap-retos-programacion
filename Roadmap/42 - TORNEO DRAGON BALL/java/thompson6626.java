
import java.util.*;

public class thompson6626 {

    public static void main(String[] args) {
        List<Luchador> luchadores = randomLuchadores();
        Torneo torneo = new Torneo(luchadores);
        torneo.iniciar();
    }
    public static List<Luchador> randomLuchadores() {
        List<String> dragonBallFighters = Arrays.asList(
                "Goku", "Vegeta", "Piccolo", "Gohan", "Freezer", "Cell",
                "Majin Boo", "Trunks", "Krilin", "Ten Shin Han", "Yamcha",
                "Broly", "Bills", "Whis", "Jiren", "Hit",
                "Zamas", "Androide 18", "Androide 17", "Gotenks", "Raditz",
                "Nappa", "Bardock", "Kid Boo", "Kaiosama", "Maestro Roshi",
                "Dende", "Videl", "Pan", "Mr. Satán", "Chichi", "Bulma",
                "Zarbon", "Dodoria", "Ginyu", "Recoome", "Burter", "Jeice", "Guldo",
                "Shenlong", "Tapion", "Puar", "Oolong"
        );

        var random = new Random();
        int numeroDeLuchadores;
        do {
            numeroDeLuchadores = random.nextInt(dragonBallFighters.size() + 1);
        }while (numeroDeLuchadores < 2 || !Utils.esPotenciadeDos(numeroDeLuchadores));

        Set<String> nombresTomados = new HashSet<>();
        List<Luchador> luchadores = new ArrayList<>();
        for (int i = 0; i < numeroDeLuchadores; i++) {
            int nombreIndex;
            do {
                nombreIndex = random.nextInt(numeroDeLuchadores);
            }while (nombresTomados.contains(dragonBallFighters.get(nombreIndex)));
            nombresTomados.add(dragonBallFighters.get(nombreIndex));
            luchadores.add(new Luchador(
                    dragonBallFighters.get(nombreIndex),
                    random.nextInt(101),
                    random.nextInt(101),
                    random.nextInt(101)
            ));
        }
        return luchadores;
    }



    static class Luchador{

        private static final int VIDA_MAXIMA = 100;
        private static final int CHANCE_DE_EVASION = 20;
        private final Random random = new Random();
        private final String nombre;
        private final int velocidad;
        private final int ataque;
        private final int defensa;
        private int vida;
        public Luchador(String nombre,int velocidad, int ataque, int defensa) {
            this.nombre = nombre;
            this.velocidad = velocidad;
            this.ataque = ataque;
            this.defensa = defensa;
            this.vida = VIDA_MAXIMA;
        }
        public void descansar(){
            this.vida = VIDA_MAXIMA;
        }
        public boolean atacar(Luchador contrincante){
            int vidaRestanteDelContrincaten = contrincante.recibirDaño(this);
            boolean fatal = vidaRestanteDelContrincaten <= 0;
            return fatal;
        }
        public int recibirDaño(Luchador atacante){
            if (esquivar()){
                System.out.printf(
                        "%s esquivo el ataque de %s %n",
                        this.nombre ,
                        atacante.nombre
                );
                return this.vida;
            }
            int dañoARecibir;
            if (this.defensa > atacante.ataque){
                dañoARecibir = Utils.porcentajeDe(10 , atacante.ataque);// Si la defensa es mayor al ataque
                System.out.printf(
                        "%s tuvo una defensa mayor al ataque de %s y el daño se reduce a 10%% del total! (%d -> %d) %n",
                        this.nombre,
                        atacante.nombre,
                        atacante.ataque,
                        dañoARecibir
                );
            }else{
                dañoARecibir = Math.max(0 , atacante.ataque - this.defensa);
            }

            int vidaAntesDeAtaque = this.vida;
            this.vida -= dañoARecibir;
            System.out.printf("%s recibe un daño total de %d (%d -> %d)%n",
                    this.nombre,
                    dañoARecibir,
                    vidaAntesDeAtaque,
                    this.vida
            );
            return this.vida;
        }
        public boolean esquivar() {
            int chance = random.nextInt(100);
            return chance < CHANCE_DE_EVASION;
        }
        public int getVelocidad() {
            return velocidad;
        }
        public int getVida() {
            return vida;
        }

        public String getNombre() {
            return nombre;
        }
    }

    static class Batalla{
        private final Luchador rapido;
        private final Luchador lento;
        public Batalla(Luchador luchador1, Luchador luchador2) {
            if (luchador1.getVelocidad() > luchador2.getVelocidad()){
                this.rapido = luchador1;
                this.lento = luchador2;
            }else {
                this.rapido = luchador2;
                this.lento = luchador1;
            }
        }
        // True gano el rapido false gano el lento
        public Map<Resultado,Luchador> iniciar(){
            System.out.printf("--- %S VS %S --- %n",
                    rapido.getNombre(),
                    lento.getNombre()
            );
            boolean rapidoGano = false;
            do{
                if (rapido.atacar(lento)){
                    rapidoGano = true;
                    break;
                }
                lento.atacar(rapido);
            }while (rapido.getVida() > 0 && lento.getVida() > 0);

            Luchador ganador;
            Luchador perdedor;
            if (rapidoGano){
                ganador = rapido;
                perdedor = lento;
            }else{
                ganador = lento;
                perdedor = rapido;
            }
            // Recuperar vida
            System.out.printf(
                    "%S gana con %d de vida restante! %n",
                    ganador.getNombre(),
                    ganador.getVida()
            );
            ganador.descansar();
            return Map.of(Resultado.GANADOR, ganador,Resultado.PERDEDOR,perdedor);
        }


    }
    static class Torneo{
        List<Luchador> luchadores;
        private final Random RANDOM = new Random();
        private int ronda = 1;
        public Torneo(List<Luchador> luchadores) {
            if (luchadores.size() % 2 != 0) throw new IllegalArgumentException("Numero de luchadores invalido.");
            this.luchadores = luchadores;
        }
        public Torneo(Luchador... luchadores){
            if (luchadores.length % 2 != 0) throw new IllegalArgumentException("Numero de luchadores invalido.");
            this.luchadores = Arrays.asList(luchadores);
        }

        public void siguienteEtapa(){
            int luchadoresRestantes = luchadores.size();
            Etapa etapa = Etapa.etapaPorLuchadores(luchadoresRestantes);

            if (etapa != null) System.out.printf("-- %s -- %n", etapa.getNombre());
            else System.out.printf("-- Ronda %d -- %n",ronda);

            Set<Integer> yaJugaron = new HashSet<>();
            List<Luchador> pasaron = new ArrayList<>();
            while (yaJugaron.size() < luchadoresRestantes){
                int participante1;
                do {
                    participante1 = RANDOM.nextInt(luchadoresRestantes);
                }while (yaJugaron.contains(participante1));
                int participante2;
                do {
                    participante2 = RANDOM.nextInt(luchadoresRestantes);
                }while (yaJugaron.contains(participante2) || participante2 == participante1);

                var batalla = new Batalla(
                        luchadores.get(participante1),
                        luchadores.get(participante2)
                );

                Map<Resultado,Luchador> resultado = batalla.iniciar();
                System.out.printf(
                        "%S ha sido eliminado! %n",
                        resultado.get(Resultado.PERDEDOR).getNombre()
                );
                pasaron.add(resultado.get(Resultado.GANADOR));
                yaJugaron.add(participante1);
                yaJugaron.add(participante2);
                luchadores.forEach(e -> System.out.println(e.getNombre()));
                System.out.println(participante1 +" "+participante2);
                System.out.println(yaJugaron);
                System.out.println(luchadoresRestantes);
            }
            System.out.println(".....");
            luchadores = pasaron;
            ronda++;
        }
        public void iniciar(){
            while (luchadores.size() > 1) {
                siguienteEtapa();
            }
            Luchador ganador = luchadores.removeLast();
            String mensaje = String.format("%S es el ganador del torneo!!!", ganador.getNombre());

            int ancho = mensaje.length() + 6;
            String borde = "*".repeat(ancho);

            System.out.println(borde);
            System.out.printf("* %-" + (ancho - 4) + "s *%n", " ");
            System.out.printf("* %-" + (ancho - 4) + "s *%n", mensaje);
            System.out.printf("* %-" + (ancho - 4) + "s *%n", " ");
            System.out.println(borde);
        }

        enum Etapa {
            GRAN_FINAL("Gran Final",2),
            SEMIFINALES("Semifinales",4),
            CUARTOS_DE_FINAL("Cuartos de Final",8),
            OCTAVOS_DE_FINAL("Octavos de Final",16);
            private final String nombre;
            private final int jugadores;
            public static final Etapa[] ETAPAS = values();
            Etapa(String nombre, int luchadores) {
                this.nombre = nombre;
                this.jugadores = luchadores;
            }
            public String getNombre() {
                return nombre;
            }
            public static Etapa etapaPorLuchadores(int luchadores){
                for(Etapa etapa : ETAPAS){
                    if (etapa.jugadores == luchadores){
                        return etapa;
                    }
                }
                return null;
            }
        }

    }
    enum Resultado{
        GANADOR,
        PERDEDOR
    }
    public static class Utils{
        public static int porcentajeDe(int porcentaje,int valor){
            return Math.round(((float) porcentaje / 100) * valor);
        }
        public static boolean esPotenciadeDos(int n) {
            if (n == 0)
                return false;

            while (n != 1) {
                if (n % 2 != 0)
                    return false;
                n = n / 2;
            }
            return true;
        }
    }

}