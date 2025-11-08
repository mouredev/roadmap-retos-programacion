/*
 * EJERCICIO:
 * Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
 * una petición a la web que tú quieras, verifica que dicha petición
 * fue exitosa y muestra por consola el contenido de la web.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la PokéAPI (https://pokeapi.co), crea un programa por
 * terminal al que le puedas solicitar información de un Pokémon concreto
 * utilizando su nombre o número.
 * - Muestra el nombre, id, peso, altura y tipo(s) del Pokémon
 * - Muestra el nombre de su cadena de evoluciones
 * - Muestra los juegos en los que aparece
 * - Controla posibles errores
 */

import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.Scanner;

public class JimsimroDev {
  private static final String URL_BASE = "https://pokeapi.co/api/v2/pokemon/";

  String consumirApi(String url) {
    HttpClient client = HttpClient.newHttpClient();
    HttpRequest request = HttpRequest.newBuilder()
        .uri(URI.create(url))
        .build();
    HttpResponse<String> response = null;

    try {
      response = client.send(request, HttpResponse.BodyHandlers.ofString());
    } catch (IOException e) {
      throw new RuntimeException(e);
    } catch (InterruptedException e) {
      throw new RuntimeException(e);
    }
    if (response.statusCode() == 200) {
      IO.println("Respuesta exitosa codigo: " + response.statusCode());
      String json = response.body();
      return json;
    }
    throw new RuntimeException("Eror al procesar la solicitud codigo de error " + response.statusCode());
  }

  // Busca campo en la Raiz
  private String getCampo(StringBuilder data, String campo) {
    String patron = "\"" + campo + "\":";
    int inicio = data.indexOf(patron);
    if (inicio != -1) {
      inicio += patron.length();
      while (inicio < data.length() && Character.isWhitespace(data.charAt(inicio))) {
        inicio++;
      }
      if (inicio < data.length()) {
        if (data.charAt(inicio) == '"') {
          inicio++;
          int fin = data.indexOf("\"", inicio);
          if (fin != -1) {
            return data.substring(inicio, fin);
          }
        } else {
          int fin = inicio;
          while (fin < data.length() &&
              data.charAt(fin) != ',' &&
              data.charAt(fin) != '}' &&
              data.charAt(fin) != '\n') {
            fin++;
          }
          return data.substring(inicio, fin).trim();
        }
      }
    }
    return null;
  }

  // Busca campo en una sección dada
  private String getCampo(StringBuilder data, String seccion, String campo) {
    int indiceSeccion = data.indexOf("\"" + seccion + "\"");
    if (indiceSeccion != -1) {
      String patron = "\"" + campo + "\":\"";
      int indiceCampo = data.indexOf(patron, indiceSeccion);

      if (indiceCampo != -1) {
        int empiezaValor = indiceCampo + patron.length();
        int terminaValor = data.indexOf("\"", empiezaValor);
        return data.substring(empiezaValor, terminaValor);
      }
    }
    return null;
  }

  // Busca los typos
  private String[] getTypes(StringBuilder data) {
    String tiposPattern = "\"types\":[";
    int startIndex = data.indexOf(tiposPattern);
    if (startIndex != -1) {
      startIndex += tiposPattern.length();
      int endIdex = data.indexOf("]", startIndex);
      if (endIdex != -1) {
        String tiposArray = data.substring(startIndex, endIdex);
        String[] tipos = tiposArray.split("},");
        String[] resultados = new String[tipos.length];
        // Procesar cada tipo
        for (int i = 0; i < tipos.length; i++) {
          String tipo = tipos[i];
          String namePattern = "\"name\":\"";
          int nameStart = tipo.indexOf(namePattern);
          if (nameStart != -1) {
            nameStart += namePattern.length();
            int nameEnd = tipo.indexOf("\"", nameStart);
            if (nameEnd != -1) {
              resultados[i] = tipo.substring(nameStart, nameEnd);
            }
          }
        }
        return resultados;
      }
    }
    return new String[0];
  }

  private String getEvolutionChainUrl(StringBuilder data) {
    String patron = "\"evolution_chain\":{\"url\":\"";
    int inicio = data.indexOf(patron);
    if (inicio != -1) {
      inicio += patron.length();
      int fin = data.indexOf("\"", inicio);
      if (fin != -1) {
        return data.substring(inicio, fin);
      }
    }
    return null;
  }

  void evolution_chain(StringBuilder data) {
    // Obtener el nombre de la especie actual
    String speciesName = getCampo(data, "species", "name");
    IO.println("Evolución: " + speciesName);

    // Buscar el patrón de evolves_to
    String evolvesToPattern = "\"evolves_to\":[";
    int evolvesToIndex = data.indexOf(evolvesToPattern);

    if (evolvesToIndex != -1) {
      // Si encontramos evolves_to y no está vacío
      evolvesToIndex += evolvesToPattern.length();
      if (data.charAt(evolvesToIndex) != ']') {
        // Obtener el contenido del evolves_to
        int endIndex = findMatchingBracket(data, evolvesToIndex);
        if (endIndex != -1) {
          // Crear un nuevo StringBuilder con el contenido de evolves_to
          StringBuilder evolvesTo = new StringBuilder(
              data.substring(evolvesToIndex, endIndex));
          // Llamada recursiva con el nuevo contenido
          evolution_chain(evolvesTo);
        }
      }
    }
  }

  // Método auxiliar para encontrar el corchete de cierre correspondiente
  private int findMatchingBracket(StringBuilder data, int startIndex) {
    int count = 1;
    for (int i = startIndex; i < data.length(); i++) {
      if (data.charAt(i) == '[')
        count++;
      if (data.charAt(i) == ']')
        count--;
      if (count == 0)
        return i;
    }
    return -1;
  }

  void main() {
    Scanner in = new Scanner(System.in);

    // HttpClient client = HttpClient.newHttpClient();
    //
    // HttpRequest request = HttpRequest.newBuilder()
    // .uri(URI.create("https://www.mercadolibre.com.co/"))
    // .build();
    // HttpResponse<String> response = null;
    //
    // try {
    // response = client.send(request, HttpResponse.BodyHandlers.ofString());
    // } catch (IOException e) {
    // throw new RuntimeException(e);
    // } catch (InterruptedException e) {
    // throw new RuntimeException(e);
    // }
    // String json = response.body();
    // IO.println("Estado " + response.statusCode());
    // IO.println(json);

    IO.println("Ingresa el nombre del pokemon a consultar");
    String pokemon = in.nextLine();

    StringBuilder data = new StringBuilder();
    StringBuilder url = new StringBuilder();

    data.append(consumirApi(URL_BASE + pokemon));

    String nombre = getCampo(data, "name");

    String id = getCampo(data, "id");

    String peso = getCampo(data, "weight");

    String altura = getCampo(data, "height");
    String[] tipos = getTypes(data);

    String urlSpecies = getCampo(data, "species", "url");

    url.append(consumirApi(urlSpecies));
    String urlEvolucion = getEvolutionChainUrl(url);

    // StringBuilder evolution = new StringBuilder();
    // String evolucin = getCampo(evolution, "species", "name");
    // IO.println("url evloucion " + evolution);
    // IO.println("evolution" + evolucin);

    StringBuilder evolutionData = new StringBuilder(consumirApi(urlEvolucion));
    evolution_chain(evolutionData);
    IO.println("Nombre: " + nombre);
    IO.println("ID: " + id);
    IO.println("Peso: " + peso);
    IO.println("Altura: " + altura);
    IO.println("Tipos:");
    for (String tipo : tipos) {
      IO.println("- " + tipo);
    }
    in.close();
  }
}
