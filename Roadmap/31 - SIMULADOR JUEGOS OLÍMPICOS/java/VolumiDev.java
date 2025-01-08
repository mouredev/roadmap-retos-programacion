import java.io.BufferedReader;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Random;


public class VolumiDev {
	/**
	 * Muestra el menu de la aplicacion.
	 * @return
	 * @throws IOException
	 */
	public static int menu() throws IOException {
		Lectura l = new Lectura();
		int op;
		System.out.println("1. Registrar eventos y participantes del evento");
		System.out.println("2. Simular Eventos");
		System.out.println("3. Creacion de informes");
		System.out.println("4. Salir");
		op = l.pedir_entero("Introduce una de las opciones anteriores", 1, 4);
		return op;
	}
	
	/**
	 * Crea y alamacena los enventos en una array list
	 * @param events
	 * @throws IOException
	 */
	public static void registrar_evento(ArrayList<Evento> events) throws IOException {
		Evento event = new Evento();
		event.registrar_evento(events);
		events.add(event);
	}
	
	/**
	 * mostramos los eventos reegistrado con el codigo del mismo para poder identificarlo.
	 * @param events
	 * @throws IOException 
	 */
	public static int mostramos_eventos(ArrayList<Evento> events) throws IOException {
		Lectura l = new Lectura();
		int event_cod;
		for (Evento event : events) {
			System.out.println(event.cod + ". " + event.nombre);
		}
		event_cod = l.pedir_entero("Elige el evento que deseas", 1, events.size());
		return event_cod-1;
	}
	
	/**
	 * Metodo que llama a la función de simulación y a la de establecer el medallero
	 * @param events
	 * @throws IOException
	 */
	public static void simular_event(ArrayList<Evento> events) throws IOException {
		Evento event = events.get(mostramos_eventos(events));
		event.simulacion();
		event.est_medallero();
	}
	
	public static boolean generar_informe(ArrayList<Evento> events, boolean flag_txt) throws IOException {
		Evento event = events.get(mostramos_eventos(events));
		if(event.informado) {
			File txt = new File("Informe_medallas.txt");
			if(flag_txt) {
				if(txt.exists()) {
					txt.delete();
				}
			}
			if(event.ejecucion == false) {
				
				FileWriter fw = new FileWriter(txt, true);
				PrintWriter pw = new PrintWriter(fw);
				
				pw.println(event.nombre.toUpperCase());
				for(String medalla : event.medallero) {
					pw.println("\t" + medalla);;
				}
				
				event.informado = false;
				pw.close();
				fw.close();			
			}else {
				System.out.println("El evento no se ha ejecutado aun");
			}
		}else {
			System.out.println("El evento ya ha generado informes");
		}
		return false;
	}
	public static void main(String[] args) throws IOException {	
		ArrayList<Evento> events  = new ArrayList<Evento>();
		Lectura l = new Lectura();
		boolean flag_txt = true;
		int op = menu();
		while(op != 4) {
			switch(op) {
			case 1:
				char terminar;
				do {
					registrar_evento(events);
					do {
						terminar = l.pedir_cad("Quieres añadir mas eventos?? S/N").toUpperCase().charAt(0);	
					} while (terminar != 'S' && terminar != 'N' );
				} while (terminar != 'N');
				break;
			case 2:
				simular_event(events);
				break;
			case 3:
				flag_txt = generar_informe(events, flag_txt);
				break;
			}
			op = menu();
		}
		System.out.println("Cerrando programa...");
	}
	
	/**
	 * Generamos la clase de los eventos con sus metodos
	 * 
	 */

	static class Evento {
		private int cod;
		private String nombre;
		private int num_participantes; //minimo de 3 participantes
		private Atleta[] participantes;
		private String[] medallero;
		private String magnitud; //tiempo, metros, kg, puntos
		private int lim_sup;
		private int lim_inf;
		private boolean ejecucion;
		private boolean informado;
		
		Evento(){
			ejecucion = true;
			informado = true;
		}
		
		/**
		 * Valida que la magnitud introducida este dentro de las permitidas, de esta forma nos permite 
		 * añadir nuevas magnitudes si metemos nuevos pruebas.
		 * @param magnitudes
		 * @param mag
		 * @return boolean
		 */
		private boolean validar_magnitud(String[] magnitudes, String mag) {
			boolean flag = true;
			for (int i = 0; i < magnitudes.length && flag == true; i++) {
				if(magnitudes[i].equalsIgnoreCase(mag)) {
					flag = false;
				}
			}
			return flag;
		}
		
		/**
		 * Registra los datos del evento
		 * @throws IOException
		 */
		public void registrar_evento(ArrayList<Evento> events) throws IOException {
			String[] magnitudes = {"minutos", "segundos", "metros", "kilogramos", "puntos"};
			Lectura l = new Lectura();
			cod = events.size() + 1;
			nombre = l.pedir_cad("Introduce el nombre del evento");
			num_participantes = l.pedir_entero("Introduce la cantidad de participantes en la prueba", 3, 30);
			participantes = new Atleta[num_participantes];
			for (int i = 0; i < participantes.length; i++) {
				Atleta atl = new Atleta();
				atl.rellenar();
				participantes[i] = atl;
				System.out.println("Atleta registrado...");
			}
			do {
				magnitud = l.pedir_cad("Introduce la magnitud del resultado (minutos, segundos, metros, kilogramos, puntos)").toLowerCase();				
			} while (validar_magnitud(magnitudes, magnitud));
			lim_inf = l.pedir_entero("Introduce el limite inferior de la magnitud", 0, 9999999);
			lim_sup = l.pedir_entero("Introduce el limite superior de la magnitud", lim_inf, 9999999);
			
		}
		
		/**
		 * Hace la simulación de forma aleatoria y redondea el double genereado como resultado
		 */
		public void simulacion() {
			if(ejecucion) {
				Random random = new Random();
				for (int i = 0; i < participantes.length; i++) {
					participantes[i].marca = Math.round(random.nextDouble(lim_inf, lim_sup) * 100.0)/100.0;
				}	
				ejecucion = false;
			}else {
				System.out.println("Este evento ya ha terminado");
			}
		}
		
		/**
		 * Establece el medallero e imprime por pantalla los resultados según el tipo de prueba que sea.
		 */
		public void est_medallero() {
			Arrays.sort(participantes);
			medallero = new String[3];
			int medalla = 0;
			switch(magnitud) {
			case "metros", "kilogramos", "puntos":
				for(int pos = participantes.length -1; pos >= participantes.length - 3; pos--) {
					if(medalla == 0) {
						medallero[medalla] = participantes[pos].datos_txt() + " ---> " + "ORO";
					} else if(medalla == 1) {
						medallero[medalla] = participantes[pos].datos_txt() + " ---> " + "PLATA";
					}else {
						medallero[medalla] = participantes[pos].datos_txt() + " ---> " + "BRONCE";
					}
					medalla++;
				}
				break;
			case "minutos", "segundos":
				for(int pos = 0; pos < 3; pos++) {
					if(medalla == 0) {
						medallero[medalla] = participantes[pos].datos_txt() + " ---> " + "ORO";
					} else if(medalla == 1) {
						medallero[medalla] = participantes[pos].datos_txt() + " ---> " + "PLATA";
					}else {
						medallero[medalla] = participantes[pos].datos_txt() + " ---> " + "BRONCE";
					}
					medalla++;
				}
				break;
			}
			for(String posicion : medallero) {
				System.out.println(posicion);
			}
		}
	}
	
	/**
	 * Clase de atleta que almacena datos del atleta
	 */
	static class Atleta implements Comparable<Atleta>{
		private String nombre;
		private String pais;
		private double marca;
		
		//metodos
		//rellena los datos del atleta
		public void rellenar() throws IOException {
			Lectura l = new Lectura();
			nombre = l.pedir_cad("Introduce el nombre del atleta");
			pais = l.pedir_cad("Introduce el pais del atleta");
		}
		
		// transforma los datos en un String
		public String datos_txt() {
			return "" + nombre + " - " + pais + " - " + marca;
		}
		
		/**
		 * Compara un atleta con otro para poder usar el metodo sort de la calse Arrays
		 */
		public int compareTo(Atleta otro) {
			return Double.compare(marca, otro.marca);
		}
	}
	
	/**
	 * Definimos una clase lectura con los metodos para los diferentes tipos de datos.
	 */
	static class Lectura{
		public static BufferedReader leer = new BufferedReader(new InputStreamReader(System.in));
		
		/**
		 * Metodo en el que pedimos una cadena de texto.
		 * 
		 * @param cad
		 * @return cadena introducida por teclado
		 * @throws IOException
		 */
		public String pedir_cad(String cad) throws IOException {
			String c;
			do {
				System.out.println(cad);
				c = leer.readLine();
			} while (c.isEmpty());
			return c;
		}
		
		/**
		 * Método con el que pedimos un entero entre un rango concreto
		 * @param cad
		 * @param n1
		 * @param n2
		 * @return
		 * @throws IOException
		 */
		public int pedir_entero(String cad, int n1, int n2) throws IOException {
			int n = n1 - 1;
			do {
				try {
					System.out.println(cad);
					n=Integer.parseInt(leer.readLine());
				}catch (NumberFormatException e) {
					System.out.println("Solo valores numericos");
				}
			} while (n < n1 || n > n2);
			
			return n;
		}
	}

}








