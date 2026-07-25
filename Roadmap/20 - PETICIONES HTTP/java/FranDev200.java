import java.io.IOException;
import java.net.HttpURLConnection;
import java.net.URI;
import java.net.URL;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.ArrayList;
import java.util.Scanner;

public class FranDev200 {

    static ArrayList<String> evoluciones = new ArrayList<>();

    // PARA EL APARTADO DE JSON, USO EL .jar DE GSON

    static void main() {

        /*

        EJERCICIO:
        * Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
        * una petición a la web que tú quieras, verifica que dicha petición
        * fue exitosa y muestra por consola el contenido de la web.

         */

        try{

            HttpClient client = HttpClient.newHttpClient();

            HttpRequest request = HttpRequest.newBuilder()
                    .uri(URI.create("https://urbansoundprints.com/products/debi-tirar-mas-fotos"))
                    .GET()
                    .build();

            HttpResponse<String> respuesta =  client.send(request, HttpResponse.BodyHandlers.ofString());

            System.out.println("Codigo de respuesta: " + respuesta.statusCode());
            System.out.println("Respuesta:\n" + respuesta.body());

        }catch (InterruptedException e){
            e.getMessage();
        }catch (IOException e){
            e.getMessage();
        }


        /*

        DIFICULTAD EXTRA (opcional):
         * Utilizando la PokéAPI (https://pokeapi.co), crea un programa por
         * terminal al que le puedas solicitar información de un Pokémon concreto
         * utilizando su nombre o número.
         * - Muestra el nombre, id, peso, altura y tipo(s) del Pokémon
         * - Muestra el nombre de su cadena de evoluciones
         * - Muestra los juegos en los que aparece
         * - Controla posibles errores

         */

        String urlInicio = "https://pokeapi.co/api/v2";


        Scanner scanner = new Scanner(System.in);

        System.out.print("Introduce el nombre o número de la pokedex del pokemon: ");
        String poke = scanner.nextLine();

        try {

            URL url = new URL(urlInicio + "/pokemon/" + poke);

            HttpURLConnection connection = (HttpURLConnection) url.openConnection();

            connection.setRequestMethod("GET");
            connection.connect();

            int responseCode = connection.getResponseCode();

            if(responseCode == 200){

                System.out.println("Conexion exitosa");

                scanner = new Scanner(connection.getInputStream());
                StringBuilder json = new StringBuilder("");
                while (scanner.hasNextLine()) {
                    json.append(scanner.nextLine());
                }

                Gson gson = new Gson();

                JsonObject pokeInfo = gson.fromJson(json.toString(), JsonObject.class);

                String nombre = pokeInfo.get("name").getAsString();
                int nroPokedex = pokeInfo.get("id").getAsInt();
                double peso = pokeInfo.get("weight").getAsDouble();
                double altura = pokeInfo.get("height").getAsDouble();
                JsonArray tiposArray =  pokeInfo.get("types").getAsJsonArray();
                ArrayList<String> tipos = new ArrayList<>();

                for(int i = 0; i < tiposArray.size(); i++){
                    JsonObject t = tiposArray.get(i).getAsJsonObject();
                    JsonObject tipo = t.get("type").getAsJsonObject();
                    String nombreTipo = tipo.get("name").getAsString();
                    String resultado = nombreTipo.substring(0, 1).toUpperCase() +
                            nombreTipo.substring(1).toLowerCase();
                    tipos.add(resultado);
                }

                ArrayList<String> juegos = new ArrayList<>();
                JsonArray juegosArray = pokeInfo.get("game_indices").getAsJsonArray();

                for(int i = 0; i < juegosArray.size(); i++){
                    JsonObject indice = juegosArray.get(i).getAsJsonObject();
                    JsonObject juego = indice.get("version").getAsJsonObject();
                    String nombreJuego = juego.get("name").getAsString();
                    juegos.add(nombreJuego);
                }


                URL urlEspecie = new  URL(urlInicio + "/pokemon-species/" + poke);

                connection = (HttpURLConnection) urlEspecie.openConnection();
                connection.setRequestMethod("GET");
                connection.connect();

                responseCode = connection.getResponseCode();

                if(responseCode == 200){

                    scanner = new Scanner(connection.getInputStream());
                    StringBuilder jsonEspecies = new StringBuilder("");
                    while (scanner.hasNextLine()) {
                        jsonEspecies.append(scanner.nextLine());
                    }

                    Gson gsonEspecies = new Gson();

                    JsonObject especieInfo = gsonEspecies.fromJson(jsonEspecies.toString(), JsonObject.class);

                    String urlEvoluciones = especieInfo.getAsJsonObject("evolution_chain").get("url").getAsString();
                    URL urlEvolucion = new URL(urlEvoluciones);

                    connection = (HttpURLConnection) urlEvolucion.openConnection();
                    connection.setRequestMethod("GET");
                    connection.connect();

                    responseCode = connection.getResponseCode();

                    if(responseCode == 200){

                        scanner = new Scanner(connection.getInputStream());
                        StringBuilder jsonEvolucion = new StringBuilder("");
                        while (scanner.hasNextLine()) {
                            jsonEvolucion.append(scanner.nextLine());
                        }

                        Gson gsonEvolucion = new Gson();

                        JsonObject evoInfo = gsonEvolucion.fromJson(jsonEvolucion.toString(), JsonObject.class);

                        getEvolucion(evoInfo.getAsJsonObject("chain"));

                    }

                }

                Pokemon pokemon = new Pokemon(nroPokedex, nombre, peso, altura, tipos, juegos,  evoluciones);

                pokemon.infoPokemon();

            }else{
                System.out.println("No se ha podido acceder a la url indicada.");
                System.out.println("Posiblemente, el pokemon indicado no exista.");
            }


        }catch (IOException e){
            e.getMessage();
        }





    }

    public static void getEvolucion(JsonObject json){
        String nombreEvolucion = json.getAsJsonObject("species").get("name").getAsString();
        evoluciones.add(nombreEvolucion);

        JsonArray evolves = json.getAsJsonArray("evolves_to");
        if(evolves.size() > 0){
            getEvolucion(evolves.get(0).getAsJsonObject());
        }
    }

    static class Pokemon{
        private String nombre;
        private int nroPokedex;
        private double peso;
        private double altura;
        private ArrayList<String> tipos;
        private ArrayList<String> juegos;
        private ArrayList<String> evoluciones;

        public Pokemon(int nroPokedex, String nombre, double peso, double altura, ArrayList<String> tipos, ArrayList<String> juegos, ArrayList<String> evoluciones){

            this.nroPokedex = nroPokedex;
            this.nombre = nombre;
            this.peso = peso / 10;
            this.altura = altura;
            this.juegos = juegos;
            this.evoluciones = evoluciones;
            this.tipos = tipos;

        }

        public Pokemon(int nroPokedex, String nombre, double peso, double altura, ArrayList<String> tipos, ArrayList<String> juegos){

            this.nroPokedex = nroPokedex;
            this.nombre = nombre;
            this.peso = peso / 10;
            this.altura = altura;
            this.juegos = juegos;
            this.tipos = tipos;

        }

        public String getNombre() {

            String nombre = this.nombre.substring(0, 1).toUpperCase() +
                    this.nombre.substring(1).toLowerCase();

            return nombre;
        }

        public void setNombre(String nombre) { this.nombre = nombre; }

        public int getNroPokedex() {
            return nroPokedex;
        }

        public void setNroPokedex(int nroPokedex) {
            this.nroPokedex = nroPokedex;
        }

        public double getPeso() {
            return peso;
        }

        public void setPeso(double peso) { this.peso = peso; }

        public double getAltura() {
            return altura;
        }

        public void setAltura(double altura) {
            this.altura = altura;
        }

        public ArrayList<String> getTipos() {
            return tipos;
        }

        public void setTipos(ArrayList<String> tipos) { this.tipos = tipos; }

        public ArrayList<String> getJuegos() {
            return juegos;
        }

        public void setJuegos(ArrayList<String> juegos) {
            this.juegos = juegos;
        }

        public ArrayList<String> getEvoluciones() {
            return evoluciones;
        }

        public void setEvoluciones(ArrayList<String> evoluciones) {
            this.evoluciones = evoluciones;
        }

        public void infoPokemon(){

            System.out.println();
            System.out.println("INFO. POKEMON");
            System.out.println("- - - - - - -");
            System.out.printf("Nº %04d\t --> %s\n", getNroPokedex(),  getNombre());
            System.out.println("===============");

            System.out.print("Tipo/s: ");
            for (String tipo : getTipos()) {
                System.out.print(tipo + " | ");
            }

            System.out.println("\n- Peso: " +  getPeso() + "Kg");
            System.out.println("- Altura: " + getAltura() + "m");

            System.out.println("=========================\n");

            System.out.println(" ---- Juegos en los que aparece ---- ");
            System.out.println("-------------------------------------");

            int contador = 0;

            System.out.print(" - ");
            for (String juego : getJuegos()) {

                if(contador == 3){
                    contador = 0;
                    System.out.print("\n - ");
                }

                System.out.print(juego + " | ");
                contador++;

            }

            System.out.println("\n\nLinea Evolutiva");
            System.out.println("===============");
            contador = 1;
            for (String evolucion : getEvoluciones()) {
                System.out.println( contador + " - " + evolucion);
                contador++;
            }

        }
    }


}
