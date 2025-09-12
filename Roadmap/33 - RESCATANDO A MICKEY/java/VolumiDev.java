import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.Stack;

import javax.print.attribute.SetOfIntegerSyntax;

public class Rescatar_Mickey {
	
	public static void generar_elementos(int row, int col, ArrayList<Elemento> elements) throws NumberFormatException, IOException {
		BufferedReader leer = new  BufferedReader(new InputStreamReader(System.in));
		Rescatar_Mickey rescatarMickey = new Rescatar_Mickey();
		System.out.println("¿Cuantos obstaculos quieres crear?");
		int num_obstaculos = Integer.parseInt(leer.readLine());
		// posicion de Mikey
		Rescatar_Mickey.Mickey mickey = rescatarMickey.new Mickey();
		
		do {
			mickey.colocar_elemento(row, 0);
		} while (esta_ocupado(elements, mickey));
		elements.add(mickey);
		// Posicion de la salida
		Rescatar_Mickey.Salida salida = rescatarMickey.new Salida(col - 1);
		do {
			salida.colocar_elemento(row, 0);
		} while (esta_ocupado(elements, salida));
		elements.add(salida);
		// posicion de los obstaculos
		for (int i = 0; i < num_obstaculos; i++) {
			Rescatar_Mickey.Obstaculo obs = rescatarMickey.new Obstaculo();
			do {
				obs.colocar_elemento(row, col);
			} while (esta_ocupado(elements, obs));
			elements.add(obs);
		}
	}
	
	//Dibujamos el laberinto
	public static void lab_draw(ArrayList<Elemento> elements, int row, int col) {
		String[][] lab = new String[row][col];

		for(Elemento element : elements) {
			lab[element.get_row()][element.get_col()] = element.vista;
		}
		
		System.out.println("------------ LABERINTO ------------");
		for (int i = 0; i < lab.length; i++) {
			for (int j = 0; j < lab[i].length; j++) {
				if(lab[i][j] == null) {
					lab[i][j] = "⬜";
				}
				System.out.print(lab[i][j] + "\t");
			}
			System.out.println();
		}
		validacion(lab, elements);
	}
	
	// Validamos si la posicion esta ocupada por alguno de lo elementos del arraylist
	public static boolean esta_ocupado(ArrayList<Elemento> elements, Elemento obs) {
		boolean flag = false;
		for (int i = 0; i < elements.size() && flag == false; i++) {
			if (obs.row == elements.get(i).row && obs.col == elements.get(i).col) {
				flag = true;
			}
		}
		return flag;
	}
	
	
	// Solicitamos movimiento de mickey
	public static void movimiento(Elemento mickey, int matrix_length) throws IOException {
		BufferedReader leer = new  BufferedReader(new InputStreamReader(System.in));
		char mov;
		do {
			System.out.println("Mueve a Mickey");
			mov = leer.readLine().toUpperCase().charAt(0);
		} while (mov != 'W' && mov != 'A' && mov != 'S' && mov != 'D');
		mickey.mov(mov, matrix_length);
	}
	
	// Comparamos la posicion de mickey con la matriz
	public static void validacion(String[][] lab, ArrayList<Elemento>elements) {
		Elemento mickey = elements.get(0);
		for (int i = 0; i < lab.length; i++) {
			for (int j = 0; j < lab.length; j++) {
				if(!lab[i][j].equalsIgnoreCase("⬜")) {
					if(lab[i][j].equalsIgnoreCase("🚪")  && mickey.get_col() == j && mickey.get_row() == i) {
						mickey.set_Exit(true);
						System.out.println("LO LOGRASTE. MICKEY ESCAPO");
					}else if(lab[i][j].equalsIgnoreCase("💣")  && mickey.get_col() == j && mickey.get_row() == i) {
						mickey.set_Life(false);
						System.out.println("MICKEY HA MUERTO");
					}
				}
			}
		}
	}
	
	
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader leer = new  BufferedReader(new InputStreamReader(System.in));
		int row = 0, col = 0;
		String[][] lab;
		do {
			try {
				System.out.println("Introduce el numero de filas y columnas");
				row = Integer.parseInt(leer.readLine());
				col = row;
			} catch (NumberFormatException e) {
				// TODO: handle exception
				System.out.println("Solo valores numericos");
			}
		} while (row < 2);
		ArrayList<Elemento> elements = new ArrayList<Elemento>();
		generar_elementos(row, col, elements);
		lab_draw(elements, row, col);
		while(elements.get(0).isLife() && elements.get(0).isexit() == false) {
			movimiento(elements.get(0), row);
			lab_draw(elements, row, col);
		}
		System.out.println("PARTIDA TERMINADA");
	}
	
	
	public class Elemento{
		private String vista;
		private int row;
		private int col;
		
		// Metodo que coloca un elemento en la matriz del laberinto
		protected void colocar_elemento(int row, int col) {

		}
		
		protected int get_row() {
			return row;
		}
		
		protected int get_col() {
			return col;
		}
		protected boolean isLife() {
			return false;
		}
		
		protected boolean isexit() {
			return false;
		}
		
		public void mov(char key, int matrix_lentgh) {
			
		}
		public void set_Exit(boolean exit) {
		}
		public void set_Life(boolean life) {
		}
	}

	// Clase que representa a Mickey Mouse
	public class Mickey extends Elemento{
		
		private boolean life;
		private boolean exit;
		
		public Mickey() {
			// TODO Auto-generated constructor stub
			super();
			super.vista = "🐭";
			super.col = 0;
			life = true;
			exit = false;
		}
		
		
		// Metodo que coloca un elemento en la matriz del laberinto
		public void colocar_elemento(int row, int col) {
			super.row = (int) (Math.random()*row);
		}
		
		public void mov(char key, int matrix_lentgh) {
			switch (key) {
			case 'W':
				if(super.row > 0) {
				super.row--;
				}
				break;
			case 'A':
				if(super.col > 0) {
					super.col--;										
				}
				break;
			case 'S':
				if(super.row < matrix_lentgh - 1) {
					super.row++;					
				}
				break;
			case 'D':
				if(super.col < matrix_lentgh - 1) {
					super.col++;					
				}
				break;
			default:
				System.out.println("Tecla incorrecta");
				break;
			}
		}
		
		public void set_Exit(boolean e) {
			this.exit = true;
		}
		public void set_Life(boolean l) {
			this.life = false;
		}
		
		public boolean isLife() {
			return life;
		}
		
		public boolean isexit() {
			return exit;
		}
		
	}
	
	// Clase que representa obstaculos
	public class Obstaculo extends Elemento{
		
		Obstaculo(){
			super();
			super.vista = "💣";
		}
		
		public void get_pos() {
			System.out.println("ROW = " + super.row + "COL = " + super.col);
		}
		
		// Metodo que coloca un elemento en la matriz del laberinto
				public void colocar_elemento(int row, int col) {
					super.row = (int) (Math.random()*row);
					super.col = (int) (Math.random()*((col-2) -1 + 1) + 1);
				}
	}
	
	//Clase que representa la salida
	public class Salida extends Elemento{
		
		Salida(int col){
			super();
			super.vista = "🚪";
			super.col = col;
		}
		
		public void get_pos() {
			System.out.println("X = " + super.row + "Y = " + super.col);
		}
		
		// Metodo que coloca un elemento en la matriz del laberinto
		public void colocar_elemento(int row, int col) {
			super.row = (int) (Math.random()*row);
		}
	}
}
